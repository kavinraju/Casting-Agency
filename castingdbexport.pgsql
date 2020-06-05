--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying(6) NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: movie_actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movie_actors (
    actor_id integer NOT NULL,
    movie_id integer NOT NULL
);


ALTER TABLE public.movie_actors OWNER TO postgres;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying NOT NULL,
    release_date timestamp without time zone NOT NULL
);


ALTER TABLE public.movies OWNER TO postgres;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO postgres;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, name, age, gender) FROM stdin;
2	Ajith	45	Male
3	Rajinikanth	69	Male
4	Kamal Haasan	65	Male
1	Vijay	45	Male
5	Samantha Akkineni	33	Female
6	Trisha Krishnan	37	Female
7	Hansika Motwani	28	Female
8	Kajal Aggarwal	34	Female
9	Sivakarthikeyan	35	Male
10	Vikram	54	Male
11	Nivetha Thomas	24	Female
12	Suriya	44	Male
13	Amy Jackson	28	Female
14	Akshay Kumar	52	Male
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
2024ac070726
\.


--
-- Data for Name: movie_actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.movie_actors (actor_id, movie_id) FROM stdin;
1	1
12	1
3	2
11	2
8	3
12	3
1	4
5	4
1	5
5	5
7	6
12	6
4	7
11	7
3	8
13	8
14	8
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.movies (id, title, release_date) FROM stdin;
1	Friends	2001-05-05 18:51:16
2	Darbar	2020-01-09 18:51:16
3	Maattrraan	2012-10-12 18:51:16
4	Aathi	2006-01-14 18:51:16
5	Ghilli	2004-04-17 18:51:16
6	Singam II	2013-04-17 18:51:16
7	Papanasam	2015-07-03 18:51:16
8	2.0	2015-07-03 18:51:16
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 14, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.movies_id_seq', 8, true);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: movie_actors movie_actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_actors
    ADD CONSTRAINT movie_actors_pkey PRIMARY KEY (actor_id, movie_id);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: movie_actors movie_actors_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_actors
    ADD CONSTRAINT movie_actors_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(id);


--
-- Name: movie_actors movie_actors_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_actors
    ADD CONSTRAINT movie_actors_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- PostgreSQL database dump complete
--

