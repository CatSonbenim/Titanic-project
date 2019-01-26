"""Program by @CatSonbenim (Lisa Bulala) 12.05.2018"""

import pandas as pd
import re


def extract_name(full_name):
    """ Функция очищает имена от "мусора". """

    # первое слово в скобках
    lam = lambda x: x.replace(full_name[x.find('\"'):x.rfind('\"') + 1:], '') if (x.find('\"') != -1) else x
    name1 = re.search(".*\((.+)\).*", lam(full_name))
    if name1 is not None:
        return name1.group(1).split(" ")[0]
    # первое слово после титула
    name1 = re.search(".*\. ([A-Z,a-z]*)", lam(full_name))
    return name1.group(1)


data_frame = pd.read_csv('train.csv')[['Survived', 'Name', 'Sex']]
alive = data_frame[data_frame.Survived == 1]
dead = data_frame[data_frame.Survived == 0]
alive_w = alive[alive.Sex == 'female']['Name']
alive_m = alive[alive.Sex == 'male']['Name']
dead_w = dead[dead.Sex == 'female']['Name']
dead_m = dead[dead.Sex == 'male']['Name']

# получаем имя с максимальной частотой
r1 = alive_w.map(lambda full_name: extract_name(full_name)).value_counts().idxmax()
r2 = alive_m.map(lambda full_name: extract_name(full_name)).value_counts().idxmax()
r3 = dead_w.map(lambda full_name: extract_name(full_name)).value_counts().idxmax()
r4 = dead_m.map(lambda full_name: extract_name(full_name)).value_counts().idxmax()

print('\nСамые популярные имена среди выживших:\n'
      'Женское:', r1,
      '\nМужское:', r2,
      '\n\nСамые популярные имена среди погибших:\n'
      'Женское:', r3,
      '\nМужское:', r4)
