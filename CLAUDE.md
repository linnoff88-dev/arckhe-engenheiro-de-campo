# CLAUDE.md — engenheiro-de-campo

Kit + guia do ARCKHÉ AI sobre a profissêo **engenheiro de campo de IA** (forward deployed engineer). Conteúdo aberto e gratuito.

## Regras do projeto

- Tudo roda local: Python só com biblioteca padrêo, páginas HTML self-contained. Nada de API, modelo local ou dependência pesada.
- **Política de números:** só número com fonte oficial registrada em `fontes/` (URL + data). Salários: só faixas copiadas do texto de vaga oficial em `fontes/mercado.json` e `fontes/vaga-openai.json`, cada uma com link e data no guia. Imprensa (ex.: Fortune/Lightcast) só com a fonte escrita ao lado; o número do relatório do MIT sobre pilotos de IA nêo entra. O teste `SemNumerosProibidos` deriva a lista do que é permitido de `fontes/` e trava isso.
- Sem crédito de terceiros: o kit nêo cita autores, canais ou comunidades.
- `kit/1-teste-metade/perguntas.json` é a fonte única: mudou, rode `gerar_pagina.py` (o teste confere).
- As notas do eval citadas no guia e no README (18/30, 30/30, 4/10) estêo presas em `tests/test_kit.py`: mudou a automaçêo ou os casos, atualize os três lugares.
- Guia: PT é a fonte; EN/ES sêo cópias traduzidas pelo `ARCKHÉ-traduz`. Nada técnico no guia; comandos ficam no README.
- Autor dos commits: `linnoff88-dev <linnoff88-dev@gmail.com>`.

## Testes

`python3 -m unittest discover -s tests -v`

## Self-learning

When I correct you, or you catch yourself making a mistake: before continuing, add the lesson as a one-line rule at the TOP of the Lessons section below, so it never happens again.

## Lessons

- (vazio)

- 2026-11-20: crítica do Nei — no teste da metade a certa estava sempre na última linha e era a mais completa. Opções agora com pontos próprios, ordem misturada (e embaralhada na página a cada abertura), tamanhos parecidos e perguntas sobre o que a pessoa fez "da última vez"; teste `test_a_melhor_opcao_nao_se_denuncia` barra a volta.
