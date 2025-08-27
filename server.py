"""Simple Flask server that proxies requests to OpenAI's Chat API.

This replaces the previous Playwright-based approach for interacting with
chat.openai.com directly. Instead, it uses the official OpenAI Python client
library which is more stable and requires an API key.

Run with:

```
export OPENAI_API_KEY=your_key_here
python server.py
```

Send a GET request to `/chat?q=<message>` and the server will return the model
response.
"""

import os
from flask import Flask, request
import openai


APP = Flask(__name__)

# Configure OpenAI API
openai.api_key = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")


@APP.route("/chat", methods=["GET"])
def chat() -> str:
    """Return a chat completion for the provided query string."""
    message = request.args.get("q")
    if not message:
        return "Missing 'q' query parameter", 400
    if not openai.api_key:
        return "OpenAI API key not configured", 500
    try:
        completion = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": message}],
        )
        return completion.choices[0].message["content"].strip()
    except Exception as exc:  # pragma: no cover - simple error passthrough
        return f"Error: {exc}", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    APP.run(port=port, threaded=True)

