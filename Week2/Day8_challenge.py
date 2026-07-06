account_code = []
final_code = set()

while True:
    input_code = input("Enter the account code (8 digits): ")

    if input_code == "":
        break

    code = input_code.strip()

    if len(code) != 8 or not code.isdigit():
        print("Code must be exactly 8 digits.")
        continue

    account_code.append(code)
    final_code.add(code)

if len(final_code) == 0:
    print("hich kode motabari sabt nashod")
    exit()

print(f"Total valid codes: {len(account_code)}")
print(f"Total unique codes: {len(final_code)}")
print(f"Duplicate codes: {len(account_code) - len(final_code)}")

print("\nUnique account codes:")
for code in sorted(final_code):
    print(code)