import requests
from enum import Enum
import time

# ワンピ公式のカードリストのURL
# これの後ろに番号を付け足すことでpng画像にアクセスできる。
base_url = "https://www.onepiece-cardgame.com/images/cardlist/card/"

class CardSeries(Enum):
    OP01 = ("OP01", 121)
    OP02 = ("OP02", 121)
    OP03 = ("OP03", 123)
    ST01 = ("ST01", 17)
    ST02 = ("ST02", 17)
    ST03 = ("ST03", 17)
    ST04 = ("ST04", 17)
    ST05 = ("ST05", 17)
    ST06 = ("ST06", 17)
    ST07 = ("ST07", 17)
    ST08 = ("ST08", 15)
    ST09 = ("ST09", 15)
    P = ("P", 37)
    def __init__(self, series_str, max_number):
        self.series_str = series_str
        self.max_number = max_number

def save_card_img(series: CardSeries):
    for i in range(series.max_number):
        # 3桁になるように0埋め
        number = str(i + 1).zfill(3)
        print(base_url + series.series_str + "-" + number)
        file_name = series.series_str + "-" + number + ".png"
        response = requests.get(base_url + file_name)
        if response.status_code == 200:
            with open("./images/cards/" + file_name, "wb") as f:
                f.write(response.content)
            print("保存しました")
        else:
            print("エラーが発生しました:", response.status_code)
        time.sleep(0.5)

for series in CardSeries.__members__.values():
    save_card_img(series=series)