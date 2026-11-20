# Engenheiro de campo de IA: a nova profissÃ£o e o kit para se preparar

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Engenheiro de campo: a nova profissÃ£o da IA](guia/assets/banner.jpg)](https://inematds.github.io/engenheiro-de-campo/guia/)

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

**Engenheiro de campo de IA** (em inglÃªs, *forward deployed engineer*, ou FDE) Ã© o profissional que a empresa de IA manda para dentro do cliente: ele descobre o problema real, constrÃ³i a soluÃ§Ã£o junto com a equipe, prova que funciona com um teste medido (eval) e faz as pessoas usarem. Este kit Ã© uma formaÃ§Ã£o grÃ¡tis para se preparar: um teste para saber qual metade falta em vocÃª (a do construtor ou a da pessoa em quem o cliente confia), a trilha do que aprender, um cliente simulado para treinar a descoberta, o escopo de 1 pÃ¡gina com conferidor, um eval que roda no seu computador, o roteiro do projeto-prova, o mapa das vagas e o treino da entrevista. Tudo roda local, sem API e sem instalar modelo.

## ðŸ“– Guia de uso

Guia completo (o que Ã©, o potencial, a formaÃ§Ã£o passo a passo): **https://inematds.github.io/engenheiro-de-campo/guia/**

Teste no navegador, 3 minutos: **https://inematds.github.io/engenheiro-de-campo/kit/1-teste-metade/teste-metade.html**

## Comece pedindo para a sua IA

Abra o Claude Code ou o Codex numa pasta nova e cole:

```
Leia o kit "engenheiro de campo de IA" em https://github.com/inematds/engenheiro-de-campo (o README explica tudo).
Depois me ajude a me preparar para essa profissÃ£o, em portuguÃªs simples:
1. FaÃ§a comigo o teste "qual metade vocÃª tem", uma pergunta por vez, e me diga o resultado.
2. Monte um plano de 4 semanas focado na minha metade mais fraca, usando os passos do kit.
3. Comece pelo primeiro exercÃ­cio do plano comigo.
NÃ£o instale nem mude nada no meu computador sem me mostrar antes e esperar eu dizer sim.
```

## Por que essa vaga existe

As empresas compram IA mais rÃ¡pido do que conseguem fazÃª-la funcionar nos sistemas bagunÃ§ados delas. Em vez de entregar uma senha e desejar boa sorte, a empresa de IA manda um engenheiro sentar ao lado do cliente: ele nÃ£o vende hora de trabalho nem software, entrega um resultado. O raro Ã© quem tem **as duas metades**: o construtor e a pessoa em quem o cliente confia.

## Baseado em vagas oficiais (conferidas em 20/11/2026)

- **OpenAI**, vaga *Forward Deployed Engineer (FDE) - SF*: faixa publicada "$185K â€“ $300K â€¢ Offers Equity". [Vaga](https://jobs.ashbyhq.com/openai/967f94aa-1706-4dba-ac89-bfbc2c38b688) Â· registro em [`fontes/vaga-openai.json`](fontes/vaga-openai.json).
- **Anthropic**, vagas *Forward Deployed Engineer* e *Staff Forward Deployed Engineer*: entregar "MCP servers, sub-agents, and agent skills", "identify and codify repeatable deployment patterns", chegar "with only a business problem and leave with a defensible technical strategy". [Vaga FDE](https://job-boards.greenhouse.io/anthropic/jobs/5391021008) Â· [vaga Staff](https://job-boards.greenhouse.io/anthropic/jobs/5449229008) Â· registro em [`fontes/vagas-anthropic.json`](fontes/vagas-anthropic.json).
- **Mercado, alÃ©m da OpenAI:** as vagas oficiais de engenheiro de campo publicam de US$ 135 mil (Palantir) a US$ 415 mil (Cohere) por ano, com Anthropic, Harvey, Ramp, Databricks e Scale AI no meio. HÃ¡ vagas abertas com o Brasil no endereÃ§o: Decagon (remota, pede portuguÃªs, espanhol e inglÃªs), Cognition (presencial em SÃ£o Paulo) e Databricks (FDE Brazil). A Salesforce diz, no prÃ³prio blog, que vai montar um time de 1.000 engenheiros de campo. Os 23 itens, com o texto exato, o link e o tipo de cada fonte (vaga oficial, blog oficial ou imprensa), estÃ£o em [`fontes/mercado.json`](fontes/mercado.json).

Vagas mudam: confira sempre a pÃ¡gina oficial.

---

## O processo, do inÃ­cio ao fim

Quem faz: ðŸ§  sessÃ£o (vocÃª, com a IA ao lado) Â· âš™ï¸ script do kit Â· ðŸ¤– `claude -p` (ou Codex) pela sua assinatura.

| # | Passo | Comando / arquivo | Quem |
|---|---|---|---|
| 1 | Descobrir qual metade vocÃª tem | `python3 kit/1-teste-metade/teste_metade.py` (ou a pÃ¡gina `teste-metade.html`) | âš™ï¸ |
| 2 | Seguir a trilha, uma prÃ¡tica por item | [`kit/2-trilha/TRILHA.md`](kit/2-trilha/TRILHA.md) | ðŸ§  |
| 3 | Treinar a descoberta com o cliente simulado (4 setores) | colar um bloco de [`kit/3-cliente-simulado/PROMPTS.md`](kit/3-cliente-simulado/PROMPTS.md) na IA; conferir com o [checklist](kit/3-cliente-simulado/CHECKLIST-DESCOBERTA.md) | ðŸ¤– + ðŸ§  |
| 4 | Escrever o escopo de 1 pÃ¡gina e conferir | copiar [`modelo.md`](kit/4-escopo-1-pagina/modelo.md) â†’ `python3 kit/4-escopo-1-pagina/validar_escopo.py meu-escopo.md` | ðŸ§  + âš™ï¸ |
| 5 | Rodar o eval de exemplo e depois o seu | `python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py` | âš™ï¸ |
| 6 | Projeto-prova com cliente real + estudo de caso | [`kit/6-projeto-prova/ROTEIRO.md`](kit/6-projeto-prova/ROTEIRO.md) + [`MODELO-ESTUDO-DE-CASO.md`](kit/6-projeto-prova/MODELO-ESTUDO-DE-CASO.md) | ðŸ§  |
| 7 | Procurar as vagas | [`kit/7-vagas/VAGAS.md`](kit/7-vagas/VAGAS.md) | ðŸ§  |
| 8 | Treinar a entrevista (caso, projeto, tÃ©cnica, comportamental) | colar os prompts de [`kit/8-entrevista/ENTREVISTA.md`](kit/8-entrevista/ENTREVISTA.md) na IA | ðŸ¤– + ðŸ§  |
| 9 | Entender a semana de trabalho | [`kit/9-semana/SEMANA.md`](kit/9-semana/SEMANA.md) | ðŸ§  |

---

## InstalaÃ§Ã£o tÃ©cnica

### PrÃ©-requisitos

- Python 3.8 ou mais novo (sÃ³ biblioteca padrÃ£o; nada para instalar com `pip`).
- Git, para baixar o kit. Nenhuma chave de API, nenhum modelo local.

```bash
git clone https://github.com/inematds/engenheiro-de-campo.git
cd engenheiro-de-campo
```

### Comandos

```bash
# 1. teste "qual metade vocÃª tem" (interativo, ou com o nÃºmero da opÃ§Ã£o escolhida em cada uma das 12 perguntas)
python3 kit/1-teste-metade/teste_metade.py
python3 kit/1-teste-metade/teste_metade.py --respostas 3,3,2,3,2,3,1,1,2,0,1,2
#    regerar a pÃ¡gina depois de mudar perguntas.json
python3 kit/1-teste-metade/gerar_pagina.py

# 4. conferir um escopo (0 = aprovado, 1 = reprovado)
python3 kit/4-escopo-1-pagina/validar_escopo.py kit/4-escopo-1-pagina/exemplo-preenchido.md
python3 kit/4-escopo-1-pagina/validar_escopo.py kit/4-escopo-1-pagina/exemplo-reprovado.md

# 5. eval: uma versÃ£o, comparar duas, casos novos, nota mÃ­nima
python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v1.py
python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py
python3 kit/5-eval/rodar_eval.py --casos kit/5-eval/casos-novos.json kit/5-eval/automacao_v2.py
python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v2.py --minimo 0.9
```

### O eval de exemplo, medido em 20/11/2026

| | `casos.json` (30) | `casos-novos.json` (10) |
|---|---|---|
| `automacao_v1.py` (palavra-chave simples) | 18/30 | 4/10 |
| `automacao_v2.py` (corrigida pelas falhas da v1) | 30/30 Â· 12 consertados, 0 quebrados | 4/10 |

A v2 decorou os casos que usamos para corrigi-la; nos casos novos ficou igual Ã  v1. Ã‰ a liÃ§Ã£o do kit: eval sÃ©rio tem sempre um conjunto separado. Para avaliar o seu agente, copie [`automacao_meu_agente.py`](kit/5-eval/automacao_meu_agente.py) e leia [`kit/5-eval/LEIA.md`](kit/5-eval/LEIA.md).

O conferidor de escopo aceita os tÃ­tulos das seÃ§Ãµes em portuguÃªs, inglÃªs e espanhol (`Problema`/`Problem`, `O nÃºmero`/`The number`/`El nÃºmero`, `Pronto quando`/`Done when`/`Listo cuando`, `Fora do escopo`/`Out of scope`/`Fuera del alcance`).

### Arquivos

```
kit/1-teste-metade/     perguntas.json (fonte Ãºnica), teste_metade.py, gerar_pagina.py, teste-metade.html
kit/2-trilha/           TRILHA.md
kit/3-cliente-simulado/ PROMPTS.md (4 setores), CHECKLIST-DESCOBERTA.md
kit/4-escopo-1-pagina/  modelo.md, exemplo-preenchido.md, exemplo-reprovado.md, validar_escopo.py
kit/5-eval/             casos.json, casos-novos.json, automacao_v1.py, automacao_v2.py, rodar_eval.py, automacao_meu_agente.py, LEIA.md
kit/6-projeto-prova/    ROTEIRO.md, MODELO-ESTUDO-DE-CASO.md
kit/7-vagas/            VAGAS.md
kit/8-entrevista/       ENTREVISTA.md
kit/9-semana/           SEMANA.md
fontes/                 vagas oficiais conferidas (URL, texto literal, data)
guia/                   pÃ¡gina PT + en/ + es/
tests/                  testes automÃ¡ticos
```

### Testes

```bash
python3 -m unittest discover -s tests -v
```

31 testes cobrem: o teste-metade (12 perguntas, 6 por metade, os 3 resultados alcanÃ§Ã¡veis, empate dentro da margem, respostas invÃ¡lidas, a pÃ¡gina com as mesmas perguntas do JSON), o conferidor de escopo (exemplo aprovado, exemplo e modelo reprovados, sem nÃºmero, um nÃºmero sÃ³, sem aspas, seÃ§Ã£o faltando, tÃ­tulos em EN/ES, cÃ³digos de saÃ­da) e o eval (casos bem formados, as notas medidas 18/30, 30/30 e 4/10, a comparaÃ§Ã£o 12 consertados e 0 quebrados, automaÃ§Ã£o que explode conta como falha, cÃ³digo de saÃ­da do `--minimo`, o modelo do agente nÃ£o roda sem configurar) e a polÃ­tica de nÃºmeros: sÃ³ valores que estÃ£o no texto de uma vaga ou blog oficial registrado em `fontes/` (a faixa da OpenAI igual Ã  registrada), a Ãºnica porcentagem de imprensa sempre com a fonte (Fortune, com dados da Lightcast) ao lado, e os links da seÃ§Ã£o de mercado iguais nos trÃªs idiomas e todos registrados em `fontes/`.

## LicenÃ§a

MIT. ConteÃºdo aberto e gratuito do [INEMA.CLUB](https://inema.club).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>