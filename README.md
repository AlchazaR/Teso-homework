# Tesonet užduotis
## Serverio paruošimas:
Saugumui padidinti buvo atlikti šie pakeitimai:
* Sukurtas naujas vartotojas - akaroot
* Priskirtas sudo grupei
* Uždraustas root prisijungimas (SSH + pakeistas shell'as į nologin)
* Sukonfigutuotas public key prisijungimas per SSH
* Atjungta galimybė jungtis per SSH su slaptažodžiu
* Aktyvotas komandų loginimas + log rotation - /var/log/commands.log
* Sukonfiguruotas ir aktyvuotas FW, palikti tik 22, 80, 443 portai

	
Sudiegtas Nginx:
* Sukonfiguruotas Let's encript sertifikatas
* Sukonfiguriotas reverse proxy
* Norint padaryti 2FA buvo paruoštas kliento sertifikatas - su juo iškylo problemu, dėl laiko stokos jo konfiguravimas nebuvo užbaigtas. Sertifikatai sudėti /etc/nginx/client-certs 


## API:
Panaudotas Python + Flask
### Flask moduliai:
* flask-login
* flask-migrate
* flask-pymongo
* flask-wtf

### API:
 /login - login puslapis
 /logout - vartotojo sesijos nutraukimas
 /manage - Vartotojų administravimas
 
Metodas |    URL                           | Komentaras
--------|----------------------------------|-----------------------------
POST    | /adduser/_user_/_email_/_passwd_ | naujo vartotojo sukurimas
GET     | /search/_id_                     | el. pašto paieška
GET     | /bulksearch                      | el. pašto paiešką iš sąrašo


