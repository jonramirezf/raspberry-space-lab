import json
from urllib.request import urlopen


API_URL = "https://epic.gsfc.nasa.gov/api/natural"


def get_latest_earth():
    with urlopen(API_URL, timeout=10) as response:
        datos = json.load(response)

    ultima = datos[-1]

    nombre = ultima["image"]
    fecha = ultima["date"]

    fecha_solo = fecha.split()[0]
    anio, mes, dia = fecha_solo.split("-")

    image_url = (
        f"https://epic.gsfc.nasa.gov/archive/natural/"
        f"{anio}/{mes}/{dia}/jpg/{nombre}.jpg"
    )

    return {
        "name": nombre,
        "date": fecha,
        "source": "NASA DSCOVR / EPIC",
        "image_url": image_url,
    }
