<p align="center">
  <img src="https://raw.githubusercontent.com/Project-PixelStar/manifest/14-qpr3/Banner.png" />
</p>

# Official Devices

This is our repo where all stuff related to official devices is stored.

You also need to use this to apply for official maintainership for your device.

## Folder Structure

Follow below folder structure before adding/modifying any data.

| Directory       | Notes                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| `/changelogs`   | Device changelog goes here. See [`/changelogs/README.md`](./changelogs/README.md) for more details.   |
| `/devices`      | Device information goes here. See [`/devices/README.md`](./devices/README.md) for more details.       |
| `/instructions` | Flashing instructions for device.                                                                     |
| `/images`       | Device images go here, in **PNG** format. Filename must be the device codename e.g., `beryllium.png`. |

## `devices.json` Structure

This file should contain every device supported by **Pixelstar** in the given format:

```json
{
  "devices": [
    {
      "codename": "beryllium",
      "codename_alt": "beryllium",
      "vendor": "Xiaomi",
      "model": "Xiaomi Pocophone F1",
      "maintainer_name": "Ninad Patil",
      "active": true
    },
    {
      "codename": "cepheus",
      "vendor": "Xiaomi",
      "model": "Xiaomi Mi 9",
      "maintainer_name": "Sven",
      "active": true
    }
  ]
}
```

> **Warning**
>
> Fields marked as required should not be empty!

| Fields            | Notes                                               | Required   |
| ----------------- | --------------------------------------------------- | ---------- |
| `codename`        | Primary codename of the device                      | `true`     |
| `codename_alt`    | Alternate codename of the device if any             | `optional` |
| `vendor`          | Device manufacturer name                            | `true`     |
| `model`           | Device name                                         | `true`     |
| `maintainer_name` | Maintainer name                                     | `true`     |
| `active`          | Whether this device is in active development or not | `true`     |

## `team.json` Structure

This file should contain every team member working on **Pixelstar** in the given format:

```json
{
  "team": [
    {
      "name": "Mudit",
      "role": "Founder & Lead Developer",
      "socials": {
        "github": "Mudit200408",
        "telegram": "Mudit1808",
        "xda": ""
      }
    }
  ]
}
```

> **Warning**
>
> Fields marked as required should not be empty!

| Fields     | Notes                     | Required   |
| ---------- | ------------------------- | ---------- |
| `name`     | Member name               | `true`     |
| `role`     | Role of the member        | `true`     |
| `github`   | Member's github username  | `true`     |
| `telegram` | Member's telegram profile | `optional` |
| `xda`      | Member's XDA profile      | `optional` |


<!--START_SECTION:devices-->
## Motorola Devices
```
Moto G60 / G40 Fusion (hanoip) supported by Vivin Varma
```

## Realme Devices
```
Realme GT NEO 3T (spartan) supported by YP
```

## Xiaomi Devices
```
POCO F6 Pro / Redmi K70 (vermeer) supported by Lunark :3(ByteWave)
Poco F6 / Redmi Turbo 3 (peridot) supported by Ramshell688
Redmi 12 5G / Poco M6 Pro 5G (sky) supported by Suvojeet Sengupta
Redmi 12 5G / Poco M6 Pro 5G (spes) supported by JASSI V
Redmi K40S/POCO F4 (munch) supported by Mudit
Redmi Note 10 Pro/Redmi Note 12 Pro 4G (sweet) supported by Goku San
Redmi Note 11E Pro/Redmi Note 11 Pro 5G/POCO X4 Pro 5G (veux) supported by REX
Redmi Note 12 Pro SE 5G / Poco X5 Pro 5G (redwood) supported by Thereache
Redmi Note 13 Pro 5G/Poco x6 5G (garnet) supported by Mohammad kibria
Xiaomi 11 Lite 5G NE / Mi 11 LE (lisa) supported by Zaid Khan
```
<!--END_SECTION:devices-->

1. [Device stability requirements](requirements.md)
2. [Maintainer requirements](maintainerreq.md)
3. To Apply Message [here](https://telegram.me/Project_PixelStar)

