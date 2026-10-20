---
name: praticas-scrum
description: Referência das práticas do Scrum (Scrum Guide 2020) que o agente compara com o board para dar sugestões: Sprint Goal, mudança de escopo na sprint, Sprint Planning, Daily Scrum, refinamento do backlog, Definition of Done, Sprint Review, Retrospectiva e impedimentos. Define como classificar as sugestões (críticas e melhorias), a ordem, o limite por resposta e o meio-termo quando uma prática conflita com uma convenção do time. Não faz nada sozinha: as skills planejar-sprint, refinar-backlog, atualizar-horas, relatorio-status e analisar-estimativas carregam esta skill para fechar a resposta com as sugestões. Use também quando perguntarem o que o Scrum diz sobre algo do board ou por que o agente fez uma sugestão.
---

# Práticas do Scrum

Esta skill só define as práticas e como sugerir. Ela não lê nem grava nada no board: os dados vêm da skill que a carregou.

## 1. Fonte
- A referência é o Scrum Guide de 2020 (scrumguides.org). Cada sugestão cita a parte dele que a sustenta, pelo nome: Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, Product Backlog, Sprint Backlog, Increment, Developers, Product Owner ou Scrum Master.
- Não atribua ao Scrum o que ele não diz. O Scrum Guide não fala de horas, tasks, story points, velocidade, Effort nem estados do board. Onde ele não diz nada, vale a convenção do time e não há sugestão.
- Práticas de mercado que não estão no Scrum Guide (limite de trabalho em andamento, Definition of Ready) só entram como melhoria, dizendo que são práticas de mercado, não do Scrum.

## 2. Práticas e sinais
Uma sugestão só existe quando há um sinal concreto no board. A coluna Grupo é o ponto de partida da classificação (seção 4).

### Sprint e Sprint Goal
| Sinal no board | Sugestão | Scrum Guide | Grupo |
|---|---|---|---|
| Sprint sem objetivo, ou com um objetivo que é só a lista de itens | Definir o Sprint Goal em uma frase, com o resultado esperado. A skill planejar-sprint propõe um | Sprint Backlog (Sprint Goal) | Crítica |
| RW da sprint maior que as horas que o time ainda tem, ou PBI ligado ao objetivo que não começou na segunda metade da sprint | Conversar com o Product Owner agora sobre o que sai da sprint, para proteger o objetivo | Sprint | Crítica |
| Itens que entraram depois do início da sprint | Trocar em vez de somar: combinar com o Product Owner o que sai quando algo entra | Sprint | Crítica se o objetivo estiver em risco; senão, melhoria |
| Itens da sprint sem relação com o objetivo | Explicitar o que é fora do objetivo (suporte, bugs) ou rever se o item deveria estar na sprint | Sprint Planning | Melhoria |

### Sprint Planning
| Sinal no board | Sugestão | Scrum Guide | Grupo |
|---|---|---|---|
| Sprint planejada acima da velocidade ou da capacidade | Planejar pelo que o time costuma terminar e pela capacidade real da sprint | Sprint Planning | Crítica |
| Tasks com OE acima de 10h (um dia) | Quebrar em tasks de até um dia no planning | Sprint Planning | Melhoria |
| PBI ou Bug na sprint sem nenhuma task depois do primeiro dia útil | Planejar o "como" no planning: o item vira tasks antes de começar | Sprint Planning | Melhoria |

### Daily Scrum e impedimentos
| Sinal no board | Sugestão | Scrum Guide | Grupo |
|---|---|---|---|
| Task com `bloqueado` há mais de 2 dias úteis sem novidade no comentário | Tratar o impedimento logo depois da daily, com quem pode resolver. O Scrum Master ajuda a remover | Scrum Master; Daily Scrum | Crítica |
| Dev com mais de 2 tasks em In Progress ao mesmo tempo | Terminar antes de começar: o time ajuda a fechar o que está aberto (limite de trabalho em andamento, prática de mercado) | Daily Scrum | Melhoria |
| Várias tasks sem atualização no mesmo dia | Usar a daily para ajustar o plano da sprint, não só para relatar | Daily Scrum | Melhoria |

### Product Backlog e refinamento
| Sinal no board | Sugestão | Scrum Guide | Grupo |
|---|---|---|---|
| Backlog pronto cobre menos de 1 sprint (saúde da skill refinar-backlog) | Refinar de forma contínua, não só na véspera do planning | Product Backlog | Crítica |
| Item que deve entrar na próxima sprint com problema que bloqueia | Resolver antes do planning: só entra o que o time consegue terminar numa sprint | Product Backlog | Crítica |
| Item grande demais para uma sprint | Dividir em itens que caibam numa sprint | Product Backlog | Crítica no topo do backlog; melhoria abaixo dele |
| Effort dado por quem não vai fazer o trabalho, ou item sem Effort perto do topo | Quem vai fazer o trabalho estima. O Product Owner ajuda a entender as trocas | Product Backlog | Melhoria |
| Features sem Epic, ou backlog sem um objetivo maior que oriente a ordem | Explicitar o Product Goal e ordenar o backlog por ele | Product Backlog (Product Goal) | Melhoria |

### Increment e Definition of Done
| Sinal no board | Sugestão | Scrum Guide | Grupo |
|---|---|---|---|
| PBI ou Bug em Done com task que não está em Done | Conferir se o item cumpre a Definition of Done. O que não cumpre não é apresentado na Review e volta para o Product Backlog | Increment (Definition of Done) | Crítica |
| PBI ou Bug "aguardando aceite" (todas as tasks em Done) há mais de 2 dias úteis | Aceitar logo, conferindo a Definition of Done, para o Increment ficar utilizável | Increment | Melhoria |
| PBIs indo para Done sem nenhuma task de teste ou revisão, quando o time costuma ter | Conferir a Definition of Done do time e, se ela não estiver escrita, escrever | Increment (Definition of Done) | Melhoria |

### Sprint Review e Retrospectiva
| Sinal no board | Sugestão | Scrum Guide | Grupo |
|---|---|---|---|
| A mesma tag `causa-*` em 3 ou mais tasks da sprint, ou a mesma origem de estouro dominando | Levar para a Retrospectiva como tema, com o número | Sprint Retrospective | Melhoria |
| `causa-interrupcao` recorrente | Decidir na Retrospectiva se o time reserva parte da sprint para suporte | Sprint Retrospective | Melhoria |
| Feature estourada ou com PBIs novos depois de DEV | Mostrar na Sprint Review quanto ela cresceu e ajustar o Product Backlog com os stakeholders | Sprint Review | Melhoria |

## 3. Conflitos com as convenções do time
As convenções do time não são erro. Quando uma sugestão esbarra numa delas, não mande seguir o Scrum e não descarte a sugestão: proponha um meio-termo que mantenha o que a convenção protege e alcance o objetivo da prática do Scrum. Sugestão com conflito vai sempre em melhorias.

| Convenção do time | O que o Scrum diz | O que a convenção protege | Meio-termo |
|---|---|---|---|
| O Effort do PBI ou Bug congela ao entrar na sprint, e trabalho a mais vira task nova | O Sprint Backlog muda durante a sprint, e o escopo é renegociado com o Product Owner | A medição de estimado × realizado | Manter o Effort congelado e a task nova. Quando as tasks novas puserem o Sprint Goal em risco, levar ao Product Owner a decisão do que sai da sprint |
| A sobra da sprint entra primeiro na próxima, com o Effort inteiro | Item que não ficou pronto volta para o Product Backlog e é reconsiderado | A continuidade do trabalho e o Effort congelado | Manter o item com o Effort congelado, mas confirmar no planning, com o Product Owner, se ele ainda serve ao novo Sprint Goal antes de entrar na frente |
| A daily do agente atualiza horas, task por task | A Daily Scrum é dos Developers e inspeciona o progresso até o Sprint Goal | Os dados de horas para medir as estimativas | Manter a atualização de horas e abrir a daily com uma linha sobre o Sprint Goal: no caminho ou em risco, e por quê |
| O agente e quem lidera montam a proposta de sprint e a distribuição entre os devs | Os Developers escolhem os itens com o Product Owner no Sprint Planning e decidem como fazer o trabalho | A preparação do planning | Levar a proposta como rascunho para o planning e deixar a distribuição para os devs confirmarem ou trocarem |
| Quem lidera decide a ordem do backlog, quando não é o Product Owner | O Product Owner responde pela ordem do Product Backlog | A agilidade de decidir sem esperar | Alinhar a proposta de ordem com o Product Owner antes do "sim", e registrar no comentário que foi alinhada |

Para um conflito que não está na tabela, monte o meio-termo da mesma forma:
1. Diga o que a convenção protege.
2. Diga o que a prática do Scrum quer alcançar.
3. Proponha um ajuste que mantenha o primeiro e alcance o segundo, ou a maior parte dele.

## 4. Como sugerir

### Classificar
- Crítica: o sinal põe em risco o Sprint Goal, a qualidade do Increment ou a próxima sprint, e a sugestão não conflita com nenhuma convenção do time.
- Melhoria: não há risco imediato, mas a prática faria diferença no resultado do time. Toda sugestão com conflito (seção 3) é melhoria.
- O sinal concreto pode mudar o grupo da tabela: item grande no fundo do backlog é melhoria; no topo, é crítica.

### Ordenar
Críticas primeiro, depois melhorias. Dentro de cada grupo, do maior impacto para o menor:
1. Sprint Goal da sprint atual.
2. Qualidade do Increment.
3. Próxima sprint: backlog pronto e planejamento.
4. Fluxo e impedimentos.
5. Inspeção e adaptação: Review e Retrospectiva.

Empate: primeiro a que envolve mais horas.

### Limitar
- Até 2 críticas e 2 melhorias por resposta. Quem lidera pode pedir outro número ("todas as sugestões", "só as críticas").
- Se sobrar sugestão, diga no fim quantas ficaram de fora: "Há mais 3 sugestões. Peça 'mais sugestões' para ver."
- Em respostas curtas (um item, uma pergunta direta), só as críticas.
- Sem sinal, sem seção: não escreva "nenhuma sugestão".
- Se o sinal já aparece nos riscos ou alertas da resposta, cite-o pelo ID e vá direto à prática, sem repetir o problema.
- Sugestão que quem lidera recusou não volta na mesma sessão.
- Nada de dica genérica: cada sugestão cita o sinal, com IDs e números.

### Formato
```
Sugestões (Scrum)
Críticas
1. <sinal, com IDs e números> → <o que fazer e com quem>. (Scrum Guide: <parte>)
Melhorias
1. <sinal> → <o que fazer>. (Scrum Guide: <parte>)
2. <sinal> → Meio-termo: <proposta>. Convenção do time: <o quê>. Scrum: <o quê>. (Scrum Guide: <parte>)
```

- Grupo sem sugestão não aparece.
- Sugestão não é proposta de escrita: não termina com "Aplico?" e não entra no "sim" da proposta da skill. Se quem lidera quiser aplicar uma (ex.: dividir um PBI), monte uma proposta separada pelo protocolo de escrita.

### Exemplo
Ilustrativo: mostra o formato, não dados reais.

```
Sugestões (Scrum)
Críticas
1. Faltam 3 dias, o RW da sprint é 140h (14 dias) para 90h disponíveis, e o #4502, do objetivo, não começou → conversar hoje com o Product Owner sobre o que sai da sprint. (Scrum Guide: Sprint)
Melhorias
1. `causa-interrupcao` em 5 tasks nesta sprint → levar para a Retrospectiva e decidir se o time reserva parte da sprint para suporte. (Scrum Guide: Sprint Retrospective)
2. O #4510 ganhou 3 tasks novas (+22h) → Meio-termo: manter o Effort congelado e as tasks novas, e mostrar na Sprint Review quanto o item cresceu. Convenção do time: Effort congelado na sprint. Scrum: o escopo é renegociado com o Product Owner. (Scrum Guide: Sprint)
Há mais 2 sugestões. Peça "mais sugestões" para ver.
```
