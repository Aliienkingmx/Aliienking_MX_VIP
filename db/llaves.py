import hashlib, time, os
def gen():
    os.system('clear')
    print("\033[1;32m👽 GENERADOR DE LICENCIAS - ALIIENKING MX 👽\033[0m")
    nombre = input("\033[1;33mNombre del Cliente: \033[0m")
    key = "AK-" + hashlib.md5(f"{nombre}{time.time()}".encode()).hexdigest()[:8].upper()
    with open("/data/data/com.termux/files/home/ALIIENKING_MX/db/keys.txt", "a") as f:
        f.write(f"{key}\n")
    print(f"\n✅ LLAVE CREADA: \033[1;32m{key}\033[0m")
    print(f"Dale esta llave a tu cliente para que sea un Aliienking VIP.")
gen()
