# Source Changelog #

## v3.6-LTS-Uday ##
 NOTE:
 1. With 3.6 We Are Moving To Long Term Support Till Android 16 , Android 15 Coming Soon
 2. Due My Exams There is kinda less changes than any other months 
 3. This Update Won't be visible In Updater . So, Dirty Flash From Recovery
 
 Changes: 
- Merged December Patch (credits: [Lineage OS](https://github.com/lineageos))
- Fixed Clone Apps
- Dropped Pixel Framework
- Dropped Quick Tap
- Added Enable 5G Toggle in Internet QS tiles
- Nuked Game Dashboard
- Various Optimization and under the hood changes
- Updated Wallpaper 

## v3.5-Uday ##
- Merged November Patch (credits: [Lineage OS](https://github.com/lineageos))
- Fix Selinux Permissive Visual Bug
- Fix Sensors Not Working Especially Gyroscope
- Add nano_recovery support
- Add Multiple APNs By Default
- fix for carriers using 5 bars of signal
- Use Material icons for missed calls in status bar Notifications
- Remove unnecessary videos To clean some storage
- Add Prebuilt Custom Apps
- Improve contextual dashboard messages
- Various Optimization and under the hood changes
- Updated Wallpaper 

## v3.4-Uday ##
- Merged October Patch (credits: [Lineage OS](https://github.com/lineageos))
- Add 24 hrs. option to snooze times
- Add Triluminous Display Engine
- Remove Ad-Blocker
- Add Cloudflare as default ntp server
- disable safe volume everywhere, not just the US
- Allow users to use all rotations
- Brightness Tweaks
- More notification icons on AOD screen
- Add build date to device info
- Show more than 4 items in the menus!
- Introduce contextual dashboard messages
- Various Optimization and under the hood changes
- Updated Wallpaper (credits: [NEX](https://t.me/spesmynuts))

## v3.3-Uday ##
- Merged September Patch
- Passes STRONG Integrity by default
- Locked Bootloader Spoof
- Update to P9 Spoofs
- Update Bootanimation from P9
- Add toggle to enable Monet Themed Bootanimation
- Disable some Tensor Specific Device configs
- Introduce Ad-Blocker
- Remove useless addon.d file to Avoid detection as custom ROM
- Updates and Improvements in Gamespace
- Move Blurs toggle in Display Settings
- Various Optimization and under the hood changes

## v3.2-Uday ##
- Merged August Security Patch
- Add Light/Dark Theme Bootanimation
- Nuked Screen Off Animations (Glitchy)
- Open mobile data usage from qsfooter
- Introduced Pocket Mode
- Updated Wallpaper (credits: [YoursWallpaper](https://t.me/Yourswallpapars))
- Improvements in Free-Form windows and enable it by default
- Allow Disable screenshot shutter sound 
- Update screenshot sound
- Use Groove Brightness slider (For Consistency with volumepanel)
- Inlined Weather App from Pixel 9
- Fixed issues with AndroidAuto
- Introduce Reality Display engine
- Addressed issue with gesture pill being stuck in landscape mode randomly
- Apply monet to fingerprint authentication ripple animation
- Update PIF to pass Device Integrity
- Change monet color for privacy indicators
- Make Collapsing Toolbar Scaling and Transparent
- Allow enabling Clear Calling on Unsupported device using [FLAG](https://github.com/Project-PixelStar/Flags)
- Update GMS and Mainline Module apex for August Patch
- Optimize notification fade-in/out transition
- Add dimens to set max offset of navigation bar burn-in protection
- Improve Animation when unlocking
- Improvements in StarField Design
- Adressed issues with stock recovery
- Various Optimization and Under the hood changes

## v3.0-Uday ##
- July Security Patch (QPR3 Release)
- Redesigned StarField
- Improvements and addition in Intensity Based Haptics
- Add toggle to disable haptics on Volume Button
- More Pixel Features 
- Added Quick Tap support
- Make Google System updatable
- Made Recents in Pixel Launcher Opaque/Blured (Depends on maintainer)
- Dynamic voLTE/voWIFI icons
- Redesigned FontPicker
- Add status bar battery icon for Lorns IconPack
- Update Google fonts prebuilts
- Update icon packs for QPR3
- Added some A15 features like notification snooze
- Nuked Annoying Notifications (Buggy AF)
- Allow disabling qs on secure lockscreen
- Dev toggle to ignore app wallpaper dimming requests
- Add a dev option to unlimit screenrecord filesize
- Make sensitive QS Tile secure on secure lockscreen
- More options in screen recorder qs tile
- Fix AOD and pulsing scrim color 
- Improved the design of Per App Volume
- Some Optimizations and all the previous version features are included along with the changes I forgot to mention...

## v2.5-Uday ##
- May Patch
- Fixed up some system ui crashes
- Add support for Signed builds and update FP so CTS passes (for now)
- Introeduced quick pull down
- Introduced Edge Light
- Introduced Pulse
- Add Haptics when tuning volume from rocker and per app volume panel
- Fixed crash when changing APN
- Changes in GMS
- Redesign Volume Panel
- Allowing setting ringtone for Sim2
- Fix Black Theme on QS
- Introduced Colored icons on status bar
- Introduced Notification count
- Introduced show media time
- Introduced Annoying Notifications
- Introduced Screen OFF Animations
- Introduced background process killer
- Add Notification stream in volume panel
- Misc Optimizations and under the hood changes 

## v2.0-Uday ##
- May Patch & Android 14 OPR2 Release
- Introducing Starfield 
- Moved Spoofing Options Into Starfield
- Added Clock Customization & Many More 
- Added Toggles For Enabling & Disabling Privacy Indicators
- Added Front & Icon Costomizations 
- Added Themeing setiings In starfield
- Introduced MacPaw-Fixel Font
- Want To see More, Use It & Find Yourself

## v1.3-Uday ##
- February Security patch still
- Spoof realme link
- Various changes with spoofing
- Add toggle for snapchat spoofing
- add support of the Phone Link
- fixup double tap to sleep gesture
- Redesign Settings dashboard ui
- Extend Battery info page
- Move Battery information to power usage summary
- Bring back Adaptive battery.
- apn: Update for Telus MVNO's (Canada)
- DeviceConfig: Enable Cinematic wallpaper effects

## v1.2-Uday ##
- Addressed issue related to some files systems not getting detected
- Add Illustration for dark mode page
- Enabled Circle to Search
- Ships with Gemini prebuilt
- Advanced Theming settings
- Animate the UsageProgressBarPreference
- Implement background process killer
- Rework lock gesture feature
- Hide ADB and developer setting enable status
- Extend protect sensitive info to MAC 
- add Hidden SSID preference
- add back AP Band preference into tether 
- Introduce new refresh rate selector page settings
- Move blur toggle to Display options.
- Disable blur toggle with battery saver
- Configurable 0, 90, 180 and 270 degree rotation
- Let app lock use face unlock
- Allow changing face unlock method when locked 
- Catch NPE with android.view.ViewPropertyAnimator
- Introduced Circular STD font
- Drop Toggle to disable Ripple Effects
- core: Configure SQLite to operate in MEMORY mode
- restore Android 13 "pause work profile" behavior
- Boost process priority during fork.
- KeyStore: Update local attestation spoofing
- Frameworks: Enable VoNR by default
- SystemUI: Filter out duplicate notification icons on statusbar
- LocalImageResolver: Stop the spam
- QS: Open WifiPanel on LongClick
- Settings: Add a toggle to force LTE_CA
- Settings: Move Vo5G toggle right below VoLTE
- HWUI: Use kMirror instead of kClamp
- fixup! core: Workaround for ASI crashfixup! core: Workaround for ASI crash
- PixelPropsUtils: Improve tablet spoofing
- misc Optimizations

## v1.1-Uday ##
- Merged February Patch
- bump to v1.1
- Fixed qs getting blured right after unlocking the phone
- Added Pulse Settings 
- Added Edge Lightening 
- Add newly designed Illustrations for Pulse & Edge Lightening
- Added GameSpace
- Drop Secure Tiles [Fixes Wierd glitches on some qs tiles]
- Introduce dynamic VoLTE & VoWiFi icons
- add API for disabling gestural navigation
- Export RecordingService for External Usage
- Make battery clickable again
- Introduce Immersive Navigation
- Spoof current storage encryption status
- add option to enable AOD on charging only
- Make the volume dialog expandable
- Integrate Google Lens into Screenshot UI
- Add affordance shorcut for AI Voice Assistant
- Spatializer: call postReset() instead of setting spatializer state to NOT_SUPPORTED
- Redesign seekbar
- Animate StatusBarState doze transition using DarkAnimator
- Allow to always show the time in media player
- Match the hide animation duration with show duration
- Mitigate a crash when installer is google package installer
- QS: LocationTile: make it cycle modes
- Switch notification background to monet on heads up
- Keep recent tasks for more time in memory
- Import SettingsGoogle animations from UP1A.231005.007.A1
- fixup!: Settings: Add option to launch statusbar tuner
- Add FastCharge preference into Battery settings & Extend Fastcharge implementation
- Allow editing all APNs and APN types
- Fix restore default apn dialog sometimes not dismissed.
- overlay: Increase max fling velocity

## v1.0-Uday ##
- Initial A14 update
- Follow Light Theme on QS
- Added Preferred Network QS Tile
- Add Support FOr PIF For passing CTS (Don't use prebuilt of Evox)
- Add Some Spoofing Options
- Add Network Indicator 
- Add Support for LiveDisplay & Lineage Health/Charging Controls 
- Add Pocket Mode (Does not break Deepsleep on some devices)
- Add Fonts, Icon Pack and Icon Shape Customizations
- Added Data Usage on QS
- Brightness Slider Customizations
- Show 4g icon on statusbar
- Brightness Slider Customizations
- Toggle to disable Ripple Effects
- CTS Passes by default (For Now)
- And Many More Optimizations....

