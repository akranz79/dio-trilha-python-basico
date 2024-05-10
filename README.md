## Entendendo o Desafio 🚀✨
#### Agora é a sua hora de brilhar e construir um perfil de destaque na DIO! Explore todos os conceitos explorados até aqui e replique (ou melhore, porque não?) este projeto prático. Para isso, crie seu próprio repositório e aumente ainda mais seu portfólio de projetos no GitHub, o qual pode fazer toda diferença em suas entrevistas técnicas 😎

#### Já dominamos o universo do desenvolvimento Python e projeto "Criando um Sistema Bancário com Python" oferece uma experiência prática de desenvolvimento de software financeiro. Os participantes construirão um sistema completo, abordando funcionalidades como criação de contas, transações e segurança. É uma oportunidade para aprimorar habilidades de programação Python e compreender conceitos financeiros e de segurança.

### 1º - O código desenvolvido implementa um sistema simples de gerenciamento de contas bancárias, com as seguintes funcionalidades: 
### 👉 [desafio 1](https://github.com/akranz79/dio-trilha-python-basico/blob/main/desafio.py)

- Depósito: Permite ao usuário depositar um valor em sua conta.
- Saque: Permite ao usuário sacar um valor de sua conta, desde que não exceda o saldo disponível, o limite de saques ou o limite de saldo.
- Extrato: Mostra ao usuário um extrato das transações realizadas em sua conta, incluindo depósitos e saques, além do saldo atual.
- Sair: Permite ao usuário sair do programa.

### 2º - Atualizações do código:
### 👉 [desafio 2](https://github.com/akranz79/dio-trilha-python-basico/blob/main/desafio02.py)

Vamos analisar o código e suas funcionalidades:

### Funcionalidades do Código Anterior:
- O código permite ao usuário realizar operações básicas em uma conta bancária, como depósito, saque e visualização de extrato.
- Ele possui um loop while que continua executando até que o usuário selecione a opção "Sair".
- Para cada opção do menu, ele executa uma série de verificações e operações.

### Atualizações Referentes ao Primeiro Desafio:

- As funcionalidades de depósito, saque e visualização de extrato foram separadas em funções: depositar, sacar e extrato.
- Para cada uma dessas funções, foram estabelecidos os modos de passagem de argumentos conforme solicitado: <br>
#### depositar: Recebe os argumentos apenas por posição. <br>
#### sacar: Recebe os argumentos apenas por nome (keyword only). <br>
#### extrato: Recebe os argumentos por posição e nome (positional only e keyword only). <br>
- Além disso, duas novas funções foram adicionadas:
cadastrar_usuario: Permite cadastrar usuários com nome, data de nascimento, CPF e endereço, garantindo que não haja CPFs duplicados. <br>
criar_conta_corrente: Cria contas correntes com agência fixa ("0001"), número sequencial e vincula a um usuário existente. <br>

Essas atualizações deixam o código mais organizado, modularizado e mais fácil de entender. Agora ele segue o princípio do "single responsibility", onde cada função executa uma única tarefa específica.

### 3º - Atualizações Referentes ao desafio POO: 

### 👉 [desafio 1](https://github.com/akranz79/dio-trilha-python-basico/blob/main/desafio03.py)
### 👉 [desafio 2](https://github.com/akranz79/dio-trilha-python-basico/blob/main/desafio03p2.py)

Neste desafio iremos atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML. <br>

Python


---
<br />

<a href="https://github.com/akranz79/"><img src="https://github.com/akranz79/akranz79/blob/main/img/img2.png" width="100px;" alt="" /> </a>
 
[![Linkedin Badge](https://img.shields.io/badge/-Alexandre-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/akranz/)](https://www.linkedin.com/in/akranz/)
[![Gmail Badge](https://img.shields.io/badge/-ahkranz79@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ahkranz79@gmail.com)](mailto:ahkranz79@gmail.com)

⚙ O desenvolvimento de software é uma arte em constante evolução - nunca se contente com o suficiente. ⚙
