import random

hooks = [
    "🚀 ¿Tu Vivo V25e va lento? Mira esto...",
    "👽 El secreto de los pro-players de MX.",
    "🔥 Domina el juego con Aliienking MX VIP.",
    "🛑 Deja de perder por culpa del LAG."
]

hashtags = "#AliienkingMX #GamerMX #VivoV25e #SinLag #FreeFireMX #WarzoneMobile #GamingTips"

def generar_descripcion():
    gancho = random.choice(hooks)
    link = "🔗 LINK EN MI PERFIL"
    return f"{gancho}\n\n{link}\n\n{hashtags}"

if __name__ == "__main__":
    print("\n\033[1;32m--- DESCRIPCIÓN PARA TIKTOK GENERADA POR ALIIENKING MX ---")
    print("\033[1;37m" + generar_descripcion() + "\033[0m")
