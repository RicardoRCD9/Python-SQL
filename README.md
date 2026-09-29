# Python + MySQL

Projeto desenvolvido em Python com integração ao MySQL para gerenciamento de uma biblioteca pessoal de jogos concluídos.

A aplicação permite cadastrar, consultar, editar e excluir registros de jogos por meio de um menu interativo no terminal.

## Tecnologias utilizadas

* Python
* MySQL
* mysql-connector-python
* python-dotenv

## Funcionalidades

* Conexão com banco de dados MySQL
* Cadastro de jogos
* Consulta de jogos cadastrados
* Edição de registros
* Exclusão de registros
* Registro de horas jogadas
* Registro de conclusão 100% (platina)
* Validação de dados informados pelo usuário
* Menu interativo no terminal

## Operações realizadas no banco de dados

* `INSERT` — cadastro de novos jogos
* `SELECT` — consulta dos jogos cadastrados
* `UPDATE` — edição de registros
* `DELETE` — exclusão de registros

## Segurança

As credenciais de acesso ao banco de dados são armazenadas em variáveis de ambiente utilizando um arquivo `.env`, que não é enviado ao GitHub.
