"""Automação de exemplo, VERSÃO 2: a mesma triagem, corrigida a partir das falhas do eval da v1.

O que mudou (cada item veio de um caso que falhou):
- tira acento e caixa antes de comparar ("Nao", "cobranca", "LOGAR");
- mais sinais por fila (reembolso, pix, rastreio, SMS, bloqueio, encerrar, desistir…);
- prioridade: dinheiro > acesso > entrega > cancelamento. "Cancelei e continuo sendo cobrado"
  é problema de cobrança; "cancelaram meu pedido" é problema de entrega;
- "pag" só no começo da palavra, para "apagar" não virar cobrança.

Contrato: classificar(texto: str) -> str
"""
import re
import unicodedata

SINAIS = [
    ("cobranca", [r"cobr", r"boleto", r"fatura", r"estorn", r"reembols", r"\bpix\b", r"\bpag"]),
    ("acesso", [r"senha", r"login", r"\blog", r"entrar", r"bloque", r"verificacao", r"\bsms\b", r"usuario", r"invad"]),
    ("entrega", [r"pedido\b", r"entreg", r"chegou", r"rastreio", r"transportadora", r"endereco", r"\btroc"]),
    ("cancelamento", [r"cancel", r"encerr", r"desist"]),
]


def normalizar(texto):
    t = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in t if not unicodedata.combining(c))


def classificar(texto):
    t = normalizar(texto)
    for categoria, padroes in SINAIS:
        if any(re.search(p, t) for p in padroes):
            return categoria
    return "outro"
