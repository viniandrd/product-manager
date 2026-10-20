---
name: relatorio-status
description: Gera o relatório de status da sprint atual do time em duas versões, uma para o time e outra para gestores, com o que foi concluído, o que está em andamento, o que está bloqueado e os riscos. Use quando pedirem status, resumo, relatório, andamento ou fechamento da semana ou da sprint.
---

# Relatório de status

Esta skill só lê o board. Nunca crie, altere ou comente itens enquanto gera o relatório.

## 1. Dados
- Sprint atual do time (work, ação list_team_iterations): nome, datas e dias úteis que faltam.
- Itens da sprint (wit_work_item, ação list_for_iteration): tipo, título, estado, responsável, Effort, Remaining Work das tasks e data da última alteração.
- Semana: o que mudou de estado nos últimos 7 dias. Use list_revisions só quando precisar confirmar.
- Bloqueios: itens com a tag bloqueado e Impediments ligados a itens da sprint. PBIs e Bugs em Committed e tasks em In Progress sem alteração há mais de 3 dias úteis entram como "possível bloqueio".
- Concluído = Done. PBI ou Bug com todas as tasks em Done, mas que ainda não está em Done, aparece à parte, como "aguardando aceite".
- Features dos itens da sprint: título, Effort, CW, RW e tags.

## 2. Versão para o time
Por dev, em listas curtas com IDs:
- Concluído na semana
- Em andamento
- Bloqueado ou possível bloqueio, com o motivo se estiver escrito no item
No fim: itens sem responsável e itens que entraram na sprint depois do início.

## 3. Versão para gestores
No máximo 8 linhas, sem IDs no texto:
- Objetivo da sprint e dias restantes.
- Progresso: Effort concluído / planejado, em dias (1 dia = 10h), e a porcentagem.
- Riscos: o que pode não ser entregue e por quê.
- Features estouradas ou bloqueadas: título, quanto passou do Effort e as causas, pelas tags `estimativa-subestimada`, `causa-*` e `bloqueado`.
- Decisões ou ajuda necessárias.

## 4. Regras de texto
- Português, frases curtas, sem jargão interno.
- Não invente causas. Se o motivo de um bloqueio não estiver no item, escreva "motivo não registrado".
- Datas em dd/mm/aaaa.
- Comece cada versão com o título "Status do time <TIME> · dd/mm/aaaa".