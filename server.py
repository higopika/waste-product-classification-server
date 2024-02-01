'''
Client - sends data of object detected to server
       - sends health state to server
Server - When server recieves any of the above data, it sends back 
         current version of the weights.
         The client validate the current version with its version
         and if they are not same it requests for the weight file
'''

import socket
import os
#import train 
import csv
import time

latest_version = 1
client_status = 0 


#def train_model():
    #train.run(data='data.yaml', imgsz=320, weights='yolov5s.pt',epochs = 99)

def send_updated_weight_to_client():
    file = open("best93_8.pt","rb")
    file_size = os.path.getsize("best93_8.pt")
    print("side of text.zip", file_size)
    data = file.read()
    print("size of data getting sent ", len(data))
    conn.send(b'<WRONG>')
    conn.sendall(data)
    conn.send(b"<END>")
    print("sent",b"<END>")
    file.close()

        
def update_client_status(address):
    f = open("client_status.csv","w+")
    data = csv.reader(f)
    
    time_now = time.time()
    
    for i in data:
        if(len(i) > 0):
            if(i[0] == address):
                if(time_now - i[2] > 5.0):
                    i[1] = "inactive"


def add_client(address,time_stamp):
    f = open("client_status.csv",'a+')
    file_content = csv.reader(f)
    for i in file_content:
        if(i[0] == address):
            update_client_status(str(address))
            return
    data = (address,'active',time_stamp)
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()
    
def store_data(received_data):
    f= open("data.csv",'a+')
    writer = csv.writer(f)
    store_file = csv.reader(f)
    for i in received_data:
        now = time.time()
        writer.writerow([i,now])
    f.close()
'''  
      if(i[0]==0):
          i[1]=i[1]+received_data[1] 
          print("total no.of cococola bottles"+received_data[1])
'''
  

 

def server_program():
    host = socket.gethostname() 
    port = 5000 

    server_socket = socket.socket()  
    server_socket.bind((host, port))  

    server_socket.listen(5) 
    print("Listening")

    global conn 

    while True:
        conn, address = server_socket.accept() 
        print("Connection from: " + str(address))
        ts = time.time()
        add_client(str(address),ts)

        while True:
        
            # recieved data is of the format -  weight version : data 
            received_data = conn.recv(1024).decode() 
            print(">>>>>>>>>>>>>",received_data)
            
            received_data = received_data.split("\n")
            print(">>>>>>>>>>>>",received_data)
            
            if not received_data[0] or received_data[0] == '':
                print("ERROR: Recieved None, breaking ....")
                break
            elif(received_data[-1].split(":")[-1] != latest_version):
            
                    print("received_data with latest version check - " + received_data[-1].split(":")[-1])
                    print("received_data = ", received_data[0:-1])
                    send_updated_weight_to_client()
                    store_data(received_data[0:-1])
            else:
                #store recieved data to database
                conn.send(b"<RIGHT>")
                store_data(received_data[0:-1])    
         
if __name__ == '__main__':
    server_program()
