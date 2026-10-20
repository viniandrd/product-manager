---
name: atualizar-horas
description: Atualiza as horas (Completed Work e Remaining Work) e o estado das tasks da sprint atual do time da sessão, na daily ou para um card específico, a partir do que quem lidera informar. Detecta tasks estouradas, atrasadas e superestimadas, pergunta a causa, marca a estimativa, registra o uso de IA nas tasks que fecham e registra trabalho a mais como task nova. No fim, usa a skill atualizar-cadeia para acertar os pais (PBI ou Bug, Feature e Epic). Use quando pedirem para fazer a daily, atualizar o board, as horas ou o status de uma task ou de um card, ou quando disserem algo como "trabalhei 3h na #123", "terminei a #123" ou "comecei a #124".
---

# Atualizar horas e estado

Siga o protocolo de escrita do agente, com a exceção de comentários da seção 8.

As horas são lançadas nas tasks. Esta skill cuida das tasks; os pais ficam com a skill atualizar-cadeia.

## Passo a passo
1. Carregue a skill regras-de-estimativa. Os limites, as fórmulas e as causas usados aqui estão lá.
2. Busque os dados e mostre as tasks por dev (seção 2).
3. Colete e interprete o que quem lidera disser (seção 3).
4. Aplique as regras dos campos (seção 4).
5. Calcule os sinais das tasks (seção 5) e as marcações (seção 6).
6. Carregue a skill atualizar-cadeia e rode-a com os valores das tasks já atualizados. Ela devolve a tabela da cadeia, os alertas e as tags dos pais.
7. Monte uma proposta única com tudo (seção 7).
8. Depois do "sim", grave na ordem da seção 8.

## 1. Escolha o modo
- Daily do time: todas as tasks da sprint atual, por dev. É o padrão quando pedirem "daily" ou para "atualizar o board".
- Um card: só a task citada ou, se o ID for de um PBI ou Bug, as tasks dele. A cadeia desse card também é conferida (passo 6).

## 2. Dados
- Tasks da sprint atual (wit_work_item, ação list_for_iteration), fora as que estão em Done ou Removed. De cada task: título, estado, Assigned To, Original Estimate (OE), Completed Work (CW), Remaining Work (RW), Changed Date, tags e o PBI ou Bug pai.
- Tasks da sprint que foram para Done desde o último dia útil (State Change Date) e ainda não têm tag de uso de IA: foram fechadas fora do agente. Elas entram na reconciliação (seção 6) e na pergunta de uso de IA (seção 4).
- Data em que a task entrou em In Progress: o campo de data de ativação, se o tipo tiver; se não, a revisão em que o estado mudou para In Progress (list_revisions).
- Capacidade da sprint (work, ação get_team_capacity): horas por dia e folgas de cada dev.

Mostre, por dev, primeiro as tasks em In Progress e depois as em To Do:

| ID | Título | Estado | OE | CW | RW | Dias em In Progress | Última alteração |
|---|---|---|---|---|---|---|---|

Depois peça: "Diga o andamento de cada dev. Pode ser em texto livre."

## 3. Interprete o que foi dito

| O que disseram | O que muda |
|---|---|
| "#123 3h, faltam 2h" | CW = CW atual + 3; RW = 2 |
| "#123 3h" (sem dizer quanto falta) | CW = CW atual + 3; RW = RW atual − 3, nunca abaixo de 0, marcado como "calculado" na proposta |
| "#123 faltam 5h" | RW = 5; CW não muda |
| "#123 terminei" | Estado Done e RW = 0. Se não disserem as horas de hoje, pergunte quantas foram. O uso de IA é perguntado junto com as causas (seção 4) |
| "#124 terminei, a IA fez boa parte" | Done e RW = 0, tag `ia-intenso` |
| "#124 terminei, a IA ajudou" / "#124 terminei, sem IA" | Done e RW = 0, tag `ia-parcial` / `ia-nenhum` |
| "#124 comecei" | Estado In Progress |
| "#125 travada", "#125 esperando o time X" | Tag `bloqueado`; o motivo vai num comentário |
| "#125 destravou" | Tirar a tag `bloqueado` |
| "#120 vai precisar de mais 10h", "o Effort do #120 sobe para 45" | O Effort não muda (regra do time). Proponha uma task nova, filha do #120, com OE = horas a mais (seção 4) |
| "surgiu mais trabalho no #120: <o quê>, 1 dia" | Task nova, filha do #120, com esse título e OE = 10 |

- Horas como "1h30" ou "1,5h" viram 1,5. Dias viram horas pela regras-de-estimativa (seção 1).
- Se não ficar claro de qual task se fala, pergunte antes de propor. Não chute o ID.
- Horas ditas para um PBI ou Bug: se ele tem tasks, pergunte em qual delas lançar. Se não tem, proponha criar uma task filha para receber as horas (pergunte a estimativa dela), em vez de lançar no PBI.
- No fim, pergunte uma vez só pelas tasks em In Progress que ninguém citou: "Sem atualização: #x, #y. Algum andamento?". Sem resposta, elas ficam como estão e entram no alerta "sem atualização".

## 4. Regras dos campos
- OE é a estimativa original e é gravado uma vez só. Se a task entra em In Progress sem OE, proponha OE = RW atual. Se o RW também estiver vazio, pergunte a estimativa antes de mudar o estado.
- Nunca altere um OE que já existe, mesmo que peçam para "corrigir a estimativa": a nova previsão vai no RW. É o OE fixo que permite medir a precisão depois.
- CW só aumenta. Para corrigir um lançamento errado, mostre o valor atual e o novo e diga na proposta que é uma correção.
- RW nunca fica negativo. Task em Done tem RW = 0.
- Task com RW = 0 que não está em Done: pergunte se terminou.
- Task em To Do que recebeu horas: proponha também passar para In Progress.
- Task sem responsável que recebeu horas de um dev: proponha esse dev como responsável, na mesma proposta.
- Horas do dia de um dev acima de 10h, ou acima das horas por dia dele na capacidade, se forem menores: avise e confirme antes de propor.
- Dev com 0 hora na capacidade hoje (folga, férias) que aparece com horas: avise.
- Não mude Effort, prioridade nem Iteration nesta skill. O Effort congelado (regras-de-estimativa, seção 2) só pode voltar ao valor congelado, pela skill atualizar-cadeia.
- Trabalho a mais dentro de uma task que já existe vai no RW dela, e pode virar estouro. Trabalho que não cabe em nenhuma task vira task nova, filha do PBI ou Bug, na sprint atual:
  - título começando com verbo no infinitivo, OE = horas a mais, Activity e responsável se forem ditos;
  - pergunte se é escopo novo ou algo que faltou na quebra (complexidade), e grave a tag da causa na task nova;
  - comentário na task nova: "Trabalho a mais no #<PBI>, registrado na daily de dd/mm/aaaa."
- Se o trabalho a mais for uma entrega nova, e não parte do que o PBI já prometia, sugira um PBI novo com a skill escrever-work-item, em vez de uma task.
- Uso de IA: toda task que vai para Done recebe uma tag de uso de IA (regras-de-estimativa, seção 9). Se não disserem, faça uma pergunta só para todas as tasks fechadas, junto com as causas: "Uso de IA em #124 e #132: nenhum, parcial ou intenso?". Inclua as tasks fechadas fora do agente (seção 2). Se quem lidera não souber, deixe sem tag: a task conta como não registrada.

## 5. Sinais das tasks
Para cada task em In Progress e para as que vão para Done nesta daily, calcule os sinais de task da regras-de-estimativa (seção 5):

| Sinal | O que fazer |
|---|---|
| Estouro | Perguntar a causa |
| Atrasada | Perguntar a causa |
| Risco na sprint | Só avisar |
| Sem atualização | Só avisar |

- Pergunte a causa uma vez por task, não em toda daily. Se a task já tem uma tag de causa, só mostre o sinal.
- Ofereça todas as causas de subestimada da regras-de-estimativa (seção 8): escopo, complexidade, IA (retrabalho), bloqueio, interrupção ou não sei ainda.
- Se a causa for complexidade ou escopo, pergunte também se o RW precisa subir.

## 6. Marcação das tasks
- Estouro com causa confirmada: tag `estimativa-subestimada` e a tag da causa.
- Atraso sem estouro, com causa confirmada: só a tag da causa. Se a causa for complexidade, também `estimativa-subestimada`.
- Ao ir para Done, inclusive fora do agente (seção 2), classifique a task pelo realizado (CW ÷ OE) com os limites da regras-de-estimativa (seção 4):
  - Subestimada e sem a tag: `estimativa-subestimada`. Pergunte a causa, se ainda não houver.
  - Superestimada: `estimativa-superestimada`. Pergunte a causa, oferecendo todas as de superestimada (regras-de-estimativa, seção 8): IA acelerou, aproveitou algo pronto, era mais simples, escopo diminuiu ou não sei.
  - Precisa, com a tag `estimativa-subestimada`: proponha tirar essa tag. A tag da causa fica.
  - Task sem OE ou sem CW: não marque, e diga que faltou o dado.
- Toda marcação leva um comentário: "Estimativa: OE <x>h, projeção <y>h (<z>%). Causa: <causa>. Daily de dd/mm/aaaa." Na reconciliação, escreva "realizado" no lugar de "projeção" e acrescente "Uso de IA: <nenhum, parcial ou intenso>."

## 7. Proposta
Uma proposta só para a daily inteira, com as tasks e o que a skill atualizar-cadeia devolveu. Exemplo ilustrativo:

```
Daily do time <TIME> · dd/mm/aaaa · sprint <nome>

| Dev   | ID   | Título                  | Estado              | CW      | RW                 | OE | Projeção/OE | Sinal         |
|-------|------|-------------------------|---------------------|---------|--------------------|----|-------------|---------------|
| Ana   | #123 | Criar endpoint de reset | In Progress         | 5 → 8   | 4 → 2              | 10 | 100%        | —             |
| Ana   | #130 | Testar o reset          | To Do → In Progress | 0 → 2   | 10 → 8 (calculado) | 10 | 100%        | —             |
| Bruno | #127 | Migrar tabela de ordens | In Progress         | 18 → 24 | 2 → 10             | 20 | 170%        | estouro       |
| Carla | #132 | Ajustar log de acesso   | In Progress → Done  | 2 → 4   | 3 → 0              | 10 | 40%         | superestimada |

Cadeia (da skill atualizar-cadeia)
| Tipo    | ID   | Título            | Estado               | CW        | RW        | Effort | Projeção/Effort | Motivo                                     |
|---------|------|-------------------|----------------------|-----------|-----------|--------|-----------------|--------------------------------------------|
| PBI     | #120 | Reset de senha    | Approved → Committed | 15 → 20   | 18 → 14   | 30     | 113%            | está na sprint atual                       |
| Feature | #100 | Autenticação      | New → DEV            | 40 → 45   | 60 → 56   | 120    | 84%             | filho #120 na sprint                       |
| Epic    | #90  | Portal do cliente | New → In Progress    | 120 → 125 | 200 → 196 | —      | —               | Feature #100 em DEV · fora da área do time |

Alertas
- #127 estourou: OE 20h (2 dias), projeção 34h (3,4 dias), 170%. Qual a causa? (escopo, complexidade, bloqueio, interrupção, não sei ainda)
- #131 atrasada: deveria ter terminado em dd/mm/aaaa. Qual a causa?
- Sem atualização: #129 (Carla).
- Risco na sprint: Bruno tem 10h de RW e 6h disponíveis até o fim da sprint.
- #132 terminou com 4h de 10h estimadas (40%). Qual a causa? (IA acelerou, aproveitou algo pronto, era mais simples, escopo diminuiu, não sei)
- Uso de IA nas tasks fechadas: #132, e #133, que foi para Done ontem direto no board. Nenhum, parcial ou intenso?
- (alertas da cadeia, ex.: PBI estourado com a origem da diferença, Effort alterado, pai à frente do filho)

Marcação das tasks (depende da causa)
- #127 → estimativa-subestimada + causa-<resposta>, com comentário.
- #132 → estimativa-superestimada + causa-<resposta> + ia-<resposta>, com comentário.
- #133 → ia-<resposta>.

Tags na cadeia (da skill atualizar-cadeia)
- PBI #126 e Feature #100: + bloqueado, por causa da task #125, com comentário.
```

- Mostre só as linhas que mudam. Tasks sem mudança aparecem só nos alertas, se tiverem algum sinal.
- Peça as causas e o uso de IA junto com o "Aplico?". Termine com: "Aplico? Se quiser, responda junto as causas e o uso de IA (ex.: 'sim; #127 complexidade; #132 IA acelerou, intenso; #133 parcial'). Itens fora da área do time só entram se você citar o ID (ex.: 'sim, inclusive #90')."
- Causa sem resposta: as horas e o estado são gravados com o "sim", e a marcação daquela task fica para a próxima daily. Uso de IA sem resposta: a task fica sem tag e volta na pergunta da daily seguinte.

## 8. Aplicar
Grave nesta ordem:
1. Tasks novas (trabalho a mais), com wit_work_item_write (ação add_child) a partir do PBI ou Bug.
2. Tasks, com wit_work_item_write (ação update_batch): estado, CW, RW, OE (só quando estava vazio), responsável (só quando aprovado) e tags.
3. Pais, como manda a skill atualizar-cadeia (seção 10 dela).

- Mantenha as tags que já existem e acrescente pm-agent.
- Atualizações de horas e estado não recebem comentário: as revisões do item já guardam o histórico.
- Recebem comentário: a marcação de estimativa (seção 6), o motivo de um bloqueio e as tasks novas de trabalho a mais (seção 4). Os comentários dos pais seguem a skill atualizar-cadeia.
- No fim, responda em até 5 linhas: quantas tasks e quantos pais foram atualizados, as horas lançadas por dev, o RW total da sprint e o que ficou pendente (causas sem resposta, tasks sem atualização, pais fora da área não aprovados).
