from flask import Flask, render_template, jsonify, request
from scapy.all import sniff, get_if_list, conf, Ether, IP, TCP, UDP
import threading

app = Flask(__name__)

# Store packets
packets = []
lock = threading.Lock()
MAX_PACKETS = 500

# Active interface (string only)
current_iface = None

def get_interfaces():
    """Return list of available interfaces (name + description as strings)."""
    interfaces = []
    for iface in get_if_list():
        try:
            iface_obj = conf.ifaces[iface]
            interfaces.append({
                "name": iface_obj.name,
                "description": iface_obj.description
            })
        except Exception:
            interfaces.append({"name": iface, "description": iface})
    return interfaces


def packet_handler(pkt):
    """Process and store packet data."""
    with lock:
        if IP in pkt:
            src = pkt[IP].src
            dst = pkt[IP].dst
            proto = pkt[IP].proto
            sport = pkt[TCP].sport if TCP in pkt else (pkt[UDP].sport if UDP in pkt else "")
            dport = pkt[TCP].dport if TCP in pkt else (pkt[UDP].dport if UDP in pkt else "")
            payload = bytes(pkt[IP].payload)[:30].hex()  # first 30 bytes
        else:
            src = dst = proto = sport = dport = ""
            payload = bytes(pkt[Ether].payload)[:30].hex() if Ether in pkt else ""

        packets.append({
            "src": src,
            "dst": dst,
            "proto": str(proto),
            "sport": str(sport),
            "dport": str(dport),
            "payload": payload
        })

        if len(packets) > MAX_PACKETS:
            packets.pop(0)


def start_sniffing(iface):
    """Background packet sniffer."""
    sniff(prn=packet_handler, iface=iface, store=False)


@app.route("/")
def index():
    interfaces = get_interfaces()
    return render_template("index.html", interfaces=interfaces, current_iface=current_iface)


@app.route("/packets")
def get_packets():
    with lock:
        return jsonify(packets)


@app.route("/set_interface", methods=["POST"])
def set_interface():
    global current_iface
    data = request.get_json()
    iface = data.get("iface")
    if iface:
        current_iface = iface
        # Start background sniffing thread
        threading.Thread(target=start_sniffing, args=(iface,), daemon=True).start()
        return jsonify({"status": "ok", "iface": iface})
    return jsonify({"status": "error"})


@app.route("/clear", methods=["POST"])
def clear_packets():
    global packets
    with lock:
        packets = []
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)
