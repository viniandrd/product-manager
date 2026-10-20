---
name: atualizar-cadeia
description: Confere e acerta a cadeia de pais dos itens da sprint do time da sessão (task → PBI ou Bug → Feature → Epic). Cuida do estado dos pais, da soma de Completed Work e Remaining Work, das tags de estimativa, causa e bloqueio e do Effort congelado. É chamada pela skill atualizar-horas no fim da daily e também pode ser usada sozinha. Use quando pedirem para acertar a cadeia, atualizar os pais, conferir uma Feature ou um Epic, ou quando uma Feature não estiver com o status ou as horas certos.
---

# Atualizar a cadeia de pais

Siga o protocolo de escrita do agente. Atualizações de horas e estado dos pais não recebem comentário (exceção prevista no agente).

## Passo a passo
1. Carregue a skill regras-de-estimativa. A estimativa de cada tipo, a projeção, os limites, os sinais e as origens usados aqui estão lá.
2. Busque os dados (seção 2).
3. Acerte o estado (seção 3), as horas (seção 4), as tags de estimativa (seção 5) e o bloqueio (seção 6).
4. Calcule os sinais da cadeia (seção 7) e confira a área (seção 8).
5. Dentro da daily, devolva as linhas para a proposta da skill atualizar-horas. Sozinha, monte a proposta (seção 9).
6. Depois do "sim", grave na ordem da seção 10.

## 1. Escolha o modo
- Dentro da daily: a skill atualizar-horas chama esta skill com os valores das tasks já com as mudanças da daily. Confira a cadeia de todo PBI e Bug da sprint atual, não só dos que mudaram hoje. Não monte proposta própria: devolva a tabela "Cadeia", os alertas e as "Tags na cadeia" para entrarem na proposta única da daily.
- Sozinha: quando pedirem algo como "acerta a cadeia da sprint" ou "confere a Feature #100". Para um ID, confira os pais dele e, se ele for Feature ou Epic, tudo abaixo dele. Monte a proposta da seção 9.
- Cada pai aparece uma vez só na proposta, mesmo que tenha vários filhos.

## 2. Dados
- PBIs e Bugs da sprint atual, ou do recorte pedido, com a Feature e o Epic acima de cada um: tipo, estado, Area Path, CW, RW, Effort e tags.
- Das revisões (list_revisions): o Effort congelado e o dia de entrada de cada PBI e Bug, e o Effort congelado em DEV de cada Feature, com a data (regras-de-estimativa, seção 2).
- Tasks e PBIs abaixo de cada pai: consulta em árvore com wit_query (ação wiql), e depois os campos dos IDs com wit_work_item (tipo, estado, OE, CW, RW, Effort, tags e Created Date):

```sql
SELECT [System.Id]
FROM WorkItemLinks
WHERE [Source].[System.Id] = <ID do pai>
  AND [System.Links.LinkType] = 'System.LinkTypes.Hierarchy-Forward'
MODE (Recursive)
```

- Estados de PBI, Bug, Feature e Epic (wit_work_item, ação get_type), na ordem do tipo e com a categoria de cada um (Proposed, In Progress, Resolved, Completed, Removed). Busque uma vez por sessão. Se a ferramenta não trouxer a categoria, pergunte uma vez qual é o primeiro estado "em andamento" de cada tipo.

## 3. Estado
O pai nunca fica atrás do filho mais adiantado, e nunca volta de estado.
- PBI ou Bug na sprint atual, ou com alguma task em In Progress, que ainda está num estado da categoria Proposed (ex.: New, Approved): proponha o primeiro estado da categoria In Progress do tipo.
- Feature com algum filho na sprint atual ou em andamento, ainda num estado anterior a DEV: proponha DEV. Se o tipo Feature não tiver o estado DEV, avise e proponha o primeiro estado da categoria In Progress.
- Epic com alguma Feature em DEV ou num estado depois dele, ainda num estado da categoria Proposed: proponha o primeiro estado da categoria In Progress do tipo.
- Todos os filhos em Done ou Removed, com pelo menos um em Done: proponha passar o pai para o primeiro estado da categoria Completed, numa linha marcada como "fechamento". O aceite é decisão de quem lidera.
- Pai à frente do filho (ex.: Feature em Done com um PBI na sprint): não mude nada. Mostre nos alertas e pergunte se é para reabrir o pai ou tirar o filho dele.
- "Anterior" e "depois" seguem a ordem dos estados no get_type. Na proposta, use o nome exato do estado.

## 4. Horas
- CW e RW de cada pai = as somas da regras-de-estimativa (seção 2), sempre a partir das tasks abaixo dele, em qualquer sprint.
- PBI ou Bug sem nenhuma task: não mexa no CW e no RW dele.
- Não altere o Effort dos pais, a não ser para voltar ao Effort congelado (sinal "Effort alterado", seção 7).
- Se o tipo do pai não tiver CW ou RW (veja no get_type), pule o campo naquele nível e avise uma vez.
- Mostre só os pais cujo valor muda.

## 5. Tags de estimativa nos pais
PBI, Bug e Feature recebem as tags, porque a Feature é a visão de quem acompanha o time de fora. O Epic não recebe.

Durante o trabalho, a cada daily:
- Pai estourado (regras-de-estimativa, seção 5): tag `estimativa-subestimada` no pai, mais as tags `causa-*` que existirem nas tasks abaixo dele.
- Projeção que voltou para dentro da faixa: proponha tirar `estimativa-subestimada` e as tags de causa que vieram das tasks.

No fechamento, quando o pai vai para Done (na linha de fechamento da seção 3, ou porque quem lidera disse que foi entregue), classifique o realizado contra a estimativa pelos limites da regras-de-estimativa (seção 4):
- Subestimado: `estimativa-subestimada`, com as tags de causa.
- Superestimado: `estimativa-superestimada`.
- Preciso: tire `estimativa-subestimada`, se houver.
- Pai que foi para Done fora do agente, fora da faixa e sem tag de estimativa: proponha a marcação na daily seguinte.
- Sem estimativa, ou com alguma task sem CW: não marque, e diga que faltou o dado.

Comentário, só quando a tag entra, sai ou no fechamento (não em toda daily). As origens são as da regras-de-estimativa (seção 7):
- PBI ou Bug: "Estimativa do PBI: Effort <e>h, <projeção ou realizado> <r>h (<z>%). Quebra <±q>h, estimativa das tasks <±t>h, trabalho descoberto <+d>h. Causas: <tags>. Daily de dd/mm/aaaa."
- Feature: "Estimativa da Feature: Effort <e>h (congelado em DEV), <projeção ou realizado> <r>h (<z>%). PBIs novos depois de DEV <+n>h, estouro dos PBIs <±p>h, diferença entre o Effort da Feature e os PBIs iniciais <±f>h. Causas: <tags>. Daily de dd/mm/aaaa."

## 6. Bloqueio
- PBI ou Bug com alguma task com `bloqueado`, e Feature com algum item abaixo com `bloqueado`: tag `bloqueado` no pai. Na primeira vez, comente no pai: "Bloqueio em #<ID> (<título>)."
- Bloqueio marcado direto num PBI ou Bug, e não numa task, também sobe para a Feature.
- Quando nada abaixo estiver bloqueado: proponha tirar a tag do pai, sem comentário.
- O Epic não recebe.

## 7. Sinais da cadeia
Sinais definidos na regras-de-estimativa (seção 5):

| Sinal | O que fazer |
|---|---|
| Pai estourado | Marcar o pai (seção 5) e mostrar no alerta a origem da diferença (regras-de-estimativa, seção 7) |
| Quebra acima do Effort | Só avisar, uma vez por item |
| Effort alterado | Propor voltar ao valor congelado. Num PBI ou Bug, se a diferença for trabalho a mais, propor também uma task nova com ela, seguindo a skill atualizar-horas (seção 4) |

## 8. Área e pai faltando
- Feature e Epic podem ser de outra área. Pai fora de <ÁREA-DO-TIME> aparece na proposta com o aviso "fora da área do time" e só é gravado se quem lidera aprovar aquele item pelo ID (ex.: "sim, inclusive #90").
- PBI ou Bug sem Feature: só avise ("sem Feature"). Esta skill não cria nem escolhe pai.

## 9. Proposta (quando usada sozinha)
Exemplo ilustrativo:

```
Cadeia do time <TIME> · dd/mm/aaaa

| Tipo    | ID   | Título            | Estado               | CW        | RW        | Effort | Projeção/Effort | Motivo                                     |
|---------|------|-------------------|----------------------|-----------|-----------|--------|-----------------|--------------------------------------------|
| PBI     | #120 | Reset de senha    | Approved → Committed | 15 → 20   | 18 → 14   | 30     | 113%            | está na sprint atual                       |
| Feature | #100 | Autenticação      | New → DEV            | 40 → 45   | 60 → 56   | 120    | 84%             | filho #120 na sprint                       |
| Epic    | #90  | Portal do cliente | New → In Progress    | 120 → 125 | 200 → 196 | —      | —               | Feature #100 em DEV · fora da área do time |

Alertas
- Feature #105 está em Done, mas o PBI #140 está na sprint. Nada foi mudado: reabrir a Feature ou tirar o PBI dela?
- PBI #122 estourado: Effort 20h, projeção 32h (160%). Quebra +4h, estimativa das tasks +2h, trabalho descoberto +6h.
- Quebra acima do Effort: o PBI #124 tem Effort 20h, mas as tasks do planejamento somam 28h.
- Effort do PBI #121 mudou de 20 para 30 depois de entrar na sprint. Voltar para 20 e criar uma task de 10h com a diferença?

Tags na cadeia
- PBI #122 e Feature #110: + estimativa-subestimada e causa-escopo (PBI em 160% do Effort, Feature em 132% do Effort de DEV), com comentário.
- PBI #126 e Feature #100: + bloqueado, por causa da task #125, com comentário.
```

- Mostre só as linhas que mudam.
- Termine com: "Aplico? Itens fora da área do time só entram se você citar o ID (ex.: 'sim, inclusive #90')."
- Dentro da daily, a tabela, os alertas e as tags entram na proposta da skill atualizar-horas, e esta seção não é usada.

## 10. Aplicar
- Task nova da diferença (Effort alterado): crie antes de tudo, com wit_work_item_write (ação add_child) a partir do PBI ou Bug, seguindo a skill atualizar-horas (seção 4).
- Grave os pais com wit_work_item_write (ação update_batch), de baixo para cima: PBI ou Bug, depois Feature, depois Epic. Dentro da daily, os pais vêm depois das tasks.
- Nos pais: estado, CW, RW, as tags de estimativa, causa e bloqueio e, só para voltar ao Effort congelado e com aprovação, o Effort.
- Mantenha as tags que já existem e acrescente pm-agent.
- Estado e horas não recebem comentário. Recebem comentário: a marcação de estimativa (seção 5) e o bloqueio que sobe para o pai (seção 6).
- Usada sozinha, responda no fim em até 3 linhas: quantos pais foram atualizados e o que ficou pendente (pais fora da área não aprovados, alertas sem resposta).
