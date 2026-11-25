#!/usr/bin/env python3
"""Runner de eval: roda uma automaçêo contra os casos e dá nota.

Uso:
  python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v1.py
  python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v2.py --minimo 0.9
  python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py
  python3 kit/5-eval/rodar_eval.py minha_automacao.py --casos meus_casos.json --json

A automaçêo é qualquer arquivo .py com a funçêo classificar(texto) -> str.
Para avaliar o SEU agente, veja automacao_meu_agente.py (modelo para copiar).

Saída: nota geral, acerto por categoria e a lista de falhas (entrada, esperado, obtido).
Código de saída: 0 se a nota >= --minimo (padrêo 0), 1 se ficou abaixo, 2 em erro.
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CASOS = AQUI / "casos.json"


def carregar_automacao(caminho):
    caminho = Path(caminho).resolve()
    spec = importlib.util.spec_from_file_location(f"automacao_{caminho.stem}", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "classificar"):
        raise AttributeError(f"{caminho.name} nêo tem a funçêo classificar(texto)")
    return mod.classificar


def carregar_casos(caminho=CASOS):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def avaliar(classificar, dados):
    resultados = []
    for c in dados["casos"]:
        try:
            obtido = classificar(c["entrada"])
        except Exception as e:  # uma automaçêo que explode conta como falha, nêo derruba o eval
            obtido = f"ERRO: {e.__class__.__name__}"
        resultados.append({"id": c["id"], "entrada": c["entrada"], "esperado": c["esperado"],
                           "obtido": obtido, "ok": obtido == c["esperado"]})
    total = len(resultados)
    acertos = sum(r["ok"] for r in resultados)
    por_cat = {}
    for cat in dados.get("categorias", sorted({r["esperado"] for r in resultados})):
        rs = [r for r in resultados if r["esperado"] == cat]
        if rs:
            por_cat[cat] = {"acertos": sum(r["ok"] for r in rs), "total": len(rs)}
    return {"acertos": acertos, "total": total, "nota": acertos / total if total else 0.0,
            "por_categoria": por_cat, "falhas": [r for r in resultados if not r["ok"]],
            "resultados": resultados}


def comparar(res_a, res_b):
    a = {r["id"]: r for r in res_a["resultados"]}
    b = {r["id"]: r for r in res_b["resultados"]}
    consertou = [b[i] for i in a if not a[i]["ok"] and b[i]["ok"]]
    quebrou = [b[i] for i in a if a[i]["ok"] and not b[i]["ok"]]
    return {"consertou": consertou, "quebrou": quebrou}


def imprimir(nome, res):
    print(f"== {nome}: {res['acertos']}/{res['total']} certos (nota {res['nota']:.0%})")
    for cat, v in res["por_categoria"].items():
        print(f"   {cat:<13} {v['acertos']}/{v['total']}")
    if res["falhas"]:
        print("   falhas:")
        for r in res["falhas"]:
            print(f"   #{r['id']:<3} esperado={r['esperado']:<13} obtido={r['obtido']:<13} \"{r['entrada']}\"")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Eval local de uma automaçêo de classificaçêo")
    ap.add_argument("automacao", nargs="?", help="arquivo .py com classificar(texto)")
    ap.add_argument("--comparar", nargs=2, metavar=("V1", "V2"), help="compara duas versões")
    ap.add_argument("--casos", default=str(CASOS), help="arquivo de casos (padrêo: casos.json do kit)")
    ap.add_argument("--minimo", type=float, default=0.0, help="nota mínima para passar (0 a 1)")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    a = ap.parse_args(argv)
    try:
        dados = carregar_casos(a.casos)
        if a.comparar:
            ra = avaliar(carregar_automacao(a.comparar[0]), dados)
            rb = avaliar(carregar_automacao(a.comparar[1]), dados)
            cmp_ = comparar(ra, rb)
            if a.json:
                print(json.dumps({"v1": {k: ra[k] for k in ("acertos", "total", "nota")},
                                  "v2": {k: rb[k] for k in ("acertos", "total", "nota")},
                                  "consertou": [r["id"] for r in cmp_["consertou"]],
                                  "quebrou": [r["id"] for r in cmp_["quebrou"]]}, ensure_ascii=False, indent=2))
            else:
                imprimir(Path(a.comparar[0]).name, ra)
                print()
                imprimir(Path(a.comparar[1]).name, rb)
                print(f"\n== comparaçêo: {len(cmp_['consertou'])} casos consertados, {len(cmp_['quebrou'])} quebrados")
                for r in cmp_["quebrou"]:
                    print(f"   QUEBROU #{r['id']} \"{r['entrada']}\"")
            return 0 if rb["nota"] >= a.minimo else 1
        if not a.automacao:
            ap.error("diga a automaçêo ou use --comparar V1 V2")
        res = avaliar(carregar_automacao(a.automacao), dados)
    except (OSError, AttributeError, json.JSONDecodeError) as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps({k: res[k] for k in ("acertos", "total", "nota", "por_categoria", "falhas")},
                         ensure_ascii=False, indent=2))
    else:
        imprimir(Path(a.automacao).name, res)
    return 0 if res["nota"] >= a.minimo else 1


if __name__ == "__main__":
    sys.exit(main())
