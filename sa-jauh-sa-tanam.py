import time
import os

lyrics = [
    {"text": "su jauh sa tanam hati tapi tra hasil", "speed": 99},
    {"text": "cobalah dewasa ko su bukan anak kecil", "speed": 99},
    {"text": "sa coba imbangi namun hati tra kuat", "speed": 70},
    {"text": "tersiksa makan hati dan itu sa su muak", "speed": 80},
    {"text": "nanti pasti ko mengerti", "speed": 150},
    {"text": "setelah sa hilang dan sa jauh untuk pergi", "speed": 99},
    {"text": "ko akan tau bagaimana", "speed": 90},
    {"text": "so sayang ko tapi sa rasa percuma", "speed": 80},
    {"text": "ko terus ungkit ", "speed": 60},
    {"text": "ungkit luka lama", "speed": 70},
    {"text": "yang buat sa trauma", "speed": 80},
]

delays = [1.0, 2.0, 2.7, 3.0, 4.1, 7.1, 10.2, 11.2, 12.0, 14.2, 17.0]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_lyrics():
    clear_screen()
    for i, line in enumerate(lyrics):
        text = line["text"]
        speed = line["speed"] / 1000
        delay = delays[i] if i == 0 else delays[i] - delays[i - 1]
        time.sleep(delay)
        for char in text:
            print(char, end="", flush=True)
            time.sleep(speed)
        print()

type_lyrics()
