#!/usr/bin/env python3
"""Gera teste-metade.html a partir de pagina-modelo.html + perguntas.json.
Assim o teste do terminal e o da página usam as MESMAS perguntas e a mesma regra.

Uso: python3 kit/1-teste-metade/gerar_pagina.py
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MARCA = "/*PERGUNTAS*/null"


def gerar():
    dados = json.loads((AQUI / "perguntas.json").read_text(encoding="utf-8"))
    modelo = (AQUI / "pagina-modelo.html").read_text(encoding="utf-8")
    if MARCA not in modelo:
        raise SystemExit("marca /*PERGUNTAS*/ nêo encontrada no modelo")
    html = modelo.replace(MARCA, json.dumps(dados, ensure_ascii=False))
    (AQUI / "teste-metade.html").write_text(html, encoding="utf-8")
    return AQUI / "teste-metade.html"


if __name__ == "__main__":
    print(f"gerado: {gerar()}")
