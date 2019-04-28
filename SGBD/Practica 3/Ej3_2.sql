
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
SELECT continent, COUNT(*) AS cantidad FROM country WHERE (population > 2000000) GROUP BY continent HAVING (COUNT (*) > 15);

\echo Subqueries
SELECT name , lifeexpectancy FROM country WHERE lifeexpectancy = (SELECT MIN (lifeexpectancy) FROM country )
