import paramiko
import sys
from Logger import logging
class SSHHandler:
    def __init__(self) -> None:
        super().__init__()
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.exit_code = 0

    def connect (self, host, username, password): #функция отетственна за подключение ssh: ssh lynx@192.168.10.17 + password
        self.exit_code = 0
        logging.info(f"Выполнена команда: Подключение к уаделнной ЭВМ через протоколы SSH")
        try:
            self.client.connect(hostname=host, username=username, password=password, timeout=10)
            #print("Good connection")
        except TimeoutError:
            print('Timeout reached while connecting to {0}'.format(host), file=sys.stderr)
            self.exit_code = 3

    def disconnect(self): #exit в ssh
        logging.info(f"Выполнена команда: Выход из сеанса подключения по SSH")
        self.client.close()

    def execute(self, command): #прямое исполнение кода в командной строке
        stdin, stdout, stderr = self.client.exec_command(command)
        exit_code = stdout.channel.recv_exit_status()
        output = stdout.readlines()
        logging.info(f"Выполнена команда: {command}")
        print(stderr.readlines())
        return exit_code, output

    def send(self, name, sender_email, recipient_email, password, verbose=True):
        # exit codes: 0 - ok, 1 - error, 3 - connection timeout
        logging.info(f"Выполнена команда: Отправка определенной команды/скрипта через функцию SEND")
        if not self.exit_code:
            # command1 = './send.sh -n ' + name + \
            #           ' -r ' + recipient_email +  \
            #           ' -u ' + sender_email + \
            #           ' -p ' + password + \
            #           (' -v' if verbose else '')
            command1 = 'cd ~ | ./info.sh'
            self.exit_code, output = self.execute(command1)

            if verbose:
                for i in output:
                    print(i, end='')

        return self.exit_code

    def receive(self, name, password, verbose=True, erase=True):
        # exit codes: 0 - ok, 1 - no messages, 2 - error, 3 - connection timeout
        logging.info(f"Выполнена команда: Получение определенныч данных через функцию RECEIVE")
        if not self.exit_code:
            command2 = './receive.sh -u ' + name + ' -p ' + password + ' -i '+ \
                      (' -v' if verbose else '') + (' -e' if erase else '')
            self.exit_code, output = self.execute(command2)
            if verbose:
                for i in output:
                    print(i, end='11')
            if self.exit_code == 0:
                print(i, end='22')

        return self.exit_code
