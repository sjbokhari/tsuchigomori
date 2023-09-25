
![Logo](https://www.nautiljon.com/images/manga_persos/00/36/tsuchigomori_8563.webp?0)


# tsuchigomori

tsuchigomori (土籠龍仁郎) is a simple tool for extracting the information from the german website "gelbe seiten". It is a diffrent type of API. Written with Go using colly for scraping. As a database it uses MySQL with the Gorm ORM for mapping the entries. As API it would be fitting to choose echo. It is in planing to include a kinda admin page for interacting on a nice enviroment.

The name reference comes from the manga series Jibaku Shōnen Hanako-kun (地縛少年花子くん) and represents the 5th myth. As well the wordplay for the number 5 (五, go) and the main language golang to be used. 

<!-- ## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Please Create an ```.env``` file or rename the ```.env.example``and fill in the following fields:

|Field| Example Values
|---|---|
| `MYSQL_URL`  |  localhost |
| `MYSQL_PORT`  | 3303  |
| `MYSQL_USER` |  root |
| `MYSQL_PASSWORD` | SECUREPASSWORD  |
| `MYSQL_DATABASE` |  gobase |


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

To deploy this project ... please wait :) TBA -->



## Support

For support, email to shehryar@bokhari.de


## License

[GNU General Public License](./LICENSE)


## Authors

- [@sjbokhari](https://www.github.com/sjbokhari)
- [usmanmalik](https://www.github.com)

