# 📢 EscolaVoz

**Sistema de Gestão de Demandas Escolares**

EscolaVoz é uma plataforma web para registro, acompanhamento e gestão de demandas de escolas da rede pública. O projeto nasce da necessidade de dar voz às escolas, um canal digital onde funcionários podem relatar necessidades do dia a dia e gestores podem acompanhar, priorizar e resolver cada solicitação de forma organizada e transparente.

Desenvolvido como projeto integrador da disciplina **DRP06 - Projeto Integrador em Computação I** (Turma 001).

---

## 🧭 Motivação

Em muitas redes de ensino, as solicitações das escolas ainda são feitas por meios informais, telefonemas, e-mails, papel impresso, o que dificulta o rastreamento, a priorização e a prestação de contas. O EscolaVoz surge para:

- **Centralizar** todas as demandas escolares em um único sistema
- **Dar visibilidade** ao andamento de cada solicitação
- **Organizar** por categorias (infraestrutura, merenda, pedagógico, etc.)
- **Empoderar** funcionários de escola a registrarem demandas de forma simples
- **Fornecer dados** para que gestores tomem decisões baseadas em evidências

---

## ✨ Funcionalidades

### 👤 Funcionário
- Autenticação segura via JWT
- Registro de novas demandas com descrição, categoria e escola
- Acompanhamento de suas próprias demandas em formato de cards
- Visualização do status atualizado em tempo real

### 👑 Administrador
- Dashboard com gráfico de demandas por escola e categoria
- Tabela completa de demandas com filtros (escola, categoria, status, período)
- Atualização de status (aberto, em andamento, resolvido, rejeitado)
- Cadastro e gerenciamento de funcionários
- Exportação de relatório CSV

---

## 🛠️ Stack Tecnológica

| Camada       | Tecnologia                                                  |
|-------------|-------------------------------------------------------------|
| **Frontend** | Nuxt 3 (Vue 3 + TypeScript) + Tailwind CSS + Pinia          |
| **Backend**  | Python 3.12 / Django 5 + Django REST Framework + SimpleJWT  |
| **Banco**    | MySQL 8.0                                                   |
| **Gráficos** | Chart.js + vue-chartjs                                      |
| **Infra**    | Docker + Docker Compose                                     |

---

## 🏗️ Arquitetura

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│   Frontend   │──────▶│   Backend    │──────▶│    MySQL     │
│  Nuxt 3 SPA  │       │  Django REST │       │              │
│   :3000      │◀──────│   :8000      │◀──────│   :3306      │
└──────────────┘       └──────────────┘       └──────────────┘
       │                      │
       │        JWT Auth      │
       └──────────────────────┘
```

- **Frontend** SPA (Single Page Application) consome a API REST
- **Backend** expõe endpoints protegidos por JWT
- **Autenticação** stateful no frontend (Pinia + localStorage) com guarda de rotas
- **Filtros** no backend via django-filter

---

## 🚀 Como Executar

### Com Docker (recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/escolavoz.git
cd escolavoz

# 2. Configure as variáveis de ambiente
cp .env.example .env

# 3. Inicie os serviços
docker compose up -d
```

Acesse:
- **Frontend**: http://localhost:3000
- **Backend (API)**: http://localhost:8000
- **Admin Django**: http://localhost:8000/admin/

### Sem Docker (desenvolvimento)

**Backend:**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend:**

```bash
cd frontend
npm install
npm run dev
```

> ⚠️ Ajuste `NUXT_PUBLIC_API_URL` no `.env` para apontar para o backend local.

---

## 📡 API Endpoints

| Método | Rota                            | Descrição                       | Autenticação |
|--------|--------------------------------|--------------------------------|-------------|
| POST   | `/api/auth/login/`              | Login (retorna JWT + perfil)    | ❌          |
| GET    | `/api/employees/`               | Listar funcionários             | ✅          |
| POST   | `/api/employees/`               | Criar funcionário               | ✅          |
| GET    | `/api/schools/`                 | Listar escolas                  | ✅          |
| GET    | `/api/categories/`              | Listar categorias               | ✅          |
| GET    | `/api/demands/`                 | Listar demandas                 | ✅          |
| POST   | `/api/demands/`                 | Criar demanda                   | ✅          |
| GET    | `/api/demands/my/`              | Minhas demandas                 | ✅          |
| PATCH  | `/api/demands/{id}/`            | Atualizar status                | ✅          |
| GET    | `/api/demands/export/csv/`      | Exportar CSV                    | ✅ (admin)  |

---

## 🗂️ Estrutura do Projeto

```
escolavoz/
├── backend/
│   ├── config/              # Configuração Django (settings, urls, wsgi)
│   ├── users/               # App de usuários e autenticação
│   ├── core/                # App principal (escolas, categorias, demandas)
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── components/          # Componentes reutilizáveis
│   ├── composables/         # Hooks (useApi)
│   ├── layouts/             # Layout padrão
│   ├── pages/               # Páginas (admin, funcionario, login)
│   ├── plugins/             # Plugin de guarda de autenticação
│   ├── stores/              # Pinia stores (auth, demands, schools)
│   ├── types/               # Tipos TypeScript
│   ├── nuxt.config.ts
│   ├── tailwind.config.ts
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── LICENSE
```

---

## 👤 Fluxo de Usuário

1. **Login** — Funcionário ou admin faz login com username e senha
2. **Role-based routing** — O sistema redireciona automaticamente:
   - **Admin** → Dashboard com gráficos e visão geral
   - **Funcionário** → Lista de suas demandas
3. **Criação de demanda** — Funcionário preenche formulário com descrição e categoria
4. **Acompanhamento** — Status visível em tempo real (aberto → em andamento → resolvido/rejeitado)
5. **Gestão** — Admin atualiza status, gerencia funcionários e exporta relatórios

---

## 📄 Licença

Distribuído sob licença MIT. Copyright © 2026 Elias Mateus.

---

<p align="center">
  <em>Dê voz à sua escola. 🎯</em>
</p>
