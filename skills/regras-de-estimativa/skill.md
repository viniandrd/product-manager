---
name: regras-de-estimativa
description: Referência única das regras de estimativa do time. Define as unidades (1 dia = 10h), qual campo é a estimativa de cada tipo, o Effort congelado, a projeção, os limites de estouro e de superestimativa, os sinais, as tasks do planejamento, as origens da diferença de PBI e Feature e as causas. Não faz nada sozinha: as skills atualizar-horas, atualizar-cadeia, analisar-estimativas e planejar-sprint carregam esta skill para usar as mesmas definições. Use também quando perguntarem como o agente calcula estouro, atraso ou precisão.
---

# Regras de estimativa

Esta skill só define regras. Ela não lê nem grava nada no board.

Se mudar uma regra aqui, mude também a cópia curta na skill lembrete-diario. Ela roda sem ninguém acompanhando e não carrega esta skill.

## 1. Unidades
- Effort, Original Estimate, Completed Work e Remaining Work são em horas.
- 1 dia de trabalho = 10h. "Meio dia" = 5h; "2 dias" = 20h.
- Ao mostrar valores acima de 10h, mostre também em dias (25h = 2,5 dias).
- Arredonde para uma casa decimal.

## 2. Campos e estimativa de cada tipo

| Tipo | Estimativa | Gasto | Falta |
|---|---|---|---|
| Task | Original Estimate (OE), gravado uma vez só e nunca alterado | Completed Work (CW) | Remaining Work (RW) |
| PBI e Bug | Effort congelado: o Effort que o item tinha quando entrou numa sprint pela primeira vez | Soma do CW das tasks | Soma do RW das tasks |
| Feature | Effort congelado em DEV: o Effort que ela tinha quando entrou em DEV pela primeira vez. Se estava vazio, a soma do Effort dos PBIs e Bugs filhos | Soma do CW das tasks | Soma do RW das tasks |
| Epic | Não é comparado | Soma do CW das tasks | Soma do RW das tasks |

- O Effort congelado e a data em que congelou vêm das revisões do item (list_revisions). A data em que o PBI ou Bug entrou na sprint é o "dia de entrada".
- Some sempre as tasks, nunca os valores dos pais intermediários, para não contar a mesma hora duas vezes. Tasks em Removed não entram.
- PBI ou Bug sem nenhuma task: o CW e o RW são os dele mesmo, e ele conta como uma task nas somas acima dele.

## 3. Projeção e realizado
- Projeção = CW + RW: quanto o item vai custar no total, se a previsão estiver certa.
  - Task: CW + RW dela.
  - PBI ou Bug: soma de (CW + RW) das tasks dele.
  - Feature: soma de (CW + RW) das tasks abaixo dela. PBI ou Bug filho sem task entra com o CW + RW dele; se os dois estiverem vazios, com o Effort, que é o trabalho que falta e ainda não foi quebrado.
- Realizado = CW, quando o item está em Done (o RW é 0).
- Razão = projeção (ou realizado) ÷ estimativa.

## 4. Limites

| Classe | Regra |
|---|---|
| Subestimada (estouro) | Razão acima de 1,25 |
| Precisa | Razão de 0,8 a 1,25 |
| Superestimada | Razão abaixo de 0,8. Só no fechamento |

Diferença menor que 5h (meio dia) conta como precisa, qualquer que seja a razão.

## 5. Sinais

| Sinal | Regra |
|---|---|
| Estouro | Task com projeção acima de 125% da OE, com diferença de pelo menos 5h |
| Atrasada | Task em que hoje passou da data prevista: data em que entrou em In Progress + (OE ÷ 10, arredondado para cima) dias úteis, mais os dias de folga do dev nesse período |
| Risco na sprint | Task com RW maior que as horas que o dev ainda tem até o fim da sprint |
| Sem atualização | Task em In Progress sem nenhuma alteração desde o último dia útil |
| Pai estourado | PBI, Bug ou Feature com projeção acima de 125% da estimativa dele (seção 2), com diferença de pelo menos 5h |
| Quebra acima do Effort | PBI ou Bug em que a soma do OE das tasks do planejamento passa do Effort congelado, com diferença de pelo menos 5h |
| Effort alterado | PBI ou Bug, ou Feature que já passou por DEV, com o Effort atual diferente do Effort congelado |

O que fazer com cada sinal fica em cada skill: a daily pergunta a causa, o lembrete só lista, a análise conta.

## 6. Tasks do planejamento e tasks novas
Pela Created Date das tasks de um PBI ou Bug:
- Tasks do planejamento: criadas até o fim do mais tarde entre o dia de entrada do item na sprint e o primeiro dia útil da sprint.
- Tasks novas: criadas depois. São o trabalho descoberto no meio.

## 7. Origem da diferença
Em cada caso, as três partes somam a diferença total entre a projeção (ou o realizado) e a estimativa. Cada parte pode ser negativa, quando sobrou hora.

PBI ou Bug:
- Quebra = soma do OE das tasks do planejamento − Effort congelado.
- Estimativa das tasks = soma de (CW + RW) das tasks do planejamento − soma do OE delas.
- Trabalho descoberto = soma de (CW + RW) das tasks novas.
- Task do planejamento sem OE deixa a quebra incompleta: diga isso.

Feature:
- PBIs iniciais são os PBIs e Bugs filhos criados até o dia em que a Feature entrou em DEV. PBIs novos são os criados depois.
- Diferença entre a Feature e os PBIs iniciais = soma do Effort dos PBIs iniciais − Effort congelado da Feature.
- Estouro dos PBIs = soma de (projeção − Effort) dos PBIs iniciais. PBI sem task conta com projeção = CW + RW dele, ou o Effort, se os dois estiverem vazios.
- PBIs novos depois de DEV = soma da projeção dos PBIs novos.
- Feature sem Effort em DEV: mostre só o estouro dos PBIs.

O que cada origem indica:

| Origem | Indica | O que corrigir |
|---|---|---|
| Quebra | O Effort foi dado antes de pensar nas tasks | Estimar o PBI depois de pensar na quebra |
| Estimativa das tasks | As tasks custaram mais do que o previsto | Calibrar a estimativa das tasks (Activity, tamanho) |
| Trabalho descoberto | Apareceu trabalho depois do planejamento | Refinamento: critérios de aceite e dúvidas em aberto |
| PBIs novos depois de DEV | A Feature cresceu | Escopo da Feature: negociar ou re-planejar |
| Diferença entre a Feature e os PBIs iniciais | A quebra da Feature em PBIs não fechava com o Effort dela | Estimar a Feature depois de pensar nos PBIs |

## 8. Causas
Causas de estouro ou atraso de task, cada uma com a sua tag:
- escopo (`causa-escopo`): a task cresceu ou mudou depois de estimada.
- complexidade (`causa-complexidade`): era mais difícil do que parecia. É o erro de estimativa propriamente dito.
- bloqueio (`causa-bloqueio`): ficou esperando alguém ou alguma coisa.
- interrupção (`causa-interrupcao`): o dev foi puxado para suporte, incidente ou outra demanda.
- não sei ainda: não marca nada e pergunta de novo depois.

Atraso sem estouro de horas quase sempre é bloqueio, interrupção, trabalho em paralelo ou board desatualizado, e não erro de estimativa. Por isso a causa é perguntada, não deduzida.
