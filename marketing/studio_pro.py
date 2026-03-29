import os, sys, time

G, C, Y, R, N = '\033[1;32m', '\033[1;36m', '\033[1;33m', '\033[1;31m', '\033[0m'

def logo():
    os.system('clear')
    print(f"{G}      👽 ALIIENKING MX - STUDIO PRO v1.0 👽")
    print(f"{C}══════════════════════════════════════════════{N}")

def procesar_video(tipo):
    logo()
    input_v = "/sdcard/Download/ENTRADAMP4.mp4"
    game_v = "/sdcard/Download/GAMEPLAY_FPSMP4.mp4"
    output = "/sdcard/Download/ALIIENKING_FINAL.mp4"
    
    if not os.path.exists(input_v) or not os.path.exists(game_v):
        print(f"{R}[X] ERROR: Faltan archivos en Descargas.{N}")
        return

    print(f"{Y}[*] Iniciando Renderizado Profesional...{N}")
    
    # EFECTOS DE ALTA GAMA:
    # unsharp: Da nitidez extrema (HD)
    # eq: Mejora contraste y saturación (Color Pro)
    # minterpolate: Simula fluidez de 120 FPS
    
    if tipo == "1": # PANTALLA DIVIDIDA (TOP/BOTTOM)
        cmd = (f"ffmpeg -i {input_v} -i {game_v} -filter_complex "
               "\"[0:v]scale=1080:960:force_original_aspect_ratio=increase,crop=1080:960,trim=0:5[t]; "
               "[1:v]scale=1080:960:force_original_aspect_ratio=increase,crop=1080:960,unsharp=5:5:1.5,eq=saturation=1.6,trim=0:10[b]; "
               "[t][b]vstack=inputs=2,drawtext=text='@AliienkingMX':fontcolor=white@0.3:fontsize=30:x=W-text_w-20:y=H-40[v]\" "
               f"-map \"[v]\" -c:v libx264 -preset fast -y {output}")
    
    elif tipo == "2": # CINEMÁTICO (Juego con marca de agua y color)
        cmd = (f"ffmpeg -i {game_v} -vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920, "
               "unsharp=7:7:1.2,eq=contrast=1.2:saturation=1.7, "
               "drawtext=text='ALIIENKING MX VIP':fontcolor=lime:fontsize=80:x=(w-text_w)/2:y=300:enable='between(t,0,4)'\" "
               f"-c:v libx264 -preset fast -y {output}")

    os.system(cmd)
    dest = "/sdcard/DCIM/Camera/ALIIENKING_PRO_" + str(int(time.time())) + ".mp4"
    os.system(f"mv {output} {dest}")
    os.system(f"termux-media-scan {dest}")
    print(f"\n{G}[✓] ¡VIDEO PROFESIONAL CREADO! {N}")
    print(f"{C}Búscalo en tu galería como un archivo nuevo.{N}")

while True:
    logo()
    print(f"{G}[1]{N} Crear Video Split (Script + Juego)")
    print(f"{G}[2]{N} Crear Clip Cinemático (Solo Juego HD)")
    print(f"{R}[3] Salir{N}")
    op = input(f"\n{Y}Selecciona estilo de marketing: {N}")
    if op in ['1', '2']: procesar_video(op)
    elif op == '3': break
