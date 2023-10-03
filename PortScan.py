import socket

user = 'Icarus'
password = 'IMK2110'

print('\n \033[2;31m''WARNING! TO CONTINUE, CONFIRM YOUR CREDENTIALS!\033[m')

userlog = input('\n\033[2;36m''Login: \033[m')
userpsw = input('\033[2;36m''Password: \033[m')

if userlog == user and userpsw == password:
    print('\n\033[2;31;49m''ACCESS ALLOWED! LOADING PORTSCAN...\033[m')
else:
    print('\n\033[2;31;49m''ACCESS DENIED!\033[m')
    exit()

target = input('\nTarget (IP-Adress): ')

for port in range(1,65535):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    print('Scanning Port > ',port)
    if s.connect_ex((target, port)) == 0:
        print('\n\033[2;31m''OPEN ==> \033[m', port)
        s.close()
