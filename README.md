# Engenheiro de campo de IA: a nova profissêÂ£o e o kit para se preparar

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Engenheiro de campo: a nova profissêÂ£o da IA](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

**Engenheiro de campo de IA** (em inglêÂªs, *forward deployed engineer*, ou FDE) êÂ© o profissional que a empresa de IA manda para dentro do cliente: ele descobre o problema real, constrêÂ³i a soluêÂ§êÂ£o junto com a equipe, prova que funciona com um teste medido (eval) e faz as pessoas usarem. Este kit êÂ© uma formaêÂ§êÂ£o grêÂ¡tis para se preparar: um teste para saber qual metade falta em vocêÂª (a do construtor ou a da pessoa em quem o cliente confia), a trilha do que aprender, um cliente simulado para treinar a descoberta, o escopo de 1 pêÂ¡gina com conferidor, um eval que roda no seu computador, o roteiro do projeto-prova, o mapa das vagas e o treino da entrevista. Tudo roda local, sem API e sem instalar modelo.

## ê°Å¸ââ Guia de uso

Guia completo (o que êÂ©, o potencial, a formaêÂ§êÂ£o passo a passo): **https://linnoff88-dev.github.io/

Teste no navegador, 3 minutos: **https://linnoff88-dev.github.io/

## Comece pedindo para a sua IA

Abra o Claude Code ou o Codex numa pasta nova e cole:

```
Leia o kit "engenheiro de campo de IA" em https://github.com/linnoff88-dev/engenheiro-de-campo (o README explica tudo).
Depois me ajude a me preparar para essa profissêÂ£o, em portuguêÂªs simples:
1. FaêÂ§a comigo o teste "qual metade vocêÂª tem", uma pergunta por vez, e me diga o resultado.
2. Monte um plano de 4 semanas focado na minha metade mais fraca, usando os passos do kit.
3. Comece pelo primeiro exercêÂ­cio do plano comigo.
NêÂ£o instale nem mude nada no meu computador sem me mostrar antes e esperar eu dizer sim.
```

## Por que essa vaga existe

As empresas compram IA mais rêÂ¡pido do que conseguem fazêÂª-la funcionar nos sistemas bagunêÂ§ados delas. Em vez de entregar uma senha e desejar boa sorte, a empresa de IA manda um engenheiro sentar ao lado do cliente: ele nêÂ£o vende hora de trabalho nem software, entrega um resultado. O raro êÂ© quem tem **as duas metades**: o construtor e a pessoa em quem o cliente confia.

## Baseado em vagas oficiais (conferidas em 20/11/2026)

- **OpenAI**, vaga *Forward Deployed Engineer (FDE) - SF*: faixa publicada "$185K ê¢â¬â $300K ê¢â¬Â¢ Offers Equity". [Vaga](https://jobs.ashbyhq.com/openai/967f94aa-1706-4dba-ac89-bfbc2c38b688) êÂ· registro em [`fontes/vaga-openai.json`](fontes/vaga-openai.json).
- **Anthropic**, vagas *Forward Deployed Engineer* e *Staff Forward Deployed Engineer*: entregar "MCP servers, sub-agents, and agent skills", "identify and codify repeatable deployment patterns", chegar "with only a business problem and leave with a defensible technical strategy". [Vaga FDE](https://job-boards.greenhouse.io/anthropic/jobs/5391021008) êÂ· [vaga Staff](https://job-boards.greenhouse.io/anthropic/jobs/5449229008) êÂ· registro em [`fontes/vagas-anthropic.json`](fontes/vagas-anthropic.json).
- **Mercado, alêÂ©m da OpenAI:** as vagas oficiais de engenheiro de campo publicam de US$ 135 mil (Palantir) a US$ 415 mil (Cohere) por ano, com Anthropic, Harvey, Ramp, Databricks e Scale AI no meio. HêÂ¡ vagas abertas com o Brasil no endereêÂ§o: Decagon (remota, pede portuguêÂªs, espanhol e inglêÂªs), Cognition (presencial em SêÂ£o Paulo) e Databricks (FDE Brazil). A Salesforce diz, no prêÂ³prio blog, que vai montar um time de 1.000 engenheiros de campo. Os 23 itens, com o texto exato, o link e o tipo de cada fonte (vaga oficial, blog oficial ou imprensa), estêÂ£o em [`fontes/mercado.json`](fontes/mercado.json).

Vagas mudam: confira sempre a pêÂ¡gina oficial.

---

## O processo, do inêÂ­cio ao fim

Quem faz: ê°Å¸Â§Â  sessêÂ£o (vocêÂª, com a IA ao lado) êÂ· ê¢Å¡â¢ê¯Â¸Â script do kit êÂ· ê°Å¸Â¤â `claude -p` (ou Codex) pela sua assinatura.

| # | Passo | Comando / arquivo | Quem |
|---|---|---|---|
| 1 | Descobrir qual metade vocêÂª tem | `python3 kit/1-teste-metade/teste_metade.py` (ou a pêÂ¡gina `teste-metade.html`) | ê¢Å¡â¢ê¯Â¸Â |
| 2 | Seguir a trilha, uma prêÂ¡tica por item | [`kit/2-trilha/TRILHA.md`](kit/2-trilha/TRILHA.md) | ê°Å¸Â§Â  |
| 3 | Treinar a descoberta com o cliente simulado (4 setores) | colar um bloco de [`kit/3-cliente-simulado/PROMPTS.md`](kit/3-cliente-simulado/PROMPTS.md) na IA; conferir com o [checklist](kit/3-cliente-simulado/CHECKLIST-DESCOBERTA.md) | ê°Å¸Â¤â + ê°Å¸Â§Â  |
| 4 | Escrever o escopo de 1 pêÂ¡gina e conferir | copiar [`modelo.md`](kit/4-escopo-1-pagina/modelo.md) ê¢â â `python3 kit/4-escopo-1-pagina/validar_escopo.py meu-escopo.md` | ê°Å¸Â§Â  + ê¢Å¡â¢ê¯Â¸Â |
| 5 | Rodar o eval de exemplo e depois o seu | `python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py` | ê¢Å¡â¢ê¯Â¸Â |
| 6 | Projeto-prova com cliente real + estudo de caso | [`kit/6-projeto-prova/ROTEIRO.md`](kit/6-projeto-prova/ROTEIRO.md) + [`MODELO-ESTUDO-DE-CASO.md`](kit/6-projeto-prova/MODELO-ESTUDO-DE-CASO.md) | ê°Å¸Â§Â  |
| 7 | Procurar as vagas | [`kit/7-vagas/VAGAS.md`](kit/7-vagas/VAGAS.md) | ê°Å¸Â§Â  |
| 8 | Treinar a entrevista (caso, projeto, têÂ©cnica, comportamental) | colar os prompts de [`kit/8-entrevista/ENTREVISTA.md`](kit/8-entrevista/ENTREVISTA.md) na IA | ê°Å¸Â¤â + ê°Å¸Â§Â  |
| 9 | Entender a semana de trabalho | [`kit/9-semana/SEMANA.md`](kit/9-semana/SEMANA.md) | ê°Å¸Â§Â  |

---

## InstalaêÂ§êÂ£o têÂ©cnica

### PrêÂ©-requisitos

- Python 3.8 ou mais novo (sêÂ³ biblioteca padrêÂ£o; nada para instalar com `pip`).
- Git, para baixar o kit. Nenhuma chave de API, nenhum modelo local.

```bash
git clone https://github.com/linnoff88-dev/engenheiro-de-campo.git
cd engenheiro-de-campo
```

### Comandos

```bash
# 1. teste "qual metade vocêÂª tem" (interativo, ou com o nêÂºmero da opêÂ§êÂ£o escolhida em cada uma das 12 perguntas)
python3 kit/1-teste-metade/teste_metade.py
python3 kit/1-teste-metade/teste_metade.py --respostas 3,3,2,3,2,3,1,1,2,0,1,2
#    regerar a pêÂ¡gina depois de mudar perguntas.json
python3 kit/1-teste-metade/gerar_pagina.py

# 4. conferir um escopo (0 = aprovado, 1 = reprovado)
python3 kit/4-escopo-1-pagina/validar_escopo.py kit/4-escopo-1-pagina/exemplo-preenchido.md
python3 kit/4-escopo-1-pagina/validar_escopo.py kit/4-escopo-1-pagina/exemplo-reprovado.md

# 5. eval: uma versêÂ£o, comparar duas, casos novos, nota mêÂ­nima
python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v1.py
python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py
python3 kit/5-eval/rodar_eval.py --casos kit/5-eval/casos-novos.json kit/5-eval/automacao_v2.py
python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v2.py --minimo 0.9
```

### O eval de exemplo, medido em 20/11/2026

| | `casos.json` (30) | `casos-novos.json` (10) |
|---|---|---|
| `automacao_v1.py` (palavra-chave simples) | 18/30 | 4/10 |
| `automacao_v2.py` (corrigida pelas falhas da v1) | 30/30 êÂ· 12 consertados, 0 quebrados | 4/10 |

A v2 decorou os casos que usamos para corrigi-la; nos casos novos ficou igual êÂ  v1. êâ° a liêÂ§êÂ£o do kit: eval sêÂ©rio tem sempre um conjunto separado. Para avaliar o seu agente, copie [`automacao_meu_agente.py`](kit/5-eval/automacao_meu_agente.py) e leia [`kit/5-eval/LEIA.md`](kit/5-eval/LEIA.md).

O conferidor de escopo aceita os têÂ­tulos das seêÂ§êÂµes em portuguêÂªs, inglêÂªs e espanhol (`Problema`/`Problem`, `O nêÂºmero`/`The number`/`El nêÂºmero`, `Pronto quando`/`Done when`/`Listo cuando`, `Fora do escopo`/`Out of scope`/`Fuera del alcance`).

### Arquivos

```
kit/1-teste-metade/     perguntas.json (fonte êÂºnica), teste_metade.py, gerar_pagina.py, teste-metade.html
kit/2-trilha/           TRILHA.md
kit/3-cliente-simulado/ PROMPTS.md (4 setores), CHECKLIST-DESCOBERTA.md
kit/4-escopo-1-pagina/  modelo.md, exemplo-preenchido.md, exemplo-reprovado.md, validar_escopo.py
kit/5-eval/             casos.json, casos-novos.json, automacao_v1.py, automacao_v2.py, rodar_eval.py, automacao_meu_agente.py, LEIA.md
kit/6-projeto-prova/    ROTEIRO.md, MODELO-ESTUDO-DE-CASO.md
kit/7-vagas/            VAGAS.md
kit/8-entrevista/       ENTREVISTA.md
kit/9-semana/           SEMANA.md
fontes/                 vagas oficiais conferidas (URL, texto literal, data)
guia/                   pêÂ¡gina PT + en/ + es/
tests/                  testes automêÂ¡ticos
```

### Testes

```bash
python3 -m unittest discover -s tests -v
```

31 testes cobrem: o teste-metade (12 perguntas, 6 por metade, os 3 resultados alcanêÂ§êÂ¡veis, empate dentro da margem, respostas invêÂ¡lidas, a pêÂ¡gina com as mesmas perguntas do JSON), o conferidor de escopo (exemplo aprovado, exemplo e modelo reprovados, sem nêÂºmero, um nêÂºmero sêÂ³, sem aspas, seêÂ§êÂ£o faltando, têÂ­tulos em EN/ES, cêÂ³digos de saêÂ­da) e o eval (casos bem formados, as notas medidas 18/30, 30/30 e 4/10, a comparaêÂ§êÂ£o 12 consertados e 0 quebrados, automaêÂ§êÂ£o que explode conta como falha, cêÂ³digo de saêÂ­da do `--minimo`, o modelo do agente nêÂ£o roda sem configurar) e a polêÂ­tica de nêÂºmeros: sêÂ³ valores que estêÂ£o no texto de uma vaga ou blog oficial registrado em `fontes/` (a faixa da OpenAI igual êÂ  registrada), a êÂºnica porcentagem de imprensa sempre com a fonte (Fortune, com dados da Lightcast) ao lado, e os links da seêÂ§êÂ£o de mercado iguais nos trêÂªs idiomas e todos registrados em `fontes/`.

## LicenêÂ§a

MIT. ConteêÂºdo aberto e gratuito do [ARCKHê AI](https://ARCKHê AI).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>