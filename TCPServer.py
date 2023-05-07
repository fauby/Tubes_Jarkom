from socket import *    # Mengimport modul socket
import sys              # Mengimport sys yang berguna untuk menghentikan program

serverSocket = socket(AF_INET, SOCK_STREAM)     # Membuat soket TCP dengan memanggil fungsi socket dan disimpan di variabel serverSocket

host = ''           # Memasukan string kosong kepada variabel HOST yang berarti setiap interface yang tersedia
serverPort = 8080   # Memasukan value 8080 kepaa variabel PORT sebagai port yang dipakai
serverSocket.bind((host, serverPort))   # Mengaitkan nomor port server dan host
serverSocket.listen(1)                  # Menunggu dan mendengarkan koneksi TCP dari klien yang masuk

while True:
    print('Server is ready!!!')  # Mencetak indikasi jika server sudah nyala
    connectionSocket, addr = serverSocket.accept() # Membuat soket baru diserver bernama connectionSocket yang didedikasikan untuk klien dengan cara memanggil metode accept() pada serverSocket, klien dan server menyelesaikan handshake yang membuat sekarang dapat mengirim byte satu sama lain melalui koneksi.
    try:    # Mencoba menjalankan code yang berguna untuk mencari dan mengambil file dari file system
        message = connectionSocket.recv(1024).decode()  # Memasukkan paket ke yang sudah tiba kedalam variabel message dan mengkonversikan paketnya dari byte ke tipe data yang normal
        filename = message.split()[1]                   # Memasukkan value dengan indeks ke 1 dari message yang sudah displit kedalam variabel filename 
        f = open(filename[1:])                          # Membuka dan memasukkan isi konten dari filename ke variabel f
        outputdata = f.read()                           # Membaca konten dari file f ke variabel outputdata  
        
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())               # Mengirimkan header HTTP ke soket klien
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())  

        # Mengirimkan konten yang berupa HTML atau teks ke klien yang dikonversikan ke byte terlebih dahulu dengan metode encode()
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close() # Menutup koneksi soket connectionSocket

    except IOError: # Menjalankan code jika codingan pada block try error (Jika file tidak ketemu)
        # Mengirimkan respon pesan 404 not found 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        connectionSocket.close()    # Menutup koneksi soket connectionSocket

serverSocket.close()    # Menutup koneksi soket serverSocket
sys.exit()              # Mengakhiri program dengan metode exit() 