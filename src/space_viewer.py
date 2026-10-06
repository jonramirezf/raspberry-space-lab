import json
from urllib.request import urlopen

url = "https://epic.gsfc.nasa.gov/api/natural"

with urlopen(url) as response:
    datos = json.load(response)

ultima = datos[-1]

print("Última imagen disponible:")
print("Nombre:", ultima["image"])
print("Fecha:", ultima["date"])

print("Cantidad de imágenes:", len(datos))

from pathlib import Path
from urllib.request import urlretrieve

fecha = ultima["date"].split()[0]
anio, mes, dia = fecha.split("-")

nombre = ultima["image"]

url_imagen = (
    f"https://epic.gsfc.nasa.gov/archive/natural/"
    f"{anio}/{mes}/{dia}/jpg/{nombre}.jpg"
)

carpeta = Path("data/epic")
carpeta.mkdir(parents=True, exist_ok=True)

archivo = carpeta / f"{nombre}.jpg"

urlretrieve(url_imagen, archivo)

print("Imagen guardada en:", archivo)
