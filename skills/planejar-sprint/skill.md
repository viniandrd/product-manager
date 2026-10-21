---
name: planejar-sprint
description: Monta uma proposta de sprint para o time da sessão escolhendo, na ordem do backlog, os itens prontos que cabem na velocidade e na capacidade dos devs, descontando folgas, o que sobra da sprint atual e a reserva para imprevistos; aponta o que não está pronto, propõe um objetivo e, se pedirem, uma distribuição entre os devs. Também revisa uma sprint já montada e avalia se cabe um item novo. Use quando pedirem para planejar, montar ou preparar a próxima sprint, escolher o que entra nela, conferir se a sprint está grande demais ou perguntar se cabe mais um item.
---

# Planejar a sprint

Siga o protocolo de escrita do agente. A sprint é decisão do time e de quem lidera: você monta a proposta.

As seções 1 a 5 só leem o board. Nada é gravado antes da seção 6, e só depois de um "sim".

## 1. Escolha o modo
- Planejar a próxima sprint: seções 2 a 6. É o padrão.
- Revisar uma sprint já montada ("a sprint está grande demais?"): seções 2, 4 e 5, só com os itens que já estão nela, sem buscar novos no backlog. Aponte o que passa da meta ou da capacidade e sugira o que tirar, de baixo para cima na ordem do backlog.
- Encaixar um item na sprint atual ("cabe o #123?"): compare o Effort do item com o que ainda cabe na sprint atual (seção 2). Se não couber, sugira quais itens sairiam, de baixo para cima na ordem do backlog, só entre os que ainda não começaram (nenhuma task em In Progress ou Done). Termine com "Aplico?" só se houver mudança a fazer.

## 2. Dados e meta de Effort
Junte numa mensagem só as perguntas desta seção (velocidade, feriados, sobra da sprint atual e reserva).

### Sprint
- A próxima sprint do time (work, ação list_team_iterations): nome, datas de início e fim e dias úteis (segunda a sexta, menos as folgas do time).
- Feriados só entram no cálculo se estiverem cadastrados como folga do time. Se não houver nenhuma folga do time cadastrada, pergunte se há feriado no período.

### Capacidade
- work (ação get_team_capacity) para essa sprint: devs, horas por dia, atividade e folgas de cada um.
- Horas disponíveis de cada dev = horas por dia × (dias úteis da sprint − dias de folga do dev).
- Os devs do time são os que aparecem na capacidade. Dev com 0 hora (férias) não recebe item na distribuição.
- Se não houver capacidade cadastrada, avise e sugira cadastrar em Boards → Sprints → Capacity. Enquanto isso, pergunte quem são os devs e as folgas de cada um, e use 10h por dia (1 dia = 10h).

### Velocidade
- Peça a média de Effort concluído nas últimas 3 sprints (relatório Velocity em Boards → Backlogs → Analytics). Se quem lidera não souber, some o Effort dos itens em Done de cada uma das 3 últimas iterações (wit_work_item, ação list_for_iteration) e diga que é uma estimativa.
- Mostre também o menor e o maior valor das 3 sprints. Se a diferença entre eles passar de 30% da média, avise que a previsão é incerta.
- Time com menos de 3 sprints: use as que houver e diga quantas foram.

### Meta de Effort
Comece pela velocidade e ajuste, nesta ordem:
1. Folgas: velocidade × (dias-dev disponíveis nesta sprint ÷ dias-dev de uma sprint sem folgas). Dias-dev é a soma dos dias úteis de cada dev. Ex.: 4 devs × 10 dias = 40; com 6 dias de folga no total, 34 ÷ 40 = 85% da velocidade.
2. Reserva: pergunte se o time reserva parte da sprint para suporte, incidentes ou bugs que chegam no meio. Se sim, desconte essa porcentagem.
3. Teto: como o Effort é em horas, a meta não passa das horas disponíveis do time (a soma das horas disponíveis dos devs, já sem a reserva). Se a velocidade ajustada passar desse teto, use o teto e diga isso.

Se houver capacidade cadastrada nas 3 últimas sprints, mostre também o aproveitamento: Effort concluído ÷ horas disponíveis, em cada sprint. Abaixo de 70%, avise que o time entrega bem menos horas de Effort do que tem disponível. Isso costuma indicar estimativas baixas, interrupções ou trabalho fora do board; a skill analisar-estimativas ajuda a ver qual.

O resultado é a meta de Effort. Mostre a conta na proposta.

### O que já ocupa a sprint
- Sobra da sprint atual: itens da sprint atual que não estão em Done. Liste-os com o Effort e pergunte quais passam para a próxima. Os que passarem entram primeiro na proposta, com o Effort inteiro e sem re-estimar: o que falta já está no RW das tasks.
- Já planejados: itens que já estão na próxima sprint também entram primeiro e contam na meta. Não tire nenhum sem aprovação.
- Item que sobra pela segunda sprint seguida: destaque nos riscos.

## 3. Seleção
- Depois do que já ocupa a sprint, percorra o backlog na ordem atual (wit_backlog, ação list_work_items). Essa ordem é a prioridade de quem lidera.
- Só entram itens prontos: sem nenhum problema que bloqueia, na definição da skill refinar-backlog (sem-critérios, critério-vago, sem-esforço, grande, vago, dúvida-aberta, dependência, bug-incompleto). Carregue a skill refinar-backlog para ver como identificar cada um.
- Exceção à dependência: se o item de que ele depende também entra nesta sprint, acima dele, o item pode entrar. Mostre a dependência nos riscos.
- Item que não está pronto é pulado e vai para a lista "Fora da sprint", com o que falta.
- Some o Effort dos itens prontos até chegar perto da meta, sem passar. No primeiro item pronto que estouraria a meta, pare e pergunte o que fazer:
  - incluir mesmo assim, passando da meta (mostre quanto);
  - parar antes dele;
  - dividir o item e incluir só a primeira parte (com a skill escrever-work-item).
- Não pule para itens menores mais abaixo sem que quem lidera peça.

### Objetivo da sprint
Proponha um objetivo em uma frase: o resultado que o time quer ter no fim da sprint, não a lista de itens. Se os itens forem de vários assuntos, use os 1 ou 2 com mais Effort. Ex.: "Clientes de opções conseguem consultar e exportar as posições por vencimento."

## 4. Checagem de capacidade
- Se os itens já têm tasks com Remaining Work, some as horas por dev (Assigned To das tasks) e compare com as horas disponíveis. Aponte quem passaria de 100% e quem ficaria abaixo de 50%.
- Tasks sem responsável: some à parte e compare com as horas que sobram no time.
- Se a capacidade estiver cadastrada por atividade (Development, Testing etc.), compare também por atividade.
- Se os itens não têm tasks, avise que a checagem por dev fica para o planning, quando o time quebrar os PBIs em tasks.
- Quebra acima do Effort (sinal definido na skill regras-de-estimativa, seção 5): em cada item que já tem tasks com OE, compare a soma dos OE com o Effort. Se passar do limite, aponte nos riscos e sugira re-estimar o Effort antes do "sim", porque depois ele congela. Se quem lidera disser o novo valor, inclua a mudança de Effort na proposta. Task sem OE deixa a quebra incompleta: diga isso.

## 5. Proposta
Use este formato:

```
Proposta da sprint <nome> · time <TIME>
Datas: dd/mm/aaaa a dd/mm/aaaa · <n> dias úteis
Objetivo: <uma frase>

Conta
- Velocidade: <média>h (de <menor>h a <maior>h nas últimas 3 sprints; aproveitamento de <x>%)
- Folgas: <x>% dos dias-dev → <effort>h
- Reserva: <x>% → <effort>h
- Teto: <h>h disponíveis no time → meta de <effort>h (<dias> dias)
- Proposta: <effort>h (<x>% da meta), dos quais <effort>h são sobra da sprint atual e <effort>h já estavam planejados

Itens, na ordem
| # | ID | Tipo | Título | Effort | Origem |
(Origem: sobra, já planejado ou backlog)

Fora da sprint
| ID | Título | Motivo |
(Motivo: não está pronto, com o que falta, ou não coube)

Capacidade por dev (se houver tasks)
| Dev | Disponível (h) | Planejado (h) | % |

Riscos
- ...

Sugestões (Scrum)
- ...
```

- Riscos a apontar, quando houver: previsão incerta, item que sobra pela segunda vez, dependência dentro da sprint, item no limite do tamanho, quebra acima do Effort, dev acima de 100%, bug com Severity 1 ou 2 pronto que ficou de fora, item com Priority 1 pronto que ficou de fora, item com Target Date até o fim da sprint seguinte que ficou de fora.
- Distribuição entre os devs: só se pedirem. Para cada item, sugira um dev com o motivo: horas livres na sprint e itens parecidos ou da mesma Feature que já fez. Ninguém passa de 100% das horas disponíveis. Se um dev ficar com todos os itens de uma Feature, aponte isso nos riscos.
- Avise na proposta que o Effort dos itens fica congelado a partir da entrada na sprint (regra do time). Se o time quiser re-estimar algum item, isso precisa acontecer antes do "sim".
- Sugestões (Scrum): carregue a skill praticas-scrum e acrescente a seção dela depois dos riscos. Elas não entram no "sim" da sprint.
- Termine com "Aplico esta sprint?".

## 6. Aplicar
- Depois de um "sim", mude a Iteration dos itens aprovados para a sprint (wit_work_item_write, ação update_batch). É mudança de planejamento.
- Se o time usa o estado Committed para o que entra na sprint, proponha também passar os PBIs e Bugs para Committed, na mesma proposta.
- As tasks filhas dos itens vão para a mesma sprint. O Azure DevOps não move as filhas sozinho.
- Itens que sobram da sprint atual: mude a Iteration deles e das tasks que não estão em Done. Tasks em Done ficam na sprint atual.
- Itens que já estavam na próxima sprint e ficaram de fora: só saem com aprovação explícita de cada um, e voltam para <ITERAÇÃO-DO-BACKLOG>.
- Responsável só com aprovação explícita de cada nome. Busque a identidade exata com core_get_identity_ids.
- Não mude ordem nem prioridade. O Effort só muda quando quem lidera re-estimar um item na proposta (quebra acima do Effort); depois que o item entra na sprint, ele fica congelado.
- Toda alteração leva a tag pm-agent e o comentário do protocolo, com o motivo "Planejamento da sprint <nome>".
- O objetivo da sprint não fica gravado no board. No fim, mostre-o de novo para quem lidera registrar onde o time costuma guardar.
- No fim, liste os itens movidos, com ID, título e link (https://dev.azure.com/btgpactual/<PROJETO>/_workitems/edit/<ID>), e o total de Effort da sprint.
