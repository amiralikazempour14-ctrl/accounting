i = 0

while True:
    raw = input("Enter account code (Enter to quit): ")

    if raw == "":
        break

    code = raw.strip()

    if len(code) != 8 or not code.isdigit():
        print("Invalid account code. It must contain exactly 8 digits.")
        continue

    i += 1

    group = code[:2]
    kol = code[2:4]
    moein = code[4:6]
    tafsili = code[6:]

    print(f"Group    : {group}")
    print(f"Kol      : {kol}")
    print(f"Moein    : {moein}")
    print(f"Tafsili  : {tafsili}")

    shomare_sanad = "SND-" + str(i).zfill(4)
    print(f"Shomare sanad: {shomare_sanad}")

if i == 0:
    print("hich kode motabari sabt nashod")
else:
    print(f"Tedad kode haye motabar: {i}")