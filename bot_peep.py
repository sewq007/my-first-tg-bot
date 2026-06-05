import telebot
import webbrowser 
import random
import os 
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN") 

bot = telebot.TeleBot(TOKEN)

facts = [
"если жизнь - это вызов, то я перезвоню",
"я так много читал о вреде алкоголя, что решил бросить читать",
"не знаешь, как поступить, поступи как знаешь",
"девушки как кредит, кому-то дают, а кому-то нет",
"пары - не удары, можно и пропустить",
"пиво,водка, турничок через часик я качок",
"у меня с собой две пушки, одна огнестрел, другая для подружки",
"настоящий мужик на руках носит только ящик пива, а не свою кралю",
"дают - бери, не дают - отбери",
"детство - это когда все в колготках, но не педики",
"иногда мне так лень ставить чайник, что я просто иду за пивом!",
"одна ошибка и ты ошибся",
"однажды мне стало лень обходить гору, так что я прошел её насквозь, теперь это называют туннелем",
"если жена делает тебя счастливой, то какая разница, чья это жена?",
"какая разница кто с кем спит? главное что все выспались",
"я раньше работал курьером, только я разносил не посылки, а ебальники",
"на днях был в качалке, занимался с тренажерами... тренажеры стали сильнее, пацаны стали слабее, я ушел домой"
] 

todo_list = {}

@bot.message_handler(commands=["fact"])
def send_fact(message):
    random_fact = random.choice(facts)
    bot.send_message(message.chat.id, random_fact)

#-----------------------------------------------------------

@bot.message_handler(commands=["todo"])
def manage_todo(message):
    user_id = message.chat.id
    parts = message.text.split(maxsplit=1)
    if len(parts) > 1:
        new_task = parts[1]
        if user_id not in todo_list:
            todo_list[user_id] = []
        todo_list[user_id].append(new_task)
        bot.send_message(message.chat.id, f"✅ Задача '{new_task}' добавлена!")
    else:
        if user_id in todo_list and todo_list[user_id]:
            tasks_text = "📋 Твой список задач:\n"
            for index, task in enumerate(todo_list[user_id], 1):
                tasks_text += f"{index}, {task}\n"
            bot.send_message(message.chat.id, tasks_text)
        else:
            bot.send_message(message.chat.id, "Твой список задач пока пуст. Добавь задачу так: `/todo Помыть посуду`", parse_mode="Markdown")       

#-----------------------------------------------------------

@bot.message_handler(commands=["start"])
def start_cmd(message):
    bot.send_message(message.chat.id, f"Приветики-Пистолетики, {message.from_user.first_name} {message.from_user.last_name}")

#----------------------------------------------------------- 

@bot.message_handler(commands=["help"])
def send_help(message):
    help_text = (
        "Вот что я умею:\n"
        "🤖 /start - Начать общение\n"
        "ℹ️ /help - Показать это меню\n"
        "💡 /fact - Рассказать случайный факт\n"
        "📝 /todo [задача] - Добавить задачу в список\n"
        "📋 /todo - Показать мой список задач\n"
    )
    bot.send_message(message.chat.id, help_text) 

#----------------------------------------------------------- 

@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"Пошел нахуй, {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text.lower() == "id":
        bot.reply_to(message, f"Твой ID: {message.from_user.id}") 

#-----------------------------------------------------------

bot.infinity_polling()