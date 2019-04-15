## Número por Extenso

### Subindo o servidor com Docker
Gerando a imagem:  
`docker build -t numero_por_extenso .`

Rodando o container:  
`docker run -p 3000:3000 numero_por_extenso`

Acesse:  
`localhost:3000/-123`  
`localhost:3000/2019`  

### Subindo servidor sem Docker
Requerimentos:  
* python 3.6+  
1) `pip install pipenv`  
2) `pipenv shell`  
3) `pipenv install`  
4) `./manage.py runserver 0.0.0.0:3000`  


### Rodando os testes unitários
`pytest`  
ou  
`./manage.py test`
