import telebot
from random import randint
import os
import json
from telegram_bot_shop.models import *
from telebot import types

config = {
    "name": "Shoppi_bot",
    "token": "5637985384:AAFRliKZEvoVbu1t1MXmFdMcbTckB6361DY"
}

fedo = telebot.TeleBot(config["token"])

list_cat = []
list_data = []
lst1 = []
lst2 = []

customer1 = Customer.objects.values()
for ele in customer1:
    lst1.append(ele['name'])
print(lst1)

pr1 = Category.objects.values()
for ele in pr1:
    lst2.append(ele['name'])


@fedo.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data:
        print(str(call.data))
        list_data.append(str(call.data))
        fedo.send_message(call.message.chat.id, f"Added to basket")


@fedo.message_handler(commands=["shop"])
def shop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Basket")
    btn2 = types.InlineKeyboardButton("Sort")
    btn3 = types.InlineKeyboardButton("Clear Basket")
    btn4 = types.InlineKeyboardButton("Pay")
    btn5 = types.InlineKeyboardButton("Go back")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    fedo.send_message(message.chat.id, 'Shop', reply_markup=markup)


def sort(message):
    global list_cat
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cat = Category.objects.values()
    btn3 = types.InlineKeyboardButton("Go back")
    for key in cat:
        list_cat.append(key['name'])
        markup.add(key['name'])
    markup.add(btn3)
    fedo.send_message(message.chat.id, 'Choose sorting', reply_markup=markup)


@fedo.message_handler(commands=["start"])
def authorization(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Registration")
    btn2 = types.InlineKeyboardButton("Authorisation")
    btn3 = types.InlineKeyboardButton("Shop", callback_data="basket")
    markup.add(btn1, btn2, btn3)
    fedo.send_message(message.chat.id, 'Hi', reply_markup=markup)


@fedo.message_handler(content_types=["text"])
def get_text(message):
    lst = []

    customer = Customer.objects.values()
    for el in customer:
        lst.append(el['name'])

    if message.text == "Registration":
        password = fedo.send_message(message.chat.id,
                                     f"Write password for your account(your unique username was taken as login):")
        fedo.register_next_step_handler(password, register)
    elif message.text == "Authorisation":
        password = fedo.send_message(message.chat.id,
                                     f"Write password of your account(your unique username was taken as login):")
        fedo.register_next_step_handler(password, login)
    elif message.text.lower() == "shop" and message.from_user.username in lst:
        shop(message)
        goods = Product.objects.values()

        inlines = telebot.types.InlineKeyboardMarkup()
        for i in range(len(goods)):
            inlines.add(telebot.types.InlineKeyboardButton(text=f"{goods[i]['name']} - {goods[i]['price']}$",
                                                           callback_data=f"{goods[i]['name']} - {goods[i]['price']}$"))
        fedo.send_message(message.chat.id, f"List of goods:", reply_markup=inlines)
    elif message.text.lower() == "basket" and message.from_user.username in lst:
        for e in list_data:
            fedo.send_message(message.chat.id, e)
    elif message.text.lower() == "clear basket" and message.from_user.username in lst:
        list_data.clear()
        fedo.send_message(message.chat.id, "Cleared")
    elif message.text.lower() == "sort" and message.from_user.username in lst:
        sort(message)
    elif message.text.lower() == "go back":
        authorization(message)
    elif message.text in list_cat and message.from_user.username in lst:
        categories = Category.objects.values()
        goods = Product.objects.values()

        inlines = telebot.types.InlineKeyboardMarkup()
        for i in range(len(categories)):
            if categories[i]['name'] == message.text:
                for e in range(len(goods)):
                    if goods[e]['category_id'] == i + 1:
                        inlines.add(telebot.types.InlineKeyboardButton(text=f"{goods[e]['name']} -"
                                                                            f" {goods[e]['price']}$",
                                                                       callback_data=f"{goods[e]['name']} - "
                                                                                     f"{goods[e]['price']}$"))
                    else:
                        continue
            else:
                continue
        fedo.send_message(message.chat.id, f"List of goods:", reply_markup=inlines)
    elif message.text.lower() == "pay" and message.from_user.username in lst:
        bill = 0
        for element in list_data:
            elem = element.split()
            bill += float(elem[-1][0:-1])
        fedo.send_message(message.chat.id, f"Prepare {round(bill, 2)}$ for paying your purchase")
    else:
        if message.from_user.username in lst:
            fedo.send_message(message.chat.id, "Nothing")
        else:
            fedo.send_message(message.chat.id, "Register,please")


def register(message):
    lst = []

    customer = Customer.objects.values()
    for el in customer:
        lst.append(el['name'])

    if message.from_user.username in lst:
        fedo.send_message(message.chat.id, f"Username - {message.from_user.username} has already registered")
    else:
        Customer.objects.get_or_create(
            name=message.from_user.username,
            password=message.text
        )
        fedo.send_message(message.chat.id, f"Registered")


def login(message):
    lst = []

    customer = Customer.objects.values()
    for el in customer:
        lst.append(el['name'])

    if message.from_user.username in lst:
        if message.text == customer[lst.index(message.from_user.username)]['password']:
            fedo.send_message(message.chat.id, f"Lo-ginned")
        else:
            fedo.send_message(message.chat.id, f"Try again,you wrote wrong password")
    else:
        fedo.send_message(message.chat.id, f"{message.from_user.username} hasn't registered yet")


fedo.polling(none_stop=True, interval=0)
