---
name: refinar-backlog
description: Revisa o backlog do time, de uma área ou de um item e aponta o que não está pronto para a sprint (sem critérios de aceite, sem estimativa, grande demais, duplicado, parado, vago, sem pai, com dúvidas em aberto ou dependência), monta a pauta do refinamento e propõe uma ordem com justificativa. Use quando pedirem para refinar, revisar, limpar, organizar ou priorizar o backlog, preparar a reunião de refinamento, ou perguntarem se um item está pronto para a sprint.
---

# Refinar o backlog

Siga o protocolo de escrita do agente. A ordem final é decisão de quem lidera.

As seções 1 a 5 só leem o board. Nada é gravado antes da seção 6, e só depois de um "sim".

## 1. Escolha o modo
- Backlog completo: diagnóstico, relatório, pauta e proposta de ordem (seções 2 a 6). É o padrão quando pedirem para "refinar o backlog".
- Pauta do refinamento: diagnóstico, relatório e pauta (seções 2 a 4), sem proposta de ordem. Use quando pedirem para preparar a reunião.
- Um item ("o #123 está pronto?"): diagnóstico só daquele item (seção 3), respondido em até 5 linhas: pronto ou não, e o que falta.
- Só a ordem: proposta de ordem (seção 5). Faça o diagnóstico só para saber quais itens estão prontos e não mostre o relatório.

## 2. Recorte e dados

### Recorte
- Backlog do time: wit_backlog (ação list_work_items), no nível de requisitos (Microsoft.RequirementCategory): PBIs e, se o time mostra bugs no backlog, Bugs. A ordem que vier é a ordem atual, decidida por quem lidera.
- Uma área específica (por exemplo, a PM Sandbox): wit_query (ação wiql):

```sql
SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State]
FROM WorkItems
WHERE [System.TeamProject] = '<PROJETO>'
  AND [System.AreaPath] UNDER '<ÁREA>'
  AND [System.WorkItemType] IN ('Product Backlog Item', 'Bug')
  AND [System.State] IN ('New', 'Approved', 'Committed')
ORDER BY [Microsoft.VSTS.Common.BacklogPriority] ASC
```

- Só entram itens em New, Approved ou Committed. Ignore Done e Removed.
- Itens da sprint atual estão em andamento: ficam fora do diagnóstico e da ordem.
- Itens planejados para uma sprint futura entram no diagnóstico, mas não na ordem.
- Itens com a Iteration de uma sprint que já terminou entram, com o problema sobrou-de-sprint.
- Limite: analise os 50 primeiros itens na ordem do backlog. Se houver mais, diga quantos ficaram de fora e pergunte se é para continuar.

### Campos
Busque de cada item com wit_work_item: tipo, título, estado, Description, Acceptance Criteria, Repro Steps e Severity (bugs), Effort, Priority e Risk (esses dois quando o tipo tiver), Tags, Iteration Path, Created By, Created Date, Changed Date, Target Date e as relações (pai, filhos, predecessor, sucessor e duplicado). Do pai, busque o título e o estado.

### Velocidade
Para a saúde do backlog (seção 4), use a média de Effort concluído nas últimas 3 sprints, se quem lidera informar. Se não, some o Effort dos itens em Done de cada uma das 3 últimas iterações (work, ação list_team_iterations; wit_work_item, ação list_for_iteration) e diga que é uma estimativa. Se não der para calcular, pule a saúde do backlog e diga isso.

## 3. Diagnóstico, item a item

Marque cada item com os problemas que encontrar. Um item está pronto para a sprint quando não tem nenhum problema que bloqueia. Os problemas de atenção não tiram o item da sprint, mas entram na pauta.

### Bloqueia
| Código | Como identificar | Sugestão |
|---|---|---|
| sem-critérios | Acceptance Criteria vazio, só repete o título ou tem menos de 3 itens. | Rascunhar os critérios no formato "Dado, quando, então", com "A confirmar" no que não se sabe. |
| critério-vago | Algum critério não dá para verificar ("funcionar corretamente", "ser rápido", "ser intuitivo"). | Reescrever só os critérios vagos. |
| sem-esforço | Effort vazio. | Levar para o time estimar. Não sugira número. |
| grande | Mais de 6 tasks, mais de 6 critérios, critérios que descrevem mais de uma entrega, ou Effort acima de 50 (5 dias). | Propor a divisão com os títulos dos novos PBIs: por fluxo, por variação, por operação, simples primeiro ou por consumidor. Nunca por camada técnica. |
| vago | Descrição sem quem, o quê ou por quê. | Dizer qual dos três falta e que quem abriu o item (Created By) pode responder. |
| dúvida-aberta | O texto tem "A confirmar" ou uma seção "Dúvidas em aberto" com pontos sem resposta. | Levar as dúvidas para a pauta, com quem pode responder. |
| dependência | Tem predecessor que não está em Done, ou a descrição cita algo de outro time que ainda não foi entregue. | Dizer de quem depende e em que estado está. |
| bug-incompleto | Bug sem Repro Steps, sem resultado esperado e atual, ou sem Severity. | Dizer o que falta. Para Severity, propor um valor com a régua da skill escrever-work-item. |

### Atenção
| Código | Como identificar | Sugestão |
|---|---|---|
| sem-caso-de-erro | Nenhum critério cobre erro, permissão ou indisponibilidade. | Sugerir um critério de erro. |
| sem-pai | PBI ou Bug sem Feature pai. | Sugerir até 3 Features candidatas, com ID e título. |
| pai-fechado | A Feature pai está em Done ou Removed. | Perguntar se o item ainda faz sentido ou se muda de pai. |
| duplicado | Título ou descrição muito parecidos com outro item aberto. | Mostrar os dois IDs e sugerir qual manter: o mais completo; se forem equivalentes, o mais antigo. |
| parado | Em New ou Approved, sem nenhuma alteração há mais de 90 dias (Changed Date). | Propor manter, juntar com outro item ou mudar para Removed. |
| sobrou-de-sprint | A Iteration é de uma sprint que já terminou. | Propor voltar para o backlog ou entrar na próxima sprint. |
| título-ruim | Genérico ("Ajustes", "Melhorias"), com a solução no lugar do resultado, ou com mais de 80 caracteres. | Sugerir um título novo. |
| só-solução | A descrição diz como implementar, mas não por quê. | Perguntar o motivo a quem abriu o item. |
| tipo-errado | Bug que descreve algo que nunca foi pedido, ou PBI que descreve um defeito. | Sugerir o tipo certo. A troca de tipo fica com quem lidera, no board. |
| prazo | Target Date vencida ou nas próximas 2 sprints, ou prazo regulatório citado no item. | Destacar no resumo. |
| sem-prioridade | PBI ou Bug sem Priority. | Classificar com a skill priorizar-itens. |
| prioridade-fora-de-ordem | Item abaixo de outro com Priority pelo menos 2 números maior (ex.: Priority 1 abaixo de um 3). | Levar para quem lidera: mudar a ordem ou a prioridade. |

### Regras do diagnóstico
- Não invente: ao sugerir critérios, títulos ou divisões, use só o que está no item e no board. O que faltar entra como "A confirmar".
- Qualquer alteração muda a Changed Date, inclusive tags. Um item "parado" pode ter tido só uma tag trocada; olhe as revisões (list_revisions) quando isso mudar a sugestão.
- Para escrever critérios, títulos, descrições ou PBIs novos, carregue a skill escrever-work-item e siga as regras dela.

## 4. Relatório e pauta

### Resumo
Comece com o título "Refinamento do time <TIME> · dd/mm/aaaa" e até 6 linhas:
- Quantos itens analisados, quantos prontos e quantos com problema que bloqueia.
- Quantos itens com cada problema, do mais comum para o menos comum.
- Saúde do backlog: Effort dos itens prontos ÷ velocidade = quantas sprints o backlog pronto cobre. O ideal é entre 1,5 e 2. Abaixo de 1, destaque como risco para a próxima sprint.
- Bugs com Severity 1 ou 2 e itens com prazo, se houver, com a posição atual de cada um.

### Tabela
- Na ordem atual do backlog, primeiro os itens com problema, depois os prontos.
- Colunas: Posição, ID, Tipo, Título, Effort, Bloqueia, Atenção, Sugestão.
- Título com até 50 caracteres; corte com "…".
- Sugestão em uma frase concreta.
- Os itens prontos podem vir numa lista curta, só com posição, ID e título.

### Pauta do refinamento
Separe por quem resolve, começando pelos itens mais perto do topo do backlog, que são os que entram na próxima sprint:
- Para o time: itens para estimar e divisões para discutir.
- Para quem lidera: duplicados, itens parados, itens sem pai, prazos e conflitos de ordem.
- Para outras pessoas: dúvidas que dependem de quem abriu o item ou de outro time, com o nome de quem abriu (Created By).

### Sugestões (Scrum)
Carregue a skill praticas-scrum e feche o relatório com a seção dela, depois da pauta. No modo de um item (seção 1), só as críticas, depois das 5 linhas.

### Exemplo
Ilustrativo: mostra o formato, não dados reais.

```
Refinamento do time <TIME> · 18/10/2026
- 32 itens analisados: 14 prontos, 18 com problema que bloqueia.
- Mais comuns: sem-esforço (11), sem-critérios (7), vago (4), dependência (2).
- Saúde: 340h prontas para uma velocidade de 280h → 1,2 sprint. Abaixo do ideal.
- #4521 (Bug, Severity 2) está na posição 9.

| Pos. | ID    | Tipo  | Título                   | Eff | Bloqueia            | Atenção     | Sugestão                         |
|------|-------|-------|--------------------------|-----|---------------------|-------------|----------------------------------|
| 1    | #4502 | PBI   | Exportar posições em CSV | —   | sem-esforço         | —           | Levar para o time estimar        |
| 3    | #4498 | PBI   | Ajustes na consulta      | —   | vago, sem-critérios | título-ruim | Perguntar o porquê a quem abriu  |
```

## 5. Proposta de ordem
- A ordem atual é a prioridade de quem lidera. Parta dela e mova um item só quando uma das regras abaixo justificar. Sem motivo, ele fica onde está.
- Proponha a ordem dos 10 primeiros itens prontos. Itens com problema que bloqueia não entram no topo: diga o que falta para entrarem.
- Regras, nesta ordem:
  1. Dependência: um item nunca fica acima do item de que depende. Esta regra não tem exceção.
  2. Bugs com Severity 1 ou 2.
  3. Prazo: Target Date ou prazo regulatório citado no item, do mais próximo para o mais distante.
  4. Priority, quando o tipo tiver (1 é a mais alta). Itens sem Priority não sobem nem descem por esta regra.
  5. Risk, quando o tipo tiver: entre itens iguais nas regras acima, risco alto primeiro, para descobrir problemas cedo.
  6. Feature: entre itens parecidos, aproxime os PBIs da mesma Feature, para terminar uma Feature antes de começar outra.
  7. Valor: o "para <por quê>" do PBI, só como desempate e sempre com a frase que justifica.
- Duplicados: use só o item que você sugeriu manter.
- Mostre uma tabela com Posição atual, Posição proposta, ID, Título e Motivo. Item que não mudou fica com "—" no motivo.
- Diga quantos itens mudaram de posição. Se nenhum mudou, diga que a ordem atual já segue as regras e não peça para aplicar.
- Termine com "Aplico esta ordem?".

## 6. Aplicar
- Faça primeiro as correções de conteúdo e depois a ordem. Se uma correção deixou um item pronto, refaça a proposta de ordem antes de aplicá-la.
- Ordem: só depois de um "sim" para a ordem, com wit_backlog (ação reorder). Mova só os itens que mudaram de posição. É mudança de planejamento.
- Correções de conteúdo: mostre cada item com os campos que mudam (valor atual → valor novo). Até 5 itens por proposta; o "sim" vale para os itens mostrados nela. Nunca altere em lote sem mostrar cada item.
  - Critérios, título ou descrição: não apague texto. Se o campo já tem conteúdo, mostre o atual e o novo, e mantenha o que existia, a não ser que quem lidera peça para tirar.
  - Divisão: crie os novos PBIs como filhos da mesma Feature. Proponha o que fazer com o original: virar a primeira parte, com título e critérios ajustados, ou ir para Removed com um comentário apontando os novos.
  - Duplicado: antes, copie para o item que fica qualquer informação que só o outro tinha, e mostre isso na proposta. O que sai vai para Removed, com o comentário "Duplicado de #<ID que fica>."
  - Parado: Removed só com aprovação, com o motivo no comentário.
  - Sobrou de sprint: a Iteration volta para o backlog ou vai para a próxima sprint, como quem lidera escolher.
- Não mude Effort nem Assigned To. Priority só pela skill priorizar-itens. Severity só em bug que não tem, com aprovação.
- Toda alteração leva a tag pm-agent e o comentário do protocolo, com o motivo começando por "Refinamento de dd/mm/aaaa:".
- No fim, liste o que foi alterado: ID, o que mudou e o link (https://dev.azure.com/btgpactual/<PROJETO>/_workitems/edit/<ID>).
