import datetime

from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from config import bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINS


async def go_to_sleep():
        await bot.send_message(ADMINS[0], "Сегодня пятница!")


async def wake_up(text):
        audio = open("media/audio.mp3", "rb")
        await bot.send_audio(ADMINS[0], audio=audio, caption=text)


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        go_to_sleep,
        trigger=CronTrigger(
            day_of_week=5,
            hour=10,
            minute=30,
            start_date=datetime.datetime.now()
        )

    )

    scheduler.add_job(
        wake_up,
        kwargs={
            "text": "Отдохни!",
        },
        trigger=IntervalTrigger(
            hours=2,
            start_date=datetime.datetime.now()
        )
    )

    scheduler.start()
