#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request


DEFAULT_MODEL = "sonar-pro"
DEFAULT_BASE_URL = "https://api.perplexity.ai"


SYSTEM_PROMPT = """Je bent een research-assistent voor Arthur Jansen.
Doe vergelijkend productonderzoek in helder Nederlands.
Prioriteer officiële bronnen voor pricing, features, API-toegang en limieten.
Gebruik community/reviewbronnen alleen als risico-indicator.
Geef een duidelijke aanbeveling, maar benoem onzekerheden.
Let extra op: gratis tier, eenvoud, samenwerking, API-toegang voor Codex, privacy, en risico op onnodige systeemcomplexiteit.
"""


OUTPUT_INSTRUCTIONS = """Geef antwoord in Markdown met:

## Advies
## Waarom
## Vergelijking
Een tabel met: Optie, Beste voor, Gratis tier, Codex/API toegang, Sterk, Risico.
## Bronnen
## Volgende Stap

Gebruik concrete bronverwijzingen waar mogelijk.
"""


def build_payload(question: str, model: str) -> dict:
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Onderzoeksvraag: {question}\n\n{OUTPUT_INSTRUCTIONS}",
            },
        ],
    }


def call_perplexity(question: str, model: str, timeout: int) -> dict:
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        raise RuntimeError("PERPLEXITY_API_KEY ontbreekt. Zet deze lokaal als environment variable.")

    base_url = os.environ.get("PERPLEXITY_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    url = f"{base_url}/chat/completions"
    body = json.dumps(build_payload(question, model)).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Perplexity API fout {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Kan Perplexity API niet bereiken: {exc}") from exc


def extract_markdown(response: dict) -> str:
    choices = response.get("choices") or []
    if not choices:
        return json.dumps(response, indent=2, ensure_ascii=False)

    message = choices[0].get("message") or {}
    content = message.get("content") or ""

    citations = response.get("citations") or response.get("search_results") or []
    if citations:
        content += "\n\n## API Brondata\n"
        for item in citations:
            if isinstance(item, str):
                content += f"- {item}\n"
            elif isinstance(item, dict):
                title = item.get("title") or item.get("name") or "Bron"
                url = item.get("url") or item.get("link") or ""
                content += f"- [{title}]({url})\n" if url else f"- {title}\n"

    return content.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Doe productonderzoek via de Perplexity API.")
    parser.add_argument("question", help="De onderzoeksvraag of vergelijking.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Perplexity model. Default: {DEFAULT_MODEL}")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout in seconden. Default: 300")
    parser.add_argument("--output", help="Optioneel pad om Markdown-output op te slaan.")
    args = parser.parse_args()

    try:
        response = call_perplexity(args.question, args.model, args.timeout)
        markdown = extract_markdown(response)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(markdown + "\n")
    else:
        print(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
