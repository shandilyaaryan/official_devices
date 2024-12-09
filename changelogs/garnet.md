 ```
Device name: Redmi note 13 Pro 5G / Poco X6 5G
Device codename: garnet
Device maintainer: Mohammad Kibria
```

# Notes:
- Clean flash recommended
- Flash Guide [here](https://github.com/Project-PixelStar/official_devices/blob/14/instructions/garnet.md)
- Dolby Atmos Included
- Miuicamera Included
- Don't report bugs with custom kernels

# v3.6-LTS - uday :
- Add thermal parts
- add per app refresh rate parts
- add clear speaker parts
- Improve cpu Governor 
- Improve runtime cpu set
- Add input boost for cpu and power key
- Adapt to xiaomi vibrator effects
- Change adreno blobs to 615.86
- Fix HDR issue 
- A lot of fixes and Improvement
- Increase system stability and smoothness 

# v3.5 - Uday - Hotfix :
- Update blobs from V816.0.17.0.UNRMIXM
- Upgrade kernel from V816.0.17.0.UNRMIXM
- Update miuicamera from V816.0.17.0.UNRMIXM
- A lot of fixes and Improvement
- Increase system stability and smoothness 

# v3.5 - Uday :
- Integrity pass default
- Based nov security patch
- Bump to version 3.5
- All sensors fixed
- Update blobs v816.0.15.0 UNRMIXM
- Upgrade stock kernel from miui_GARNETGlobal_OS1.0.15.0.UNRMIXM
- Update vendor blobs from V816.0.15.0.UNRMIXM
- Update CPU Frequency Scaling Max Values
- Fixed miuicamera recording filters
- Switch Oneplus dolby

# v3.4 - Uday :
- Integrity pass default
- Based oct security patch
- Bump to version 3.4
- PixelPropsUtils: Restore keystore safetynet attestation blocking
- PixelPropsUtils: update to latest komodo beta
- Switch to CUSTOM QTI thermal
- Added missing sepolicy thermal logs spam
- Fixed flickering in AOD (POCO DEVICES)
- Improved udfps unlock speed
- Improvements in miuicamera (redmi and poco devices)
- Fixed filters video recording miuicamera
- Fixed small micro lags in 60hz (qs)
- Fixed icon face unlock in loockscreen
- Switch Kernel to STRIX 5.10.226 clang version 19.0.0 ksu support
- Build libutils.vendor
- Allow setsockopt syscall for qcom c2audio
- Update from V816.0.12.0.UNRMIXM
- Import missing media codec blobs
- Move media codecs dolby to vendor
- Use AOSP default Codec2/OMX ranks
- Move dolby to hw/xiaomi
- Update vendor blobs from V816.0.12.0 UNRMIXM

# v3.3 - Uday
- Sep security patch
- Integrity pass default
- Add intelligent equalizer setting in dolby
- Added zram support
- Enable option for full screen aspect ratio
- Remove hw_acc effect
- Configure RefreshRate brightness thresholds
- Build oss soundtrigger hal
- Disable ELF checks for some camera libraries
- Set display idle time to 0 fixes screen flickering in low brightness
- Improved automatic brightness
- Improvements in colors, now they are more vivid
- Fix the faceunlock icon from being hidden in fod
- Improved speed and performance in games
