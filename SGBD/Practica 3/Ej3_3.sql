--
-- PostgreSQL port of the MySQL "World" database.
--
-- The sample data used in the world database is Copyright Statistics 
-- Finland, http://www.stat.fi/worldinfigures.
--

BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE stats (countrycode character(3) NOT NULL, cant_lenguas integer, pop_urbana integer);

ALTER TABLE ONLY stats ADD CONSTRAINT stats_pkey PRIMARY KEY (countrycode);

ALTER TABLE ONLY stats ADD CONSTRAINT stats_countrycode_fkey FOREIGN KEY (countrycode) REFERENCES country(code);

INSERT INTO stats SELECT country.code FROM country;
UPDATE stats SET cant_lenguas =(SELECT count(language) FROM countrylanguage where countrylanguage.countrycode = stats.countrycode);
UPDATE stats SET pop_urbana =(SELECT sum(population) FROM city where city.countrycode = stats.countrycode);

COMMIT;

ANALYZE stats;
