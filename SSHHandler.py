import sys
import logging
import paramiko

# ToDo TimeoutError handler
class SSHHandler:
    def __init__(self) -> None:
        super().__init__()
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.exit_code = 0
        logging.basicConfig(filename='log/log_file.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def connect(self, host, username, password, port=22):
        self.exit_code = 0
        print(host,username,password)
        try:
            self.client.connect(hostname=host, username=username, password=password, port=port, timeout=10)
        except TimeoutError:
            print('Timeout reached while connecting to {0}'.format(host), file=sys.stderr)
            self.exit_code = 3

    def disconnect(self):
        logging.info(f"Выполнена команда: Выход из сеанса подключения по SSH")
        self.client.close()

    def execute(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        exit_code = stdout.channel.recv_exit_status()
        logging.info(f"Выполнена команда: {command}")
        output = stdout.readlines()
        return exit_code, output

    def send(self, name, sender_email, recipient_email, password, msg_id, flag, verbose=False, domain='polygon.mil.zs'):
        # exit codes: 0 - ok, 1 - error, 3 - connection timeout
        if not self.exit_code:
            command = './send.sh -n ' + name + \
                      ' -f ' + sender_email + '@' + domain + \
                      ' -r ' + recipient_email + '@' + domain + \
                      ' -u ' + sender_email +'@' + domain + \
                      ' -p ' + password + \
                      ' -s id:' + msg_id + \
                      ' -t ' + flag + \
                      (' -v' if verbose else '')
            self.exit_code, output = self.execute(command)
            logging.info(f"Выполнена команда: Отправка определенной команды/скрипта через функцию SEND")

            if verbose:
                for i in output:
                    print(i, end='')
        return self.exit_code

    def receive(self, name, password, msg_id, verbose=False, erase=False):
        # exit codes: 0 - ok, 1 - no messages, 2 - error, 3 - connection timeout
        flag = 'na'
        if not self.exit_code:
            command = './receive.sh -u ' + name + ' -p ' + password + ' -i ' + msg_id + \
                      (' -v' if verbose else '') + (' -e' if erase else '')
            self.exit_code, output = self.execute(command)
            if verbose:
                for i in output:
                    print(i, end='')
            if self.exit_code == 0:
                flag = output[-1].strip()
        logging.info(f"Выполнена команда: Получение определенныч данных через функцию RECEIVE")
        return self.exit_code, flag


if __name__ == '__main__':
    host = '11.11.11.151'
    sender = 'alice'
    recipient = 'bob'
    domain = 'polygon.mil.zs'
    secret = '123qweR%'
    message_id = '001'
    flag = 'ABCDEFGH'
    handler = SSHHandler()
    handler.connect(host=host, username=sender, password=secret)
    print(handler.send(name=sender, sender_email=sender, recipient_email=recipient,
                 password=secret, msg_id=message_id, flag=flag))
    # rcv_flag = handler.receive(name=recipient, password=secret, msg_id=message_id, erase=True)
    handler.disconnect()
    # print(rcv_flag)
