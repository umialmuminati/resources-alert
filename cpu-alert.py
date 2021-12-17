from json import dumps
import psutil
import socket
import pytz
import datetime
from httplib2 import Http

def main():

    # URL WEBHOOK
    url = 'https://chat.emporiadigital.com/hooks/niqfkg6j3bnu8eixo3h3znd8to'
    # GET HOSTNAME SERVER
    myhost = socket.gethostname()
    
    # GET VALUE OF CPU USAGE dalam bentuk persen dalam rentang 0.5 detik
    get_cpu = psutil.cpu_percent(interval=0.5)

    current_datetime = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    
    # open file for read:
    f = open("/home/umial/resources-alert/file.txt", "r+")
    count = int(f.read())
    
    print("")
    print("------------------------- CPU --------------------------")
    print(current_datetime, "Count: {}".format(count))
    f.close()

    # threshold
    if get_cpu > 70:
        count += 1
    elif get_cpu <= 70:
        count = 0

    print(current_datetime, "Count: {}".format(count))
    print(current_datetime, "Cpu usage in %: {}".format(get_cpu))
    
    f = open("/home/umial/resources-alert/file.txt", "w")

    # reset 0 kalau sudah alert sekali (setiap 4 menit)
    if count >= 240:
        f.write("0")
    else:
        f.write(str(count))
    f.close()

    # 240 artinya apabila terdapat kejadian memory/cpu usage mencapai threshold 240 kali berturut-turut maka
    # program akan mengirimkan alert. 240/60 = 4 (4 menit)
    if count >= 240:
        bot_message = {
            #CPU usage alert at (Nginx-Proxy : 147.139.138.145) UBAH IP SESUAI IP SERVER
            #CPU mencapai 100.0% selama 4 menit
            'text' : 'CPU usage alert at (' + myhost + ' : 147.139.138.145)\n'
                     'CPU mencapai ' + str(get_cpu) + '%' + ' selama 4 menit'
        }

        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

        http_obj = Http()

        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message)
        )
    
        return get_cpu

if __name__ == '__main__':
    main()