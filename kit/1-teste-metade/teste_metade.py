#!/usr/bin/env python3
"""Teste "qual metade você tem": construtor x confiança do cliente.

Uso:
  python3 kit/1-teste-metade/teste_metade.py                 # perguntas no terminal
  python3 kit/1-teste-metade/teste_metade.py --respostas 3,2,1,0,2,3,1,1,2,0,1,2
  python3 kit/1-teste-metade/teste_metade.py --respostas ... --json

Cada resposta é o NÚMERO DA OPÇêO como aparece na tela (0 a 3), na ordem das perguntas.
A ordem das opções é misturada de propósito: a melhor nêo fica sempre no mesmo lugar
nem é sempre a mais longa. Os pontos de cada opçêo estêo em perguntas.json (campo "pontos").
Só biblioteca padrêo do Python. Nada sai da sua máquina.
"""
import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PERGUNTAS = AQUI / "perguntas.json"


def carregar(caminho=PERGUNTAS):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def pontuar(dados, respostas):
    """respostas: lista com o número da opçêo escolhida (0..3, como aparece), na ordem das perguntas.
    Devolve dict com pontos por metade, a metade mais fraca (ou 'empate') e o plano."""
    perguntas = dados["perguntas"]
    if len(respostas) != len(perguntas):
        raise ValueError(f"esperava {len(perguntas)} respostas, recebi {len(respostas)}")
    pontos = {m: 0 for m in dados["metades"]}
    for p, r in zip(perguntas, respostas):
        r = int(r)
        if not 0 <= r < len(p["opcoes"]):
            raise ValueError(f"resposta {r} fora da faixa na pergunta {p['id']}")
        pontos[p["metade"]] += p["opcoes"][r]["pontos"]
    maximo = {m: sum(max(o["pontos"] for o in p["opcoes"]) for p in perguntas if p["metade"] == m) for m in pontos}
    diferenca = pontos["construtor"] - pontos["confianca"]
    if abs(diferenca) <= dados["empate_ate"]:
        fraca = "empate"
    elif diferenca < 0:
        fraca = "construtor"
    else:
        fraca = "confianca"
    return {"pontos": pontos, "maximo": maximo, "mais_fraca": fraca, "plano": dados["planos"][fraca]}


def perguntar(dados):
    respostas = []
    for i, p in enumerate(dados["perguntas"], 1):
        print(f"\n{i}. {p['texto']}")
        for j, o in enumerate(p["opcoes"]):
            print(f"   {j}) {o['texto']}")
        while True:
            try:
                r = input("   sua resposta (0-3): ").strip()
            except EOFError:
                raise SystemExit("\nentrada encerrada antes do fim; para rodar sem perguntas, use --respostas")
            if r in {"0", "1", "2", "3"}:
                respostas.append(int(r))
                break
            print("   digite 0, 1, 2 ou 3")
    return respostas


def mostrar(dados, res):
    pt, mx = res["pontos"], res["maximo"]
    print("\n=== Resultado ===")
    for m, nome in dados["metades"].items():
        barra = "#" * pt[m] + "." * (mx[m] - pt[m])
        print(f"{nome.split(':')[0]:<22} {pt[m]:>2}/{mx[m]}  {barra}")
    plano = res["plano"]
    print(f"\n{plano['titulo']}\n{plano['foco']}\n\nSeu plano de estudo:")
    for i, passo in enumerate(plano["passos"], 1):
        print(f"  {i}. {passo}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Qual metade você tem: construtor ou confiança do cliente")
    ap.add_argument("--respostas", help="número da opçêo escolhida em cada pergunta, ex.: 3,2,1,0,2,3,1,1,2,0,1,2")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    a = ap.parse_args(argv)
    dados = carregar()
    if a.respostas:
        respostas = [int(x) for x in a.respostas.split(",") if x.strip() != ""]
    else:
        respostas = perguntar(dados)
    try:
        res = pontuar(dados, respostas)
    except ValueError as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        mostrar(dados, res)
    return 0


if __name__ == "__main__":
    sys.exit(main())
