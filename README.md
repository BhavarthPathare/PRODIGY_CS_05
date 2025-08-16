# PRODIGY_CS_05

🌐 Network Packet Analyzer – PRODIGY\_CS\_05
A web-based packet sniffer tool built with Flask and Scapy for PRODIGY\_CS Task 5. It captures and analyzes live network packets, displaying details such as **source & destination IPs, ports, protocol, and payload previews** in a browser-based dashboard.

---

## 🛠 Tech Stack

* Python
* Flask
* Scapy
* HTML, CSS, JavaScript

---

## 🚀 Features

* Live **network packet sniffing**
* Selectable **network interface**
* Real-time auto-refresh dashboard
* Displays:

  * Source & Destination IPs
  * Protocols
  * Source & Destination Ports
  * Payload preview
* Simple and clean UI

---

## 📂 Project Structure

```
PRODIGY_CS_05/  
│  
├── static/  
│   └── style.css         # Styling for the dashboard  
│  
├── templates/  
│   └── index.html        # Web UI for packet display  
│  
├── app.py                # Main Flask application + Scapy sniffer  
├── requirements.txt      # Required dependencies  
└── README.md             # Project description  
```

---

## ⚙️ Setup & Installation

### 1. Install Dependencies

Run inside your project folder:

```bash
pip install -r requirements.txt
```

**requirements.txt** will contain:

```
flask
scapy
```

### 2. Windows Users – Install Npcap

* Download from [Npcap Official Site](https://npcap.com/#download)
* During installation, **check "Install Npcap in WinPcap API-compatible Mode"**

### 3. Run with Admin Privileges

* **Windows:** Run VS Code as *Administrator*
* **Linux/Mac:** Run the app with `sudo`

```bash
python app.py   # Windows (Admin)
sudo python3 app.py   # Linux / Mac
```

Then open: 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**.

* Do **not** use on networks without explicit permission.
* Requires **Administrator (Windows)** or **root (Linux/Mac)** privileges.
* Intended for **learning and research** only.

---
