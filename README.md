# 📋 Gerenciador de Tarefas (To-Do List) - AV2 POO

Projeto desenvolvido como requisito avaliativo da 2ª Avaliação (AV2) da disciplina de **Programação Orientada a Objetos**, do curso de Análise e Desenvolvimento de Sistemas.

O sistema consiste em uma aplicação web desenvolvida em **Django** para gerenciamento de tarefas, implementando o padrão CRUD (Create, Read, Update, Delete) e relacionamentos entre tabelas (Categorias e Tarefas), utilizando **Class Based Views**.

---

## 👥 Equipe de Desenvolvimento

| Nome | Matrícula |
| :--- | :--- |
| **Mateus Pacífico Alves de Castro** | 01795693 |
| **Guilherme Nascimento da Silva** | 01798743 |
| **Maria Tainá de Miranda Feitosa** | 01792213 |
| **Maria Lara de Miranda Rodrigues** | 01849204 |
| **Sara Beatriz Silva Oliveira** | 01792477 |
| **Adiel Alves Sousa** | 01812909 |

---

## 🚀 Funcionalidades

* **Cadastro de Tarefas:** Criação de tarefas com título, descrição, data de conclusão e categoria.
* **Listagem Dinâmica:** Visualização de todas as tarefas com indicadores de status (Pendente/Feito).
* **Edição:** Atualização de dados de tarefas existentes.
* **Exclusão:** Remoção de tarefas do banco de dados.
* **Categorização:** Organização de tarefas por categorias (ex: Trabalho, Faculdade, Pessoal).
* **Interface Responsiva:** Layout estilizado com **Bootstrap 5 (Tema Cyborg)** e personalização em modo escuro/neon.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Framework:** Django 6.0
* **Banco de Dados:** SQLite3 (Padrão do Django)
* **Front-end:** HTML5, CSS3, Bootstrap 5 (Bootswatch Cyborg)
* **Estilização:** Custom CSS (Dark Mode + Neon Green)

---

## 📂 Estrutura do Projeto

O projeto segue a arquitetura MVT (Model-View-Template) do Django e contém 2 Models principais:

1.  **Categoria:** Define os tipos de tarefas (Relacionamento 1:N).
2.  **Tarefa:** Contém os dados da atividade e o status de conclusão.

---

## ⚙️ Como Rodar o Projeto

Pré-requisitos: Ter o **Python** instalado na máquina.

### 1. Clone o repositório ou extraia os arquivos
Entre na pasta do projeto via terminal:
```bash
cd nome-da-pasta-do-projeto
