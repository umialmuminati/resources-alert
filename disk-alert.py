from json import dumps
import psutil
import socket
import datetime
import pytz
from httplib2 import Http

def main():
    url = 'https://chat.emporiadigital.com/hooks/niqfkg6j3bnu8eixo3h3znd8to'
    myhost = socket.gethostname()
    get_disk = psutil.disk_usage('/').percent
    current_datetime = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))

    print("")
    print("------------------------- DISk -------------------------")
    print(current_datetime, "Disk usage in %: {}".format(get_disk))

    if get_disk > 90:
        bot_message = {
            #CPU usage alert at (Nginx-Proxy : 147.139.138.145) UBAH IP SESUAI IP SERVER
            #CPU mencapai lebih dari 100.0% 
            'text' : 'Disk Usage alert at (' + myhost + ' : 147.139.138.145)\n'
                     'Disk mencapai ' + str(get_disk) + '%'
        }

        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

        http_obj = Http()

        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message)
        )

        return get_disk

if __name__ == '__main__':
    main()