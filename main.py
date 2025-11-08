import os
import threading
import asyncio
from flask import Flask
from hypercorn.config import Config
from hypercorn.asyncio import serve

# Import your bot’s main runner
from bot.__main__ import something, LOGS

app = Flask(__name__)

@app.route("/")
def home():
    return "Render Dummy Server: OK", 200

@app.route("/health")
def health():
    return "OK", 200


def run_bot():
    """Run Telegram bot loop in background thread."""
    LOGS.info("Starting Telegram bot background loop...")
    asyncio.run(something())


async def run_web():
    """Run Flask web server for Render health check."""
    port = os.environ.get("PORT", "8080")
    cfg = Config()
    cfg.bind = [f"0.0.0.0:{port}"]
    await serve(app, cfg)


if __name__ == "__main__":
    # Start Telegram bot in a background thread
    threading.Thread(target=run_bot, daemon=True).start()
    # Run dummy web server in main thread
    asyncio.run(run_web())
