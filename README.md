# Tesonet užduotis
## Serverio paruošimas:
Saugumui padidinti buvo atlikti šie pakeitimai:
* Sukurtas naujas vartotojas - akaroot
* Priskirtas sudo grupei
* Uždraustas root prisijungimas (SSH + pakeistas shell'as į nologin)
* Sukonfigūruotas public key prisijungimas per SSH
* Atjungta galimybė jungtis per SSH su slaptažodžiu
* Aktyvuotas komandų loginimas + log rotation - /var/log/commands.log
* Sukonfigūruotas ir aktyvuotas FW, palikti tik 22, 80, 443 portai

Papildomai galima pasinaudoti port knocking ir taip paslėpti SSH nuo skenavimų. 
Taip pat apsaugai padidinti galima sudiegti Snort ir sukonfigūruoti, kad jis blokuotu IP adresus iš kuriu bandoma skenuoti pvz. 80, 443, 22 portus.

	
Sudiegtas Nginx:
* Sukonfigūruotas Let's encript sertifikatas
* Sukonfigūruotas reverse proxy
* Padarytas 2FA. Paruoštas kliento sertifikatas ir padaryta nginx konfigūracija. Sertifikatai sudėti /etc/nginx/client_certs 


## API
Panaudotas Python + Flask
### Flask moduliai:
* flask-login
* flask-migrate
* flask-pymongo
* flask-wtf
* flask-sqlalchemy

### API:
 /login - login puslapis
 /logout - vartotojo sesijos nutraukimas
 /manage - Vartotojų administravimas
 
Metodas |    URL                           | Komentaras
--------|----------------------------------|-----------------------------
POST    | /adduser/_user_/_email_/_passwd_ | naujo vartotojo sukurimas
GET     | /search/_id_                     | el. pašto paieška
GET     | /bulksearch/_id-list_            | el. pašto paiešką iš sąrašo (comma separated)


## Komentarai
1. API vartotojams saugoti panaudota SQLite duomenų baze. Mano manymu produkcijai toks sprendimas nėra pats tinkamiausias, jis labiau tinka testavimams atlikti kadangi nereikalauja jokiu papildomu diegimo ir konfigūravimo darbų.
2. Nėra numatyta el. pašto adresų paieška, kuriose naudojamas + simbolis. Tokiu atveju reikėtu naudoti regular expression arba galvoti kitą - greitesni sprendimą. Pvz. atlikti paiešką pagal pirmą el. pašto dalį (iki @) ir gautame sąraše ieškoti el. pašto su + simboliu.
3. Dėl dingusios prieigos prie mongoDB nepavyko su ją padirbti.
