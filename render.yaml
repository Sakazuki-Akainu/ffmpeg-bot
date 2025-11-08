import os
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from bot.__main__ import app, something

async def main():
    # Configure Hypercorn to bind to the Render-assigned port
    port = os.environ.get("PORT", "8080")
    config = Config()
    config.bind = [f"0.0.0.0:{port}"]
    config.keep_alive_timeout = 65

    # Start the Telegram bot in background
    asyncio.create_task(something())

    # Run Flask for health check endpoint
    await serve(app, config)

if __name__ == "__main__":
    asyncio.run(main())
