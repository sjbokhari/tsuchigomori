
<!-- ![Logo](https://www.nautiljon.com/images/manga_persos/00/36/tsuchigomori_8563.webp?0) -->


# tsuchigomori

tsuchigomori (土籠龍仁郎) is a simple tool for extracting the information from the german website "gelbe seiten". It is a diffrent type of API. Written with Python using the selenium framework. As a database it uses MySQL with the SQLAlchemy ORM for mapping the entries.

The name reference comes from the manga series Jibaku Shōnen Hanako-kun and represents the 5th myth.
## Tech Stack

**Client:** TBA

**Server:** Python, FastAPI, Selenium, SQLAlchemy

**Database:** MySQL


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Please Create an ```.env``` file and fill the following fields:

|Field| Example Values  
|---|---|
| `MYSQL_URL`  |  localhost |  
| `MYSQL_PORT`  | 3303  |  
| `MYSQL_USER |  root |
| `MYSQL_PASSWORD` | SECUREPASSWORD  |
| `MYSQL_DATABASE` |  pybase |


## Usage

Start the MySQL container running on Port 3303 (3306 is often taken by the on system running MySQL server.)
```bash
docker-compose up
```



## API Reference (NOT FINAL)

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Deployment

To deploy this project ... please wait :) TBA



## Support

For support, email to shehryar@bokhari.de


## License

[TBA](https://choosealicense.com/licenses/)


## Authors

- [@sjbokhari](https://www.github.com/sjbokhari)

