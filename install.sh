#!/data/data/com.termux/files/usr/bin/bash
clear
echo -e "\033[1;32m👽 INSTALADOR OFICIAL ALIIENKING MX VIP 👽\033[0m"
echo -e "\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
echo -e "\033[1;33m[*] Configurando entorno en tu dispositivo...\033[0m"
sleep 2

# Instalar dependencias necesarias
pkg update && pkg upgrade -y
pkg install python ffmpeg termux-api -y

# Descargar la Suite Aliienking MX desde tu GitHub
mkdir -p $HOME/ALIIENKING_MX
curl -L https://raw.githubusercontent.com/Aliienkingmx/Aliienking_MX_VIP/main/apps/aliienking.py -o $HOME/ALIIENKING_MX/aliienking.py
curl -L https://raw.githubusercontent.com/Aliienkingmx/Aliienking_MX_VIP/main/apps/inyector.py -o $HOME/ALIIENKING_MX/inyector.py
curl -L https://raw.githubusercontent.com/Aliienkingmx/Aliienking_MX_VIP/main/apps/sensi_pro.py -o $HOME/ALIIENKING_MX/sensi_pro.py
curl -L https://raw.githubusercontent.com/Aliienkingmx/Aliienking_MX_VIP/main/apps/limpiador.py -o $HOME/ALIIENKING_MX/limpiador.py

echo -e "\n\033[1;32m[✓] INSTALACIÓN COMPLETADA EXITOSAMENTE.\033[0m"
echo -e "\033[1;33mPara iniciar el sistema VIP, escribe:\033[0m"
echo -e "\033[1;36mpython $HOME/ALIIENKING_MX/aliienking.py\033[0m"
