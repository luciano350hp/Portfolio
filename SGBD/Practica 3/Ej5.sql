--
-- PostgreSQL port of the MySQL "World" database.
--
-- The sample data used in the world database is Copyright Statistics 
-- Finland, http://www.stat.fi/worldinfigures.
--

--PRACTICA 3 EJERCICIO 5

select *
from sitio s1 , sitio s2
where s1.countrycode = s2.countrycode
and s1.entidad like 'a%' and s2.entidad like 'b%'
limit 100

/*En la consulta,
 cada fila trae de a dos sitios, 
 que sean del mismo codigo de pais, 
 y traeria uno q comience con a... y otro que comience con b
 */

EXPLAIN ANALYZE select *
from sitio s1 , sitio s2
where s1.countrycode = s2.countrycode
and s1.entidad like 'a%' and s2.entidad like 'b%'
limit 100;

--CREATE INDEX sitio_idx ON sitio (countrycode);

/*
PLAN DE EJECUCION SIN INDICE

 Limit  (cost=0.00..293.65 rows=100 width=50) (actual time=198.360..198.850 rows=100 loops=1)
   ->  Nested Loop  (cost=0.00..54084024.84 rows=18417951 width=50) (actual time=198.359..198.839 rows=100 loops=1)
         Join Filter: (s1.countrycode = s2.countrycode)
         Rows Removed by Join Filter: 270309
         ->  Seq Scan on sitio s2  (cost=0.00..18540.53 rows=60059 width=25) (actual time=0.015..0.059 rows=5 loops=1)
               Filter: ((entidad)::text ~~ 'b%'::text)
               Rows Removed by Filter: 155
         ->  Materialize  (cost=0.00..18840.49 rows=59993 width=25) (actual time=0.009..35.211 rows=54082 loops=5)
               ->  Seq Scan on sitio s1  (cost=0.00..18540.53 rows=59993 width=25) (actual time=0.008..140.701 rows=66932 loops=1)
                     Filter: ((entidad)::text ~~ 'a%'::text)
                     Rows Removed by Filter: 914390
 Planning time: 0.487 ms
 Execution time: 199.455 ms
(13 rows)



PLAN DE EJECUCION CON INDICE

 Limit  (cost=0.85..2.93 rows=100 width=50) (actual time=0.047..0.405 rows=100 loops=1)
   ->  Merge Join  (cost=0.85..382396.38 rows=18417951 width=50) (actual time=0.046..0.394 rows=100 loops=1)
         Merge Cond: (s1.countrycode = s2.countrycode)
         ->  Index Scan using sitio_idx on sitio s1  (cost=0.42..52988.57 rows=59993 width=25) (actual time=0.013..0.051 rows=23 loops=1)
               Filter: ((entidad)::text ~~ 'a%'::text)
               Rows Removed by Filter: 83
         ->  Materialize  (cost=0.42..53138.71 rows=60059 width=25) (actual time=0.030..0.310 rows=100 loops=1)
               ->  Index Scan using sitio_idx on sitio s2  (cost=0.42..52988.57 rows=60059 width=25) (actual time=0.019..0.291 rows=20 loops=1)
                     Filter: ((entidad)::text ~~ 'b%'::text)
                     Rows Removed by Filter: 258
 Planning time: 0.739 ms
 Execution time: 0.461 ms
(12 rows)

Se tarta mucho menos con el indice creado
*/

