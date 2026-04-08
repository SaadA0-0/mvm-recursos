# Exercicis XQuery (muntanyes, deserts i aeroports amb format HTML)

Fent servir `BaseX` amb el fitxer [mondial_geo_accidents.xml](../recursos/mondial_geo_accidents.xml), executeu les consultes **XQuery** (fent servir clàusules `for`, `let`, `where`, `return`, etc.) necessàries per extreure la informació i generar els resultats en format **HTML**:

## Nivell 1
1. Obtenir una llista desordenada (`<ul>` amb elements `<li>`) amb el nom de tots els deserts llistats al fitxer.
2. Retornar un paràgraf (`<p>`) que digui exactament: "El tipus del desert Aralkum és: [valor_del_tipus]".
3. Retornar un títol de nivell 2 (`<h2>`) amb el text: "Elevació de la muntanya Musala: [valor] metres".
4. Obtenir una llista ordenada (`<ol>` i `<li>`) de tots els codis IATA dels aeroports.
5. Generar una llista desordenada (`<ul>`) amb el nom de les muntanyes que pertanyen a la serralada anomenada "Balkan".
6. Retornar un paràgraf (`<p>`) amb el text "Latitud del Gobi: " seguit del valor de la latitud marcat en negreta (`<strong>`).
7. Obtenir el nom de l'aeroport que té l'atribut `city` igual a "cty-Yemen-Aden" dins d'una etiqueta d'encapçalament (`<h3>`).
8. Crear un element `<div>` que contingui el text: "Àrea del Great Sandy Desert: [valor]". *(Nota: Fes servir "Great Sandy Desert" per assegurar resultat)*.
9. Obtenir una llista (`<ul>`) on cada `<li>` contingui l'identificador (`id`) de cadascuna de les muntanyes.
10. Seleccionar el nom de tots els accidents geogràfics de tipus `<desert>` i retornar-los separats en etiquetes `<span>`.

## Nivell 2

11. Generar una llista desordenada (`<ul>`) amb el nom de les muntanyes que superen els 2500 metres d'elevació.
12. Construir una taula d'una sola columna (`<table>`, `<tr>`, `<td>`) amb el nom dels deserts que tenen una àrea superior a 100.000.
13. Generar una llista (`<ul>`) amb el nom dels aeroports que tenen un desplaçament horari (`gmtOffset`) negatiu (menor que 0).
14. Crear paràgrafs indiviudals (`<p>`) indicant "Desert de sorra: [nom]" per a tots els deserts que són de tipus "sand".
15. Obtenir el nom de les muntanyes situades al país amb codi "GR" (Grècia) dins de blocs `<blockquote>`.
16. Mostrar en una llista no ordenada (`<ul>`) els identificadors dels deserts que contenen la paraula "Erg" al seu nom.
17. Generar una llista (`<ol>`) amb el nom de les muntanyes que NO tenen assignada una serralada (no tenen l'element `<mountains>`).
18. Construir una taula (`<table>`) de dues columnes on a la primera es mostri el nom de l'aeroport i a la segona la seva elevació, per aquells aeroports que es troben a una elevació entre 100 i 500 metres.
19. Llistar dins de punts de vinyeta (`<li>`) el nom dels mars que limiten amb el "sea-Nordsee" (Mar del Nord).
20. Crear una llista (`<ul>`) indicant en cada ítem (`<li>`) el nom de les muntanyes que tenen una latitud major de 45.

### Nivell 3

21. Calcular quantes muntanyes hi ha registrades al fitxer i mostrar-ho en un sol paràgraf (`<p>`) que digui: "Total de muntanyes registrades: [quantitat]".
22. Calcular la suma total de l'àrea de tots els deserts i mostrar el resultat dins d'un encapçalament (`<h1>`).
23. Obtenir el nom de l'últim desert que apareix al document XML i formatar-ho dins d'un `<footer>`.
24. Obtenir el nom del desert que apareix immediatament abans del desert "Gobi" i retornar-ho com un text subratllat (`<u>`).
25. Obtenir l'identificador de l'element pare del nom "Kyllini" dins d'una etiqueta de codi (`<code>`).
26. Construir una taula (`<table>`) amb encapçalaments (`<th>`) per a "Element" i "Nom". Les files (`<tr>`) han de contenir a la primera columna el tipus d'element (el nom de l'etiqueta xml: sea, mountain, etc.) i a la segona el seu nom, per a tots aquells que tinguin un atribut `country` amb valor "F" (França).
27. Extreure tots els atributs del segon element `<located>` dins del mar "Atlantic Ocean" i mostrar-los agrupats dins d'un `<pre>`.
28. Crear una llista descriptiva (`<dl>`). Per cada desert que tingui definit un tipus (`@type`) i una àrea superior a 50000, crea un terme (`<dt>`) amb el nom del desert i una descripció (`<dd>`) indicant el seu tipus i àrea.
29. Obtenir el nom de l'aeroport que està llistat just després de l'aeroport "Aden Intl" formatat com a text en cursiva (`<i>`).
30. Generar una taula (`<table>`) per a les muntanyes on la longitud és menor que 20 o l'elevació és superior a 2800. La taula ha de tenir tres columnes: Nom, Longitud i Elevació.