# FALHAS

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-11-20 | nav do guia transbordava na horizontal (EN 1600 px numa tela de 1440; com o link "O mercado", também em 900 px) | breakpoints do nav: `opt` some até 1760 px, `sec` até 1220 px; medir scrollWidth por HTTP em 390/900/1440/1761 | infra |
| 2026-11-20 | deploy do Pages do 2º push falhou: "No artifacts named github-pages" (instabilidade do GitHub) | `gh run rerun <id>`; passou na 1ª | infra |
