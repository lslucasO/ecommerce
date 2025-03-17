# E-commerce com Django 🛒

Este projeto é um e-commerce totalmente responsivo desenvolvido com Django no backend e Bootstrap no frontend. Ele foi criado para aprofundar conhecimentos e consolidar o aprendizado em desenvolvimento web, explorando conceitos como autenticação de usuários, manipulação dinâmica de dados no frontend com AJAX e gerenciamento de produtos e usuários.

## 📌 Funcionalidades

### 👥 Usuário:
- ✅ Cadastro e login com autenticação e validação
- ✅ Carrinho de compras dinâmico (adicionar, remover e editar quantidade)
- ✅ Avaliação de produtos na loja
- ✅ Página de perfil para visualizar suas informações e avaliações

### 🔧 Admin:
- 📊 Dashboard de administração
- 👤 Gerenciamento de usuários
- 📦 Controle de produtos e avaliações

## 🛠️ Tecnologias utilizadas

- **Frontend:** HTML | CSS | JavaScript (AJAX) | Bootstrap 5
- **Backend:** Python | Django

## 🚀 Como instalar e rodar o projeto

### 1️⃣ Pré-requisitos
Antes de começar, certifique-se de ter instalado:
- Python (>=3.8)
- Git
- Virtualenv
- Banco de dados SQLite (padrão) ou PostgreSQL (opcional)

### 2️⃣ Clonando o repositório
```bash
 git clone https://github.com/seu-usuario/seu-repositorio.git
 cd seu-repositorio
```

### 3️⃣ Criando e ativando o ambiente virtual
```bash
 python -m venv venv  # Criando o ambiente virtual
 source venv/bin/activate  # No Linux/macOS
 venv\Scripts\activate  # No Windows
```

### 4️⃣ Instalando as dependências
```bash
 pip install -r requirements.txt
```

### 5️⃣ Configurando o banco de dados
Rodar as migrações:
```bash
 python manage.py migrate
```

### 6️⃣ Criando um superusuário para acessar o painel administrativo
```bash
 python manage.py createsuperuser
```
Siga as instruções para criar o usuário.

### 7️⃣ Rodando o servidor localmente
```bash
 python manage.py runserver
```
O projeto estará disponível em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para modificá-lo e utilizá-lo da melhor forma para seus estudos ou projetos pessoais!

---


![Home](https://github.com/user-attachments/assets/0c90e073-2bb9-4b93-a98e-995386478705)

![Avaliações](https://github.com/user-attachments/assets/f80c62c1-8367-40dd-83a6-58cf497ece51)



