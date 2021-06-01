sec = int(input("Insira os segundos: "))


dias = sec//86400
hrs = (sec-(dias*86400))//3600
min = (sec-(dias*86400)-(hrs*3600))//60
sec = (sec-(dias*86400)-(hrs*3600))%60


print(str(dias)+' dias, '+'{:0>2}'.format(hrs)+' horas, '+'{:0>2}'.format(min)+' minutos e '+'{:0>2} segundos'.format(sec))
