# Raspberry Space Lab

Laboratorio experimental con Raspberry Pi orientado a la adquisición, procesamiento y visualización de datos espaciales y señales de radio.

El proyecto combina Linux, Python, fuentes de datos públicas y, en etapas posteriores, hardware SDR para construir progresivamente una pequeña estación de monitoreo.

## Objetivo

Desarrollar una plataforma capaz de obtener, procesar, almacenar y visualizar información relacionada con observación espacial y radiofrecuencia.

Mientras se incorpora hardware RTL-SDR, el laboratorio utiliza datos reales provenientes de fuentes públicas como NASA y SatNOGS para trabajar con APIs, imágenes satelitales y señales previamente capturadas.

## Estado actual

Actualmente el proyecto cuenta con:

- Raspberry Pi OS Lite configurado.
- Administración remota mediante SSH.
- Almacenamiento USB adicional.
- Aplicación inicial en Python para consultar NASA DSCOVR / EPIC.
- Descarga local de imágenes de la Tierra.
- Dataset real de una observación NOAA 19.
- Visualización de waterfall y datos demodulados.
- Separación entre código, documentación y datos de trabajo.

## NASA DSCOVR / EPIC

Se desarrolló `src/space_viewer.py`, una primera herramienta en Python que consulta la API pública de NASA DSCOVR / EPIC.

El programa obtiene:

- nombre de la última imagen disponible;
- fecha de la observación;
- cantidad de imágenes disponibles;
- imagen correspondiente a la observación seleccionada.

Flujo actual:

```text
NASA DSCOVR / EPIC
        │
        ▼
      API REST
        │
        ▼
       JSON
        │
        ▼
      Python
        │
        ▼
   Imagen local
```

Las imágenes descargadas se almacenan localmente en:

```text
data/epic/
```

Esta carpeta está excluida mediante `.gitignore` para evitar acumular imágenes generadas durante las consultas.

## Primera observación satelital

El repositorio también incluye una observación pública de **NOAA 19** obtenida desde SatNOGS.

Datos principales:

- Satélite: NOAA 19
- Frecuencia: 137.100 MHz
- Modo: APT
- Fuente: SatNOGS
- Observación: 9505836

Archivos conservados:

```text
data/raw/noaa19-9505836/
├── demoddata.png
└── waterfall.png
```

El waterfall permite observar la distribución de energía de la señal a través de la frecuencia y el tiempo.

Los datos demodulados permiten comenzar a estudiar el procesamiento de una transmisión satelital real antes de disponer de un receptor propio.

## Arquitectura

```text
Fuentes públicas
      │
      ├── NASA DSCOVR / EPIC
      │
      └── SatNOGS / NOAA 19
      │
      ▼
     Python
      │
      ├── JSON
      ├── Imágenes
      └── Datos de señales
      │
      ▼
Raspberry Space Lab


Próxima etapa de hardware:

RTL-SDR
   │
   ▼
Raspberry Pi
   │
   ├── ADS-B 1090 MHz
   └── Señales satelitales
```

## Estructura del repositorio

```text
raspberry-space-lab/
├── data/
│   └── raw/
│       └── noaa19-9505836/
│           ├── demoddata.png
│           └── waterfall.png
│
├── docs/
│   └── setup.md
│
├── src/
│   └── space_viewer.py
│
├── .gitignore
└── README.md
```

`data/epic/` se crea localmente durante la ejecución y no se versiona.

## Tecnologías utilizadas

- Raspberry Pi
- Raspberry Pi OS / Linux
- Python
- SSH
- Git / GitHub
- APIs REST
- JSON
- NASA DSCOVR / EPIC
- SatNOGS

### Próximas tecnologías

- RTL-SDR
- ADS-B 1090 MHz
- Recepción de señales satelitales
- Telemetría
- Dashboards
- Automatización
- Observabilidad

## Roadmap

- [x] Preparación de la Raspberry Pi
- [x] Configuración de almacenamiento externo
- [x] Administración remota mediante SSH
- [x] Consulta de datos espaciales mediante API
- [x] Integración inicial con NASA DSCOVR / EPIC
- [x] Descarga y almacenamiento local de imágenes
- [x] Incorporación de observación NOAA 19 / SatNOGS
- [x] Primera visualización de waterfall
- [ ] Ampliar análisis de imágenes y datasets espaciales
- [ ] Incorporar nuevas fuentes de observación
- [ ] Integrar RTL-SDR
- [ ] Recibir ADS-B en 1090 MHz
- [ ] Visualizar tráfico aéreo
- [ ] Recibir señales satelitales directamente
- [ ] Incorporar telemetría y métricas
- [ ] Crear dashboards
- [ ] Automatizar tareas de adquisición y monitoreo

## Documentación

La preparación inicial de la Raspberry Pi, red, SSH, almacenamiento y pruebas realizadas se encuentra documentada en:

[`docs/setup.md`](docs/setup.md)

## Próxima etapa

Continuar desarrollando la capa de adquisición de datos espaciales utilizando fuentes públicas.

El siguiente objetivo es incorporar nuevas observaciones e imágenes y mejorar su organización y visualización antes de integrar el receptor RTL-SDR.
