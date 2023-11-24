from openai import OpenAI
import telegram
import asyncio
import schedule
import time
import pytz
import datetime
token = "6804735527:AAFvVD6okO8SVtHL9sI6eLymUSs9VB7GdDw"


client = OpenAI(
    api_key =  "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"
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a assistant."},
        {"role": "user", "content": "유명한 축구 선수에 대해서 알려줘 "}
    ]
)

bot = telegram.Bot(token = token)
public_chat_name = "@k20222test"

async def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    
    if 6 <= now.hour < 23:
        return
    
    id_channel = await bot.sendMessage(
        chat_id = public_chat_name,
        text = completion.choices[0].message.content)
    print(id_channel)

async def main():
    while True:
        await job()
        await asyncio.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())
