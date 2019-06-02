--
-- PostgreSQL port of the MySQL "World" database.
--
-- The sample data used in the world database is Copyright Statistics 
-- Finland, http://www.stat.fi/worldinfigures.
--

--PRACTICA 3 EJERCICIO 3.4

BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE sitio (id int NOT NULL, entidad varchar, tipo_entidad varchar, pais varchar,countrycode character (3));

ALTER TABLE ONLY sitio ADD CONSTRAINT sitio_pkey PRIMARY KEY (id);

ALTER TABLE ONLY sitio ADD CONSTRAINT sitio_countrycode_fkey FOREIGN KEY (countrycode) REFERENCES country(code);

COMMIT;

ANALYZE sitio;
