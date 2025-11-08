import os
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from bot.__main__ import app, something

async def main():
    # Create Hypercorn config for Flask
    config = Config()
    port = os.environ.get("PORT", "8080")
    config.bind = [f"0.0.0.0:{port}"]

    # Run your Telegram bot in background
    asyncio.create_task(something())

    # Serve Flask app for Render health checks
    await serve(app, config)

if __name__ == "__main__":
    asyncio.run(main())
