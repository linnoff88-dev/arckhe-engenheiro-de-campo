"""MODELO para avaliar o SEU agente com o mesmo runner (copie e adapte).

O runner só exige uma função classificar(texto) -> str. Aqui ela chama um programa seu
(o seu agente, o seu fluxo, a sua CLI) e devolve a resposta dele.

Exemplo de uso depois de adaptar:
    python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_meu_agente.py

Atenção: este arquivo NÃO roda nada sozinho no teste do kit. Quem decide qual agente,
qual conta e qual custo é você. Rodar 30 casos = 30 chamadas ao seu agente.
"""
import subprocess

CATEGORIAS = ["cobranca", "acesso", "entrega", "cancelamento", "outro"]

# Troque pelo comando do seu agente. Ele recebe o e-mail na entrada e deve imprimir a fila.
# Ex.: ["python3", "meu_agente.py"]  ou  ["claude", "-p", PROMPT]  (pela sua assinatura)
COMANDO = None

PROMPT = (
    "Classifique o e-mail de suporte abaixo em UMA destas filas: "
    + ", ".join(CATEGORIAS)
    + ". Responda só com o nome da fila, sem mais nada.\n\nE-mail: "
)


def classificar(texto):
    if COMANDO is None:
        raise RuntimeError("defina COMANDO com o programa do seu agente")
    saida = subprocess.run(COMANDO, input=PROMPT + texto, capture_output=True, text=True, timeout=120)
    resposta = saida.stdout.strip().lower()
    # o agente pode responder com uma frase; fica com a primeira fila citada
    for c in CATEGORIAS:
        if c in resposta:
            return c
    return resposta or "vazio"
