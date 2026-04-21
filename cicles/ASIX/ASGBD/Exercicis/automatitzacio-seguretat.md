# Pràctica: Automatització, Seguretat i Integritat en PostgreSQL (Cas Pagila)

## Descripció de l'escenari
L'empresa de lloguer de pel·lícules **Pagila Video** vol modernitzar el seu sistema de gestió de dades. Actualment, el desplegament de l'entorn és manual, el control d'accessos és inexistent i no hi ha mecanismes que garanteixin la integritat de les dades davant d'errors humans.

Se t'ha encarregat crear un **sistema d'automatització integral** que permeti aixecar l'entorn de zero, configurar la seguretat i establir rutines de manteniment i integritat de dades.

---

## Requeriments de l'Exercici

### Bloc A: Desplegament i Infraestructura (Scripts Bash)
Has de crear un script orquestrador anomenat `configura.sh` que gestioni tot el procés d'instal·lació i configuració. 

* **Fase 0 (Preparació):** L'script ha de cridar un sub-script Bash (`00-prepara-pagila.sh`) que:
    * Faci un `git clone` del repositori oficial de Pagila (https://github.com/devrimgunduz/pagila.git).
    * Creï la base de dades `pagila` en local.
    * Carregui l'esquema (`pagila-schema.sql`) i les dades (`pagila-insert-data.sql`).
* **Fase de Configuració:** L'script ha d'executar seqüencialment els fitxers SQL emmagatzemats a la carpeta `scripts-sql/` (numerats del 01 al 04).
* **Traçabilitat:** Tota la sortida (estàndard i errors) s'ha de mostrar per pantalla i guardar-se simultàniament en un fitxer anomenat `configuracio-pagila.log`.
* **No Interactivitat:** No s'ha de demanar la contrasenya de l'usuari `postgres` de forma interactiva durant l'execució (utilitza fitxers de credencials o variables d'entorn segures).

### Bloc B: Control d'Accés i Rols (SQL)
Dins dels scripts SQL (`01-rols.sql`, `02-permisos.sql`, `03-vistes.sql`), cal implantar:
* **Definició d'usuaris:** Crea almenys dos usuaris (ex: `manager_user` i `staff_user`).
* **Agrupació de privilegis:** Crea rols de grup (ex: `grup_gerencia`, `grup_atencio`) i assigna els usuaris a aquests grups.
* **Privilegis detallats:** Defineix permisos de lectura i escriptura específics sobre taules clau com `film`, `rental` i `inventory`.
* **Vistes personalitzades:** Crea una vista per al personal de recepció que mostri títols de pel·lícules i disponibilitat sense mostrar dades sensibles de l'empresa.

### Bloc C: Integritat i Disparadors (Trigger)
Dins de l'script `04-triggers.sql`:
* **Lògica de Negoci:** Defineix un disparador (`TRIGGER`) que impedeixi que un client pugui llogar una pel·lícula si té deutes pendents o lloguers no retornats de fa més de 30 dies.
* **Estructures de control:** La funció associada al disparador ha d'estar escrita en **PL/pgSQL**, utilitzant estructures `IF/THEN` i llançant excepcions quan no es compleixin els requisits.

### Bloc D: Automatització del Manteniment
Crea un script independent `manteniment.sh` que realitzi tasques d'optimització (`VACUUM ANALYZE` i `REINDEX`) sobre les taules amb més trànsit de la base de dades. Aquest script també ha de generar el seu propi log d'execució.

---

## Lliurament
Heu de lliurar, al respositori de la tasca, la següent estructura:
1. `documentacio.md` on detalleu i expliqueu tot el que heu fet.
2. `configura.sh` (Script principal)
3. `manteniment.sh` (Script de manteniment)
4. Carpeta `scripts-sql/`:
    * `00-prepara-pagila.sh`
    * `01-rols.sql`
    * `02-permisos.sql`
    * `03-vistes.sql`
    * `04-triggers.sql`
5. `configuracio-pagila.log` (Evidència d'una execució correcta)
6. El link del repositori a la tasca de Moodle

---

## Rúbrica d'avaluació

| Criteri d'Avaluació | Pes | Excel·lent (100%) | Notable (75%) | Satisfactori (50%) | Insuficient (0%) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Instal·lació i Automatització (Pas 0)** | **2.5p** | L'script clona, crea i carrega la BDD sense errors. Gestió perfecta de fitxers temporals. **(+2.5p)** | L'script funciona, però no gestiona bé la neteja de carpetes o falla si la BDD ja existeix. **(+1.85p)** | La BDD es crea, però requereix algun ajust manual o el camí de fitxers és rígid. **(+1.25p)** | L'script no aconsegueix carregar l'esquema o les dades de GitHub. **(0p)** |
| **Gestió de Rols i Usuaris** | **2.0p** | Estructura clara: usuaris assignats a rols de grup. Mínim privilegi aplicat amb èxit. **(+2.0p)** | Crea usuaris i rols, però assigna alguns permisos directament a l'usuari (no al grup). **(+1.5p)** | Crea els usuaris, però la gestió de permisos és massa genèrica (ex: `ALL PRIVILEGES`). **(+1.0p)** | No crea els rols o els usuaris no tenen els permisos necessaris. **(0p)** |
| **Seguretat i Credencials** | **1.0p** | No demana contrasenya (ús de `.pgpass` o `PGPASSWORD`). L'script és 100% autònom. **(+1.0p)** | No demana contrasenya, però les credencials estan exposades de forma poc segura. **(+0.75p)** | Demana la contrasenya manualment en algun punt de l'execució. **(+0.5p)** | L'script s'atura constantment demanant credencials o falla per autenticació. **(0p)** |
| **Integritat (Triggers)** | **2.0p** | Trigger complex amb PL/pgSQL que controla la lògica de negoci. Missatges d'error clars. **(+2.0p)** | El trigger funciona però no gestiona bé tots els casos. **(+1.5p)** | El trigger existeix però dóna errors en certes condicions de prova. **(+1.0p)** | No hi ha triggers o la funció PL/pgSQL no s'executa correctament. **(0p)** |
| **Qualitat del Script Bash i Logs** | **1.5p** | Ús de colors, logs detallats, `PIPESTATUS` i `ON_ERROR_STOP`. Codi modular i net. **(+1.5p)** | L'script és funcional i té logs, però falta control d'errors en algun pas intermedi. **(+1.15p)** | L'script funciona però és una llista d'ordres sense estructura ni missatges d'estat. **(+0.75p)** | L'script no s'executa o no redirigeix la sortida al fitxer de log correcte. **(0p)** |
| **Manteniment (VACUUM/REINDEX)** | **1.0p** | Script de manteniment independent, ben documentat i optimitzat per a taules específiques. **(+1.0p)** | L'script de manteniment funciona però és massa genèric (sobre tota la BDD). **(+0.75p)** | Executa les comandes de manteniment però no mostra el progrés ni genera log. **(+0.5p)** | No s'ha lliurat l'script de manteniment o té errors de connexió. **(0p)** |
| **TOTAL** | **10p** | **10 Punts** | **7.5 Punts** | **5.0 Punts** | **0 Punts** |

---

### Penalitzacions i Bonificacions
* **Documentació (-1p):** Si el codi (Bash o SQL) no conté cap comentari explicatiu o si els comentaris no son vostres
* **Creativitat (+1p):** Si s'afegeixen funcionalitats extres com notificacions de finalització o logs amb rotació de dates.
