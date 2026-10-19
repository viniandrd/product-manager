"""Envia o relatório como card para o webhook do Teams (Workflows)."""
import json
import os
import sys
import urllib.request

LIMITE = 20000  # mensagens do Teams têm limite de tamanho

texto = open(sys.argv[1], encoding="utf-8").read().strip()
if not texto:
    sys.exit("Relatório vazio: nada foi enviado.")
if len(texto) > LIMITE:
    texto = texto[:LIMITE] + "\n\n(relatório cortado; versão completa no artefato da pipeline)"

card = {
    "type": "message",
    "attachments": [{
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.4",
            "body": [{"type": "TextBlock", "text": texto, "wrap": True}],
        },
    }],
}

pedido = urllib.request.Request(
    os.environ["TEAMS_WEBHOOK_URL"],
    data=json.dumps(card).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(pedido, timeout=30) as resposta:
    print("Teams respondeu", resposta.status)