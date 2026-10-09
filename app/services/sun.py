import json
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import urlopen

API_URL = "https://api.helioviewer.org/v1/getClosestImage/"
SCREENSHOT_URL = "https://api.helioviewer.org/v1/takeScreenshot/"


def get_latest_sun():
    ahora = datetime.now(timezone.utc)

    params = {
        "date": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sourceId": 11,
    }

    url = f"{API_URL}?{urlencode(params)}"

    with urlopen(url, timeout=10) as response:
        datos = json.load(response)

    fecha = datos["date"].replace(" ", "T") + "Z"

    image_params = {
        "date": fecha,
        "imageScale": 4,
        "layers": "[SDO,AIA,AIA,193,1,100]",
        "events": "",
        "eventLabels": "false",
        "x0": 0,
        "y0": 0,
        "width": 700,
        "height": 700,
        "display": "true",
        "watermark": "true",
    }

    image_url = f"{SCREENSHOT_URL}?{urlencode(image_params)}"

    return {
        "date": datos["date"],
        "source": "SDO / AIA 193 Å",
        "image_id": datos["id"],
        "image_url": image_url,
    }
