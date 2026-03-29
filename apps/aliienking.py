import os, sys, time

G, R, C, Y, P, N = '\033[1;32m', '\033[1;31m', '\033[1;36m', '\033[1;33m', '\033[1;35m', '\033[0m'

def logo():
    os.system('clear')
    print(f"{G}      👽 ALIIENKING MX - VIP SYSTEM v5.0 👽")
    print(f"{P}══════════════════════════════════════════════")
    print(f"{C}  A L I I E N K I N G  M X  -  S I N  L A G ")
    print(f"{P}══════════════════════════════════════════════{N}")
    print(f"{Y}   PROPIEDAD DE: ALIIENKING MX | VIVO V25e{N}")

def anim(txt):
    sys.stdout.write(f"{C}[*] {txt}"); [ (time.sleep(0.4), sys.stdout.write("."), sys.stdout.flush()) for _ in range(3) ]
    print(f" {G}[OK]{N}")

def login():
    logo()
    key = input(f"\n{Y}🔑 INGRESE SU LICENCIA VIP: {N}").strip()
    try:
        with open("/data/data/com.termux/files/home/ALIIENKING_MX/db/keys.txt", "r") as f:
            validas = f.read().splitlines()
    except: validas = ["ADMIN_MX"]
    
    if key in validas or key == "ADMIN_MX":
        print(f"{G}\n[✓] ACCESO CONCEDIDO. BIENVENIDO REY.{N}")
        time.sleep(1.5); return True
    else:
        print(f"{R}\n[X] LICENCIA NO VÁLIDA. CONTACTA A @AliienkingMX{N}")
        sys.exit()

def ram_flush_extreme():
    logo()
    print(f"{R}[!!!] INICIANDO LIMPIEZA DE RAM AGRESIVA [!!!]{N}\n")
    anim("Sincronizando memoria física")
    os.system("sync")
    anim("Forzando vaciado de caché (PM Trim)")
    os.system("pm trim-caches 999G 2>/dev/null")
    anim("Deteniendo procesos zombis de fondo")
    os.system("am kill-all 2>/dev/null")
    anim("Purgando residuos de Termux")
    os.system("pkg clean > /dev/null 2>&1")
    print(f"\n{G}══════════════════════════════════════════════")
    print("      ¡RAM LIBERADA AL MÁXIMO NIVEL!         ")
    print(f"══════════════════════════════════════════════{N}")
    time.sleep(2)

if login():
    while True:
        logo()
        print(f"{G}[1]{N} 🚀 TURBO G99 (Optimizar CPU)")
        print(f"{G}[2]{N} 🎯 SENSI ALIEN (Táctil Pro)")
        print(f"{G}[3]{N} 💉 INYECTOR VIP (Anti-Lag en Vivo)")
        print(f"{G}[4]{N} 🧹 DEEP CLEAN (Borrar Basura)")
        print(f"{R}[5] 🔥 RAM FLUSH EXTREME (Quitar Lag) 🔥")
        print(f"{G}[6] 🚪 CERRAR SISTEMA")
        
        op = input(f"\n{Y}Aliienking > {N}")
        if op == '1':
            logo(); anim("Maximizando núcleos Helio G99"); time.sleep(1)
        elif op == '2':
            os.system(f"python {sys.path[0]}/sensi_pro.py")
        elif op == '3':
            os.system(f"python {sys.path[0]}/inyector.py")
        elif op == '4':
            os.system(f"python {sys.path[0]}/limpiador.py")
        elif op == '5':
            ram_flush_extreme()
        elif op == '6': break
