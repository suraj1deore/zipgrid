
# Ecommerce admin panel 

create an e-commerce admin panel, we need to define an admin screen and order screen wherever Admin can make the order on a phone call and book the order in screen.




## Documentation
1. Goals:
```bash
  create an e-commerce admin panel, to define an admin screen and order screen wherever Admin can make the order on a phone call and book the order in screen.
```
2. Database design:
```bash
Brand
Category
Product
Create relations between Brand, Category and Product
```
3. Web application design:
```bash
    Create a functinallity that Admin create order
    Create a functinallity that Admin can book order
```

## Deployment

To run amulated server 

```windwos powershell
 python manage.py runserver
```
To map with the templates please add template path to DIRS as smention below

```
 TEMPLATES = [
     'DIRS': ['C:\\Users\\Mansi.P\\Desktop\\Korlek Client\\Clientinvoice\\templates'],
 ]
```


## Environment Variables


`SECRET_KEY`

`DEBUG`

Find admin login details in .env file

url = 'localhost/admin'

## Installation

Install Django Framework for creating Ecommerce project

```bash
  python -m pip install Django 
  ```
Install decouple for enviornment variables
```bash
  pip install python-decouple
```
    