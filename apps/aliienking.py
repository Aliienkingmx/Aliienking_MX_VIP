import os, sys, time

# Paleta de Colores VIP
G, R, C, Y, P, W, N = '\033[1;32m', '\033[1;31m', '\033[1;36m', '\033[1;33m', '\033[1;35m', '\033[1;37m', '\033[0m'

def alien_logo():
    os.system('clear')
    print(f"""{G}
             ___
           / @  @ \\
          |        |
          \\  V V  /
           \\____/
      {W}ALIIENKING MX VIP
    {G}═══════════════════════{N}""")

def login():
    alien_logo()
    print(f"{Y}🔑 SISTEMA BLOQUEADO POR ALIIENKING{N}")
    key = input(f"{C}INGRESE LICENCIA: {N}").strip()
    return True if key == "ADMIN_MX" or key.startswith("AK-") else sys.exit(f"{R}ERROR: ACCESO DENEGADO{N}")

def loading_anim(txt, iterations=10):
    sys.stdout.write(f"{C}[*] {txt} ")
    for i in range(iterations):
        time.sleep(0.1)
        sys.stdout.write(f"{G}█")
        sys.stdout.flush()
    print(f" {W}[100%]{N}")

def activate_system():
    alien_logo()
    print(f"{P}⚡ INICIANDO PROTOCOLO DE DOMINACIÓN ALIEN ⚡{N}\n")
    
    # 1. Buffer de Triple Pantalla
    loading_anim("Triple Buffer Active")
    os.system("setprop debug.gr.num_frames 3")
    
    # 2. Renderizado Extremo GPU
    loading_anim("GPU Extreme Render")
    os.system("setprop debug.hwui.renderer skia")
    os.system("setprop hwui.render_dirty_regions false")
    
    # 3. Latencia de Red & Ping / DNS Fast Gaming
    loading_anim("DNS & Ping Stabilizer")
    os.system("setprop net.dns1 8.8.8.8; setprop net.dns2 8.8.4.4")
    os.system("setprop net.tcp.buffersize.wifi 524288,1048576,2097152")
    
    # 4. Forzado Bruto de Renderizado
    loading_anim("Brute Force Rendering")
    os.system("setprop persist.sys.ui.hw true")
    
    # 5. Gestión Inteligente RAM / Limpieza profunda
    loading_anim("Smart RAM Management")
    os.system("pm trim-caches 999G 2>/dev/null")
    os.system("sync")
    
    # 6. Low Latency Touch / Kernel Boost
    loading_anim("Touch Low Latency Fix")
    os.system("settings put system pointer_speed 7")
    os.system("settings put secure long_press_timeout 250")
    
    # 7. Desactivación de Dithering / Prioridad
    loading_anim("Disabling Dithering")
    os.system("setprop debug.sf.disable_backpressure 1")
    os.system("renice -n -20 -p $$")

    print(f"\n{G}══════════════════════════════════════════════")
    print("      ¡SISTEMA ALIIENKING MX ACTIVADO!       ")
    print("      DISPOSITIVO LISTO PARA EL COMBATE      ")
    print(f"══════════════════════════════════════════════{N}")
    print(f"{Y}🎮 JUEGOS SOPORTADOS:{N} FF, COD, BLOOD STRIKE, ROBLOX.")
    time.sleep(4)

def show_dashboard():
    alien_logo()
    print(f"{P}╔════════════════════════════════════════════╗")
    print(f"║ {G}[1] ACTIVAR OPTIMIZACIÓN COMPLETA         {P}║")
    print(f"║ {G}[2] SOPORTE Y SCRIPTS PERSONALIZADOS      {P}║")
    print(f"║ {G}[3] LIMPIEZA PROFUNDA DE CACHÉ            {P}║")
    print(f"║ {R}[4] SALIR DEL SISTEMA                     {P}║")
    print(f"{P}╚════════════════════════════════════════════╝")
    print(f"{C}Canal WhatsApp: https://whatsapp.com/channel/TuLink{N}")

if login():
    while True:
        show_dashboard()
        op = input(f"\n{Y}Aliienking > {N}").upper()
        if op == '1': activate_system()
        elif op == '2':
            print(f"\n{W}Manda mensaje para tu script personalizado aqui:{N}")
            print(f"{G}https://whatsapp.com/channel/TuLink{N}")
            input("\nPresiona Enter...")
        elif op == '3':
            os.system("python $HOME/ALIIENKING_MX/apps/limpiador.py")
        elif op == '4': break
