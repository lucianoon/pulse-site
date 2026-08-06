# Guia de Deploy - Pulse

Este documento contém instruções detalhadas para fazer deploy da aplicação Pulse em diferentes plataformas.

## 📋 Pré-requisitos

- Git instalado
- Conta em uma plataforma de hosting (Heroku, PythonAnywhere, AWS, DigitalOcean, etc.)
- Variáveis de ambiente configuradas

## 🚀 Deploy no Heroku (Recomendado para Iniciantes)

### Passo 1: Instalar Heroku CLI
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Windows
# Baixe em: https://devcenter.heroku.com/articles/heroku-cli

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

### Passo 2: Fazer Login
```bash
heroku login
```

### Passo 3: Criar Aplicação no Heroku
```bash
heroku create pulse-site
```

### Passo 4: Configurar Variáveis de Ambiente
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY='sua-chave-secreta-super-segura'
heroku config:set ALLOWED_HOSTS='pulse-site.herokuapp.com'
```

### Passo 5: Fazer Deploy
```bash
git push heroku main
```

### Passo 6: Executar Migrações
```bash
heroku run python manage.py migrate
```

### Passo 7: Criar Superusuário (Opcional)
```bash
heroku run python manage.py createsuperuser
```

## 🐳 Deploy com Docker

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "pulse_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=sua-chave-secreta
      - ALLOWED_HOSTS=localhost,127.0.0.1
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=pulse_db
      - POSTGRES_USER=pulse_user
      - POSTGRES_PASSWORD=sua-senha-segura
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Executar com Docker
```bash
docker-compose up -d
docker-compose exec web python manage.py migrate
```

## 🚈 Deploy no Railway (Altamente Recomendado)

O Railway é uma das formas mais modernas e fáceis de hospedar Django hoje, sendo o sucessor espiritual do Heroku (com melhor custo-benefício).

### Passo 1: Conectar GitHub
- Crie um repositório no GitHub e faça o push do seu código.
- No Railway, clique em "New Project" > "Deploy from GitHub repo".

### Passo 2: Adicionar Banco de Dados
- Clique em "Add Service" > "Database" > "Add PostgreSQL".
- O Railway injetará automaticamente a variável `DATABASE_URL`.

### Passo 3: Configurar Variáveis de Ambiente
No painel do Railway, adicione:
- `DEBUG=False`
- `SECRET_KEY=sua-chave-secreta`
- `ALLOWED_HOSTS=seu-app.railway.app`

### Passo 4: Arquivo `Procfile`
Certifique-se de que o arquivo `Procfile` na raiz contém:
```
web: gunicorn pulse_project.wsgi
```

## ☁️ Deploy no PythonAnywhere

### Passo 1: Criar Conta
Acesse: https://www.pythonanywhere.com

### Passo 2: Upload dos Arquivos
- Use o console web ou FTP para fazer upload dos arquivos

### Passo 3: Criar Ambiente Virtual
```bash
mkvirtualenv --python=/usr/bin/python3.11 pulse
pip install -r requirements.txt
```

### Passo 4: Configurar Aplicação Web
- Vá em "Web" > "Add a new web app"
- Escolha "Manual configuration" > "Python 3.11"
- Configure o WSGI file

### Passo 5: Configurar Variáveis de Ambiente
- Edite o arquivo de configuração WSGI
- Adicione as variáveis de ambiente necessárias

## 🖥️ Deploy em DigitalOcean (Droplet)

### Passo 1: Criar Droplet
- Escolha Ubuntu 22.04 LTS
- Tamanho mínimo: 1GB RAM

### Passo 2: Conectar via SSH
```bash
ssh root@seu_ip_droplet
```

### Passo 3: Atualizar Sistema
```bash
apt update && apt upgrade -y
```

### Passo 4: Instalar Dependências
```bash
apt install -y python3.11 python3-pip python3-venv postgresql nginx git
```

### Passo 5: Clonar Repositório
```bash
cd /home
git clone seu-repositorio pulse
cd pulse
```

### Passo 6: Criar Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Passo 7: Configurar PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE pulse_db;
CREATE USER pulse_user WITH PASSWORD 'senha-segura';
ALTER ROLE pulse_user SET client_encoding TO 'utf8';
ALTER ROLE pulse_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pulse_user SET default_transaction_deferrable TO on;
ALTER ROLE pulse_user SET timezone TO 'America/Sao_Paulo';
GRANT ALL PRIVILEGES ON DATABASE pulse_db TO pulse_user;
\q
```

### Passo 8: Configurar Django
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### Passo 9: Configurar Gunicorn
```bash
pip install gunicorn
gunicorn pulse_project.wsgi:application --bind 0.0.0.0:8000
```

### Passo 10: Configurar Nginx
Crie `/etc/nginx/sites-available/pulse`:
```nginx
server {
    listen 80;
    server_name seu-dominio.com;

    location /static/ {
        alias /home/pulse/staticfiles/;
    }

    location /media/ {
        alias /home/pulse/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Passo 11: Ativar Site Nginx
```bash
ln -s /etc/nginx/sites-available/pulse /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

### Passo 12: Configurar SSL com Let's Encrypt
```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d seu-dominio.com
```

## 🔒 Checklist de Segurança

- [ ] `DEBUG = False` em produção
- [ ] `SECRET_KEY` alterada e segura
- [ ] `ALLOWED_HOSTS` configurado corretamente
- [ ] HTTPS/SSL ativado
- [ ] Banco de dados PostgreSQL (não SQLite)
- [ ] Backups automáticos configurados
- [ ] Logs monitorados
- [ ] Firewall configurado
- [ ] Variáveis sensíveis em `.env`
- [ ] CORS configurado corretamente

## 📊 Monitoramento

### Logs
```bash
# Heroku
heroku logs --tail

# DigitalOcean
tail -f /var/log/nginx/error.log
tail -f /var/log/nginx/access.log
```

### Performance
- Use ferramentas como New Relic ou Sentry
- Monitore uso de CPU e memória
- Configure alertas

## 🔄 Atualizações

### Fazer Deploy de Atualizações
```bash
# Heroku
git push heroku main

# DigitalOcean
cd /home/pulse
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
systemctl restart gunicorn
```

## 🆘 Troubleshooting

### Erro 500
- Verifique os logs
- Verifique variáveis de ambiente
- Verifique permissões de arquivo

### Banco de dados não conecta
- Verifique credenciais
- Verifique firewall
- Verifique se banco está rodando

### Arquivos estáticos não carregam
```bash
python manage.py collectstatic --noinput
```

### Erro de permissão
```bash
chown -R www-data:www-data /home/pulse
chmod -R 755 /home/pulse
```

---

Para mais informações, consulte a documentação oficial do Django:
https://docs.djangoproject.com/en/5.2/howto/deployment/


