# whatsapp-gpt

This repo links WhatsApp messages to OpenAI's ChatGPT through a small Flask
server and a Go client using [whatsmeow](https://github.com/tulir/whatsmeow).

## Usage

1. Install Python dependencies:

   ```bash
   pip install flask openai
   ```

2. Export your OpenAI API key:

   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

3. Run the Flask server and WhatsApp client in separate terminals:

   ```bash
   python server.py
   go run main.go
   ```

Incoming WhatsApp messages are forwarded to the local server, which responds
with OpenAI's ChatCompletion API.

* `multichat.py` can be used to watch two ChatGPTs talk to each other.

This marks the end of the readme file; it is a bit sparse; thankfully the code
is too! Just tuck in if you can... and I will try to add more here later.
