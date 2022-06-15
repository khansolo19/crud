# HTTP - Hyper Text Transfer Protocol


# Клиент ----> request ---> HTTP ----> request ----> SERVER
#                 <----- response  <-----

 
# CRUD       HTTP

# Create   --->  POST
# Read/Retrieve    ---> GET
# Update  ---> PUT/PATCH (PATCH - Partial Update)
# Delete  ---> DELETE


# import requests
# print(requests.get('http://3.125.115.120/').text)


# 1хх - информационные коды
# 2хх - SUCCESS
# 3xx - REDIRECTION
# 4xx - CLIENT ERROR
# 5xx - SERVER ERROR

'http://3.125.115.120/crud/products/'

# используемый протокол - http://
# имя сервера - 3.125.115.120/
# параметры - /crud/products/


# request
# GET / HTTP/1.1
# Host: 3.125.115.120/


# request
# GET /crud/products HTTP/1.1
# Host: 3.125.115.120/

# response
# HTTP/1.1 200 OK
# Date: Wed, 15 Jun 2022 08:44:10 GMT
# Server: nginx/1.18.0 (Ubuntu)

# 'keydGwz8zs6pfYQEo'




