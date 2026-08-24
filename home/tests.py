"""Testes de fumaça do site institucional.

Garante que as quatro páginas renderizam com o conteúdo comercial esperado
e que o endpoint de contato se comporta nos caminhos feliz e de erro.
"""
import json

from django.test import TestCase


class PaginasSmokeTest(TestCase):
    def test_home_renderiza(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/index.html")
        self.assertContains(resp, "Pulse")
        self.assertContains(resp, "Atendimentos Personalizados")
        # estudo de caso aparece na home
        self.assertContains(resp, "Rede de Clínicas Médicas")

    def test_sobre_renderiza(self):
        resp = self.client.get("/sobre/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/sobre.html")

    def test_servicos_renderiza_com_os_quatro_servicos(self):
        resp = self.client.get("/servicos/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/servicos.html")
        for titulo in (
            "Atendimentos Personalizados",
            "Análise de Dados",
            "Páginas Web",
            "Automações",
        ):
            self.assertContains(resp, titulo)

    def test_contato_renderiza(self):
        resp = self.client.get("/contato/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/contato.html")


class ContatoEndpointTest(TestCase):
    def test_post_valido_retorna_sucesso(self):
        payload = {"nome": "Ana", "email": "ana@ex.com", "mensagem": "Olá"}
        resp = self.client.post(
            "/contato/", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["status"], "sucesso")

    def test_post_com_json_invalido_retorna_400(self):
        resp = self.client.post(
            "/contato/", data="isto não é json", content_type="application/json"
        )
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json()["status"], "erro")
