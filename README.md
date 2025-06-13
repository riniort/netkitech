# 🧰 Netkitech - Network Utility Toolkit

**Netkitech** is a lightweight, GUI-based network utility app built with Python and available as an `.exe` for Windows users. It provides essential tools for checking IP and DNS, pinging major game servers, resetting adapters, and more — all in a simple graphical interface.

---

## 🔧 Features

- **View Current IP & DNS**
- **Ping Tools**
  - Cloudflare (1.1.1.1)
  - Popular game servers (Overwatch, CoD, Ubisoft, etc.)
- **Flush IP & DNS Cache**
- **Reset Network Adapters (Windows only)**
- **Export Network Info to `network_info.txt`**
- **Quick Access**
  - Router login page
  - [Fast.com](https://fast.com/) speed test
  - [GameServerPing.com](https://gameserverping.com/)

---

## 💻 Platform Support

- 🪟 Windows (with `.exe` build)
- 🐍 Cross-platform Python source (some features Windows-only)

---

## 🚀 How to Use

### Option 1: Run `.exe` (No Setup Required)

Download the `.exe` file from [Releases](#) and double-click to run.

### Option 2: Run from Python Source

#### Requirements

- Python 3.6+
- Standard libraries (no third-party modules required for default GUI)
- **Optional:**  
  To add CLI-based speed test support, install:

  ```bash
  pip install speedtest-cli
