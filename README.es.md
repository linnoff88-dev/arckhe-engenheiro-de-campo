# Ingeniero de campo de IA: la nueva profesión y el kit para prepararte

[![Ingeniero de campo: la nueva profesión de la IA](guia/assets/banner-es.jpg)](https://inematds.github.io/engenheiro-de-campo/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

**Ingeniero de campo de IA** (en inglés, *forward deployed engineer*, o FDE) es el profesional que la empresa de IA envía a las instalaciones del cliente: descubre el problema real, construye la solución junto con el equipo, demuestra que funciona mediante una prueba medida (eval) y consigue que las personas la usen. Este kit es una formación gratuita para prepararte: una prueba para saber qué mitad te falta (la de quien construye o la de la persona en quien confía el cliente), la ruta de aprendizaje, un cliente simulado para practicar el descubrimiento, el alcance de 1 página con validador, un eval que se ejecuta en tu computadora, la guía del proyecto de prueba, el mapa de las vacantes y la práctica para la entrevista. Todo funciona localmente, sin API y sin instalar modelos.

## 📖 Guía de uso

Guía completa (qué es, su potencial, formación paso a paso): **https://inematds.github.io/engenheiro-de-campo/guia/es/**

Prueba en el navegador, 3 minutos: **https://inematds.github.io/engenheiro-de-campo/kit/1-teste-metade/teste-metade.html** (en portugués)

## Empieza pidiéndoselo a tu IA

Abre Claude Code o Codex en una carpeta nueva y pega:

```
Lee el kit "ingeniero de campo de IA" en https://github.com/inematds/engenheiro-de-campo (el README lo explica todo).
Después ayúdame a prepararme para esta profesión, en español sencillo:
1. Haz conmigo la prueba "qué mitad tienes", una pregunta a la vez, y dime el resultado.
2. Prepara un plan de 4 semanas centrado en mi mitad más débil, usando los pasos del kit.
3. Empieza conmigo el primer ejercicio del plan.
No instales ni cambies nada en mi computadora sin mostrármelo antes y esperar a que diga que sí.
```

## Por qué existe esta vacante

Las empresas compran IA más rápido de lo que logran hacerla funcionar en sus sistemas desordenados. En vez de entregar una contraseña y desearle suerte al cliente, la empresa de IA envía a un ingeniero para que se siente a su lado: no vende horas de trabajo ni software, entrega un resultado. Lo poco común es tener **las dos mitades**: quien construye y la persona en quien confía el cliente.

## Basado en vacantes oficiales (verificadas el 20/11/2026)

- **OpenAI**, vacante *Forward Deployed Engineer (FDE) - SF*: rango publicado "$185K – $300K • Offers Equity". [Vacante](https://jobs.ashbyhq.com/openai/967f94aa-1706-4dba-ac89-bfbc2c38b688) · registro en [`fontes/vaga-openai.json`](fontes/vaga-openai.json) (en portugués).
- **Anthropic**, vacantes *Forward Deployed Engineer* y *Staff Forward Deployed Engineer*: entregar "MCP servers, sub-agents, and agent skills", "identify and codify repeatable deployment patterns", llegar "with only a business problem and leave with a defensible technical strategy". [Vacante FDE](https://job-boards.greenhouse.io/anthropic/jobs/5391021008) · [vacante Staff](https://job-boards.greenhouse.io/anthropic/jobs/5449229008) · registro en [`fontes/vagas-anthropic.json`](fontes/vagas-anthropic.json) (en portugués).
- **Mercado, más allá de OpenAI:** las ofertas oficiales de ingeniero de campo publican salarios anuales de US$ 135 mil (Palantir) a US$ 415 mil (Cohere), con Anthropic, Harvey, Ramp, Databricks y Scale AI entre ambos extremos. Hay ofertas abiertas con Brasil en la ubicación: Decagon (remota, pide portugués, español e inglés), Cognition (presencial en São Paulo) y Databricks (FDE Brazil). Salesforce dice en su propio blog que formará un equipo de 1.000 ingenieros de campo. Los 23 elementos, con el texto exacto, el enlace y el tipo de cada fuente (oferta oficial, blog oficial o prensa), están en [`fontes/mercado.json`](fontes/mercado.json) (en portugués).

Las vacantes cambian: consulta siempre la página oficial.

---

## El proceso, de principio a fin

Quién lo hace: 🧠 sesión (tú, con la IA a tu lado) · ⚙️ script del kit · 🤖 `claude -p` (o Codex) con tu suscripción.

| # | Paso | Comando / archivo | Quién |
|---|---|---|---|
| 1 | Descubrir qué mitad tienes | `python3 kit/1-teste-metade/teste_metade.py` (o la página `teste-metade.html`) | ⚙️ |
| 2 | Seguir la ruta, una práctica por elemento | [`kit/2-trilha/TRILHA.md`](kit/2-trilha/TRILHA.md) (en portugués) | 🧠 |
| 3 | Practicar el descubrimiento con el cliente simulado (4 sectores) | pegar un bloque de [`kit/3-cliente-simulado/PROMPTS.md`](kit/3-cliente-simulado/PROMPTS.md) en la IA; revisar con la [lista de verificación](kit/3-cliente-simulado/CHECKLIST-DESCOBERTA.md) | 🤖 + 🧠 |
| 4 | Escribir el alcance de 1 página y validarlo | copiar [`modelo.md`](kit/4-escopo-1-pagina/modelo.md) → `python3 kit/4-escopo-1-pagina/validar_escopo.py meu-escopo.md` | 🧠 + ⚙️ |
| 5 | Ejecutar el eval de ejemplo y luego el tuyo | `python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py` | ⚙️ |
| 6 | Proyecto de prueba con cliente real + estudio de caso | [`kit/6-projeto-prova/ROTEIRO.md`](kit/6-projeto-prova/ROTEIRO.md) + [`MODELO-ESTUDO-DE-CASO.md`](kit/6-projeto-prova/MODELO-ESTUDO-DE-CASO.md) | 🧠 |
| 7 | Buscar vacantes | [`kit/7-vagas/VAGAS.md`](kit/7-vagas/VAGAS.md) | 🧠 |
| 8 | Practicar la entrevista (caso, proyecto, técnica, habilidades interpersonales) | pegar los prompts de [`kit/8-entrevista/ENTREVISTA.md`](kit/8-entrevista/ENTREVISTA.md) en la IA | 🤖 + 🧠 |
| 9 | Entender la semana de trabajo | [`kit/9-semana/SEMANA.md`](kit/9-semana/SEMANA.md) | 🧠 |

---

## Instalación técnica

### Requisitos previos

- Python 3.8 o posterior (solo biblioteca estándar; no hace falta instalar nada con `pip`).
- Git, para descargar el kit. No se necesita ninguna clave de API ni ningún modelo local.

```bash
git clone https://github.com/inematds/engenheiro-de-campo.git
cd engenheiro-de-campo
```

### Comandos

```bash
# 1. prueba "qué mitad tienes" (interactiva o con el número de la opción elegida en cada una de las 12 preguntas)
python3 kit/1-teste-metade/teste_metade.py
python3 kit/1-teste-metade/teste_metade.py --respostas 3,3,2,3,2,3,1,1,2,0,1,2
#    volver a generar la página después de cambiar perguntas.json
python3 kit/1-teste-metade/gerar_pagina.py

# 4. validar un alcance (0 = aprobado, 1 = reprobado)
python3 kit/4-escopo-1-pagina/validar_escopo.py kit/4-escopo-1-pagina/exemplo-preenchido.md
python3 kit/4-escopo-1-pagina/validar_escopo.py kit/4-escopo-1-pagina/exemplo-reprovado.md

# 5. eval: una versión, comparar dos, casos nuevos, nota mínima
python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v1.py
python3 kit/5-eval/rodar_eval.py --comparar kit/5-eval/automacao_v1.py kit/5-eval/automacao_v2.py
python3 kit/5-eval/rodar_eval.py --casos kit/5-eval/casos-novos.json kit/5-eval/automacao_v2.py
python3 kit/5-eval/rodar_eval.py kit/5-eval/automacao_v2.py --minimo 0.9
```

### El eval de ejemplo, medido el 20/11/2026

| | `casos.json` (30) | `casos-novos.json` (10) |
|---|---|---|
| `automacao_v1.py` (palabra clave simple) | 18/30 | 4/10 |
| `automacao_v2.py` (corregida a partir de los fallos de la v1) | 30/30 · 12 corregidos, 0 rotos | 4/10 |

La v2 memorizó los casos que usamos para corregirla; en los casos nuevos quedó igual que la v1. Esa es la lección del kit: un eval serio siempre tiene un conjunto separado. Para evaluar tu agente, copia [`automacao_meu_agente.py`](kit/5-eval/automacao_meu_agente.py) y lee [`kit/5-eval/LEIA.md`](kit/5-eval/LEIA.md).

El validador de alcance acepta los títulos de sección en portugués, inglés y español (`Problema`/`Problem`, `O número`/`The number`/`El número`, `Pronto quando`/`Done when`/`Listo cuando`, `Fora do escopo`/`Out of scope`/`Fuera del alcance`).

### Archivos

```
kit/1-teste-metade/     perguntas.json (fuente única), teste_metade.py, gerar_pagina.py, teste-metade.html
kit/2-trilha/           TRILHA.md
kit/3-cliente-simulado/ PROMPTS.md (4 sectores), CHECKLIST-DESCOBERTA.md
kit/4-escopo-1-pagina/  modelo.md, exemplo-preenchido.md, exemplo-reprovado.md, validar_escopo.py
kit/5-eval/             casos.json, casos-novos.json, automacao_v1.py, automacao_v2.py, rodar_eval.py, automacao_meu_agente.py, LEIA.md
kit/6-projeto-prova/    ROTEIRO.md, MODELO-ESTUDO-DE-CASO.md
kit/7-vagas/            VAGAS.md
kit/8-entrevista/       ENTREVISTA.md
kit/9-semana/           SEMANA.md
fontes/                 vacantes oficiales verificadas (URL, texto literal, fecha)
guia/                   página PT + en/ + es/
tests/                  pruebas automáticas
```

### Pruebas

```bash
python3 -m unittest discover -s tests -v
```

31 pruebas cubren: la prueba mitad (12 preguntas, 6 por mitad, los 3 resultados posibles, empate dentro del margen, respuestas no válidas, la página con las mismas preguntas del JSON), el validador de alcance (ejemplo aprobado, ejemplo y modelo reprobados, sin número, un solo número, sin comillas, sección faltante, títulos en EN/ES, códigos de salida) y el eval (casos bien formados, las puntuaciones medidas 18/30, 30/30 y 4/10, la comparación de 12 corregidos y 0 rotos, una automatización que falla cuenta como error, código de salida de `--minimo`, el modelo del agente no se ejecuta sin configurarlo), y la política de cifras: solo valores que aparecen en el texto de una oferta o blog oficial registrado en `fontes/` (el rango de OpenAI, igual al registrado), el único porcentaje de prensa siempre acompañado de la fuente (Fortune, con datos de Lightcast) y los enlaces de la sección de mercado iguales en los tres idiomas y todos registrados en `fontes/`.

## Licencia

MIT. Contenido abierto y gratuito de [INEMA.CLUB](https://inema.club).