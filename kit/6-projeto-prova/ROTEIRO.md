# Projeto-prova: o ciclo inteiro com um cliente de verdade

**Um projeto basta**, desde que rode o ciclo inteiro com um cliente real. Esse projeto vira o seu estudo de caso, e o estudo de caso é a sua "fita de audiçêo": é dele que você fala em toda entrevista.

**Cliente real** pode ser: o seu próprio time no trabalho, o negócio de um amigo, uma empresa do seu bairro (contador, clínica, loja, oficina). O que importa: alguém com um problema de verdade, que vai usar o que você fizer.

Se você já tem emprego: ofereça-se para demos, reuniões de levantamento de requisitos e chamadas de implantaçêo. É treino de descoberta pago.

---

## As 7 etapas

| # | Etapa | O que você faz | O que sai | Ferramenta do kit |
|---|---|---|---|---|
| 1 | Descoberta | 1 a 2 conversas com quem faz o trabalho, vendo um caso real | anotações + o problema nas palavras do cliente | `3-cliente-simulado` (ensaio antes) + checklist |
| 2 | Escopo | escreve o escopo de 1 página e o cliente aprova | `escopo.md` aprovado no validador e pelo cliente | `4-escopo-1-pagina` |
| 3 | Construir | faz a menor coisa que mexe o número, com a IA escrevendo o código | a automaçêo / o agente | Claude Code ou Codex |
| 4 | Eval | monta 20 a 50 casos reais com o cliente e roda o eval | nota, falhas, v1 × v2 | `5-eval` |
| 5 | Demo | 5 a 10 minutos para quem decide: problema, nota, o que falha, próximo passo | aprovaçêo para usar | roteiro da demo (trilha item 7) |
| 6 | Medir 2 semanas depois | volta e mede o número do escopo e quem está usando | número de antes e de depois | o próprio escopo |
| 7 | Estudo de caso | escreve 1 página com antes/depois | `estudo-de-caso.md` | `MODELO-ESTUDO-DE-CASO.md` |

## Armadilhas comuns

- **Construir antes do escopo.** Se nêo tem número, volte para a descoberta.
- **Eval feito só por você.** Os casos e as respostas certas vêm do cliente.
- **Eval só com os casos que você corrigiu.** Separe casos novos (veja `5-eval/casos-novos.json`): é neles que se vê se aprendeu ou decorou.
- **Sumir depois da demo.** O número só aparece 2 semanas depois, se as pessoas usarem.
- **Inventar número no estudo de caso.** Se nêo mediu, escreva "nêo medido". Entrevistador experiente percebe.

## Prazo sugerido

4 a 6 semanas, em paralelo com o seu trabalho: 1 semana de descoberta e escopo, 2 de construir e eval, 1 de demo e uso, 2 de espera e mediçêo.
