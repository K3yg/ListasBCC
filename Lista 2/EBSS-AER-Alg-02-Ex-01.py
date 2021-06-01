dias = int(input('Insira o intervalo de tempo em dias: '))
hrs = int(input('Insira o intervalo de tempo em horas: '))
min = int(input('Insira o intervalo de tempo em minutos: '))
sec = int(input('Insira o intervalo de tempo em segundos: '))



result = print(f'O tempo em segundos é de: {(((dias*86400) + (hrs*3600) + (min*60)) + sec)} segundos')