# Pulse - Soluções em IA

Página web profissional desenvolvida em Django para a empresa Pulse, especializada em soluções de inteligência artificial.

## 📋 Características

- **Design Responsivo**: Interface moderna e adaptável para todos os dispositivos
- **Múltiplas Páginas**: Início, Serviços, Sobre e Contato
- **Formulário de Contato**: Sistema funcional para receber mensagens de clientes
- **Integração com Redes Sociais**: Links para Instagram (@pulse)
- **Otimizado para SEO**: Meta tags e estrutura semântica
- **Animações Suaves**: Transições e efeitos visuais profissionais

## 🚀 Tecnologias Utilizadas

- **Backend**: Django 5.2.10
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (desenvolvimento)
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Poppins)

## 📁 Estrutura do Projeto

```
pulse_project/
├── pulse_project/          # Configurações principais do Django
│   ├── settings.py           # Configurações do projeto
│   ├── urls.py              # URLs principais
│   └── wsgi.py              # WSGI para produção
├── home/                      # Aplicação principal
│   ├── views.py             # Views das páginas
│   ├── urls.py              # URLs da aplicação
│   └── templates/           # Templates HTML
├── templates/                 # Templates base
│   └── home/
│       ├── base.html        # Template base com header/footer
│       ├── index.html       # Página inicial
│       ├── servicos.html    # Página de serviços
│       ├── sobre.html       # Página sobre
│       └── contato.html     # Página de contato
├── static/                    # Arquivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py                  # Script de gerenciamento Django
└── db.sqlite3                # Banco de dados (desenvolvimento)
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone ou extraia o projeto**
   ```bash
   cd pulse_project
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install django djangorestframework django-cors-headers pillow
   ```

4. **Execute as migrações**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação**
   - Abra seu navegador e vá para: `http://localhost:8000`

## 📄 Páginas Disponíveis

### Página Inicial (`/`)
- Hero section com chamada para ação
- Apresentação dos 4 serviços principais
- Seção de diferenciais da empresa
- CTA para contato

### Serviços (`/servicos/`)
- Descrição detalhada de cada serviço
- Benefícios e características
- Processo de implementação
- Chamada para agendamento

### Sobre (`/sobre/`)
- Missão, Visão e Valores
- Informações sobre a empresa
- Diferenciais competitivos
- Informações de localização

### Contato (`/contato/`)
- Formulário de contato funcional
- Informações de localização
- Horário de atendimento
- Mapa interativo
- Links para redes sociais

## 🎨 Personalização

### Cores Principais
- **Primária**: `#0066cc` (Azul)
- **Secundária**: `#00d4ff` (Ciano)
- **Escura**: `#1a1a2e` (Azul escuro)
- **Clara**: `#f5f7fa` (Cinza claro)

### Modificar Informações da Empresa

Edite o arquivo `home/views.py` para atualizar:
- Nome da empresa
- Descrição dos serviços
- Endereço
- Redes sociais

### Adicionar Novas Páginas

1. Crie uma nova view em `home/views.py`
2. Adicione a URL em `home/urls.py`
3. Crie o template correspondente em `templates/home/`
4. Adicione o link no menu de navegação em `base.html`

## 📧 Formulário de Contato

O formulário de contato está integrado com JavaScript para envio via AJAX. As mensagens podem ser:

1. **Salvadas em banco de dados** (criar modelo Contact)
2. **Enviadas por email** (configurar SMTP)
3. **Armazenadas em serviço externo** (integrar com serviços como SendGrid)

### Configurar Envio de Email

Adicione ao `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'seu-smtp-host.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@example.com'
EMAIL_HOST_PASSWORD = 'sua-senha'
DEFAULT_FROM_EMAIL = 'seu-email@example.com'
```

## 🚀 Deploy em Produção

### Opção 1: Heroku

1. Instale o Heroku CLI
2. Crie um arquivo `Procfile`:
   ```
   web: gunicorn pulse_project.wsgi
   ```
3. Crie um arquivo `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
4. Deploy:
   ```bash
   heroku create seu-app-name
   git push heroku main
   ```

### Opção 2: PythonAnywhere

1. Faça upload dos arquivos
2. Configure o WSGI
3. Defina as variáveis de ambiente
4. Reinicie a aplicação

### Opção 3: Servidor VPS (DigitalOcean, AWS, etc.)

1. Configure Nginx como proxy reverso
2. Use Gunicorn como servidor WSGI
3. Configure SSL com Let's Encrypt
4. Configure banco de dados PostgreSQL

### Checklist de Produção

- [ ] Defina `DEBUG = False` em `settings.py`
- [ ] Configure `ALLOWED_HOSTS` com seu domínio
- [ ] Gere uma nova `SECRET_KEY`
- [ ] Configure HTTPS/SSL
- [ ] Configure banco de dados PostgreSQL
- [ ] Configure variáveis de ambiente
- [ ] Execute `python manage.py collectstatic`
- [ ] Configure backups automáticos

## 🔧 Comandos Úteis

```bash
# Criar superusuário para admin
python manage.py createsuperuser

# Acessar painel admin
# http://localhost:8000/admin

# Coletar arquivos estáticos
python manage.py collectstatic

# Criar nova app
python manage.py startapp nome_app

# Fazer dump do banco de dados
python manage.py dumpdata > backup.json

# Restaurar banco de dados
python manage.py loaddata backup.json

# Executar testes
python manage.py test

# Shell interativo Django
python manage.py shell
```

## 📱 Responsividade

O site é totalmente responsivo e funciona perfeitamente em:
- Desktop (1920px+)
- Tablet (768px - 1024px)
- Mobile (320px - 767px)

## 🔐 Segurança

- CSRF protection ativado
- XSS protection
- SQL injection protection
- Headers de segurança configurados

## 📞 Informações de Contato

**Pulse - Soluções em IA**

- 📱 Instagram: [@pulse](https://instagram.com/pulse)

## 📝 Licença

Este projeto é propriedade da Pulse.

## 🤝 Suporte

Para suporte e dúvidas, entre em contato através do formulário no site ou pelo Instagram.

---

**Desenvolvido com ❤️ para Pulse**


