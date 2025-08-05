# Sistema Bancário - OOP e conceitos

Este projeto é a terceira versão do desafio "Sistema Bancário" da **Digital Innovation One (DIO)**. Nesta etapa, o sistema foi totalmente refatorado para utilizar os principais conceitos de orientação a objetos (OOP) em Python, tornando o código mais organizado, escalável e próximo de aplicações reais.

## 🚀 Principais Mudanças em Relação à Versão 2

- **Orientação a Objetos:**  
  O sistema agora utiliza classes para representar usuários, contas, banco, histórico e transações. Funções foram transformadas em métodos, e os dados são encapsulados em objetos.
- **Encapsulamento:**  
  Cada entidade (usuário, conta, banco, histórico) possui seus próprios atributos e métodos, protegendo e organizando melhor os dados.
- **Herança e Polimorfismo:**  
  Estrutura pronta para diferentes tipos de contas e transações, facilitando futuras expansões. Exemplo: `PessoaFisica` herda de `Cliente`, `Deposito` e `Saque` herdam de `Transacao`.
- **Classe Abstrata:**  
  A classe `Transacao` foi definida como abstrata, permitindo a implementação de diferentes tipos de transações (depósito, saque).
- **Classe Historico:**  
  Agora o extrato é gerenciado por uma classe própria (`Historico`), que armazena todas as transações realizadas na conta.
- **Menus e Fluxo:**  
  O fluxo de menus foi mantido, mas agora as operações são realizadas por métodos das classes, tornando o código mais limpo e intuitivo.
- **Código Modular:**  
  O código principal está em `logica.py`, podendo ser facilmente expandido para múltiplos arquivos e módulos.

## ✨ Funcionalidades

- Cadastro de usuários com CPF, nome, data de nascimento e endereço
- Criação de múltiplas contas por usuário
- Depósito e saque com controle de limites diários
- Consulta de extrato da conta (com histórico detalhado)
- Menus interativos via terminal

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- Não são necessárias bibliotecas externas

## 📂 Estrutura do Projeto

```
Sistema_bancario/
├── logica.py   # Lógica principal orientada a objetos
├── main.py     # Ponto de entrada do sistema
```

## 💻 Como Executar

1. Clone o repositório:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
2. Execute o sistema:
    ```bash
    python Sistema_bancario/main.py
    ```

## 🖱️ Como Usar

O sistema funciona por menus:
1. Crie ou acesse um usuário
2. Crie ou acesse uma conta
3. Realize depósitos, saques ou consulte o extrato

## 📚 Sobre o Desafio

Este projeto faz parte dos desafios práticos da DIO, evoluindo a cada versão para aplicar novos conceitos de programação e boas práticas de desenvolvimento.

## 📬 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gustavo-vitor-gutierrez-b520a2341/) 
[![Instagram](https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/gustavo.gutierreez/) 
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/+5511952018042)

---
Projeto desenvolvido para fins de estudo e evolução prática em Python.
