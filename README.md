# s1-mvp-backend
Essa é a contra-parte do projeto [frontend](https://github.com/stephaniefay/s1-mvp-frontend/tree/main), contendo as rotas utilizadas pela SPA do projeto. Para mais detalhes das rotas o swagger foi instalado e está localizado no path raiz da API.

O projeto é uma API que contém informações detalhadas sobre coleções e cartas de um trading card game onde o Usuário poderá navegar e buscar informações relativas, além de poder adicioná-las à sua lista de desejos (`Wish` como é referenciado nos projetos)

Dados mockados foram gerados utilizando uma API pública em json e posteriormente convertido usando o seguinte [projeto](https://github.com/stephaniefay/json_reader/tree/master), a primeira execução pode ser um pouco mais demorada porque ele estará inicializando o banco com todas as informações necessárias para a real utilização da API.

## Como executar

Antes de qualquer coisa será necessário ter certeza de que você está com um `venv` ativo e funcional. No diretório raiz do projeto você encontrará um arquivo `requirements.txt` que contém todas as libs que foram utilizadas e precisarão ser instaladas.

```
$ pip install -r requirements.txt
```

Após as libs terem sido instaladas corretamente, você poderá executar a API utilizando o código abaixo e ela estará disponível no caminho [http://localhost:5000/#/](http://localhost:5000/#/).

```
$ flask run --host 0.0.0.0 --port 5000
```
