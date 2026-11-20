# Entrevista: treino com a IA

As entrevistas para engenheiro de campo costumam ter 4 partes. Espere sempre um **caso**.

| Rodada | O que testam | Como treinar |
|---|---|---|
| Caso de negócio | chegar só com um problema de negócio e sair com uma estratégia técnica que se defende | prompt 1 |
| Projeto-prova | contar o seu projeto como se o entrevistador fosse o cliente | prompt 2 |
| Técnica | depurar código existente usando ferramentas de IA; desenho de sistema | prompts 3 e 4 |
| Comportamental | conflito com cliente, prazo, erro seu, dizer não | prompt 5 |

Regra da entrevista de caso: **pergunte o que o negócio quer mexer antes de propor qualquer solução.**

---

## Prompt 1: entrevista de caso

```
Você é entrevistador de uma empresa de IA contratando um engenheiro de campo (forward deployed
engineer). Me dê UM problema de negócio de um cliente fictício, em 3 frases, sem detalhes técnicos
(ex.: uma seguradora que demora para responder sinistro). Depois:
- responda só o que eu perguntar, como o cliente responderia;
- se eu propuser solução antes de entender o problema e o número, anote como ponto negativo;
- após 20 minutos, ou quando eu disser "minha proposta é", me peça a estratégia técnica:
  arquitetura simples, dados, riscos, como vou provar que funciona (eval) e como vou medir.
No fim, saia do papel e dê nota de 0 a 10 em: descoberta, clareza, defesa técnica, prova e
comunicação, com 3 melhorias concretas. Faça a entrevista em português (ou em inglês, se eu pedir).
```

## Prompt 2: o projeto-prova como se o entrevistador fosse o cliente

```
Vou te contar um projeto que fiz. Faça o papel de um cliente cético da área de <setor>, que está
pensando em contratar algo parecido. Interrompa como um cliente real: "quanto custou?", "e se
der errado?", "como você sabe que funcionou?", "minha equipe vai usar?". Depois de 15 minutos,
saia do papel e diga: onde eu fui convincente, onde soei técnico demais, que número faltou.
```

## Prompt 3: depurar código existente com IA

```
Escreva um script Python de uns 80 linhas, de uma integração real (ler pedidos de um CSV, chamar
uma API fictícia, gravar resultado), com 3 bugs escondidos: um de dado, um de lógica e um de
tratamento de erro. Não me diga onde estão. Eu vou achar usando uma ferramenta de IA e você vai
avaliar: como eu investiguei, se eu confirmei cada correção com um teste e se eu expliquei o
porquê. Me dê o script e espere.
```

## Prompt 4: desenho de sistema

```
Me dê um desafio de desenho de sistema de engenheiro de campo: um agente de IA que precisa
funcionar dentro de uma empresa com sistema antigo, controle de acesso e regra de privacidade.
Peça que eu desenhe em texto: componentes, de onde vêm os dados, o que o agente pode e não pode
fazer, como registro o que ele fez, como avalio (eval) e como implanto aos poucos. Faça 5
perguntas difíceis durante, uma de cada vez, e no fim dê nota e diga o que um sênior faria.
```

## Prompt 5: comportamental

```
Faça 5 perguntas comportamentais de entrevista para engenheiro de campo de IA, uma de cada vez:
cliente insatisfeito, pedido que cresceu no meio do projeto, erro meu em produção, discordância
com o time de produto, e uma vez em que eu disse não a um cliente. Peça respostas no formato
situação, o que eu fiz, resultado com número. Depois de cada resposta, diga o que faltou.
```

---

## Roteiro da sua história (2 minutos)

1. O cliente pediu ___. O problema real era ___ (como você descobriu).
2. O número: de ___ para ___ .
3. O que eu construí, em uma frase.
4. Como provei: eval com ___ casos, nota ___ ; em casos novos ___ .
5. O que deu errado e o que eu fiz.
6. O que medi 2 semanas depois e quem está usando.
