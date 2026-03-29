import os, time

def logo():
    os.system('clear')
    print("\033[1;32m      👽 ALIIENKING MX - FUSION ENGINE v7.2 👽")
    print("\033[1;36m══════════════════════════════════════════════\033[0m")

def generar():
    logo()
    intro = "/sdcard/Download/ENTRADAMP4.mp4"
    gameplay = "/sdcard/Download/GAMEPLAY_FPSMP4.mp4"
    output = "/sdcard/Download/ALIIENKING_TIKTOK_LIMPIO.mp4"
    
    if not os.path.exists(intro) or not os.path.exists(gameplay):
        print("\033[1;31m[X] ERROR: No encontré los archivos en Descargas.\033[0m")
        return

    print("\033[1;33m[*] Renderizando nueva versión limpia del video...")
    
    # Comando FFmpeg actualizado:
    # 1. Se eliminó el drawtext de '90 FPS STABLE'
    # 2. Se mantiene el logo al inicio y tu @ en la esquina
    comando = (
        "ffmpeg -i " + intro + " -i " + gameplay + " -filter_complex "
        "\"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,trim=0:4[v0]; "
        "[1:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,trim=0:10,hue=s=1.4[v1]; "
        "[v0][v1]concat=n=2:v=1:a=0[outv]; "
        "[outv]drawtext=text='ALIIENKING MX VIP':fontcolor=lime:fontsize=80:x=(w-text_w)/2:y=300:enable='between(t,0,4)', "
        "drawtext=text='@AliienkingMX':fontcolor=lime@0.4:fontsize=30:x=W-text_w-20:y=H-40[final]\" "
        "-map \"[final]\" -c:v libx264 -preset fast -y " + output
    )
    
    os.system(comando)
    
    # Mover a galería
    dest = "/sdcard/DCIM/Camera/ALIIENKING_TIKTOK_PRO.mp4"
    os.system("mv " + output + " " + dest)
    os.system("termux-media-scan " + dest)
    
    print("\n\033[1;32m✅ ¡VIDEO ACTUALIZADO GENERADO! \033[0m")
    print("\033[1;37mBúscalo en tu galería como: ALIIENKING_TIKTOK_PRO.mp4\033[0m")

if __name__ == "__main__":
    generar()
