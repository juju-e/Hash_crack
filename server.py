import socket
import hashlib

host="localhost"
port=4000
found=False
def encode_md5(crack):
    return hashlib.md5(crack).hexdigest()
def encode_sha1(crack):
    return hashlib.sha1(crack).hexdigest()
def encode_sha224(crack):
    return hashlib.sha224(crack).hexdigest()
def encode_sha512(crack):
    return hashlib.sha512(crack).hexdigest()
def encode_sha384(crack):
    return hashlib.sha384(crack).hexdigest()

def create():
  try:
    global sock
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  except socket.error as err:
      return("Failed to create socket: "+str(err))

def bind():
    try:
        global sock
        sock.bind((host,port))
        sock.listen(5)
    except socket.error as err:
      return("Failed to bind socket: "+str(err)+"  retrying....")
      bind()
def rec_and_send():
       global sock
       file_dict="words.txt"
       while True:
         conn,addr=sock.accept()
         msg=conn.recv(1024)
         conn.send(crack(msg.strip()))
def crack(hash):
       filex="words.txt"
       with open(filex,"r") as file:
        for word in file.readlines():
         word_clone=word
         word1=encode_md5(word.strip())
         if word1==hash:
             return "[@]md5mode---->word found---->"+word_clone
             found=True
             break
         word1=encode_sha1(word.strip())
         if word1==hash:
            return "[@]sha1---->word found---->"+word_clone
            found=True
            break
         word2=encode_sha224(word.strip())
         if word2==hash:
            return "[@]sha224---->word found---->"+word_clone
            found=True
            break
         word3=encode_sha384(word.strip())
         if word3==hash:
            return "[@]sha384---->word found---->"+word_clone
            found=True
            break
         word4=encode_sha512(word.strip())
         if word4==hash:
            return "[@]sha512---->word found---->"+word_clone
            found=True
            break
       return "not found on server"

create()
bind()
rec_and_send()
