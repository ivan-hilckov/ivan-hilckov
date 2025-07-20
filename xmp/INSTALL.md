# XMP Preset Installation Guide for Adobe Lightroom

A comprehensive guide for installing XMP profiles as user presets in Adobe Lightroom Classic and Lightroom CC.

## Quick Start

**For most users:**

1. Open Lightroom (Develop module)
2. Go to **File > Import Develop Profiles & Presets**
3. Select your XMP files and click **Import**
4. Find presets in the Presets panel

---

## Installation Methods

### Method 1: Automatic Import (Recommended)

**Lightroom Classic CC 7.3+:**

1. Switch to **Develop** module (press `D`)
2. Navigate to **File > Import Develop Profiles & Presets**
3. Browse to your XMP files or ZIP folder
4. Select files and click **Import**
5. Restart Lightroom if presets don't appear immediately

**Lightroom CC (Desktop):**

1. Go to **File > Import Profiles & Presets**
2. Select your XMP files
3. Click **Import**
4. Presets automatically sync to mobile devices

### Method 2: Manual Installation

For advanced users or when automatic import fails:

**File Locations:**

_Windows:_

```
C:\Users\[Username]\AppData\Roaming\Adobe\CameraRaw\Settings
```

_macOS:_

```
~/Library/Application Support/Adobe/CameraRaw/Settings
```

**Installation Steps:**

1. Download and extract XMP files
2. Copy files to the appropriate Settings folder above
3. Restart Lightroom
4. Check Presets panel in Develop module

---

## Troubleshooting

### Presets Not Visible

**Check Preset Visibility:**

1. In Develop module, click **+** at top of Presets panel
2. Select **Manage Presets**
3. Ensure all preset groups are checked

**Enable Compatibility Mode:**

1. **Edit > Preferences** (Win) or **Lightroom > Preferences** (Mac)
2. Select **Presets** tab
3. Check **"Show Partially Compatible Develop Presets"**
4. Restart Lightroom

## Advanced Features

### Cross-Application Integration

XMP presets installed in Lightroom Classic automatically appear in Adobe Camera Raw within Photoshop, providing seamless workflow integration.

### Profiles vs. Presets

Some XMP files contain camera profiles rather than develop presets. These appear in:

- **Develop > Profile Browser** (not the Presets panel)
- **Basic panel > Profile section**

### Batch Installation

For large preset collections:

- Keep presets in ZIP format when possible
- Use automatic import for multiple files simultaneously
- Organize into logical folders before installation
- Consider preset management tools for extensive libraries
