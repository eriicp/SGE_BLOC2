# SGE_BLOC2
![image](https://github.com/user-attachments/assets/533bd0cd-b515-454b-a18c-1a0994285d12)

El primer que fem es connectar-nos a la base de dades de PostgreSQL utilitzant el fitxer connect.py, que utilitza una connexio amb psycopg2 que ens ajuda a connectar python amb PostgreSQL.

![Captura de pantalla 2025-02-04 084523](https://github.com/user-attachments/assets/b0acffa6-4e1e-4687-ad62-886e60963240)

En aquesta imatge veiem com despres de crear la taula fent servir sql al arxiu CREATE_TABE_TO_DB, hem transformat l'informacio del csv a format diccionari per a poder introduirla a la base de dades. 

![Captura de pantalla 2025-02-04 084456](https://github.com/user-attachments/assets/3724db72-d61e-4223-b47d-81c559942f7d)

Despres executem l'arxiu DICT_TO_DB per a introduir aquesta informacio i podem veure que ja la tenim a la base de dades.

![image](https://github.com/user-attachments/assets/c38c327f-af1b-4096-bae9-bfbc8e5a017d)

Amb l'arxiu CREATE_REGISTRE podem afegir registres d'un en un, fent insert amb sql, en aquest cas hem afegit al client Roger.

![image](https://github.com/user-attachments/assets/eda11778-500d-4925-bd39-620b43f18ed8)

Amb l'arxiu READ_REGISTRE podem veure les dades que tenim a la base de dades.

![image](https://github.com/user-attachments/assets/aa2d5e26-af56-459a-8a77-57a810e66b25)

Amb l'arxiu UPDATE_REGISTRE podem modificar els valors de les files ja inserides, en aquest cas hem cambiar el telefon Roger.

![image](https://github.com/user-attachments/assets/e61c3deb-bc58-4503-893b-8cc66aeb3c62)

Amb l'arxiu DELETE_REGISTRE podem borrar els registres, en aquest cas hem borrat a Veronica.
