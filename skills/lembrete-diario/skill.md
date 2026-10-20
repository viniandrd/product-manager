---
name: lembrete-diario
description: Gera o lembrete diário do board do time, só de leitura, com as tasks da sprint atual que estão desatualizadas, estourando a estimativa, atrasadas ou sem estimativa, e os pais (PBI, Feature, Epic) com estado atrasado em relação aos filhos, para cobrar a atualização na daily. É usada pela rotina automática de manhã e também quando pedirem o lembrete ou o que está desatualizado no board.
---

# Lembrete diário

Esta skill só lê o board. Nunca crie, altere ou comente itens.

As regras de sinal abaixo são uma cópia curta da skill regras-de-estimativa. Elas ficam copiadas aqui porque a rotina roda sem ninguém acompanhando. Se mudar uma regra lá, mude aqui também.

## 1. Dados
- Sprint atual do time (work, ação list_team_iterations): nome e dias úteis que faltam. Se hoje não estiver dentro de nenhuma sprint, responda só com "Sem sprint em andamento hoje."
- Tasks da sprint (wit_work_item, ação list_for_iteration), fora as que estão em Done ou Removed: título, estado, Assigned To, Original Estimate (OE), Completed Work (CW), Remaining Work (RW), Changed Date, tags e a data em que entrou em In Progress.
- Capacidade da sprint (work, ação get_team_capacity): horas por dia e folgas de cada dev.
- Tasks da sprint que foram para Done desde o último dia útil (State Change Date), com as tags.
- PBIs e Bugs da sprint, com a Feature e o Epic acima de cada um, e o estado de todos.
- Estados de PBI, Bug, Feature e Epic (wit_work_item, ação get_type), na ordem do tipo e com a categoria de cada um.

## 2. O que apontar

| Sinal | Regra |
|---|---|
| Estouro | CW + RW acima de 125% da OE, com diferença de pelo menos 5h (meio dia) |
| Atrasada | Hoje passou da data em que entrou em In Progress + (OE ÷ 10, arredondado para cima) dias úteis, mais os dias de folga do dev nesse período. O time usa 1 dia = 10h |
| Sem atualização | Em In Progress, com Changed Date anterior ao último dia útil |
| Pronta para fechar | RW = 0 e não está em Done |
| Sem estimativa | Em In Progress sem OE |
| Sem responsável | Em In Progress sem Assigned To |
| Sem task em andamento | Dev com horas na capacidade hoje e nenhuma task em In Progress |
| Fechada sem uso de IA | Task que foi para Done desde o último dia útil sem nenhuma tag `ia-*` |

Pais desatualizados (só o estado; a soma de horas fica para a daily):
- PBI ou Bug da sprint ainda num estado da categoria Proposed (ex.: New, Approved).
- Feature com filho na sprint ainda num estado anterior a DEV.
- Epic com Feature em DEV, ou num estado depois dele, ainda num estado da categoria Proposed.
- Pai em Done com filho na sprint.

- Task com a tag `bloqueado` não entra como "sem atualização": vai para a linha "Bloqueadas".
- Dev de folga hoje (na capacidade) aparece com "(de folga)" e não entra em "sem task em andamento".

## 3. Formato
O card do Teams mostra texto simples: use listas, sem tabelas nem títulos com #.

```
Board de hoje · time <TIME> · dd/mm/aaaa
Sprint <nome> · faltam <n> dias úteis

Ana
- #123 Criar endpoint de reset: sem atualização desde dd/mm/aaaa
- #127 Migrar tabela de ordens: estouro (OE 20h, projeção 34h); atrasada

Bruno
- tudo em dia

Bloqueadas: #125 (Carla)

Pais desatualizados
- Feature #100 Autenticação: em New, com o PBI #120 na sprint
- PBI #120 Reset de senha: em Approved, mas está na sprint

Atualize na daily: diga ao agente pm as horas e o estado de cada task.
```

- Agrupe por dev, em ordem alfabética. Dev sem nenhum sinal aparece com "tudo em dia".
- Uma linha por task. Se ela tiver mais de um sinal, junte-os na mesma linha, separados por ";", nesta ordem: estouro, atrasada, sem atualização, pronta para fechar, sem estimativa, sem responsável, fechada sem uso de IA.
- No máximo 60 linhas. Se passar disso, mostre as primeiras e diga quantas ficaram de fora.
- Não invente causas nem nomes. Datas em dd/mm/aaaa.
