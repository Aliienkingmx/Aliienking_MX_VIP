import os, sys, time

G, R, C, Y, P, W, N = '\033[1;32m', '\033[1;31m', '\033[1;36m', '\033[1;33m', '\033[1;35m', '\033[1;37m', '\033[0m'

def logo_gamer_real():
    os.system('clear')
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
                |   \ 0 /             \ 0 /     |
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
    key = input(f"{Y}🔑 KEY VIP: {N}").strip()
    return True if key == "ADMIN_MX" or key.startswith("AK-") else sys.exit(f"{R}LLAVE INVÁLIDA{N}")

if login():
    while True:
        logo_gamer_real()
        print(f"{G}[1] ACTIVAR OPTIMIZACIÓN FULL (12 MÓDULOS)")
        print(f"{G}[2] 📢 CANAL DE WHATSAPP (SCRIPTS)")
        print(f"{G}[3] RAM FLUSH (Quitar Lag)")
        print(f"{R}[4] CERRAR SISTEMA")
        op = input(f"\n{Y}Aliienking@Ultimate ~$ {N}")
        if op == '1':
            logo_gamer_real()
            print(f"{C}[*] Inyectando mods..."); time.sleep(2)
        elif op == '2':
            logo_gamer_real()
            print(f"{W}Sigue mi canal para Scripts y Módulos:{N}")
            print(f"{G}https://whatsapp.com/channel/0029VbCcFzILY6d7SA9jhL1A{N}")
            input(f"\n{Y}[ Enter para volver ]{N}")
        elif op == '3': os.system("bash $HOME/ALIIENKING_MX/apps/ram_flush.sh")
        elif op == '4': break
