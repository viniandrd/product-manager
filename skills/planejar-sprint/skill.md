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
- Encaixar um item na sprint atual ("cabe o #123?"): compare os pontos do item com o que ainda cabe na sprint atual (seção 2). Se não couber, sugira quais itens sairiam, de baixo para cima na ordem do backlog, só entre os que ainda estão em New. Termine com "Aplico?" só se houver mudança a fazer.

## 2. Dados e meta de pontos
Junte numa mensagem só as perguntas desta seção (velocidade, feriados, sobra da sprint atual e reserva).

### Sprint
- A próxima sprint do time (work, ação list_team_iterations): nome, datas de início e fim e dias úteis (segunda a sexta, menos as folgas do time).
- Feriados só entram no cálculo se estiverem cadastrados como folga do time. Se não houver nenhuma folga do time cadastrada, pergunte se há feriado no período.

### Capacidade
- work (ação get_team_capacity) para essa sprint: devs, horas por dia, atividade e folgas de cada um.
- Horas disponíveis de cada dev = horas por dia × (dias úteis da sprint − dias de folga do dev).
- Os devs do time são os que aparecem na capacidade. Dev com 0 hora (férias) não recebe item na distribuição.
- Se não houver capacidade cadastrada, avise, sugira cadastrar em Boards → Sprints → Capacity e siga só com a velocidade: sem o ajuste por folgas e sem a checagem por dev (seção 4).

### Velocidade
- Peça a média de Story Points concluídos nas últimas 3 sprints (relatório Velocity em Boards → Backlogs → Analytics). Se quem lidera não souber, some os Story Points dos itens em Closed de cada uma das 3 últimas iterações (wit_work_item, ação list_for_iteration) e diga que é uma estimativa.
- Mostre também o menor e o maior valor das 3 sprints. Se a diferença entre eles passar de 30% da média, avise que a previsão é incerta.
- Time com menos de 3 sprints: use as que houver e diga quantas foram.

### Meta de pontos
Comece pela velocidade e ajuste, nesta ordem:
1. Folgas: velocidade × (dias-dev disponíveis nesta sprint ÷ dias-dev de uma sprint sem folgas). Dias-dev é a soma dos dias úteis de cada dev. Ex.: 4 devs × 10 dias = 40; com 6 dias de folga no total, 34 ÷ 40 = 85% da velocidade.
2. Reserva: pergunte se o time reserva parte da sprint para suporte, incidentes ou bugs que chegam no meio. Se sim, desconte essa porcentagem.

O resultado é a meta de pontos. Mostre a conta na proposta.

### O que já ocupa a sprint
- Sobra da sprint atual: itens da sprint atual que não estão em Resolved nem Closed. Liste-os com os pontos e pergunte quais passam para a próxima. Os que passarem entram primeiro na proposta, com os pontos inteiros.
- Já planejados: itens que já estão na próxima sprint também entram primeiro e contam na meta. Não tire nenhum sem aprovação.
- Item que sobra pela segunda sprint seguida: destaque nos riscos.

## 3. Seleção
- Depois do que já ocupa a sprint, percorra o backlog na ordem atual (wit_backlog, ação list_work_items). Essa ordem é a prioridade de quem lidera.
- Só entram itens prontos: sem nenhum problema que bloqueia, na definição da skill refinar-backlog (sem-critérios, critério-vago, sem-pontos, grande, vago, dúvida-aberta, dependência, bug-incompleto). Carregue a skill refinar-backlog para ver como identificar cada um.
- Exceção à dependência: se o item de que ele depende também entra nesta sprint, acima dele, o item pode entrar. Mostre a dependência nos riscos.
- Item que não está pronto é pulado e vai para a lista "Fora da sprint", com o que falta.
- Some os pontos dos itens prontos até chegar perto da meta, sem passar. No primeiro item pronto que estouraria a meta, pare e pergunte o que fazer:
  - incluir mesmo assim, passando da meta (mostre quanto);
  - parar antes dele;
  - dividir o item e incluir só a primeira parte (com a skill escrever-work-item).
- Não pule para itens menores mais abaixo sem que quem lidera peça.

### Objetivo da sprint
Proponha um objetivo em uma frase: o resultado que o time quer ter no fim da sprint, não a lista de itens. Se os itens forem de vários assuntos, use os 1 ou 2 com mais pontos. Ex.: "Clientes de opções conseguem consultar e exportar as posições por vencimento."

## 4. Checagem de capacidade
- Se os itens já têm tasks com Remaining Work, some as horas por dev (Assigned To das tasks) e compare com as horas disponíveis. Aponte quem passaria de 100% e quem ficaria abaixo de 50%.
- Tasks sem responsável: some à parte e compare com as horas que sobram no time.
- Se a capacidade estiver cadastrada por atividade (Development, Testing etc.), compare também por atividade.
- Se os itens não têm tasks, avise que a checagem por dev fica para o planning, quando o time quebrar as stories.

## 5. Proposta
Use este formato:

```
Proposta da sprint <nome> · time <TIME>
Datas: dd/mm/aaaa a dd/mm/aaaa · <n> dias úteis
Objetivo: <uma frase>

Conta
- Velocidade: <média> (de <menor> a <maior> nas últimas 3 sprints)
- Folgas: <x>% dos dias-dev → <pontos>
- Reserva: <x>% → meta de <pontos>
- Proposta: <pontos> (<x>% da meta), dos quais <pontos> são sobra da sprint atual e <pontos> já estavam planejados

Itens, na ordem
| # | ID | Tipo | Título | Pts | Origem |
(Origem: sobra, já planejado ou backlog)

Fora da sprint
| ID | Título | Motivo |
(Motivo: não está pronto, com o que falta, ou não coube)

Capacidade por dev (se houver tasks)
| Dev | Disponível (h) | Planejado (h) | % |

Riscos
- ...
```

- Riscos a apontar, quando houver: previsão incerta, item que sobra pela segunda vez, dependência dentro da sprint, item no limite do tamanho, dev acima de 100%, bug com Severity 1 ou 2 pronto que ficou de fora, item com Target Date até o fim da sprint seguinte que ficou de fora.
- Distribuição entre os devs: só se pedirem. Para cada item, sugira um dev com o motivo: horas livres na sprint e itens parecidos ou da mesma Feature que já fez. Ninguém passa de 100% das horas disponíveis. Se um dev ficar com todos os itens de uma Feature, aponte isso nos riscos.
- Termine com "Aplico esta sprint?".

## 6. Aplicar
- Depois de um "sim", mude a Iteration dos itens aprovados para a sprint (wit_work_item_write, ação update_batch). É mudança de planejamento.
- As tasks filhas dos itens vão para a mesma sprint. O Azure DevOps não move as filhas sozinho.
- Itens que sobram da sprint atual: mude a Iteration deles e das tasks que não estão em Closed. Tasks em Closed ficam na sprint atual.
- Itens que já estavam na próxima sprint e ficaram de fora: só saem com aprovação explícita de cada um, e voltam para <ITERAÇÃO-DO-BACKLOG>.
- Responsável só com aprovação explícita de cada nome. Busque a identidade exata com core_get_identity_ids.
- Não mude Story Points, ordem nem prioridade.
- Toda alteração leva a tag pm-agent e o comentário do protocolo, com o motivo "Planejamento da sprint <nome>".
- O objetivo da sprint não fica gravado no board. No fim, mostre-o de novo para quem lidera registrar onde o time costuma guardar.
- No fim, liste os itens movidos, com ID, título e link (https://dev.azure.com/btgpactual/<PROJETO>/_workitems/edit/<ID>), e o total de pontos da sprint.
