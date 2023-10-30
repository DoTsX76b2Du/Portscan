import socket

    print('\n\033[2;31;49m''ACCESS ALLOWED! LOADING PORTSCAN...\033[m')

target = input('\n Target (IP-Adress): ')

for port in range(1,65535):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    print('Scanning Port > ',port)
    if s.connect_ex((target, port)) == 0:
        print('\n\033[2;31m''OPEN ==> \033[m', port)
        s.close()
