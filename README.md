# Raspberry Space Lab

Estación experimental con Raspberry Pi orientada a datos espaciales, SDR, ADS-B, señales satelitales, telemetría y observabilidad.

## Objetivo

Construir de forma progresiva una estación capaz de obtener, procesar, almacenar y visualizar datos espaciales y señales de radio.

Mientras se prepara la integración de hardware RTL-SDR, el proyecto utiliza APIs, datasets y observaciones públicas reales para comenzar a trabajar con información satelital.

Actualmente se integró NASA DSCOVR / EPIC mediante Python y se incorporó una primera observación de NOAA 19 obtenida desde SatNOGS.

Posteriormente se añadirá recepción directa mediante RTL-SDR, comenzando con tráfico aéreo ADS-B en 1090 MHz y avanzando hacia señales satelitales, telemetría, automatización y observabilidad.

## Tecnologías

- Raspberry Pi
- Linux
- SSH
- Python
- APIs REST
- JSON
- NASA DSCOVR / EPIC
- SatNOGS
- RTL-SDR
- ADS-B
- Docker
- Telemetría
- Dashboards
- Observabilidad

## Arquitectura actual

```text
NASA DSCOVR / EPIC ──┐
                     │
SatNOGS / NOAA 19 ───┼──> Raspberry Space Lab
                     │          │
                     │          ├── Python
                     │          ├── JSON
                     │          ├── Imágenes
                     │          └── Análisis de señales
                     │
                     └──> Fuentes públicas reales

Próximamente:

RTL-SDR
   │
   └──> Raspberry Pi
           │
           ├── ADS-B
           └── Señales satelitales

Estado
Proyecto en desarrollo.
La Raspberry Pi se encuentra preparada para administración remota mediante SSH y cuenta con almacenamiento USB adicional para futuras capturas, datasets y servicios.
Actualmente se desarrolló una aplicación inicial en Python capaz de consultar la API de NASA DSCOVR / EPIC, obtener información de las imágenes disponibles y descargar imágenes bajo demanda.
También se incorporó una observación pública de NOAA 19 para comenzar a trabajar con señales satelitales reales antes de disponer del hardware RTL-SDR.
La muestra incluye:
- Waterfall de la señal.
- Datos demodulados.
- Transmisión APT en 137.100 MHz.
- Observación obtenida desde la red SatNOGS.
Las imágenes descargadas desde NASA se almacenan localmente en data/epic/ y están excluidas del repositorio para evitar acumular archivos innecesarios.
Estructura
raspberry-space-lab/
├── src/
│   └── space_viewer.py
├── data/
│   ├── epic/
│   └── raw/
│       └── noaa19-9505836/
│           ├── waterfall.png
│           └── demoddata.png
├── docs/
│   └── setup.md
├── images/
├── configs/
├── README.md
└── .gitignore

Roadmap
- Preparación de la Raspberry Pi ✅
- Almacenamiento externo ✅
- Acceso remoto mediante SSH ✅
- Consulta de datos espaciales mediante APIs ✅
- Integración inicial con NASA DSCOVR / EPIC ✅
- Primera observación NOAA 19 / SatNOGS ✅
- Visualización de waterfalls ✅
- Análisis de señales y datasets públicos 🚧
- Visualización y organización de imágenes espaciales
- Integración RTL-SDR
- Recepción ADS-B en 1090 MHz
- Visualización de tráfico aéreo
- Recepción de señales satelitales
- Telemetría, métricas y dashboards
- Automatización y observabilidad
Próxima etapa
Continuar desarrollando la aplicación de consulta espacial para organizar y visualizar datos obtenidos desde fuentes públicas.
Se evaluará la incorporación de nuevas fuentes de información, como imágenes solares, observaciones satelitales y otros datasets espaciales.
La recepción directa de señales se incorporará cuando esté disponible el hardware RTL-SDR.
Documentación
La configuración de la Raspberry Pi, almacenamiento, acceso remoto y las pruebas técnicas realizadas se encuentran en:
docs/
