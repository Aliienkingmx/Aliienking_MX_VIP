#!/system/bin/sh
# ALIIENKING MX - FAST OPTIMIZER (BREVENT/ADB/SHIZUKU)
echo "👽 ALIIENKING MX - INYECTANDO POTENCIA..."
setprop debug.gr.num_frames 3
setprop debug.hwui.renderer skia
setprop net.dns1 8.8.8.8
setprop net.dns2 8.8.4.4
setprop persist.sys.ui.hw true
settings put system pointer_speed 7
settings put secure long_press_timeout 250
setprop debug.sf.disable_backpressure 1
am kill-all
sync
echo "✅ OPTIMIZACIÓN COMPLETADA EXITOSAMENTE."
