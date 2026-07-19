import subprocess
import e

try:
    subprocess.run(
        ["adb", "start-server"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
except:
    pass

e.check_activation()

while True:
    e.main_menu()
    choice = input("\nSelect Option (1, 2 or 3 to Exit): ").strip()

    if choice == "1":
        e.option_adb_connect()
    elif choice == "2":
        e.option_auto_bypass()
    elif choice == "3":
        print("\n[+] Goodbye!")
        break
    else:
        print("[-] Invalid Option!")
