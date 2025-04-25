import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.messages import Quiz

# Estado por usuário: user_id -> {"perguntas": [...], "index": 0, "pontos": 0}
user_quiz_state = {}

def setup_message_quiz(bot: telebot.TeleBot):
    @bot.message_handler(commands=['quiz'])
    def quiz_start(message):
        bot.reply_to(message, "Bem vindo ao quiz da furia CS, vamos ver o quanto você sabe sobre a furia")
        user_id = message.from_user.id
        perguntas = Quiz
        random.shuffle(perguntas)  # Embaralha as perguntas

        user_quiz_state[user_id] = {
            "perguntas": perguntas,
            "index": 0,
            "pontos": 0
        }

        enviar_pergunta(bot, message.chat.id, user_id)

    @bot.callback_query_handler(func=lambda call: call.data.startswith("quiz_"))
    def quiz_responder(call):
        user_id = call.from_user.id
        state = user_quiz_state.get(user_id)

        if not state:
            bot.answer_callback_query(call.id, text="Comece o quiz com /quiz")
            return

        resposta_usuario = call.data.replace("quiz_", "")
        pergunta_atual = state["perguntas"][state["index"]]
        resposta_correta = pergunta_atual["correta"]

        if resposta_usuario == resposta_correta:
            state["pontos"] += 1
            bot.send_message(call.message.chat.id, "✅ Resposta correta!")
        else:
            bot.send_message(call.message.chat.id, f"❌ Errado! Resposta certa: {resposta_correta}")

        state["index"] += 1

        if state["index"] < len(state["perguntas"]):
            enviar_pergunta(bot, call.message.chat.id, user_id)
        else:
            pontos = state["pontos"]
            total = len(state["perguntas"])
            bot.send_message(call.message.chat.id, f"🎉 Fim do quiz!\nVocê acertou {pontos}/{total} perguntas.")
            del user_quiz_state[user_id]  # Limpa estado do usuário


def enviar_pergunta(bot, chat_id, user_id):
    state = user_quiz_state[user_id]
    pergunta = state["perguntas"][state["index"]]

    markup = InlineKeyboardMarkup()
    for alt in pergunta["alternativas"]:
        markup.add(InlineKeyboardButton(text=alt, callback_data=f"quiz_{alt}"))

    bot.send_message(
        chat_id,
        f"*{pergunta['pergunta']}*",
        parse_mode="Markdown",
        reply_markup=markup
    )