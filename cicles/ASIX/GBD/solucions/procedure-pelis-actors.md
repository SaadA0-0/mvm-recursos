### 5.1 Manteniment de pel.lícules "orfes"
Necessitem crear un procediment que faci el següent:
- Cerqui les pel.lícules `film` "orfes", es a dir, que no tenen asignat cap actor (cap correspondència a la taula `film_actor`)
- Per cadascuna d'aquestes pel.lícules, li assignem 3 actors aleatoris a escollir entre tots els actors existents a la taula `actor`

Podeu fer servir més d'un procediment si voleu pero el procediment principal s'hauria de cridar d'una manera similar a

```sql
CALL assignar_actors_films_orfes()
```

#### Solució

```sql
CREATE OR REPLACE PROCEDURE assignar_actors_aleatoris()
LANGUAGE plpgsql
AS $$
DECLARE
    -- Variable para guardar l'ID de la pel.lícula a cada volta del bucle
    --Farem servir aquesta variable per guardar la peli que estem tractant a cada volta del bucle. Fixeu-vos que es de tipus RECORD, es a dir, es guarda TOT EL REGISTRE (fila)
    v_film RECORD; 
BEGIN
    --Cerquem les pelis sense actors i les tractem a un bucle
    FOR v_film IN (
        SELECT f.film_id
        FROM film f
        LEFT JOIN film_actor fa ON f.film_id = fa.film_id
        WHERE fa.actor_id IS NULL
    ) 
    LOOP
        --Per cada peli orfe, insertem 3 actors aleatoris
        INSERT INTO film_actor (actor_id, film_id)
        SELECT actor_id, v_film.film_id
        FROM actor
        ORDER BY RANDOM()
        LIMIT 3;
        
    END LOOP;
    
    --Llancem un missatge informatiu a la consola
    RAISE NOTICE 'Actors assignats a les pel.lícules orfes';
END;
$$;
```

Un cop creat el `PROCEDURE` el podem cridar, sempre que ho necessitem, fent servir:

```sql
CALL assignar_actors_aleatoris();
```

#### Proves

M'asseguro de que les pelis amb id > 1000 son les que m'interessa actualitzar

```sql
select * from film where film_id > 1000;
```


Forço que totes les pelis noves quedin orfes
```sql
DELETE from film_actor where film_id > 1000;
```

Comprovo que, realment, tenim pelis orfes
```sql
SELECT f.film_id
        FROM film f
        LEFT JOIN film_actor fa ON f.film_id = fa.film_id
        WHERE fa.actor_id IS NULL;
```

Crido al procedure
```sql
call assignar_actors_aleatoris();
```

I torno a comprovar que, en efecte, ja no hi ha cap peli orfe

```sql
SELECT f.film_id
        FROM film f
        LEFT JOIN film_actor fa ON f.film_id = fa.film_id
        WHERE fa.actor_id IS NULL;
```

Comprovem una de les pelis actualitzades per verificar si realment se li han assignat 3 actors

```sql
SELECT * from film_actor where film_id = 1005;
```
