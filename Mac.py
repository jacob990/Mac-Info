import uuid 
print('informazioni ottenute con successo ! ')
print ("Il tuo mac address : ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
    for elements in range(0,2*6,2)][::-1]))
