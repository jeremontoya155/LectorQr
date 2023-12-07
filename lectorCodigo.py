import qrcode
import base64
import json

# Cargar datos desde el archivo datos.json
with open('datos.json', 'r') as file:
    datos_lista = json.load(file)

# Generar un código QR para cada conjunto de datos
for datos in datos_lista:
    # Convertir datos a formato JSON
    datos_json = json.dumps(datos)

    # Codificar datos JSON en base64
    datos_base64 = base64.b64encode(datos_json.encode()).decode('utf-8')
    datos_decodificados = base64.b64decode(datos_base64).decode()
    datos_json = json.loads(datos_decodificados)
    print(datos_json)

    # Crear un objeto QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Agregar datos al QR Code
    qr.add_data(datos_json)
    qr.make(fit=True)

    # Crear la imagen del QR Code
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen del QR Code con un nombre único (puedes ajustar esto según tus necesidades)
    qr_img.save(f"codigo_qr_{datos['Codigo de barra']}.png")
