import os, time

def logo():
    os.system('clear')
    print("\033[1;32m      👽 ALIIENKING MX - GLOBAL FUSION v10.0 👽")
    print("\033[1;36m══════════════════════════════════════════════\033[0m")

def generar():
    logo()
    # Nombres de archivos exactos proporcionados por el CEO
    intro = "/sdcard/Download/Optimizer_ultraBot_MP4.MP4"
    gameplay = "/sdcard/Download/GAMEPLAY_FPSMP4.MP4"
    output = "/sdcard/Download/ALIIENKING_AD_FINAL.mp4"
    
    if not os.path.exists(intro) or not os.path.exists(gameplay):
        print("\033[1;31m[X] ERROR: Faltan archivos en Descargas.")
        print(f"Buscando: {intro}")
        print(f"Buscando: {gameplay}\033[0m")
        return

    print("\033[1;33m[*] Fusionando Script + Comparativa de 120 FPS...")
    print("\033[1;36m[*] Aplicando filtros HDR y textos de marketing multijuego...\033[0m")
    
    # Comando Maestro FFmpeg (v10.0):
    # - Intro (4 seg): Tu software inyectando potencia.
    # - Gameplay (11 seg): Comparativa de FPS fluida.
    # - Filtros: Saturación 1.6, Nitidez Pro.
    # - Texto: Dinámico para FF, Blood Strike y COD.
    
    txt_main = "drawtext=text='ALIIENKING MX VIP':fontcolor=lime:fontsize=80:x=(w-text_w)/2:y=250:enable='between(t,0,4)'"
    txt_games = "drawtext=text='BLOOD STRIKE - FF - COD':fontcolor=white:fontsize=70:x=(w-text_w)/2:y=H/2-100:enable='between(t,4,8)'"
    txt_fps = "drawtext=text='120 FPS - ZERO LAG':fontcolor=cyan:fontsize=90:x=(w-text_w)/2:y=H/2:enable='between(t,8,12)'"
    txt_sensi = "drawtext=text='SENSI PRO + CPU TURBO':fontcolor=yellow:fontsize=75:x=(w-text_w)/2:y=H/2+100:enable='between(t,12,15)'"
    txt_link = "drawtext=text='LINK EN MI PERFIL':fontcolor=white:fontsize=75:x=(w-text_w)/2:y=H-450:enable='between(t,4,15)'"
    txt_wa = "drawtext=text='WHATSAPP PARA PERSONALIZADOS':fontcolor=lime:fontsize=45:x=(w-text_w)/2:y=H-350:enable='between(t,4,15)'"
    txt_mark = "drawtext=text='@AliienkingMX':fontcolor=lime@0.3:fontsize=35:x=W-text_w-20:y=H-40"

    comando = (
        "ffmpeg -i " + intro + " -i " + gameplay + " -filter_complex "
        "\"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=0:4[vintro]; "
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=0:11,hue=s=1.6,unsharp=5:5:1.5[vgame]; "
        "[vintro][vgame]concat=n=2:v=1:a=0[outv]; "
        "[outv]" + txt_main + "," + txt_games + "," + txt_fps + "," + txt_sensi + "," + txt_link + "," + txt_wa + "," + txt_mark + "[final]\" "
        "-map \"[final]\" -c:v libx264 -preset fast -y " + output
    )
    
    os.system(comando)
    
    # Mover a galería para comodidad del CEO
    dest = "/sdcard/DCIM/Camera/ALIIENKING_TIKTOK_MASTER.mp4"
    os.system("mv " + output + " " + dest)
    os.system("termux-media-scan " + dest)
    
    print(f"\n\033[1;32m✅ ¡VIDEO MASTER GENERADO CON ÉXITO! \033[0m")
    print(f"\033[1;37mBúscalo en tu galería como: ALIIENKING_TIKTOK_MASTER.mp4\033[0m")

if __name__ == "__main__":
    generar()
