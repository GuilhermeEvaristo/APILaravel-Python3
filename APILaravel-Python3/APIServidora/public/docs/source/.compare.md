---
title: API Reference

language_tabs:
- bash
- javascript

includes:

search: true

toc_footers:
- <a href='http://github.com/mpociot/documentarian'>Documentation Powered by Documentarian</a>
---
<!-- START_INFO -->
# Info

Welcome to the generated API reference.
[Get Postman Collection](http://localhost/docs/collection.json)

<!-- END_INFO -->

#general
<!-- START_86e0ac5d4f8ce9853bc22fd08f2a0109 -->
## api/products
> Example request:

```bash
curl -X GET -G "http://localhost/api/products" 
```
```javascript
const url = new URL("http://localhost/api/products");

let headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

fetch(url, {
    method: "GET",
    headers: headers,
})
    .then(response => response.json())
    .then(json => console.log(json));
```

> Example response (200):

```json
{
    "data": {
        "current_page": 1,
        "data": [
            {
                "id": 1,
                "name": "Tyreek Stiedemann",
                "price": 4.37,
                "description": "Eum amet provident consectetur molestiae dignissimos. Exercitationem dignissimos velit est. Enim ut doloremque quia debitis et enim eligendi.",
                "created_at": "2019-05-31 17:44:15",
                "updated_at": "2019-05-31 17:44:15"
            },
            {
                "id": 2,
                "name": "Prof. Hershel Goldner",
                "price": 6.01,
                "description": "Sit nostrum id sapiente illo. Et optio saepe reprehenderit et quo. Reiciendis accusantium omnis architecto dolores aut omnis provident reprehenderit.",
                "created_at": "2019-05-31 17:44:16",
                "updated_at": "2019-05-31 17:44:16"
            },
            {
                "id": 3,
                "name": "Mr. Keyon Tillman",
                "price": 4.64,
                "description": "Et sed sed voluptatem et delectus. Fugit placeat ratione repellendus corporis. Impedit hic non quia quos. Laborum illo vel laborum nesciunt consequatur. Est aperiam molestias fugit laudantium.",
                "created_at": "2019-05-31 17:44:16",
                "updated_at": "2019-05-31 17:44:16"
            },
            {
                "id": 4,
                "name": "Damian Ortiz",
                "price": 5.6899999999999995,
                "description": "Inventore autem quam iusto ut. Et commodi dolor ut ab. Sed ad iure in earum et quae rerum autem. Molestiae corrupti iusto velit voluptatem.",
                "created_at": "2019-05-31 17:44:16",
                "updated_at": "2019-05-31 17:44:16"
            },
            {
                "id": 5,
                "name": "Kiana Predovic",
                "price": 4.8,
                "description": "Et eveniet nihil qui totam. Labore ab reprehenderit sint impedit qui ex. Ducimus quas odit velit iusto. Ab vel maiores est omnis. Ea nisi ab et et harum numquam.",
                "created_at": "2019-05-31 17:44:16",
                "updated_at": "2019-05-31 17:44:16"
            }
        ],
        "first_page_url": "http:\/\/localhost\/api\/products?page=1",
        "from": 1,
        "last_page": 2,
        "last_page_url": "http:\/\/localhost\/api\/products?page=2",
        "next_page_url": "http:\/\/localhost\/api\/products?page=2",
        "path": "http:\/\/localhost\/api\/products",
        "per_page": 5,
        "prev_page_url": null,
        "to": 5,
        "total": 10
    }
}
```

### HTTP Request
`GET api/products`


<!-- END_86e0ac5d4f8ce9853bc22fd08f2a0109 -->

<!-- START_d5a3d0c0add9ae4109a8d270310cf6c0 -->
## api/products/{id}
> Example request:

```bash
curl -X GET -G "http://localhost/api/products/1" 
```
```javascript
const url = new URL("http://localhost/api/products/1");

let headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

fetch(url, {
    method: "GET",
    headers: headers,
})
    .then(response => response.json())
    .then(json => console.log(json));
```

> Example response (200):

```json
{
    "id": {
        "id": 1,
        "name": "Tyreek Stiedemann",
        "price": 4.37,
        "description": "Eum amet provident consectetur molestiae dignissimos. Exercitationem dignissimos velit est. Enim ut doloremque quia debitis et enim eligendi.",
        "created_at": "2019-05-31 17:44:15",
        "updated_at": "2019-05-31 17:44:15"
    }
}
```

### HTTP Request
`GET api/products/{id}`


<!-- END_d5a3d0c0add9ae4109a8d270310cf6c0 -->

<!-- START_05b4383f00fd57c4828a831e7057e920 -->
## api/products
> Example request:

```bash
curl -X POST "http://localhost/api/products" 
```
```javascript
const url = new URL("http://localhost/api/products");

let headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

fetch(url, {
    method: "POST",
    headers: headers,
})
    .then(response => response.json())
    .then(json => console.log(json));
```


### HTTP Request
`POST api/products`


<!-- END_05b4383f00fd57c4828a831e7057e920 -->

<!-- START_241fd2204f9f5b65c7aa7c9618dcca22 -->
## api/products/{id}
> Example request:

```bash
curl -X PUT "http://localhost/api/products/1" 
```
```javascript
const url = new URL("http://localhost/api/products/1");

let headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

fetch(url, {
    method: "PUT",
    headers: headers,
})
    .then(response => response.json())
    .then(json => console.log(json));
```


### HTTP Request
`PUT api/products/{id}`


<!-- END_241fd2204f9f5b65c7aa7c9618dcca22 -->

<!-- START_160dac2b00e86335715987c6d1c1f3eb -->
## api/products/{id}
> Example request:

```bash
curl -X DELETE "http://localhost/api/products/1" 
```
```javascript
const url = new URL("http://localhost/api/products/1");

let headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

fetch(url, {
    method: "DELETE",
    headers: headers,
})
    .then(response => response.json())
    .then(json => console.log(json));
```


### HTTP Request
`DELETE api/products/{id}`


<!-- END_160dac2b00e86335715987c6d1c1f3eb -->


