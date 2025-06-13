# 🧰 Netkitech - Network Utility Toolkit

**Netkitech** is a simple yet powerful network utility app for Windows, built with Python and available as an executable `.exe`. It provides essential tools for checking IP and DNS settings, pinging game servers, flushing cache, and more — all in a convenient graphical interface.

---

## 🔍 Features

- **View Current IP & DNS**  
  Instantly retrieve and display your local IP address and DNS server list.

- **Ping Tools**
  - Ping Cloudflare (1.1.1.1)
  - Select and ping major game servers:
    - Blizzard
    - Overwatch
    - Call of Duty
    - Ubisoft
    - Roblox
    - NARAKA
    - HELLDIVERS 2
    - Marvel Rivals

- **Network Actions**
  - Flush IP and DNS cache
  - Reset network adapters (Windows only)
  - Export current network settings to `network_info.txt`

- **Quick Access Tools**
  - Open router configuration page
  - Run internet speed test via [Fast.com](https://fast.com/)
  - Visit [GameServerPing.com](https://gameserverping.com/)

---

## 💻 Platform Compatibility

- ✔️ Windows 10/11 (.exe supported)
- 🐍 Cross-platform source (some functions Windows-only)

---

## 🚀 Running the App

### Option 1: Use the `.exe` (No Python Needed)
Download the prebuilt `.exe` file from [Releases](#) and double-click to launch.

### Option 2: Run from Source

#### Requirements:
- Python 3.6+
- No external dependencies

#### Run:
```bash
python netkitech.py
