import asyncio
import logging
import sys


from config.config import dp, bot, ColoredFormatter
from handlers.text_h import router as add_chats_router
from handlers.redirect import router as redirect_router
from handlers.add_keyword import router as add_keyword_router
from handlers.group import router as group_router
from handlers.start_cmd import router as start_router
from handlers.project import router as project_router
from handlers.instruction import router as instruction_router
from handlers.add_project import router as add_project_router


async def main() -> None:
    dp.include_router(add_chats_router)
    dp.include_router(redirect_router)
    dp.include_router(instruction_router)
    dp.include_router(add_keyword_router)
    dp.include_router(group_router)
    dp.include_router(start_router)
    dp.include_router(project_router)
    dp.include_router(add_project_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().handlers[0].setFormatter(ColoredFormatter())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
