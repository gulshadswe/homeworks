#H-1
yosh = int(input('jasinizdi kiritin: '))

if yosh >= 18:
    print("Siz erjetkensiz!")
else:
    print("Siz ele erjetpegensiz!")

#H-2
parol = input('Paroldi kiritin: ')

if parol == "python123":
    print("xosh kelipsiz!")
else:
    print("Parol naduris!")

#H-3
cena = int(input("tovar cenasin kirgizin: "))

if cena > 500000:
    shegirme = int(cena * 0.10)
else:
    shegirme = 0

obshiy_cena = cena - shegirme
print(f"shegirme: {shegirme} sum")
print(f"hammesi : {obshiy_cena} sum")

#H-4
araliq = int(input("Aralıqtı kirgiziń: "))

if araliq > 10:
    km_bahasi = 3000
else:
    km_bahasi = 2000

uliwma_bahasi = araliq * km_bahasi
print(f"1 km bahası: {km_bahasi} sum.")
print(f"Ulıwma bahası: {uliwma_bahasi} sum.")

#H-5
bahasi = int(input("Buyırtpa bahası: "))

if bahasi > 100000:
    print("Jetkiziw biypul!")
else:
    jetkiziw = 15000
    jami = bahasi + jetkiziw
    print(f"Jetkerip beriw: {jetkiziw} sum.")
    print(f"Jámi tólem: {jami} sum.")

#H-6
ball = int(input("Balinizdi kiritin: "))

if 90 <= ball <= 100:
    baha = "zor"
elif 75 <= ball <= 89:
    baha = "jaqsi"
elif 60 <= ball <= 74:
    baha = "qanigarli"
elif 0 <= ball <= 59:
    baha = "qanigarsiz"
else:
    baha = "naduris bal"

print(f"sizdin bahaniz: {baha}")

#H-7
transportlar = ["Avtobus", "Metro", "Taksi", "Velosiped"]
cenasi = [2000, 1700, 15000, 1000]

print("===== TRANSPORT TANLAW =====")
for i, t in enumerate(transportlar, start=1):
    print(f"{i}. {t}")

tanlaw = int(input("\nTransportni tanlan: "))

if 1 <= tanlaw<= len(transportlar):
    idx = tanlaw - 1
    print(f"\nsiz {transportlar[idx]} transportin tanladiniz.")
    print(f"cenasi: {cenasi[idx]} sum")
else:
    print("\nnaduris nomer!")

#H-8
miyweler = ["alma", "banan", "juzim", "anar", "shabdali"]
miywe = input("miywe atin kirgizin: ")

if miywe in miyweler:
    print(f"{miywe} bul bar!")
else:
    print(f"{miywe} bul joq!")

#H-19
oqiwshilar = ["Ali", "Vali", "Sardor", "Malika", "Madina"]
ism = input("atin kiritin: ")

if ism in oqiwshilar:
    print("bul oqiwshi bar!")
    print(f"birinshi harip: {ism[0]}")
else:
    print("bul oqiwshi tabilmadi.")

#H-10
numbers = [12, 5, 8, 17, 20, 3, 10, 7]

for san in numbers:
    if san % 2 == 0:
        print(f"{san} - jup san")
    else:
        print(f"{san} - Taq san")

#H-11
numbers = [2, 5, 8, 11, 14, 17]

for i in range(len(numbers)):
    if numbers[i] < 10:
        numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5

print("Ózgertilgen list:", numbers)


#H-12
products = ["Gosh", "Nan", "Sut", "mayek", "gurish"]
prices = [90000, 4000, 12000, 1800, 15000]

print("tovarlar:")
for i in range(len(products)):
    print(f"{i + 1}. {products[i]} - {prices[i]} sum")

tanlaw = int(input("\nQaysi tovar kerek? "))
idx = tanlaw - 1

if 0 <= idx < len(products):
    tovar = products[idx]
    cena = prices[idx]
    sani = int(input(f"{tovar} qansha kerek? "))
    obshiy = cena * sani

    print(f"\ntovar: {tovar}")
    print(f"sani: {sani}")
    print(f"obshiy summa: {obshiy} sum")
else:
    print("Bunday nomerli tovar joq!")

#H-13
products = ["Nan", "Sut", "Gosh", "alma", "Banan"]
prices = [4000, 12000, 90000, 8000, 15000]

izlew = input("Qanday tovar almaqshisiz? ")
tawildi = False

for i in range(len(products)):
    if products[i].lower() == izlew.lower():
        tawildi = True
        sani = int(input(f"{products[i]} qansha kerek? "))
        obshiy = prices[i] * sani
        print(f"\nobshiy summa: {obshiy} sum")
        break

if not tawildi:
    print("\nBunday tovar joq!")


#H-14
grades = [
    [5, 4, 3],
    [4, 5, 5],
    [3, 2, 4]
]

for i in range(len(grades)):
    for j in range(len(grades[i])):
        if grades[i][j] == 5:
            grades[i][j] = 4
        elif grades[i][j] == 2:
            grades[i][j] = 3

print(grade)


#H-15
products = [
    ["Nan", 4000, 10],
    ["Sut", 12000, 5],
    ["Gosh", 90000, 2],
    ["alma", 8000, 0]
]

for idx, item in enumerate(products, start=1):
    ati, cena, sani = item
    if soni < 5:
        status = "Az qalǵan"
    else:
        status = "Jetkilikli"

    print(f"{idx}. {ati}, Sanı: {sani}")
    print(f"Status: {status}\n")
