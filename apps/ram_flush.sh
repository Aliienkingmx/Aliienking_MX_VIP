#!/data/data/com.termux/files/usr/bin/bash
clear
echo -e "\033[1;32m      👽 ALIIENKING MX - RAM FLUSH EXTREME 👽"
print "\033[1;36m══════════════════════════════════════════════\033[0m"

echo -e "\033[1;33m[*] Sincronizando memoria y vaciando búferes...\033[0m"
sync

echo -e "\033[1;33m[*] Solicitando liberación de caché al sistema (PM Trim)...\033[0m"
# Este comando le dice a Android que limpie cache de todas las apps
pm trim-caches 999G 2>/dev/null

echo -e "\033[1;33m[*] Deteniendo procesos 'Zombis' de usuario...\033[0m"
# Mata procesos de apps que no son del sistema pero están de fondo
am kill-all 2>/dev/null

echo -e "\033[1;33m[*] Limpiando residuos de Termux...\033[0m"
pkg clean

echo -e "\033[1;32m\n[✓] RAM LIBERADA CON ÉXITO."
echo -e "[✓] Procesador Helio G99 Despejado.\033[0m"
echo -e "\033[1;36m══════════════════════════════════════════════\033[0m"
