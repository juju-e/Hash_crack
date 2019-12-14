import hashlib
import socket
from termcolor import colored
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
def online_crack(data):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect(('localhost',4000))
    except socket.error as err:
        print("Failed to connect :"+str(err))
    if len(data):
        sock.send(str.encode(data))
        print(colored("[*]from server[#]-->  "+sock.recv(1024),"yellow"))

def bruteforce():
    mode=input(colored("[#]enter crack method------->","blue"))
    hash=input(colored("[*]enter hash[*]----->","red"))
    file_dict=input(colored("[**]enter password list file name------->","blue"))
    if mode=="all":
       with open(file_dict,"r") as file:
        for word in file.readlines():
         word_clone=word
         word1=encode_md5(word.strip())
         if word1==hash:
             print(colored("[@]md5mode---->word found---->"+word_clone,"green"))
             found=True
             break
         word1=encode_sha1(word.strip())
         if word1==hash:
            print(colored("[@]sha1---->word found---->"+word_clone,"green"))
            found=True
            break
         word2=encode_sha224(word.strip())
         if word2==hash:
            print(colored("[@]sha224---->word found---->"+word_clone,"green"))
            found=True
            break
         word3=encode_sha384(word.strip())
         if word3==hash:
            print(colored("[@]sha384---->word found---->"+word_clone,"green"))
            found=True
            break
         word4=encode_sha512(word.strip())
         if word4==hash:
            print(colored("[@]sha512---->word found---->"+word_clone,"green"))
            found=True
            break
    elif mode=="md5":
          with open(file_dict,"r") as file:
           for word in file.readlines():
              word_clone=word
              word1=encode_md5(word.strip())
              if word1==hash:
                 print(colored("[@]---->word found---->"+word_clone,"green"))
                 found=True
                 break


    elif mode=="sha1":
          with open(file_dict,"r") as file:
           for word in file.readlines():
              word_clone=word
              word1=encode_sha1(clone.strip())
              if word1==hash:
                 print(colored("[@]---->word found---->"+word_clone,"green"))
                 found=True
                 break

    elif mode=="sha224":
         with open(file_dict,"r") as file:
          for word in file.readlines():
             word_clone=word
             word1=encode_sha224(word.strip())
             if word1==hash:
                print(colored("[@]---->word found---->"+word_clone,"green"))
                found=True
                break


    elif mode=="sha384":
        with open(file_dict,"r") as file:
         for word in file.readlines():
            word1=encode_sha384(word.strip())
            if word1==hash:
               print(colored("[@]---->word found---->"+word_clone,"green"))
               found=True
               break


    elif mode=="sha512":
        with open(file_dict,"r") as file:
         for word in file.readlines():
            word_clone=word
            word1=encode_sha512(word.strip)
            if word1==hash:
               print(colored("[@]---->word found---->"+word_clone,"green"))
               found=True
               break
    return found
def encode():
    mode=input(colored("[*]enter the encription mode-----> ","red"))
    word=input(colored("[**]enter the word------> ","blue"))
    if mode=="md5":
       word=encode_md5(word)
    elif mode=="sha1":
       word=encode_sha1(word)
    elif mode=="sha224":
       word=encode_sha224(word)
    elif mode=="sha384":
       word=encode_sha384(word)
    elif mode=="sha512":
       word=encode_sha512(word)
    print("[@]here is the hash------> "+word)
m=input(colored("[-]choose 1 for encryption or 2 for decription---->","yellow"))
if m=="1":
    encode()
elif m=="2":
         y=input(colored("[#]do you want to try online cracking(Y/N)----->","blue"))
         if y.lower()=="y":
            hsh=input(colored("[*]enter the hash to decrypt----->","blue"))
            online_crack(hsh)
         else:
             if bruteforce()==False:
                 print("not found in word list")
