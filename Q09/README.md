## Testar Identificador de Triângulo - Selenium - Unittest

### Build imagem

#### Dependencias

```docker
docker build -t selenium-python .
```
#### Run container

```docker
docker run -d -p 4444:4444 selenium-python
```

#### Verificar o ID do container

```docker
docker ps
```


#### Executar testes no container

```docker
docker exec -it <container_id> python3 -m unittest -v
```