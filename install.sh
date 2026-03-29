#!/data/data/com.termux/files/usr/bin/bash
clear
echo -e "\033[1;32m      👽 ALIIENKING MX - VIP SYSTEM 👽"
echo -e "\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e "\033[1;33m[*] Instalando software de elite en tu dispositivo...\033[0m"
sleep 2

# Instalar dependencias
pkg update && pkg upgrade -y
pkg install python ffmpeg termux-api -y

# Crear carpeta y descargar los archivos reales de tu GitHub
mkdir -p $HOME/ALIIENKING_MX/apps
mkdir -p $HOME/ALIIENKING_MX/db

base_url="https://raw.githubusercontent.com/Aliienkingmx/Aliienking_MX_VIP/main"

curl -L $base_url/apps/aliienking.py -o $HOME/ALIIENKING_MX/apps/aliienking.py
curl -L $base_url/apps/inyector.py -o $HOME/ALIIENKING_MX/apps/inyector.py
curl -L $base_url/apps/sensi_pro.py -o $HOME/ALIIENKING_MX/apps/sensi_pro.py
curl -L $base_url/apps/limpiador.py -o $HOME/ALIIENKING_MX/apps/limpiador.py

echo -e "\n\033[1;32m[✓] INSTALACIÓN COMPLETADA EXITOSAMENTE.\033[0m"
echo -e "\033[1;33mPara iniciar, escribe:\033[0m"
echo -e "\033[1;36mpython \$HOME/ALIIENKING_MX/apps/aliienking.py\033[0m"
