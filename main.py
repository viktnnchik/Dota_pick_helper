import time
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from random import choice
import webbrowser

desktop_agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
]


def open_vk(vk):
    webbrowser.open(
        "https://vk.com/gn1dor"
    )


def open_DB(hero_name):

    webbrowser.open(f"https://www.dotabuff.com/heroes/{hero_name}")


def random_headers():
    return {
        "User-Agent": choice(desktop_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }


def get_hero_stats(hero_name):
    url = f"https://www.dotabuff.com/heroes/{hero_name}"
    response = requests.get(url, headers=random_headers())
    soup = BeautifulSoup(response.content, "html.parser")

    stats_block = soup.find_all("a", class_="link-type-hero")

    if stats_block:

        half = len(stats_block) // 2
        second_half = stats_block[half:]
        text_list = [str(item.text) for item in second_half]
        result = "\n ".join(text_list)
        result_text.set(f"Лучше всего пикать: \n  \n {result}")

    else:
        result_text.set(f"Статистика для героя {hero_name} недоступна.")


def on_hero_select(event):
    # Получаем выбранный герой из списка
    selected_index = hero_listbox.curselection()
    if selected_index:
        hero_name = hero_listbox.get(selected_index[0])
        # Вводим выбранный герой в поле поиска
        entry.delete(0, tk.END)
        entry.insert(tk.END, hero_name)
        # Вызываем функцию для получения статистики героя
        get_hero_stats(hero_name)


def search_hero():
    # Получим введенное пользователем значение из текстового поля
    hero_name = entry.get()
    my_link = f"https://www.dotabuff.com/heroes/{hero_name}"
    # Вызовем функцию для получения статистики героя
    get_hero_stats(hero_name)
    open_DB(hero_name)


# Создаем графический интерфейс
font_style = ("Montserrat", 12)
window = tk.Tk()
window.title("Pick_Helper_Gn1dor43")
window.iconphoto(False, tk.PhotoImage(file="icon.ico"))
window.geometry("800x600")
# Создаем список всех героев
heroes = [
    "abaddon",
    "alchemist",
    "ancient-apparition",
    "anti-mage",
    "arc-warden",
    "axe",
    "bane",
    "batrider",
    "beastmaster",
    "bloodseeker",
    "bounty-hunter",
    "brewmaster",
    "bristleback",
    "broodmother",
    "centaur-warrunner",
    "chaos-knight",
    "chen",
    "clinkz",
    "clockwerk",
    "crystal-maiden",
    "dark-seer",
    "dark-willow",
    "dazzle",
    "death-prophet",
    "disruptor",
    "doom",
    "dragon-knight",
    "drow-ranger",
    "earth-spirit",
    "earthshaker",
    "elder-titan",
    "emberspirit",
    "enchantress",
    "enigma",
    "faceless-void",
    "grimstroke",
    "gyrocopter",
    "hoodwink",
    "huskar",
    "invoker",
    "io",
    "jakiro",
    "juggernaut",
    "keeper-of-the-light",
    "kunkka",
    "legion-commander",
    "leshrac",
    "lich",
    "lifestealer",
    "lina",
    "lion",
    "lone-druid",
    "luna",
    "lycan",
    "magnus",
    "mars",
    "medusa",
    "meepo",
    "mirana",
    "monkey-king",
    "morphling",
    "naga-siren",
    "natures-prophet",
    "necrophos",
    "night-stalker",
    "nyx-assassin",
    "ogre-magi",
    "omniknight",
    "oracle",
    "outworld-destroyer",
    "pangolier",
    "phantom-assassin",
    "phantom-lancer",
    "phoenix",
    "puck",
    "pudge",
    "pugna",
    "queen-of-pain",
    "razor",
    "riki",
    "rubick",
    "sand-king",
    "shadow-demon",
    "shadow-fiend",
    "shadow-shaman",
    "silencer",
    "skywrath-mage",
    "slardar",
    "slark",
    "snapfire",
    "sniper",
    "spectre",
    "spirit-breaker",
    "storm-spirit",
    "sven",
    "techies",
    "templar-assassin",
    "terrorblade",
    "tidehunter",
    "timbersaw",
    "tinker",
    "tiny",
    "treant-protector",
    "troll-warlord",
    "tusk",
    "underlord",
    "undying",
    "ursa",
    "vengeful-spirit",
    "venomancer",
    "viper",
    "visage",
    "void-spirit",
    "warlock",
    "weaver",
    "windranger",
    "winter-wyvern",
    "witch-doctor",
    "wraith-king",
    "zeus",
]

# Создаем список со прокруткой
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

hero_listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
hero_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

for hero in heroes:
    hero_listbox.insert(tk.END, hero)

scrollbar.config(command=hero_listbox.yview)

# Привязываем функцию on_hero_select к событию выбора элемента в списке
hero_listbox.bind("<<ListboxSelect>>", on_hero_select)

# Создаем поле ввода и кнопку для поиска
entry = tk.Entry(window)
entry.pack()
search_button = tk.Button(window, text="Поиск", command=search_hero, font=font_style)
search_button.pack()

# Создаем текстовую метку для вывода результатов


result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=font_style,fg="green", cursor="hand2")
result_label.pack()

button = tk.Button(window, text="Мой вк", command=open_vk, font=font_style,fg="green", cursor="hand2")
button.pack()
button = tk.Button(window, text="Открыть дб героя", command=open_DB, font=font_style,fg="red", cursor="hand2")
button.pack()

window.mainloop()
