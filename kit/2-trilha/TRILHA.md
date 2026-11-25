# Trilha: o que o engenheiro de campo de IA precisa aprender

Regra de ouro: **estude mais a metade que o teste (passo 1) apontou como fraca**, em vez de estudar tudo igual.
Cada item tem uma **prática concreta**: só conta como aprendido quando a prática está feita e guardada numa pasta sua.

Metade do construtor = itens 1 a 4. Metade da confiança do cliente = itens 5 a 8.

---

## 1. Python com a IA escrevendo

**Por quê:** as vagas pedem Python. Mas ninguém espera que você digite tudo à mêo: o Claude Code e o Codex escrevem; você precisa **ler, pedir a mudança certa e testar**.

**Prática:** peça ao Claude Code ou ao Codex um script que lê uma planilha CSV de vendas e diz o total por mês. Depois:
- quebre de propósito (coloque uma data em formato errado no CSV) e veja o erro;
- peça para a IA tratar o caso e **escrever um teste** para ele;
- explique, em 3 frases, o que cada parte do script faz. Se nêo consegue explicar, ainda nêo aprendeu.

## 2. APIs e integrações

**Por quê:** o trabalho real é ligar sistemas que nêo foram feitos para conversar: sistema de vendas, planilha, e-mail, banco de dados, o ERP velho do cliente.

**Prática:** escolha uma API pública e gratuita (ex.: feriados nacionais, CEP, cotaçêo do dólar). Com a IA, faça um script que busca o dado, salva numa planilha e trata três problemas: a API fora do ar, resposta vazia e limite de uso. Escreva em 5 linhas o que acontece em cada caso.

## 3. Agentes: o modelo decide, chama ferramenta, em vários passos

**Por quê:** "agente" é quando o modelo decide o que fazer a seguir e chama ferramentas (buscar, gravar, consultar) até terminar. É diferente de usar a IA para escrever código. As vagas pedem que você entregue coisas como servidores MCP (o jeito padrêo de dar ferramentas para a IA), sub-agentes e skills (receitas que a IA segue).

**Prática:** monte um agente pequeno com 2 ferramentas (ex.: ler um arquivo de pedidos e gravar um resumo). Anote, para 5 pedidos diferentes, quais ferramentas ele chamou e em que ordem. Depois transforme o que funcionou numa skill reutilizável: o trabalho do engenheiro de campo é pegar o que deu certo uma vez e tornar repetível.

## 4. EVALS: o item principal

**Por quê:** **demo nêo prova; eval prova.** Uma demo mostra que funcionou uma vez, no exemplo que você escolheu. Um eval é uma lista de casos reais (entrada + resposta esperada) que dá uma nota, mostra cada falha e deixa comparar a versêo 1 com a versêo 2. É isso que convence o cliente e o diretor.

**Prática (com o passo 5 do kit):**
1. rode o eval da automaçêo v1 e da v2 e leia as falhas;
2. rode a v2 nos **casos novos** e veja a nota despencar: a v2 decorou os casos, nêo aprendeu a regra;
3. troque a automaçêo por uma sua (ou pelo seu agente) e chegue a uma nota que você consegue defender **nos casos novos**;
4. escreva os casos com o cliente, nêo sozinho: ele é quem sabe o que é "certo".

## 5. Descoberta

**Por quê:** o cliente pede o que viu no LinkedIn ("quero um chatbot"). O seu trabalho é achar o problema real, o gargalo real e quem sofre com ele. Quem pula a descoberta constrói a coisa errada muito bem.

**Prática:** 3 sessões com o cliente simulado (passo 3), cada uma de um setor. Use o checklist. Guarde a nota que a IA deu e o que você esqueceu de perguntar.

## 6. Escopo

**Por quê:** sem escopo o projeto cresce até ninguém saber o que é "pronto". O escopo de 1 página diz: o problema nas palavras do cliente, **o UM número** que vai mexer, o que é pronto e o que fica fora. Se você nêo consegue dizer o número, ainda nêo tem projeto.

**Prática:** depois de cada sessêo de descoberta, escreva o escopo (passo 4) e passe no validador até aprovar.

## 7. Demo para executivo

**Por quê:** diretor nêo quer ver o código. Quer saber: o que mudou, quanto, o que custa, qual o risco e qual o próximo passo.

**Prática:** grave 5 minutos apresentando a triagem do passo 5 como se fosse para a dona da empresa: o problema dela, a nota do eval, o que ainda falha e o que você propõe. Assista e corte tudo que for jargêo.

## 8. Gestêo de mudança (fazer o time usar)

**Por quê:** o projeto só conta quando as pessoas usam. Ferramenta boa que ninguém usa vale zero.

**Prática:** no projeto-prova (passo 6), combine com 1 pessoa do time que ela vai usar por 5 dias. Volte 2 semanas depois e meça: usou? quantas vezes? o número do escopo mexeu? Escreva o que fez as pessoas usarem ou largarem.

---

**Como saber que terminou a trilha:** você tem uma pasta com 8 práticas feitas, um eval com nota que você defende em casos novos e pelo menos 3 escopos aprovados pelo validador. Aí vá para o projeto-prova.
