"""Automação de exemplo, VERSÃO 1: triagem de e-mails por palavra-chave.

É o tipo de coisa que "funciona na demo": os 5 exemplos óbvios passam.
O eval mostra onde ela quebra. Regra simples, sem IA, para rodar sem API.

Contrato (igual em toda automação que o runner aceita):
    classificar(texto: str) -> str   # uma das categorias de casos.json
"""

REGRAS = [
    ("cancelamento", ["cancel"]),
    ("cobranca", ["cobr", "boleto", "fatura"]),
    ("acesso", ["senha", "login", "entrar"]),
    ("entrega", ["pedido", "entreg", "chegou"]),
]


def classificar(texto):
    t = texto.lower()
    for categoria, palavras in REGRAS:
        if any(p in t for p in palavras):
            return categoria
    return "outro"
