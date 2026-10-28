
import time
import sys
def type_lyric(line,char_delay=0.065):
     for char in line:
         print(char,end='',flush=True)
         time.sleep(char_delay)
     print()
def print_lyrics():
       lyrics=["Har sham aankhon par",
               "Tera aanchal lehraye",
               "Har raat yaadon ki",
               "Baarat le aaye",
               "Maein saans leta hoon",
               "Teri khushboo aati hai",
               "Ek mehka mehka sa ",
               "Paigham laati hai",
               "Meri dil ki dhadkan bhi",
               "Tere geet gati hai",
               "PAL PAL DIL KE PAAS...",
               "TUM REHTI HOOO"]
       delay = [1.6,1.4,1.8,2.1,2.4,1.7,2.0,2.0,1.7,1.8,2.0,2.0]
       print("\n🎵 Now playing :  - 'PAL PAL DIL KE PAAS'  - Kishore Kumar💕😊💌\n")
       time.sleep(1.5)
       for i, line in enumerate(lyrics):
            type_lyric(line)
            if i<len(delay):
               time.sleep(delay[i])
print_lyrics()
