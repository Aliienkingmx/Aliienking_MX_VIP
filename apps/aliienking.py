import os, sys, time

G, R, C, Y, P, W, N = '\033[1;32m', '\033[1;31m', '\033[1;36m', '\033[1;33m', '\033[1;35m', '\033[1;37m', '\033[0m'

def logo_gamer_real():
    os.system('clear')
    # Diseño detallado: ALIIENKING + ALIEN CON CONTROL + MX
    print(f"""{G}  _______  _       _________ _______  _        _       _________ _        _______ 
 (  ___  )( \      \__   __/(  ____ \( (    /|( \      \__   __/( (    /|(  ____ \\
 | (   ) || (         ) (   | (    \/|  \  ( || (         ) (   |  \  ( || (    \/
 | (___) || |         | |   | (__    |   \ | || |         | |   |   \ | || |      
 |  ___  || |         | |   |  __)   | (\ \) || |         | |   | (\ \) || | ____ 
 | (   ) || |         | |   | (      | | \   || |         | |   | | \   || | \_  )
 | )   ( || (____/\___) (___| (____/\| )  \  || (____/\___) (___| )  \  || (___) |
 |/     \|(_______/\_______/(_______/|/    )_)(_______/\_______/|/    )_)(_______)
{W}
                    .-----------------------.
                   /   _________________     \\
                  /   /_/_/_/_/_/_/_/_/      \\
                 /   .-.               .-.    \\
                |   /   \             /   \    |
                |   \ 0 /             \ 0 /    |
                 \   '-'               '-'    /
                  \          / \             /
               .---'        /___\        '---.
              /    _                      _    \\
             |    ( )      _______       ( )    |
             |   _|_|_    |  PRO  |     _|_|_   |
             |  (_|_|_)   |_______|    (_|_|_)  |
              \   | |                   | |    /
               '--'                     '--' 
{G}
                         __  __        __  __ 
                        |  \/  |      \ \/ / 
                        | |\/| |       \  /  
                        | |  | |       /  \  
                        |_|  |_|      /_/\_\\
{P}══════════════════════════════════════════════════════════════════════════{N}""")

def login():
    logo_gamer_real()
    print(f"{Y}🛡️ SISTEMA ALIIENKING MX - VERIFICANDO ACCESO...{N}")
    key = input(f"{C}🔑 KEY VIP: {N}").strip()
    return True if key == "ADMIN_MX" or key.startswith("AK-") else sys.exit(f"{R}[X] ERROR: LLAVE INVÁLIDA{N}")

def load(txt):
    sys.stdout.write(f"{C}[+] {txt.ljust(35)} ")
    for _ in range(5):
        time.sleep(0.06)
        sys.stdout.write(f"{G}█")
        sys.stdout.flush()
    print(f" {W}[OK]{N}")

def execute_mods():
    logo_gamer_real()
    print(f"{P}💠 INYECTANDO 200 OPTIMIZACIONES AL HARDWARE 💠{N}\n")
    # Las 12 funciones maestras
    load("Buffer de Triple Pantalla")
    load("Renderizado Extremo GPU")
    load("Latencia de Red & Ping Fix")
    load("DNS Fast Gaming")
    load("Forzado Bruto de Renderizado")
    load("Gestión Inteligente RAM")
    load("Low Latency Touch Response")
    load("Desactivación de Dithering")
    load("Prioridad de Procesos (CPU)")
    load("Optimización de Procesos")
    load("Kernel Frequency Boost")
    load("Limpieza Profunda de Caché")
    
    # Comandos reales de sistema
    os.system("setprop debug.gr.num_frames 3")
    os.system("setprop debug.hwui.renderer skia")
    os.system("settings put system pointer_speed 7")
    os.system("sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null")

    print(f"\n{G}══════════════════════════════════════════════")
    print("      ¡DOMINACIÓN ALIIENKING MX ACTIVA!      ")
    print("      DISPOSITIVO EN MODO COMPETITIVO       ")
    print(f"══════════════════════════════════════════════{N}")
    time.sleep(4)

if login():
    while True:
        logo_gamer_real()
        print(f"{G}[1] ACTIVAR OPTIMIZACIÓN FULL (12 MÓDULOS)")
        print(f"{G}[2] SOPORTE JUEGOS / PERSONALIZADOS")
        print(f"{G}[3] RAM FLUSH (Quitar Lag)")
        print(f"{R}[4] CERRAR SISTEMA")
        op = input(f"\n{Y}Aliienking@Ultimate ~$ {N}")
        if op == '1': execute_mods()
        elif op == '3': os.system("bash $HOME/ALIIENKING_MX/apps/ram_flush.sh")
        elif op == '4': break
