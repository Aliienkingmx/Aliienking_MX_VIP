import os, time, sys

G, R, C, Y, N = '\033[1;32m', '\033[1;31m', '\033[1;36m', '\033[1;33m', '\033[0m'

def logo():
    os.system('clear')
    print(f"{G}      👽 ALIIENKING MX - DEEP CLEANER 👽")
    print(f"{C}══════════════════════════════════════════════{N}")

def limpiar():
    logo()
    rutas_basura = [
        "/sdcard/DCIM/.thumbnails",
        "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Links",
        "/sdcard/Android/data/com.android.providers.media/cache",
        "/data/data/com.termux/files/home/.cache"
    ]
    
    extensiones = ["*.tmp", "*.log", "*.bak", "tempfile_*"]
    
    print(f"{Y}[*] Iniciando escaneo de residuos...{N}")
    time.sleep(1)
    
    # 1. Borrar carpetas de miniaturas y caché
    for ruta in rutas_basura:
        if os.path.exists(ruta):
            print(f"{C}[-] Limpiando: {ruta}{N}")
            os.system(f"rm -rf {ruta}/* 2>/dev/null")
    
    # 2. Borrar archivos por extensión
    for ext in extensiones:
        print(f"{C}[-] Eliminando archivos {ext}...{N}")
        os.system(f"find /sdcard -name '{ext}' -delete 2>/dev/null")
    
    # 3. Limpiar paquetes de Termux
    os.system("pkg clean && sync")
    
    print(f"\n{G}══════════════════════════════════════════════")
    print("      ¡SISTEMA ALIIENKING MX OPTIMIZADO!     ")
    print(f"══════════════════════════════════════════════{N}")
    print(f"{Y}El dispositivo debería sentirse más fluido ahora.{N}")

if __name__ == "__main__":
    limpiar()
