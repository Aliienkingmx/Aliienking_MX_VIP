#!/data/data/com.termux/files/usr/bin/bash
clear
echo -e "\033[1;32m      👽 ALIIENKING MX - CLOUD MANAGER 👽"
echo -e "\033[1;36m══════════════════════════════════════════════\033[0m"

echo -e "\033[1;33m[*] Conectando con los servidores de OpenCode...\033[0m"
# Aquí es donde vincularemos tu cuenta de Git
pkg install git -y > /dev/null 2>&1

echo -e "\033[1;36m[1] Subir actualizaciones (Push)"
echo -e "[2] Descargar cambios (Pull)"
echo -e "[3] Crear instalador para clientes"
read -p "Selecciona una opción: " opt

if [ "$opt" == "1" ]; then
    echo "Subiendo tu imperio a la nube..."
    # Comandos de Git para subir tu código
    git add . && git commit -m "Update Aliienking VIP" && git push
    echo "¡Actualización en línea!"
fi
