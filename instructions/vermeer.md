```
Device name: Poco F6 Pro / Redmi K70
Device codename: vermeer
Device maintainer: Lunark :3
```

- Installation Guide:
FOLLOW THE STEPS CORRECTLY!!
- Preparation:
- Flash the boot, vendor_boot, recovery using
 "fastboot flash boot boot.img
 "flasboot flash vendor_boot vendor_boot.img
 "fastboot flash recovery recovery.img"

Installation:
1. Once flashed boot, vendor_boot and recovery
2. Fastboot reboot recovery
3. abd sideload (rom-name).zip
4. Reboot, if the basic bootloader menu appears, follow step 5
5. Reboot to fastboot mode, a menu should appear where you can select fastboot or recovery (switch with the volume buttons) (select with the power button)
6. Once in recovery, change the active slot to the opposite one (from A to B or the other way around)
7. Flash rom zip again
8. If upon reboot it gets stuck in bootanimation reboot manually and that's it

# Downloads:
* ROM: [Download](https://sourceforge.net/projects/pixelstar/files/vermeer/uday)
* Images: [Download](https://sourceforge.net/projects/pixelstar/files/vermeer/uday/images)
