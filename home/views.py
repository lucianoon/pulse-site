from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json

class HomeView(View):
    """View para a página inicial"""
    def get(self, request):
        context = {
            'company_name': 'Pulse',
            'company_tagline': 'Soluções Inteligentes em IA',
            'services': [
                {
                    'title': 'Atendimentos Personalizados',
                    'description': 'Chatbots e assistentes virtuais inteligentes com IA para melhorar a experiência do cliente.',
                    'icon': 'fa-robot'
                },
                {
                    'title': 'Análise de Dados',
                    'description': 'Processamento e análise avançada de dados para insights estratégicos e tomada de decisão.',
                    'icon': 'fa-chart-line'
                },
                {
                    'title': 'Páginas Web',
                    'description': 'Desenvolvimento de websites modernos e responsivos com tecnologias de ponta.',
                    'icon': 'fa-globe'
                },
                {
                    'title': 'Automações',
                    'description': 'Automação de processos empresariais para aumentar produtividade e reduzir custos.',
                    'icon': 'fa-cogs'
                }
            ],
            'contact': {
                'address': 'Rua Visconde de Quissama, 523 - Macaé - RJ',
                'instagram': '@pulse',
                'instagram_url': 'https://instagram.com/pulse'
            },
            'case_studies': [
                {
                    'client': 'Rede de Clínicas Médicas',
                    'challenge': 'Alto índice de faltas em consultas e sobrecarga na equipe de agendamento.',
                    'solution': 'IA Conversacional para agendamentos, lembretes e confirmações automáticas via WhatsApp.',
                    'results': [
                        'Redução de 50% nas faltas',
                        '80% dos agendamentos feitos sem intervenção humana',
                        'Satisfação do cliente aumentou 40%'
                    ],
                    'icon': 'fa-hospital'
                },
                {
                    'client': 'Imobiliária',
                    'challenge': 'Responder rapidamente a um volume alto de consultas e qualificar leads de forma eficiente.',
                    'solution': 'IA Conversacional no WhatsApp para atendimento 24/7 e qualificação automática de leads.',
                    'results': [
                        'Tempo de resposta reduzido de 24h para 30s',
                        'Conversão aumentada em 35%',
                        '70% das dúvidas resolvidas sem intervenção humana'
                    ],
                    'icon': 'fa-home'
                }
            ]
        }
        return render(request, 'home/index.html', context)

class SobreView(View):
    """View para a página sobre"""
    def get(self, request):
        context = {
            'company_name': 'Pulse',
            'company_tagline': 'Soluções Inteligentes em IA'
        }
        return render(request, 'home/sobre.html', context)

class ContatoView(View):
    """View para a página de contato"""
    def get(self, request):
        context = {
            'company_name': 'Pulse',
            'contact': {
                'address': 'Rua Visconde de Quissama, 523 - Macaé - RJ',
                'instagram': '@pulse',
                'instagram_url': 'https://instagram.com/pulse'
            }
        }
        return render(request, 'home/contato.html', context)
    
    def post(self, request):
        """Processar formulário de contato"""
        try:
            data = json.loads(request.body)
            # Aqui você pode adicionar lógica para salvar mensagens
            # Por enquanto, apenas retornamos sucesso
            return JsonResponse({
                'status': 'sucesso',
                'mensagem': 'Mensagem recebida com sucesso! Entraremos em contato em breve.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'erro',
                'mensagem': 'Erro ao processar formulário'
            }, status=400)

class ServicosView(View):
    """View para a página de serviços"""
    def get(self, request):
        services = [
            {
                'title': 'Atendimentos Personalizados',
                'description': 'Chatbots e assistentes virtuais inteligentes com IA para melhorar a experiência do cliente.',
                'details': 'Desenvolvemos soluções de atendimento automatizado que entendem o contexto e personalizam respostas para cada cliente.',
                'icon': 'fa-robot'
            },
            {
                'title': 'Análise de Dados',
                'description': 'Processamento e análise avançada de dados para insights estratégicos e tomada de decisão.',
                'details': 'Transformamos dados brutos em insights valiosos através de análises preditivas e machine learning.',
                'icon': 'fa-chart-line'
            },
            {
                'title': 'Páginas Web',
                'description': 'Desenvolvimento de websites modernos e responsivos com tecnologias de ponta.',
                'details': 'Criamos websites profissionais, rápidos e otimizados para conversão e SEO.',
                'icon': 'fa-globe'
            },
            {
                'title': 'Automações',
                'description': 'Automação de processos empresariais para aumentar produtividade e reduzir custos.',
                'details': 'Automatizamos processos repetitivos para liberar sua equipe para tarefas estratégicas.',
                'icon': 'fa-cogs'
            }
        ]
        context = {
            'company_name': 'Pulse',
            'services': services
        }
        return render(request, 'home/servicos.html', context)


