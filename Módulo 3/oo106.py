# Create a mini system that uses Python’s Interactive Help. The user will type a command and the manual will appear. When the user types the word 'END', the program will terminate. Use colors.


def ajuda(comando):
    """Mostra o manual interativo de um comando Python, com cor."""
    print('\033[1;34m')  
    help(comando)
    print('\033[m')      


def titulo(msg, cor=33):
    """Exibe um título colorido no terminal."""
    print(f'\033[1;{cor}m{"~" * (len(msg) + 4)}')
    print(f'  {msg}')
    print(f'{"~" * (len(msg) + 4)}\033[m')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 32)  
    comando = str(input('\033[1;37mDigite a função ou biblioteca ("FIM" para encerrar): \033[m')).strip()
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 31)  
        break
    else:
        ajuda(comando)