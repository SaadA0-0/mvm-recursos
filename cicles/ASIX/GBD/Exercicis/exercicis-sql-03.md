# Exercicis SQL: `INSERT`, `UPDATE` i `DELETE`

## 1. `INSERT`

### 1.1
Inserta a la teva base de dades `pagila` els següents actors:

```
Tirolés Bechamel
TaoPaiPai Cafeaulait
Teruel Chevrolet
Tennebaum Cafeaulait
Timotei Bechamel
Tirolés Chandalet
Tirolés Sabadell
Timotei Chevrolet
Timotei Crivillé
Tourmalet Charmander
Traginer Sabadell
Traginer Churumbel
Tourmalet Bechamel
Tennebaum Charmander
Traginer Camembert
```

### 1.2
Inserta els següents idiomes:
```
Spanish
Portuguese
Chinese
Vietnamese
English
```

### 1.3
Inserta noves películes:
```
FIRE BEARS FROM HELL
FIRE CLOWNS FROM ANOTHER DIMENSION
FIRE NINJAS FROM OUTER SPACE
FIRE NINJAS FROM THE FUTURE
FIRE NINJAS FROM THE FUTURE
FIRE NINJAS UNDERGROUND
FIRE ROBOTS FROM THE PAST
FIRE WOLVES FROM ANOTHER DIMENSION
FLYING DINOSAURS FROM THE PAST
FLYING PIRATES UNDERGROUND
GIANT NINJAS FROM OUTER SPACE
GIANT ZOMBIES IN NEW YORK
INVISIBLE PIRATES FROM THE DEEP A B Y S S
JUMPING PIRATES FROM THE DEEP A B Y S S
JUMPING PIRATES FROM THE PAST
JUMPING PUNKS FROM HELL
JUMPING SPIDERS FROM ANOTHER DIMENSION
JUMPING SPIDERS FROM THE FUTURE
KILLING NINJAS FROM THE DEEP A B Y S S
KILLING NINJAS UNDERGROUND
KILLING PUNKS UNDERGROUND
KILLING ROBOTS FROM THE FUTURE
MUTANT NINJAS UNDERGROUND
MUTANT PIRATES FROM THE FUTURE
MUTANT ROBOTS FROM THE PAST
MUTANT ROBOTS UNDERGROUND
MUTANT WOLVES FROM THE DEEP A B Y S S
MUTANT WOLVES FROM THE FUTURE
MUTANT WOLVES IN NEW YORK
MUTANT ZOMBIES FROM ANOTHER DIMENSION
POISON ROBOTS FROM THE PAST
POISON WOLVES FROM OUTER SPACE
RADIOACTIVE NINJAS FROM THE DEEP A B Y S S
RADIOACTIVE SHARKS IN NEW YORK
RADIOACTIVE SPIDERS FROM ANOTHER DIMENSION
RADIOACTIVE SPIDERS FROM THE PAST
TIME TRAVELLING NINJAS FROM THE PAST
TIME TRAVELLING PIRATES FROM THE PAST
TIME TRAVELLING SHARKS FROM ANOTHER DIMENSION
TIME TRAVELLING ZOMBIES IN NEW YORK
```
Et pots inventar la durada, dates, etc... pero respectant la coherencia de la base de dades (per exemple, has de fer servir els ratings existents)

Fes servir, com idioma, alguns dels nous idiomes que has inserit previament.

També haurás d'informar els actors que participen a aquestes películes. El que farem es afegir un actor aleatori, de entre els actors que existeixen, a unes quantes pel.lícules (no cal fer-ho a totes).

## 2. `UPDATE`

### 2.1
Hem de corregir el títol de totes les pel.lícules que acaben en 'UNDERGROUND' per 'FROM THE UNDERGROUND'

### 2.2
Hem d'afegir una nova columna anomenada `novetat` a la taula `film`. Aquesta nova columna només ha de permetre guardar valors `true` o `false`
Un cop fet aixó: 
- farem que les pel.lícules que ja existien abans dels nostres inserts (el seu film_id arriba fins el 1000) tinguin el valor `false` al camp `novetat`
- farem que les pel.lícules que que hem inserit nosaltres (el seu film_id serà a partir del 1000) tinguin el valor `true` al camp `novetat`

### 2.3
Com que el títol de totes les noves pel.lícules inserides està en anglés, li assignarem aquest idioma, però farem servir l'anglès que hem afegit nosaltres, no el que ja existía (si ho has fet tot bé, el seu ID deuría ser el `11`, pero segur que no es el `1`)

## 3. `DELETE`

### 3.1
Ens acaben d'avisar de que algú ha inserit per error un idioma duplicat ( ¬_¬). Resulta que tenim dues vegades l'idioma `English` i hem d'eliminar el segon, que es el més antic.

### 3.2
Ens informen que tota la saga `FROM THE DEEP A B Y S S` té exemplar defectuosos i, com s'han eliminat del magatzem, nosaltres hem de eliminar qualsevol pel.lícula d'aquesta saga de la tabla `film`.
