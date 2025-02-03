# Clima-API
# Coletor de Dados Meteorológicos

Este projeto coleta dados climáticos de três cidades utilizando a API do HG Brasil e os armazena em um banco de dados PostgreSQL no Render. Ele realiza a extração dos dados, transforma as informações relevantes e as insere em uma tabela chamada clima_cidade, para depois essas informações serem colocadas dentro de um dashboard no Power BI.

## Funcionalidades
- Conexão segura com o banco de dados via SQLAlchemy e Psycopg2-binary
- Coleta de dados meteorológicos para cidades predefinidas
- Limpeza da tabela antes da inserção de novos registros
- Armazenamento estruturado dos dados no banco

## Tecnologias Utilizadas
- Python: Linguagem principal do projeto
- SQLAlchemy: Conexão com o banco de dados
- Requests: Consumo da API externa
- Dotenv: Gerenciamento de credenciais via variáveis de ambiente
- Unidecode: Tratamento de erro com string  
- Psycopg2-binary: Fazer a conexão do banco de dados via Python
                                                                                                                                                                            
   

## Melhorias Implementadas
Depois de rodar o código várias vezes, algumas melhorias foram feitas:

### 1. Evitar definição de funções dentro do loop
Problema: Antes, extracao() e transforma_dados() eram recriadas a cada iteração, gerando ineficiência.  
Solução: Agora, essas funções são declaradas uma vez e chamadas conforme necessário.

### 2. Melhor gerenciamento da conexão com o banco
Problema: A conexão com o banco ficava aberta o tempo todo, podendo gerar vazamento de conexões.  
Solução: Agora, with é usado para garantir que a conexão e o cursor sejam fechados corretamente após o uso.

### 3. Melhor uso do if _name_ == "_main_"
Problema: Esse bloco estava dentro do loop, o que não faz sentido.  
Solução: Ele foi movido para o final do arquivo para garantir a correta execução do script.

### 4. Tratamento de erros na API
Problema: Se a API falhasse, o script quebrava.  
Solução: Agora, try-except é usado para capturar erros de rede e evitar que o programa pare inesperadamente.


## Análises Possíveis com os Dados
Com os dados armazenados no banco, podemos gerar insights valiosos, como:
- Tendência de temperatura ao longo do tempo
- Padrões meteorológicos entre diferentes cidades
- Correlação entre hora do dia e variações de temperatura


## Contribuição
Se você quiser melhorar esse projeto, fique à vontade para abrir uma issue ou enviar um pull request!

## Contato

[<img src="https://avatars.githubusercontent.com/u/107763276?v=4" width=115> <br> <sub>Robert Ferreira Dantas</sub>](https://github.com/RobertFerreiraDantas)  
<br>
Caso tenha alguma dúvida ou sugestão, por favor entre em contato via [email](mailto:robertferreira1198@gmail.com).

<div>
  <a href="https://www.linkedin.com/in/robert-ferreira-b1324329a/" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
  </a>
</div>
