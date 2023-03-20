# tsuchigomori

tsuchigomori (土籠龍仁郎) is a simple tool for extracting the information from the german website "gelbe seiten". It is written with Python using the selenium framework. As a database it uses MySQL with the SQLAlchemy ORM for mapping the entries.
The name reference comes from the manga series Jibaku Shōnen Hanako-kun and represents the 5th myth.

## Start Developing

Start the MySQL container running on Port 3303 (3306 is often taken by the on system running MySQL server.)
```bash
docker-compose up
```