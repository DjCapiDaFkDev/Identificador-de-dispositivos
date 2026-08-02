print("=== Detector de teléfono pc y tablet XD ===")

ram = input("¿Cuánta RAM tiene tu teléfono? (o pc o tablet) (GB): ").lower().replace("gb", "").strip()
almacenamiento = input("¿Cuánto almacenamiento tiene? (o pc o tablet) (GB): ").lower().replace("gb", "").strip()

ram = int(ram)
almacenamiento = int(almacenamiento)

if ram < 4 or almacenamiento < 64:
    print("\n📱 Resultado: Tu dispositivo es una cagada 🥀")
elif ram < 6:
    print("\n📱 Resultado: Aguanta, pero ya le cuesta respirar 😭")
elif ram < 8:
    print("\n📱 Resultado: Está decente 👍")
else:
    print("📱 Tremenda máquina 🤑")
    print("\nCreado por el A04e User (DJ Capi da FK o el follafurras de tamaulipas)")