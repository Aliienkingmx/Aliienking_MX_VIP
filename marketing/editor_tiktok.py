import os, time

def logo():
    os.system('clear')
    print("\033[1;32m      👽 ALIIENKING MX - VIDEO ENGINE 👽")
    print("\033[1;36m══════════════════════════════════════════════\033[0m")

def procesar():
    logo()
    # Ruta exacta de tu captura de pantalla
    input_v = "/sdcard/Download/ENTRADAMP4.mp4"
    output_v = "/sdcard/Download/ALIIENKING_PROMO.mp4"
    
    if os.path.exists(input_v):
        print("\033[1;32m[✓] ARCHIVO 'ENTRADAMP4.mp4' DETECTADO.\033[0m")
        print("\033[1;36m[*] Renderizando efectos Aliienking VIP...")
        
        # Comando para formato TikTok (9:16) + Texto Neón + Marca de Agua
        comando = (
            f"ffmpeg -i {input_v} -vf \"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920, "
            f"hue=h=120:s=1.5, "
            f"drawtext=text='ALIIENKING MX VIP':fontcolor=lime:fontsize=70:x=(w-text_w)/2:y=300:shadowcolor=black:shadowx=5:shadowy=5, "
            f"drawtext=text='ELIMINA EL LAG':fontcolor=white:fontsize=45:x=(w-text_w)/2:y=420\" "
            f"-c:v libx264 -preset ultrafast -y {output_v}"
        )
        
        os.system(comando)
        print(f"\n\033[1;32m✅ ¡VIDEO EDITADO EXITOSAMENTE! \033[0m")
        print(f"\033[1;37mBúscalo en tu galería como: ALIIENKING_PROMO.mp4\033[0m")
    else:
        print("\033[1;31m❌ ERROR: No se encontró el archivo 'ENTRADAMP4.mp4'.\033[0m")
        print(f"\033[1;33mVerifica que el video esté realmente en la carpeta Download.\033[0m")

if __name__ == "__main__":
    procesar()
