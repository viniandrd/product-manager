---
name: analisar-estimativas
description: Analisa as tasks concluídas nas últimas sprints do time da sessão e identifica as que foram subestimadas ou superestimadas, comparando Original Estimate com Completed Work. Mede a precisão do time e a qualidade dos dados de horas (se o board é atualizado durante a task ou só no fim), aponta padrões por Activity, tamanho, sprint, PBI e causa, e compara as tasks com e sem uso de IA. Use quando pedirem para analisar as estimativas, a precisão das horas, estimado x realizado, quais cards foram estimados errado ou o efeito da IA no esforço das tasks.
---

# Analisar estimativas

Esta skill só lê o board. Nunca crie, altere ou comente itens enquanto gera a análise.

Carregue a skill regras-de-estimativa antes de começar. As classes, o Effort congelado, as tasks do planejamento, as origens da diferença, as causas e o registro de uso de IA usados aqui estão lá.

## 1. Recorte
- As últimas 3 sprints já encerradas do time (work, ação list_team_iterations). Se pedirem outro período, use o pedido.
- Tasks em Done dessas sprints (wit_work_item, ação list_for_iteration). Ignore Removed.
- A sprint atual não entra: as tasks dela ainda não terminaram.

## 2. Dados de cada task
- Título, Activity, Assigned To, PBI ou Bug pai (com o Effort e o estado dele), Original Estimate (OE), Completed Work (CW), Remaining Work (RW) e tags.
- Revisões (list_revisions): servem para reconstruir a estimativa e medir a qualidade dos dados. Se houver mais de 60 tasks, busque as revisões de uma amostra de 30, espalhada pelas sprints, e diga que é amostra. As tasks sem OE entram sempre, porque precisam das revisões para ter estimativa.

## 3. Estimado e realizado
- Estimado: OE. Se estiver vazio, o primeiro valor não vazio de RW nas revisões, marcado como "reconstruída". Sem nenhum dos dois: "sem estimativa".
- Realizado: CW. Vazio ou 0: "sem realizado". Não aproxime pelo tempo corrido e não misture valores aproximados com reais.
- Razão = realizado ÷ estimado.
- Classes: subestimada, precisa e superestimada, pelos limites da regras-de-estimativa (seção 4).
- Só tasks com estimado e realizado entram na precisão. As outras entram só na qualidade dos dados.

### PBIs e Bugs
Como o Effort é em horas, compare também cada PBI ou Bug em Done dessas sprints: estimado = Effort congelado; realizado = soma do CW das tasks, ou o CW do próprio item, se ele não tiver task (regras-de-estimativa, seções 2 e 3). Use as mesmas classes.
- Se o Effort mudou depois de congelar, marque "Effort alterado" e mostre os dois valores.
- Na qualidade dos dados, inclua a % de PBIs e Bugs com Effort alterado depois de entrar na sprint. Isso quebra a regra do time de congelar o Effort.
- PBI sem Effort, ou com alguma task sem CW, fica fora desta comparação.
- PBI preciso com tasks erradas: os erros se compensaram.
- PBI subestimado com tasks precisas: o trabalho cresceu com tasks criadas depois do planejamento. Isso é escopo, não estimativa da task.
- Separe a diferença entre o realizado e o Effort congelado nas três origens de PBI da regras-de-estimativa (seção 7): quebra, estimativa das tasks e trabalho descoberto. As tasks do planejamento e as tasks novas são as da seção 6 de lá.
- Task do planejamento sem OE deixa a quebra incompleta: o PBI fica fora da separação, mas continua na classificação.
- Pelas tags de causa das tasks novas, separe o trabalho descoberto em escopo novo e o que faltou na quebra (complexidade).

## 4. Qualidade dos dados
Calcule antes de qualquer conclusão, porque dados ruins invalidam a análise:
- % de tasks com OE, com estimativa reconstruída e sem estimativa.
- % de tasks com CW.
- % de tasks com registro de uso de IA (uma das tags `ia-*`).
- Atualização durante o trabalho: % de tasks com pelo menos uma mudança de CW ou RW enquanto estavam em In Progress, sem contar a revisão que as levou para Done.
- Lançamento só no fim: % de tasks em que todo o CW apareceu na mesma revisão que as levou para Done.
- Pulo de estado: % de tasks que foram de To Do direto para Done.
- Re-estimativa: % de tasks em que o RW subiu em algum momento, ou seja, descobriram mais trabalho no meio.

Se menos da metade das tasks tem estimado e realizado, diga no resumo que a precisão medida não representa o time e que o primeiro passo é atualizar o board todo dia (skill atualizar-horas) por pelo menos 2 sprints.

## 5. Padrões
Em cada recorte, mostre quantas tasks, a razão mediana e a % de precisas:
- Por Activity.
- Por tamanho da estimativa, em dias de 10h: até 1 dia (10h), mais de 1 até 2 dias, mais de 2 até 4 dias, mais de 4 dias.
- Por sprint, da mais antiga para a mais nova, para ver se melhora.
- Por PBI ou Bug pai: destaque os que têm 2 ou mais tasks subestimadas, porque isso costuma ser problema de refinamento, não da estimativa da task.
- Por causa: contagem de cada tag `causa-*`, separada entre tasks subestimadas (com as tasks novas de trabalho a mais) e superestimadas, porque a mesma causa tem leituras diferentes nos dois sentidos (regras-de-estimativa, seção 8).
- Por dev: só se quem lidera pedir. Apresente como calibração ("as estimativas de X tendem a ficar 1,4× abaixo do realizado"), nunca como ranking ou avaliação.
- Recorte com menos de 5 tasks: mostre, mas diga que a amostra é pequena.

Use a mediana, não a média: uma única task que levou 10× o estimado distorce a média.

## 6. Efeito da IA
Compare as tasks pelo uso de IA (regras-de-estimativa, seção 9), sempre dentro das mesmas sprints. Tasks sem registro de uso ficam fora.
- Grupos: `ia-intenso`, `ia-parcial` e `ia-nenhum`. Se um grupo tiver poucas tasks, junte intenso e parcial em "com IA".
- Em cada Activity e em cada faixa de tamanho, mostre para cada grupo: quantas tasks, a razão mediana e a % de superestimadas e de subestimadas.
- Efeito = razão mediana com IA ÷ razão mediana sem IA, na mesma Activity. Ex.: 0,72 ÷ 1,05 ≈ 0,69, ou seja, com IA as tasks custam cerca de 31% menos em relação ao estimado.
- Horas: soma de (OE − CW) das tasks com IA. Chame de "horas abaixo do estimado nas tasks com IA", não de "horas economizadas pela IA": se a estimativa já contava com a IA, essa diferença não aparece.
- Causas: quantas tasks têm `causa-ia` com `estimativa-superestimada` (a IA acelerou) e com `estimativa-subestimada` (a IA gerou retrabalho).
- Por sprint: se a diferença entre com IA e sem IA diminui sprint a sprint, o time está passando a estimar já contando com a IA.
- Grupo com menos de 10 tasks numa Activity: mostre os números, mas diga que ainda não dá para concluir.
- Cuidados, sempre escritos no relatório:
  - É associação, não prova. Se os devs mais experientes ou as tasks mais simples concentram o uso de IA, o efeito parece maior do que é. Mostre como os grupos se distribuem por Activity e por tamanho, para isso ficar visível. Por dev, só se quem lidera pedir.
  - Não compare antes e depois de adotar a IA: a daily nova mudou a qualidade dos dados no mesmo período.

### Produtividade do time
Quando o time passa a estimar contando com a IA, a diferença em horas some. Para ver o ganho ao longo do tempo, mostre também, por sprint:
- quantos PBIs e Bugs foram para Done;
- as horas disponíveis do time, se houver capacidade cadastrada (work, ação get_team_capacity);
- a mediana do tempo de ponta a ponta de cada PBI ou Bug, do dia de entrada na sprint até ir para Done (State Change Date).

## 7. Relatório

```
Estimativas do time <TIME> · dd/mm/aaaa
Sprints analisadas: <nomes> · <n> tasks em Done

Resumo
- Precisas: <x>% · Subestimadas: <y>% · Superestimadas: <z>%
- Razão mediana: <r> (1,0 = realizado igual ao estimado)
- Horas: <estimadas>h estimadas, <realizadas>h realizadas (<dias> e <dias> dias)
- PBIs e Bugs: <x>% precisos, <y>% subestimados, <z>% superestimados (Effort × horas das tasks)
- IA: <o efeito numa frase, ou "ainda sem amostra suficiente">
- Qualidade dos dados: <uma frase>

Qualidade dos dados
- ...

As 10 maiores diferenças
| ID | Título | Activity | Estimado | Realizado | Razão | Causa |

Origem do estouro nos PBIs e Bugs
| Origem | Horas | % do estouro | O que corrigir |
| Quebra | | | Estimar o PBI depois de pensar na quebra em tasks |
| Estimativa das tasks | | | Calibrar as tasks (ver Padrões) |
| Trabalho descoberto | | | Refinamento: critérios de aceite e dúvidas em aberto |

Os 5 PBIs com maior diferença
| ID | Título | Effort | Realizado | Razão | Quebra | Tasks | Descoberto |

Efeito da IA
| Activity | IA intenso | IA parcial | Sem IA | Efeito |
(cada célula: tasks · razão mediana)
- Causas: <n> tasks em que a IA acelerou, <m> em que gerou retrabalho
- Horas abaixo do estimado nas tasks com IA: <h>h
- Uso de IA registrado em <x>% das tasks
- Cuidados: <os dois cuidados da seção 6>

Produtividade do time
| Sprint | PBIs e Bugs em Done | Horas disponíveis | Ponta a ponta (mediana) |

Padrões
- ...

Recomendações
- ...

Sugestões (Scrum)
- ...
```

- Nas 10 maiores diferenças, ordene pela diferença em horas, não pela razão, e misture subestimadas e superestimadas. Marque estimativas reconstruídas com "(r)".
- Causa: a tag de causa, se houver; senão, "não registrada". Não invente causas.
- Na origem do estouro, some só os PBIs e Bugs subestimados, para mostrar de onde veio o estouro. Nos 5 PBIs com maior diferença, mostre as três origens com sinal (ex.: +6h, −2h).
- Recomendações: de 2 a 5, cada uma ligada a um número do relatório. Exemplos:
  - "Tasks acima de 2 dias (20h) têm razão mediana 1,6 → quebrar tasks em até 2 dias no planning."
  - "Testing tem razão mediana 1,5 → revisar como o time estima testes."
  - "Só 30% das tasks têm Completed Work → atualizar o board todo dia por 2 sprints antes de tirar conclusões."
  - "4 PBIs concentram metade das subestimadas → olhar o refinamento desses PBIs."
  - "Trabalho descoberto é 55% do estouro dos PBIs → reforçar critérios de aceite e dúvidas em aberto no refinamento."
  - "Em Development, tasks com IA intensa terminam com 70% do estimado → estimar já contando com a IA quando ela for usada."
  - "Razão mediana estável em 1,3 → considerar esse fator ao comparar horas com a capacidade no planejamento."
- Sugestões (Scrum): carregue a skill praticas-scrum. Aqui elas viram temas para a Retrospectiva e para o refinamento. Não repita as recomendações: cite a prática do Scrum que sustenta a mudança.
- Datas em dd/mm/aaaa.
