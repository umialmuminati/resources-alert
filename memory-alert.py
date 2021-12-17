from json import dumps
import psutil
import datetime
import pytz
import socket
from httplib2 import Http

def main():
    url = 'https://chat.emporiadigital.com/hooks/niqfkg6j3bnu8eixo3h3znd8to'
    myhost = socket.gethostname()
    get_memory = psutil.virtual_memory().percent
    current_datetime = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))

    f = open("/home/edrumi/resources-alert/file-memory.txt", "r+")
    count = int(f.read())

    print("")
    print("------------------------ MEMORY ------------------------")
    print(current_datetime, "Count: {}".format(count))
    f.close()

    if get_memory > 70:
        count += 1
    elif get_memory <= 70:
        count = 0

    print(current_datetime, "Count: {}".format(count))
    print(current_datetime, "Memory usage in %: {}".format(get_memory))

    f = open("/home/edrumi/resources-alert/file-memory.txt", "w")

    if count >= 240:
        f.write("0")
    else:
        f.write(str(count))
    f.close()

    # 240 artinya apabila terdapat kejadian memory/cpu usage mencapai threshold 240 kali berturut-turut maka
    # program akan mengirimkan alert. 240/60 = 4 (4 menit)
    if count >= 240:
        bot_message = {
            # Memory usage alert at (Nginx-Proxy : 147.139.138.145) UBAH IP SESUAI IP SERVER
            # Memory mencapai 100.0% selama 4 menit
            'text' : 'Memory alert at ' + myhost + '\n'
                     'Memory mencapai ' + str(get_memory) + '%' + ' selama 4 menit'
        }

        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

        http_obj = Http()

        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message)
        )

        return get_memory

if __name__ == '__main__':
    main()