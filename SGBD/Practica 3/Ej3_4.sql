--
-- PostgreSQL port of the MySQL "World" database.
--
-- The sample data used in the world database is Copyright Statistics 
-- Finland, http://www.stat.fi/worldinfigures.
--

BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE sitio (id int NOT NULL, entidad varchar, tipo_entidad varchar, pais varchar,countrycode character (3));

ALTER TABLE ONLY sitio ADD CONSTRAINT sitio_pkey PRIMARY KEY (id);

ALTER TABLE ONLY sitio ADD CONSTRAINT sitio_countrycode_fkey FOREIGN KEY (countrycode) REFERENCES country(code);

--INSERT INTO stats SELECT country.code FROM country;
--UPDATE stats SET cant_lenguas =(SELECT count(language) FROM countrylanguage where countrylanguage.countrycode = stats.countrycode);
--UPDATE stats SET pop_urbana =(SELECT sum(population) FROM city where city.countrycode = stats.countrycode);

COMMIT;

ANALYZE stats;

