from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import json

from environments.config import AUTH0_DOMAIN_ENV, ALGORITHMS_ENV, API_AUDIENCE_ENV

AUTH0_DOMAIN = AUTH0_DOMAIN_ENV
ALGORITHMS = ALGORITHMS_ENV
API_AUDIENCE = API_AUDIENCE_ENV 

## AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


## Auth Header

'''
Functionality of get_token_auth_header() method:
    - get the header from the request
    - raise an AuthError if no header is present
    - split bearer and the token
    - raise an AuthError if the header is malformed
return the token part of the header
'''
def get_token_auth_header():

    # Get 'Authorization' header from the request
    headers_auth = request.headers.get('Authorization', None)
    print(headers_auth)
    if not headers_auth:
       raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        }, 401)
    
    headers_parts = headers_auth.split(' ')

    if headers_parts[0].lower() != 'bearer':
       raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must begin with "Bearer"'
        }, 401)

    elif len(headers_parts) == 1:
       raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not Found.'
        }, 401)

    elif len(headers_parts) > 2:
       raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    # return only the JWT token from the 'Authorization' header
    token = headers_parts[1]
    return token

'''
Functionality of check_permissions(permission, payload) method:
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload

    - raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    - raise an AuthError if the requested permission string is not in the payload permissions array
return true otherwise
'''
def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'permissions_missing',
            'description': 'Missing permissions.'
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'permissions_not_granted',
            'description': 'Unauthorized action.'
        }, 401)

    return True

'''
Functionality of verify_decode_jwt(token) method:
    @INPUTS
        token: a json web token (string)

    - it should be an Auth0 token with key id (kid)
    - it should verify the token using Auth0 /.well-known/jwks.json
    - it should decode the payload from the token
    - it should validate the claims
return the decoded payload

    !!NOTE urlopen has a common certificate error described here: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
'''
def verify_decode_jwt(token):

    # Get public key from Auth0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    
    # Get data in Auth header
    unverified_header = jwt.get_unverified_header(token)

    # Choose the rsa key
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)
    
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    # If rsa key is available verify the authenticity
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 401)
    raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
            }, 401)

'''
Functionality of @requires_auth(permission) decorator method:
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    - use the get_token_auth_header method to get the token
    - use the verify_decode_jwt method to decode the jwt
    - use the check_permissions method validate claims and check the requested permission
return the decorator which passes the decoded payload to the decorated method
'''
def requires_auth(permission = ''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator