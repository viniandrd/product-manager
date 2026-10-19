---
name: escrever-work-item
description: Transforma uma ideia, um pedido ou um bug descrito em poucas palavras num work item bem escrito no Azure DevOps (Epic, Feature, User Story, Bug ou Task, processo Agile). Use quando pedirem para registrar, criar, abrir, escrever ou detalhar um épico, uma feature, uma story, um bug, um débito técnico, um spike ou uma tarefa no board.
---

# Escrever um work item

Siga o protocolo de escrita do agente: proposta completa, "Aplico?", tag pm-agent e comentário.

A ordem é sempre esta: entender o pedido, pesquisar no board, redigir, propor e, depois do "sim", gravar.

## 1. Entenda o pedido

### Qual tipo

| Tipo | Quando usar | Tamanho | Pai |
|---|---|---|---|
| Epic | Iniciativa grande com objetivo de negócio, que envolve vários sistemas ou times. Ex.: adaptar os sistemas à Reforma Tributária. | Meses; várias Features | Nenhum |
| Feature | Capacidade nova ou mudança relevante num sistema específico. Ex.: criar uma nova tela de consulta. | 1 a 3 sprints; várias stories | Epic |
| User Story | Comportamento novo ou alterado que alguém consegue usar ou verificar, geralmente pedido por usuários. | Cabe numa sprint | Feature |
| Bug | Algo que já foi entregue e não funciona como deveria. | Variável | Feature |
| Task | Um passo de trabalho dentro de uma story ou de um bug. | Horas a poucos dias | User Story ou Bug |

Casos que confundem:
- Mudança num comportamento que funciona como foi pedido é User Story, não Bug, mesmo que a pessoa chame de "erro".
- Problema numa story da sprint atual que ainda não foi fechada não vira Bug: proponha um comentário ou uma Task na própria story. Bug é para o que já foi entregue.
- Melhoria técnica sem usuário final (débito técnico, atualização de biblioteca, refatoração, monitoramento): story técnica (seção 3.2).
- Investigação para responder a uma pergunta antes de construir: spike (seção 3.3).
- Pedido de "tarefa" solta: descubra a story ou o bug pai. Não existe Task sem pai.
- Pedido que mistura várias coisas: separe em itens e proponha todos juntos (seção 8).
- Na dúvida entre dois tipos, escolha um, diga por quê em uma frase e cite a alternativa.

### O mínimo para propor
- Epic: o objetivo de negócio e o motivo (prazo regulatório, receita, risco, custo).
- Feature: o sistema afetado e o resultado esperado.
- User Story: quem usa, o que muda e por quê.
- Bug: o que acontece, o que deveria acontecer, como reproduzir e em qual ambiente.
- Task: a story ou o bug pai.

Se faltar algo desse mínimo, faça no máximo 3 perguntas curtas, todas na mesma mensagem, antes de propor. Se a pessoa não souber responder, siga e registre o ponto em "Dúvidas em aberto".

### Não invente
Não invente regras de negócio, valores, prazos, nomes de sistemas, de pessoas ou de clientes. Tudo o que não veio do pedido nem do board entra como "A confirmar" e aparece em "Dúvidas em aberto".

## 2. Pesquise no board antes de redigir

### Itens parecidos
Procure com wit_query (ação wiql), usando 2 ou 3 palavras-chave do pedido:

```sql
SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State]
FROM WorkItems
WHERE [System.TeamProject] = '<PROJETO>'
  AND [System.AreaPath] UNDER '<ÁREA-DO-TIME>'
  AND [System.State] <> 'Removed'
  AND ([System.Title] CONTAINS '<palavra 1>' OR [System.Title] CONTAINS '<palavra 2>')
ORDER BY [System.ChangedDate] DESC
```

- Se achar itens abertos parecidos, mostre ID, título e estado, e pergunte se é para criar um novo ou complementar o existente.
- Num bug, um item parecido já em Closed pode indicar regressão: diga isso e cite o ID antigo na descrição do novo.

### Pai
Respeite a hierarquia: Epic → Feature → User Story ou Bug → Task.
- Para uma Feature, procure o Epic. Para uma User Story ou um Bug, procure a Feature. Use wit_query filtrando por [System.WorkItemType] e por estado New ou Active.
- Mostre até 3 candidatos com ID e título e pergunte qual usar. Se nenhum servir, proponha o item sem pai e diga isso na proposta.
- Não pule níveis: story não é filha de Epic, task não é filha de Feature.

### Campos do tipo
Confira os campos do tipo escolhido com wit_work_item (ação get_type) e use os nomes exatos que vierem de lá. Se houver campo obrigatório que esta skill não cobre, pergunte o valor antes de propor.

### Área e iteração
- Area Path: <ÁREA-DO-TIME>. Se o pedido for de outra área (por exemplo, a PM Sandbox), confirme.
- Iteration Path: o padrão é o backlog (<ITERAÇÃO-DO-BACKLOG>). Epic e Feature ficam sempre no backlog. Para User Story e Bug, ofereça a sprint atual (work, ação list_team_iterations) como opção na hora do "Aplico?" (seção 8).

## 3. User Story

### 3.1 Story de usuário
- Título: até 80 caracteres, começando com verbo no infinitivo, dizendo o resultado para quem usa.
  - Bom: "Receber e-mail quando o pedido sair".
  - Ruim: "E-mail de pedido" (não diz o resultado), "Ajustes no pedido" (vago), "Criar fila no RabbitMQ" (é solução).
- Descrição, nesta ordem, omitindo as partes vazias:
  - "Como <quem>, quero <o quê>, para <por quê>." O "quem" é um papel concreto (operador da mesa, time de risco, o sistema de liquidação), nunca "o usuário".
  - Contexto: até 3 frases sobre o problema de hoje e o que motivou o pedido.
  - Fora de escopo: o que esta story não faz, quando houver risco de confusão.
  - Dependências: outros times, sistemas ou itens (com ID).
  - Referências: links, documentos ou normas citados no pedido.
  - Dúvidas em aberto: os pontos "A confirmar".
- Diga quem, o quê e por quê. Não diga como implementar. Restrições reais podem entrar ("não pode mudar o contrato atual da API"); a solução, não.
- Critérios de aceite: de 3 a 6 itens no formato "Dado <situação>, quando <ação>, então <resultado>".
  - Cada critério testa um comportamento só e pode ser verificado por alguém de QA sem perguntar nada ao dev.
  - Use valores concretos quando o pedido trouxer ("em até 2 segundos", "com a mensagem 'Conta inválida'"). Se não trouxer, escreva "A confirmar", sem inventar.
  - Inclua pelo menos um caso de erro (dado inválido, sem permissão, serviço fora do ar) e, quando fizer sentido, um caso de limite (lista vazia, valor zero, dia sem pregão). Caso de limite que você deduziu, e não veio do pedido, leva "(A confirmar)" no fim.
  - Quando fizer sentido, inclua um critério não funcional: tempo de resposta, log ou auditoria, permissão, compatibilidade com quem já consome o sistema.
  - Não use critérios como "funcionar corretamente", "ser rápido" ou "ser intuitivo", nem repita o título.

### 3.2 Story técnica
Para débito técnico, atualização, refatoração, infraestrutura ou monitoramento.
- Título: o resultado ("Alertar quando a fila de ordens passar de 1.000 mensagens"), não a atividade ("Mexer no monitoramento").
- Descrição: "Para <objetivo>, precisamos <mudança>, porque <risco ou custo de não fazer>.", mais o contexto.
- Value Area: Architectural. Tag: debito-tecnico.
- Critérios de aceite verificáveis, no mesmo formato. Ex.: "Dado que a fila passou de 1.000 mensagens, quando isso dura mais de 5 minutos, então o canal do time recebe um alerta."

### 3.3 Spike
Para quando o time precisa responder a uma pergunta antes de construir.
- Título: "Investigar <a pergunta>".
- Descrição: a pergunta, por que ela trava o trabalho e o prazo da investigação (no máximo uma sprint).
- Critérios de aceite: o que existe no fim. Ex.: "Recomendação registrada no item, comparando pelo menos 2 opções"; "Stories seguintes escritas e prontas para estimar".
- Tag: spike.

### 3.4 Tamanho
Sinais de que a story não cabe numa sprint: mais de 6 critérios, mais de um "quem", um "e" ligando duas entregas no título, mais de um sistema mudando, ou um cadastro completo (consultar, criar, alterar e excluir).

Se aparecer algum, proponha dividir em stories menores, cada uma entregando algo utilizável:
- Por fluxo: o caminho principal primeiro, os casos de erro depois.
- Por variação: um tipo de produto, de cliente ou de regra por vez (ex.: ações, depois opções).
- Por operação: consultar, depois criar, depois alterar.
- Simples primeiro: uma versão com menos campos ou manual, depois a completa.
- Por consumidor: um sistema ou uma tela de cada vez.

Não divida por camada técnica (uma story de backend, outra de banco): nenhuma delas entrega algo sozinha.

## 4. Bug
- Título: o sintoma que a pessoa vê, não a causa suposta. Formato: "<Sistema ou tela>: <sintoma> ao <ação>".
  - Bom: "Consulta de posições: opção vencida aparece com quantidade zero".
  - Ruim: "NullPointerException no PositionService" (é causa), "Erro na tela" (vago).
- Repro Steps, nesta ordem:
  1. Pré-condições: ambiente, perfil de acesso e dados necessários.
  2. Passos numerados, uma ação por passo.
  3. Resultado esperado.
  4. Resultado atual, com a mensagem de erro exata, se houver.
- Ainda nos Repro Steps, quando souber: frequência (sempre, às vezes, uma vez), desde quando acontece, quem e quantos são afetados e se existe contorno.
- System Info: ambiente (produção, UAT, desenvolvimento), versão ou build, data e hora da ocorrência, e o identificador da requisição ou da ordem, se houver.
- Evidências: você não anexa arquivos. Se houver prints ou logs, registre em "Dúvidas em aberto" que precisam ser anexados ao item.
- Severity: proponha um valor e justifique em uma frase. Quem lidera confirma.
  - 1 - Critical: fluxo principal parado, perda ou corrupção de dados, impacto financeiro ou regulatório, sem contorno.
  - 2 - High: funcionalidade importante quebrada, com contorno difícil ou manual.
  - 3 - Medium: funcionalidade secundária quebrada, ou importante com contorno simples.
  - 4 - Low: texto, layout ou algo cosmético.
  - Na dúvida entre dois níveis, proponha o mais alto e diga que ficou na dúvida.
- Severity 1 em produção: destaque isso no topo da proposta e sugira avisar quem precisa saber fora do board.
- Critérios de aceite, se o tipo tiver o campo: um critério com o comportamento esperado a partir dos Repro Steps e um que garanta que o que já funcionava continua funcionando.

## 5. O que deixar em branco ou só propor
- Story Points, Priority e Remaining Work: em branco. São decisões do time e de quem lidera. Não sugira número.
- Severity (Bug) e Risk (quando o tipo tiver): proponha com uma frase de justificativa. Risk só quando o pedido der base (prazo regulatório, dependência de outro time, tecnologia nova); senão, em branco.
- Assigned To: vazio. Se pedirem um responsável, sugira um dos devs com o motivo (carga na sprint atual, itens parecidos que já fez) e só preencha com aprovação. Busque a identidade exata com core_get_identity_ids.
- Iteration: ver seção 2.

## 6. Epic e Feature

### Epic
- Título: até 80 caracteres, com o resultado de negócio ("Adaptar os sistemas de derivativos à Reforma Tributária").
- Descrição:
  - Objetivo: o que muda para o negócio quando o Epic terminar.
  - Motivo: regulatório, receita, risco, custo ou eficiência, com o prazo, se houver.
  - Como medir o sucesso: de 1 a 3 indicadores. Se o pedido não trouxer, "A confirmar".
  - Escopo e fora de escopo.
  - Sistemas e times envolvidos.
  - Dúvidas em aberto.
- Value Area: Business, ou Architectural se o motivo for técnico.
- Target Date: só com um prazo real (por exemplo, a data de uma norma). Senão, em branco.
- Features candidatas: liste de 2 a 6 títulos na proposta, como sugestão. Só crie quando pedirem.

### Feature
- Título: até 80 caracteres, com a capacidade entregue ("Consultar posições de opções por vencimento").
- Descrição: o problema, o resultado esperado, o sistema afetado, fora de escopo, dependências e dúvidas em aberto.
- Critérios de aceite: de 2 a 5 itens no nível da Feature, ou seja, o que precisa ser verdade quando todas as stories estiverem prontas.
- Pai: o Epic (seção 2).
- Stories candidatas: liste de 3 a 8 títulos na proposta, como sugestão. Só crie quando pedirem; nesse caso, cada uma segue a seção 3.

## 7. Tasks, só quando pedirem
- De 2 a 6 tasks com resultado concreto, começando com verbo no infinitivo ("Criar o endpoint de reset", não "Backend"), criadas como filhas da story ou do bug.
- Activity: Development, Testing, Documentation, Deployment, Design ou Requirements (confirme os valores com get_type).
- Inclua uma task de teste que cite os números dos critérios de aceite que ela cobre.
- Inclua task de documentação ou de deploy só quando a story mudar contrato de API, configuração ou infraestrutura.
- Iteration: a mesma da story ou do bug pai.
- Remaining Work e Assigned To: em branco.
- Mais de 6 tasks é sinal de story grande demais: volte à seção 3.4 e proponha dividir.

## 8. Formato da proposta
Mostre cada item neste formato:

```
Proposta 1 de 1 · User Story
Título: Receber e-mail quando o pedido sair
Pai: #1234 Notificações de pedidos (Feature)
Área: <ÁREA-DO-TIME>
Iteração: Backlog
Tags: pm-agent
Value Area: Business

Descrição
Como cliente da mesa, quero receber um e-mail quando meu pedido for executado, para não precisar acompanhar a tela.
Contexto: ...
Dúvidas em aberto: ...

Critérios de aceite
1. Dado ..., quando ..., então ...
2. ...

Em branco: Story Points, Priority, Assigned To.
Itens parecidos: nenhum. (ou: #987, Closed, citado na descrição)
```

Para User Story e Bug, termine com: "Aplico? Responda 'sim' para gravar no backlog ou 'sim, sprint atual' para gravar na <nome da sprint atual>." Para os outros tipos, termine só com "Aplico?".

- Vários itens no mesmo pedido (uma story e suas tasks, ou várias stories) vão numa proposta só, com todos os itens completos. O "sim" vale para todos os itens mostrados nela.
- Se pedirem ajuste, mostre a proposta inteira de novo, já ajustada, e pergunte de novo. Não grave em partes.

## 9. Como gravar
- Descrição, Critérios de aceite, Repro Steps e System Info vão em HTML simples: <p>, <b>, <br>, <ol>, <ul>, <li> e <a href>. Não use Markdown nesses campos: os asteriscos aparecem no board. O título é texto puro.
- Nos critérios de aceite, use um <li> por critério dentro de <ol>, com <b>Dado</b>, <b>quando</b> e <b>então</b>.
- Item sem pai: wit_work_item_write (ação create). Item com pai (Feature sob Epic, story ou bug sob Feature, task sob story ou bug): wit_work_item_write (ação add_child), a partir do pai.
- Se o pai também for novo, crie o pai primeiro para ter o ID.
- Responda com o ID, o título e o link de cada item criado: https://dev.azure.com/btgpactual/<PROJETO>/_workitems/edit/<ID>
- Se a gravação der erro, mostre a mensagem. Não tente de novo com outros valores sem uma nova aprovação.

## 10. Exemplos
Os exemplos mostram o nível de detalhe esperado. Não são regras do negócio.

### User Story
Pedido: "o pessoal de risco quer ser avisado quando o arquivo de preços da B3 não chegar até 8h, hoje eles só descobrem quando o relatório sai vazio"

Perguntas: nenhuma obrigatória, porque quem, o quê e por quê estão no pedido. O canal do aviso fica em "Dúvidas em aberto".

Proposta:
- Título: Avisar o time de risco quando o arquivo de preços da B3 atrasar
- Descrição: Como analista do time de risco, quero ser avisado quando o arquivo de preços da B3 não chegar até as 8h, para agir antes de os relatórios da manhã saírem vazios.
- Contexto: hoje o atraso só é percebido quando o relatório sai vazio.
- Dúvidas em aberto: o canal do aviso (e-mail ou Teams); se deve haver um segundo aviso quando o arquivo chegar atrasado.
- Critérios de aceite:
  1. Dado um dia de pregão, quando o arquivo não chegou até as 8h, então o time de risco recebe um aviso com o nome do arquivo e o horário da checagem.
  2. Dado um dia de pregão, quando o arquivo chegou até as 8h, então nenhum aviso é enviado.
  3. Dado um dia sem pregão na B3, quando dá 8h, então nenhuma checagem é feita. (A confirmar)
  4. Dado que o envio do aviso falhou, quando o sistema tenta avisar, então a falha fica registrada no log com o motivo.

### Bug
Pedido: "a tela de posições tá mostrando quantidade zerada pras opções que venceram, em produção"

Perguntas (faltam o resultado esperado e a reprodução):
1. O que deveria aparecer: a opção não deveria estar na lista, ou deveria mostrar outra quantidade?
2. Acontece com todas as contas ou com alguma específica? Tem um exemplo?
3. Desde quando acontece, e existe outro jeito de ver a posição certa enquanto isso?

Respostas: "não deveria aparecer", "todas", "desde o último vencimento, dá para ver no sistema X".

Proposta:
- Título: Consulta de posições: opções vencidas aparecem com quantidade zero
- Repro Steps:
  - Pré-condições: produção; qualquer conta com posição em opção que venceu no último vencimento.
  1. Abrir a consulta de posições.
  2. Pesquisar a conta.
  3. Procurar a opção vencida na lista.
  - Esperado: a opção vencida não aparece na lista.
  - Atual: a opção aparece com quantidade 0.
  - Frequência: sempre, desde o último vencimento. Afeta todas as contas. Contorno: consultar no sistema X.
- System Info: produção; build A confirmar; percebido em <data do pedido>.
- Severity: 3 - Medium. O dado está errado em produção, mas existe contorno simples.

## 11. Antes de mostrar a proposta, confira
- Tipo certo, com justificativa se houve dúvida.
- Itens parecidos pesquisados e citados.
- Pai escolhido, ou dito que não há.
- Título no formato do tipo, com até 80 caracteres.
- Nada inventado: o que não veio do pedido está como "A confirmar".
- Critérios verificáveis, com pelo menos um caso de erro.
- Nenhuma solução técnica na descrição.
- Story Points, Priority e Assigned To em branco.
- Área, iteração e tag pm-agent na proposta.
