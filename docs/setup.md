# Configuración inicial de la Raspberry Pi

Esta fue la primera etapa del laboratorio. El objetivo fue preparar la Raspberry Pi desde cero y dejarla lista para trabajar remotamente desde el notebook.

## Instalación del sistema

Se preparó nuevamente la microSD y se instaló Raspberry Pi OS Lite.

Elegí la versión Lite porque la Raspberry se utilizará principalmente como servidor y estación de recepción, por lo que no necesitamos un entorno gráfico consumiendo recursos.

Después del primer arranque comprobamos el hardware disponible:

- Arquitectura ARM de 64 bits
- CPU de 4 núcleos
- Aproximadamente 1 GB de RAM
- Wi-Fi
- Bluetooth
- Puertos USB para almacenamiento y futuros dispositivos SDR

## Configuración del sistema

Durante la configuración inicial se ajustó la distribución del teclado y se configuró Chile como región para habilitar correctamente la interfaz Wi-Fi.

El estado de las interfaces inalámbricas se comprobó con:

`rfkill`

Wi-Fi y Bluetooth quedaron habilitados correctamente.

## Conexión a la red

La Raspberry se conectó a la red Wi-Fi local.

Después comprobamos la dirección IP asignada a la interfaz `wlan0` y dejamos habilitado SSH para administrar la Raspberry desde el ThinkPad.

SSH se activó con:

`sudo systemctl enable --now ssh`

La conexión remota fue probada correctamente desde Ubuntu:

`ssh pi@IP_RASPBERRY`

Desde este punto ya no es necesario utilizar monitor y teclado directamente en la Raspberry.

## Almacenamiento adicional

La microSD disponible tiene muy poco espacio para las futuras etapas del laboratorio.

Por este motivo se agregó un pendrive Kingston de 64 GB, formateado en `ext4`.

El almacenamiento quedó montado en:

`/mnt/datos`

Actualmente dispone de aproximadamente 54 GB libres.

También se configuró `/etc/fstab` utilizando el UUID del dispositivo para que el almacenamiento se monte automáticamente al iniciar la Raspberry.

La configuración fue comprobada con:

`sudo mount -a`

## Alimentación

Durante las primeras pruebas detectamos un problema de bajo voltaje.

La comprobación se realizó con:

`vcgencmd get_throttled`

Resultado actual:

`throttled=0x50005`

La Raspberry puede seguir utilizándose para pruebas, pero antes de conectar dispositivos que consuman más energía, como el RTL-SDR, será necesario mejorar la fuente de alimentación.

## Estado actual

La Raspberry ya cuenta con:

- Raspberry Pi OS Lite instalado
- Wi-Fi funcionando
- Bluetooth funcionando
- SSH habilitado
- Acceso remoto desde el ThinkPad
- 64 GB de almacenamiento USB
- Montaje automático del almacenamiento

## Próxima etapa

El siguiente objetivo será preparar el entorno para comenzar a trabajar con SDR y recepción ADS-B, y posteriormente incorporar Docker y observabilidad.
