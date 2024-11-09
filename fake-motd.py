import socket
import json

# MOTD and kick message configuration
motd = {
    "version": {
        "name": "1.20.1",
        "protocol": 763
    },
    "players": {
        "max": -1,
        "online": 0,
        "sample": []
    },
    "description": {
        "text": "§6Westonia.net §b§l▶§r §5§lWe are in maintenance mode\n§7We will be back soon! §4§l<3"
    }
}

def encode_var_int(value):
    """Encodes a value as a VarInt (as per Minecraft protocol)"""
    data = bytearray()
    while True:
        temp = value & 0x7F
        value >>= 7
        if value != 0:
            temp |= 0x80
        data.append(temp)
        if value == 0:
            break
    return bytes(data)

def send_packet(conn, packet_id, data):
    """Sends a packet with a VarInt length prefix and the specified content."""
    length = encode_var_int(len(data) + 1)  # +1 for the Packet ID
    conn.sendall(length + bytes([packet_id]) + data)

def create_motd_packet():
    json_motd = json.dumps(motd).encode('utf-8')
    json_length = encode_var_int(len(json_motd))
    packet_data = json_length + json_motd
    print("[DEBUG] MOTD JSON:", json_motd)
    return packet_data

def create_pong_packet(ping_payload):
    """Create a pong response with the same payload as received in the ping packet."""
    print("[DEBUG] Creating Pong Packet with payload:", ping_payload)
    return ping_payload  # Echoes back the ping packet's payload as per protocol

def read_var_int(conn):
    """Reads a VarInt from the connection as per Minecraft protocol."""
    num_read = 0
    result = 0
    while True:
        byte = conn.recv(1)
        if not byte:
            raise IOError("Connection closed before VarInt could be read.")
        byte = ord(byte)
        result |= (byte & 0x7F) << (7 * num_read)
        num_read += 1
        if num_read > 5:
            raise ValueError("VarInt is too big")
        if (byte & 0x80) == 0:
            break
    return result

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 25565))
    s.listen()
    print("MOTD Simulator is running on port 25565...")

    while True:
        conn, addr = s.accept()
        with conn:
            print('[DEBUG] Connection from', addr)

            # Read the handshake packet and validate the data
            try:
                packet_length = read_var_int(conn)  # Read packet length
                packet_data = conn.recv(packet_length)  # Read packet data

                if packet_data[0] != 0x00:
                    print("[ERROR] Unexpected packet ID in handshake")
                    conn.close()
                    continue

                # Validate handshake - Check if it's a status request (last byte should be 0x01)
                if packet_data[-1] != 0x01:
                    print("[ERROR] Invalid handshake packet or request type.")
                    conn.close()
                    continue
                print("[DEBUG] Valid Handshake Packet Received")
            except Exception as e:
                print("[ERROR] Error in handshake processing:", e)
                conn.close()
                continue

            # Respond to the status request with the MOTD
            try:
                motd_packet = create_motd_packet()
                send_packet(conn, 0x00, motd_packet)
                print("[DEBUG] MOTD Packet sent")
            except Exception as e:
                print("[ERROR] Error sending MOTD Packet:", e)
                conn.close()
                continue

            # Read the ping request and send a pong response
            try:
                packet_length = read_var_int(conn)  # Length of ping packet
                ping_data = conn.recv(packet_length)  # Ping data contains payload to echo back
                print("[DEBUG] Ping Packet Received:", ping_data)

                pong_packet = create_pong_packet(ping_data)
                send_packet(conn, 0x01, pong_packet)  # Send pong response with the same payload
                print("[DEBUG] Pong Packet sent")
            except Exception as e:
                print("[ERROR] Error processing ping request:", e)

            conn.close()
            print("[DEBUG] Connection closed")
