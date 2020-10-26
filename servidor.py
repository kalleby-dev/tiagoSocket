#IMPORT DA BIBLIOTECA SOCKET
import socket

#Criacao do Socket com parametros
#AF_INET endereco de familia do endereco IPV4
#SOCK_DGRAM e o protocolo UDP e este e baseado em datagram
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(("", 12000))

print('Hello World')