import socket
import select
import sys

def main():
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_s.bind( ("127.0.0.1", 1245) )
    # Lista de sockets conhecidos
    while 1:
        rsocks = select.select([udp_s, sys.stdin, ], [], [])[0]
        for sock in rsocks:
            if sock == udp_s:
                # Informação recebida no socket
                b_data, addr = udp_s.recvfrom(4096)
                sys.stdout.write("%s\n" % b_data.decode("utf-8"))
            elif sock == sys.stdin:
                # Informação recebida do teclado
                str_data = sys.stdin.readline()
                udp_s.sendto(("Client 1: " + str_data).encode("utf-8"), ("127.0.0.1" ,1234))
    udp_s.close()

if __name__ == "__main__":
    main()