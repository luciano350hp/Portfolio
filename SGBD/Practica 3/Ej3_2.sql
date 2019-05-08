
\echo PRACTICA 3 WORLD BD CONSULTAS '\n'

\echo CONSULTA 3.2.1
SELECT name,population FROM country WHERE name = 'Argentina';

\echo CONSULTA 3.2.2
SELECT DISTINCT continent FROM country;

\echo CONSULTA 3.2.3
SELECT name FROM country WHERE (population > 15000000 AND continent = 'South America');

\echo CONSULTA 3.2.4
SELECT name, gnp FROM country ORDER BY gnp DESC LIMIT 10;

\echo CONSULTA 3.2.5
SELECT governmentform, COUNT (*) AS cantidad FROM country GROUP BY governmentform ORDER BY cantidad DESC;

\echo CONSULTA 3.2.6
SELECT continent, SUM(surfacearea) AS superficie FROM country GROUP BY continent ORDER BY superficie DESC;

\echo CONSULTA 3.2.7 
SELECT continent, COUNT(*) AS cantidad FROM country WHERE (population > 20000000) GROUP BY continent HAVING (COUNT (*) > 15);

\echo Subqueries 1
SELECT name , lifeexpectancy FROM country WHERE lifeexpectancy = (SELECT MIN (lifeexpectancy) FROM country);

\echo Subqueries 2
SELECT name, lifeexpectancy FROM country WHERE lifeexpectancy = (select min(lifeexpectancy) from country) OR lifeexpectancy = (select max(lifeexpectancy) from country);  

\echo Subqueries 3
SELECT name, indepyear FROM country WHERE continent = (select continent from country where indepyear = (select min(indepyear) from country));

\echo Subqueries 4
SELECT DISTINCT continent FROM country WHERE continent IN (select continent FROM country ORDER BY gnp DESC LIMIT 10);

\echo Join 1
SELECT name, language FROM country, countrylanguage WHERE code = countrycode AND continent = 'Oceania';

\echo Join 2
SELECT name, COUNT(language) AS lenguas FROM country INNER JOIN countrylanguage ON (code = countrycode) GROUP BY name HAVING COUNT(language) > 1 ORDER BY lenguas DESC;

\echo Join 3
SELECT DISTINCT language from country,countrylanguage where code = countrycode AND continent = (SELECT continent FROM country GROUP BY continent HAVING SUM(gnp) > 0 ORDER BY SUM(gnp) LIMIT 1);

\echo Join 4.1
SELECT name, population FROM country; 

\echo Join 4.2
SELECT country.name, sum(city.population) FROM country INNER JOIN city ON (countrycode=code) GROUP BY country.name;

\echo Join 4.2 Porcentajes
SELECT city.name, (city.population*100/country.population) as porcentajePoblacion FROM city INNER JOIN country ON (countrycode=code) ORDER BY porcentajePoblacion DESC;
