from xml.etree import ElementTree
import urllib.request

urllib.request.urlretrieve("https://www.cbr.ru/scripts/XML_daily.asp", "cbrf.xml")

root = ElementTree.parse("cbrf.xml").getroot()

for child in root:
    if(child[1].text=="USD"):
      usd_curr = float(child[4].text.replace(',','.'))

print("Текущий курс", usd_curr)
while True:
    Perev = input("Что куда переводить? 1 -- рубли в доллары, 2 -- доллары в рубли: ")
    if (Perev == '1'):
        sum1 = input("сколько рублей?: ")
        result = float(sum1) / usd_curr;
        print(round(result,2), "долларов")
        break
    elif (Perev == '2'):
        sum1 = input("сколько долларов?: ")
        result = float(sum1) * usd_curr;
        print(round(result,2), "рублей")
        break
    else:
        print("?????????")