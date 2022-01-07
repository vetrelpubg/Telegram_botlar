import requests
from bs4 import BeautifulSoup as BS
from buttons import viloyatlar_knopkasi

def start(update, context):
    user=update.message.from_user
    update.message.reply_html("assalomu alaykum. <b>{}</b>.Hududni tanlang: ".format(user.first_name),reply_markup=viloyatlar_knopkasi)
    return 1

def toshkent(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Toshkent shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),

def sirdaryo(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Sirdaryo shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),





def jizzax(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Samarqand shahrida bugungi ob-havo\nEng past temeratura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),

def samarqand(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Toshkent shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),



def fargona(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Fargona shahrida bugungi ob-havo\nEng past temeratura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def namangan(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Namangan shahrida bugungi ob-havo\nEng past temeratura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def andijon(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Andijon shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def qashqadaryo(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Qashqadaryo shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def surxondaryo(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Surxondaryo shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def buxoro(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Buxoro shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def xorazm(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Xorazm shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def qoraqalpoq(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Qoraqalpoq shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


def navoiy(update,context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html=BS(r.content, 'html.parser')
    minimum = html.findAll("div",{"class":"min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min=minimum[0].text
    t_max=maximum[0].text

    update.message.reply_text(f"Navoiy shahrida bugungi ob-havo\nEng past temperatura: {t_min}\nEng baland temperatura: {t_max}, reply_markup=viloyatlar_knopkasi"),


