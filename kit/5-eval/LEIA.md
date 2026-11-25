# Eval: demo nêo prova, eval prova

Um eval é uma lista de casos (entrada + resposta esperada) e um programa que roda a sua automaçêo em todos, dá nota, mostra cada falha e compara versões.

## O exemplo do kit

Uma triagem de e-mails de suporte em 5 filas (cobrança, acesso, entrega, cancelamento, outro), feita com regras simples para rodar sem API e sem modelo.

| Arquivo | O que é |
|---|---|
| `casos.json` | 30 e-mails com a fila certa |
| `casos-novos.json` | 10 e-mails que **nêo** foram usados para corrigir a v2 |
| `automacao_v1.py` | primeira versêo: palavra-chave simples |
| `automacao_v2.py` | versêo corrigida a partir das falhas da v1 |
| `rodar_eval.py` | o runner |
| `automacao_meu_agente.py` | modelo para avaliar o SEU agente |

## Rodar

```bash
python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py
python3 kit/5-eval/rodar_eval.py --casos kit/5-eval/casos-novos.json kit/5-eval/automacao_v2.py
```

Medido em 20/11/2026 nesta máquina:

| | casos.json (30) | casos-novos.json (10) |
|---|---|---|
| v1 | 18/30 | 4/10 |
| v2 | 30/30 (12 consertados, 0 quebrados) | 4/10 |

**A liçêo:** a v2 tirou nota máxima nos casos que usamos para corrigi-la, e nos casos novos ficou igual à v1. Ela decorou, nêo aprendeu. Por isso o eval sério tem sempre um conjunto separado de casos que você nêo olhou enquanto corrigia. Num cliente, esse é o momento de trocar a regra por um agente e medir de novo.

## Trocar pela sua automaçêo

1. Copie `automacao_meu_agente.py` para um arquivo seu.
2. Faça `classificar(texto)` devolver a resposta do seu programa (o seu agente, o seu fluxo, a sua CLI). O modelo já mostra como chamar um comando externo.
3. Troque os casos: escreva com o cliente um `meus_casos.json` no mesmo formato (`id`, `entrada`, `esperado`, e a lista `categorias`).
4. Rode: `python3 kit/5-eval/rodar_eval.py minha_automacao.py --casos meus_casos.json --minimo 0.9`
   (sai com código 1 se a nota ficar abaixo de 90%, para usar em teste automático).

Quando a saída nêo é uma categoria (ex.: um resumo, uma resposta livre), o formato é o mesmo, mas a comparaçêo `obtido == esperado` vira uma funçêo de nota sua (contém o dado certo? cita a fonte? passou do tamanho?). Comece simples: igualdade exata em tudo que der.
