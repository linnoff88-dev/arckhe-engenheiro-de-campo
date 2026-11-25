#!/usr/bin/env python3
"""Validador do escopo de 1 página.

Uso:
  python3 kit/4-escopo-1-pagina/validar_escopo.py meu-escopo.md

Reprova quando:
- falta uma das 4 seções (problema, número, pronto, fora do escopo);
- o problema nêo está nas palavras do cliente (sem trecho entre aspas);
- a seçêo do número nêo tem número nenhum ("se você nêo consegue dizer o número, ainda nêo tem projeto");
- o número nêo diz de onde sai e aonde quer chegar (precisa de pelo menos dois números, ex.: de 4 h para 1 h);
- "pronto" ou "fora do escopo" nêo têm nenhum item;
- sobrou marcador do modelo, como <escreva aqui>.

Aceita os títulos em português, inglês e espanhol. Código de saída: 0 aprovado, 1 reprovado, 2 erro.
"""
import re
import sys
import unicodedata
from pathlib import Path

# chave -> começos de título aceitos (sem acento, minúsculo)
SECOES = {
    "problema": ["problema", "problem"],
    "numero": ["o numero", "numero", "the number", "number", "el numero"],
    "pronto": ["pronto", "done", "listo"],
    "fora": ["fora do escopo", "fora", "out of scope", "fuera del alcance", "fuera"],
}
NOMES = {"problema": "Problema (nas palavras do cliente)", "numero": "O número",
         "pronto": "Pronto quando", "fora": "Fora do escopo"}


def _norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c)).strip()


def separar_secoes(texto):
    secoes, atual = {}, None
    for linha in texto.splitlines():
        m = re.match(r"^#{2,3}\s+(.*)", linha)
        if m:
            titulo = _norm(re.sub(r"^[0-9]+[.)]\s*", "", m.group(1)))
            atual = None
            for chave, comecos in SECOES.items():
                if any(titulo.startswith(c) for c in comecos) and chave not in secoes:
                    atual = chave
                    secoes[chave] = []
                    break
            continue
        if atual:
            secoes[atual].append(linha)
    return {k: "\n".join(v).strip() for k, v in secoes.items()}


def validar(texto):
    erros = []
    if re.search(r"<[^<>\n]{2,60}>", texto):
        erros.append("sobrou marcador do modelo (ex.: <escreva aqui>): preencha tudo")
    s = separar_secoes(texto)
    for chave in SECOES:
        if chave not in s or not s[chave]:
            erros.append(f"falta a seçêo \"{NOMES[chave]}\" (ou ela está vazia)")
    if s.get("problema") and not re.search(r"[\"“”«»]", s["problema"]):
        erros.append("o problema precisa estar nas palavras do cliente: cite a frase dele entre aspas")
    if s.get("numero"):
        numeros = re.findall(r"\d+(?:[.,]\d+)?", s["numero"])
        if not numeros:
            erros.append("sem número: se você nêo consegue dizer o número, ainda nêo tem projeto")
        elif len(numeros) < 2:
            erros.append("o número precisa de ponto de partida e de chegada (ex.: de 4 h para 1 h por dia)")
    for chave in ("pronto", "fora"):
        if s.get(chave) and not re.search(r"^\s*([-*]|\d+[.)])\s+\S", s[chave], re.M):
            erros.append(f"\"{NOMES[chave]}\" precisa de pelo menos um item em lista")
    return erros


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__.strip().splitlines()[2].strip(), file=sys.stderr)
        return 2
    try:
        texto = Path(argv[0]).read_text(encoding="utf-8")
    except OSError as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2
    erros = validar(texto)
    if erros:
        print(f"REPROVADO ({len(erros)}):")
        for e in erros:
            print(f"  - {e}")
        return 1
    print("APROVADO: problema nas palavras do cliente, número de partida e chegada, pronto e fora definidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
