🧰 Netkitech - Network Utility Toolkit
Netkitech is a lightweight, GUI-based Windows network troubleshooting toolkit built with Python and packaged as an .exe for portability. It offers quick access to essential network diagnostics, DNS/IP tools, and popular game server pings — perfect for gamers, IT support, and power users.

🔧 Features
🖧 View IP & DNS Info – Quickly check your local IP and DNS configuration.

📶 Ping Tools – Test latency to:

Cloudflare DNS (1.1.1.1)

Popular game servers (Overwatch, Roblox, CoD, Helldivers 2, etc.)

🌐 Network Utilities

Flush IP and DNS cache

Reset network adapters

Export full network info to a text file

🚀 Web Shortcuts

Open router admin page

Run speed test on Fast.com

Open GameServerPing.com

💻 Platform
Windows (.exe version available)

Python-based source code available for customization

📦 How to Run
Download the .exe from the Releases section (if available) and run it directly — no installation needed.

Alternatively, run with Python 3:

bash
Copy
Edit
python netkitech.py
📁 Requirements (for source run)
Python 3.x

Standard libraries only (no third-party dependencies)

🛠 Build .exe (optional)
To package the app using pyinstaller:

bash
Copy
Edit
pyinstaller --noconfirm --onefile --windowed netkitech.py
