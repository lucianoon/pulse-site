# 🚀 Guia Rápido - Pulse

Comece a usar o site da Pulse em 5 minutos!

## ⚡ Início Rápido

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar Migrações
```bash
python manage.py migrate
```

### 3. Iniciar Servidor
```bash
python manage.py runserver
```

### 4. Acessar o Site
Abra seu navegador e vá para: **http://localhost:8000**

## 📄 Páginas Disponíveis

| URL | Descrição |
|-----|-----------|
| `/` | Página inicial com apresentação |
| `/servicos/` | Detalhes dos serviços oferecidos |
| `/sobre/` | Informações sobre a empresa |
| `/contato/` | Formulário de contato |
| `/admin/` | Painel administrativo |

## 🎨 Personalizar o Site

### Mudar Informações da Empresa

Edite o arquivo `home/views.py`:

```python
context = {
    'company_name': 'Pulse',  # Nome da empresa
    'company_tagline': 'Soluções Inteligentes em IA',  # Tagline
    'contact': {
        'address': 'Rua Visconde de Quissama, 523 - Macaé - RJ',  # Endereço
        'instagram': '@pulse',  # Instagram
        'instagram_url': 'https://instagram.com/pulse'  # URL Instagram
    }
}
```

### Mudar Cores

Edite o arquivo `templates/home/base.html` (seção `:root`):

```css
:root {
    --primary-color: #0066cc;      /* Azul principal */
    --secondary-color: #00d4ff;    /* Ciano secundário */
    --dark-color: #1a1a2e;         /* Azul escuro */
    --light-color: #f5f7fa;        /* Cinza claro */
}
```

### Adicionar Novo Serviço

1. Edite `home/views.py` e adicione um novo item na lista `services`:

```python
{
    'title': 'Novo Serviço',
    'description': 'Descrição do novo serviço',
    'icon': 'fa-icon-name'
}
```

2. Os ícones disponíveis estão em: https://fontawesome.com/icons

## 🔧 Comandos Úteis

```bash
# Criar superusuário para admin
python manage.py createsuperuser

# Acessar shell Django
python manage.py shell

# Fazer backup do banco de dados
python manage.py dumpdata > backup.json

# Restaurar backup
python manage.py loaddata backup.json

# Executar testes
python manage.py test

# Coletar arquivos estáticos (para produção)
python manage.py collectstatic
```

## 📱 Testar Responsividade

O site é totalmente responsivo! Teste em:
- Desktop (F12 > Responsive Design Mode)
- Tablet (768px)
- Mobile (320px)

## 🔗 Links Importantes

- **Django Docs**: https://docs.djangoproject.com/
- **Font Awesome Icons**: https://fontawesome.com/icons
- **Google Fonts**: https://fonts.google.com/
- **Heroku Deploy**: https://devcenter.heroku.com/articles/deploying-python

## 📞 Informações de Contato

**Pulse - Soluções em IA**
- 📍 Rua Visconde de Quissama, 523 - Macaé - RJ
- 📱 Instagram: [@pulse](https://instagram.com/pulse)

## 🆘 Problemas Comuns

### Erro: "No module named 'django'"
```bash
pip install django
```

### Erro: "Port 8000 already in use"
```bash
# Use outra porta
python manage.py runserver 8001
```

### Erro: "ModuleNotFoundError"
```bash
# Verifique se está no ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## 📚 Próximos Passos

1. ✅ Personalizar informações da empresa
2. ✅ Testar formulário de contato
3. ✅ Configurar email para receber mensagens
4. ✅ Fazer deploy em produção
5. ✅ Configurar domínio personalizado

---

**Pronto para começar? Boa sorte! 🎉**


