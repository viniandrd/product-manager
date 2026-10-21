---
name: priorizar-itens
description: Define e revisa a Priority dos PBIs e Bugs do time da sessão com uma régua de impacto e urgência, propondo o valor de cada item com a justificativa para quem lidera aprovar. Faz a classificação inicial dos itens sem prioridade, sugere a prioridade de um item e revisa as prioridades a cada sprint (prazos que chegaram, excesso de prioridade 1, ordem do backlog que contradiz a prioridade, dependências invertidas). Use quando pedirem para priorizar, definir ou revisar a prioridade, preencher o campo Priority, ou perguntarem qual a prioridade de um item.
---

# Priorizar itens

Siga o protocolo de escrita do agente. A prioridade é decisão de quem lidera: você aplica a régua e justifica.

As seções 1 a 5 só leem o board. Nada é gravado antes da seção 7, e só depois de um "sim".

## 1. Escolha o modo
- Classificação inicial: itens abertos sem Priority, a partir do topo do backlog (seção 4). Use quando o time começar a usar o campo ou quando houver muitos itens sem prioridade.
- Um item ("qual a prioridade do #123?"): a régua só daquele item, em até 5 linhas, e "Aplico?" se a Priority mudar.
- Revisão: os itens que já têm Priority, procurando o que mudou (seção 5). É a rotina de cada sprint (seção 8).

## 2. O que é a Priority
- O campo é Priority (Microsoft.VSTS.Common.Priority). Confira os valores permitidos em PBI e Bug com wit_work_item (ação get_type). O padrão do Azure DevOps é de 1 a 4, e 1 é a mais alta. Se os valores forem outros, mostre-os e pergunte como eles se encaixam na régua antes de seguir.
- Tipos: PBI e Bug. Feature e Epic só se o tipo tiver o campo e quem lidera pedir.
- A Priority é a classe de importância do item. A ordem do backlog é a sequência exata e continua sendo decisão de quem lidera. A Priority não reordena nada sozinha: ela entra na proposta de ordem da skill refinar-backlog (regra 4) e aponta conflitos (seção 5).
- Severity não é Priority. A Severity diz quanto o bug quebra; a Priority, quando resolver. A Severity entra na régua como impacto.

## 3. Régua

### Impacto
| Impacto | Quando |
|---|---|
| Alto | Risco regulatório ou financeiro, fluxo principal parado ou com contorno manual pesado, Bug com Severity 1 ou 2, ou muitos usuários ou processos afetados |
| Médio | Melhora relevante num fluxo importante, contorno manual que custa tempo toda semana, Bug com Severity 3 |
| Baixo | Ajuste pontual ou cosmético, poucos afetados, Bug com Severity 4 |

### Urgência
| Urgência | Quando |
|---|---|
| Alta | Prazo (Target Date ou prazo regulatório citado no item) até o fim da próxima sprint, ou o item trava outro time ou um item já planejado |
| Média | Prazo nas próximas 2 a 4 sprints, ou o custo de esperar cresce a cada sprint (contorno manual, volume aumentando) |
| Baixa | Sem prazo e sem custo de esperar |

### Priority
| Impacto \ Urgência | Alta | Média | Baixa |
|---|---|---|---|
| Alto | 1 | 2 | 3 |
| Médio | 2 | 3 | 4 |
| Baixo | 3 | 4 | 4 |

- Dependência: o item de que outro depende recebe pelo menos a mesma prioridade dele.
- Pai: a Priority da Feature não passa para os filhos. Ela só aparece no motivo, quando ajudar.
- Não invente: impacto e urgência vêm do item (Description, Severity, Target Date, tags e relações) ou de quem lidera. Sem base, o item fica "A confirmar" e você pergunta. Não deduza impacto pelo título.
- Na dúvida entre dois níveis, proponha o mais alto e diga que ficou na dúvida.

### Limite da prioridade 1
Se tudo é prioridade 1, nada é.
- O Effort somado dos itens abertos com Priority 1 não passa de uma sprint de velocidade. Priority 1 e 2 juntas, de 3 sprints. A velocidade é calculada como na skill refinar-backlog (seção 2).
- Se passar, mostre quanto passou e peça a quem lidera para escolher quais descem, oferecendo primeiro os de menor urgência. Não rebaixe nenhum por conta própria.
- Itens sem Effort aparecem à parte, como "Effort a confirmar".

## 4. Classificação

### Dados
- Recorte: backlog do time no nível de requisitos, em New, Approved ou Committed, como na skill refinar-backlog (seção 2). Itens da sprint atual também entram: a prioridade ajuda a decidir o que sai se a sprint precisar ser renegociada.
- De cada item, com wit_work_item: tipo, título, estado, Description, Severity (bugs), Effort, Priority, Target Date, Tags, Iteration Path, Created By, Changed Date e as relações (pai, predecessor e sucessor). Do pai, o título e a Priority.

### Rodadas
- Até 15 itens por rodada, na ordem do backlog. No fim de cada rodada, diga quantos faltam e pergunte se segue.
- Para cada item: o impacto e a urgência, cada um com o motivo tirado do item, e a Priority que sai da régua.
- Itens sem base para impacto ou urgência entram na lista "A confirmar". Pergunte numa mensagem só, junto com o "Aplico?".

## 5. Revisão

| Sinal | Como identificar | Sugestão |
|---|---|---|
| sem-prioridade | PBI ou Bug aberto sem Priority | Classificar (seção 4) |
| prazo-chegou | O prazo entrou na próxima sprint e a Priority é 3 ou 4 | Subir pela régua |
| p1-parado | Priority 1 há mais de 2 sprints (desde a revisão em que virou 1) e ainda fora de uma sprint | Entrar na próxima sprint ou descer: se não entra, não é 1 |
| excesso | Limite da seção 3 estourado | Escolher quais descem |
| ordem-contradiz | Item abaixo, na ordem do backlog, de outro com Priority pelo menos 2 números maior (ex.: Priority 1 abaixo de um 3) | Levar para quem lidera: mudar a ordem (skill refinar-backlog) ou a prioridade |
| dependência-invertida | Item com prioridade mais baixa que a de um item que depende dele | Subir para a mesma prioridade |
| severity-mudou | Bug com a Severity alterada depois da última mudança de Priority | Reavaliar pela régua |
| p4-antigo | Priority 4 sem nenhuma alteração há mais de 180 dias | Propor manter ou mudar para Removed, como no sinal "parado" da skill refinar-backlog |

- As datas das mudanças vêm das revisões do item (list_revisions). Busque-as só para os sinais que dependem delas.
- Ordem e Removed não mudam nesta skill: aponte e indique a skill refinar-backlog.

## 6. Proposta
Exemplo ilustrativo:

```
Priorização do time <TIME> · dd/mm/aaaa · <modo>

| Pos. | ID    | Tipo | Título                         | Effort | Impacto | Urgência | Priority | Motivo                                         |
|------|-------|------|--------------------------------|--------|---------|----------|----------|------------------------------------------------|
| 1    | #4502 | PBI  | Exportar posições em CSV       | 20     | Alto    | Alta     | — → 1    | Prazo regulatório em 15/11; contorno manual diário |
| 4    | #4521 | Bug  | Posições: opção vencida zerada | 10     | Médio   | Baixa    | — → 4    | Severity 3, contorno no sistema X              |

A confirmar
- #4510: impacto? urgência? (o item não diz quem é afetado nem se há prazo)

Distribuição depois da proposta
- Priority 1: 3 itens, 60h (0,6 sprint) · 2: 5 itens, 110h · 3: ... · 4: ... · sem prioridade: 12 itens

Sinais (revisão)
- ordem-contradiz: #4502 (Priority 1) está abaixo do #4490 (Priority 3).
```

- Até 15 itens por proposta. O "sim" vale para os itens mostrados nela.
- Posição é a posição atual no backlog. Mostre só os itens em que a Priority muda; os sinais sem mudança de Priority vão em "Sinais".
- Termine com: "Aplico estas prioridades? Se quiser, responda junto o que está a confirmar (ex.: 'sim; #4510 médio, baixa')."

## 7. Aplicar
- Depois do "sim", grave só a Priority, com wit_work_item_write (ação update_batch). Não mude ordem, Effort nem Iteration.
- Toda alteração leva a tag pm-agent e o comentário do protocolo, com o motivo: "Priorização de dd/mm/aaaa: Priority <antes> → <depois>. Impacto <nível> (<motivo>), urgência <nível> (<motivo>)." O comentário guarda a justificativa para a próxima revisão.
- No fim, liste os itens alterados, com ID, a Priority nova e o link (https://dev.azure.com/btgpactual/<PROJETO>/_workitems/edit/<ID>).

## 8. Rotina
- Uma vez: a classificação inicial, do topo do backlog para baixo, até cobrir pelo menos o que cabe em 3 sprints de velocidade.
- Item novo: a skill escrever-work-item propõe a Priority na criação, pela régua.
- A cada sprint, antes do refinamento: a revisão (seção 5). A skill refinar-backlog aponta os itens sem prioridade e as contradições de ordem.
