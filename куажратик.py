# -*- coding: utf-8 -*-
"""
Charles Truscott
ЧАРЛьЗ ТРУСКОТТ


"""
import math

def main():
    гиссйс = 0
    ыпс = 0.000001
    куаж = 2000
    хи = куаж
    лу = 0
    гисс = (хи + лу) / 2.0
    while (((гисс ** 4) >= (куаж) or (гисс ** 4) <= (куаж) and (not (гисс ** 4) == (куаж)))):
        print("guess: {} high: {} low: {} numguesses: {}".format(гисс, хи, лу, гиссйс))
        if ((гисс ** 4) > куаж):
            хи = гисс
        elif ((гисс ** 4) < куаж):
            лу = гисс
        гиссйс += 1
        гисс = (хи + лу) / 2.0
        if (round((гисс ** 4), 4) == (куаж)):
            break
    print("The quadratic root of {} is {}. {} ** 4 = {}".format(куаж, гисс, гисс, гисс ** 4))
    print("{} ЗТО КУАДРАТЙК РУТ {}".format(куаж, гисс))
    
if __name__ == "__main__": main()