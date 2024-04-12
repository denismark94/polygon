from RequestsFactory import Message, Request
import random
import datetime
# Класс - генератор запросов на отправку/получение/атаку
class Producer:
    # конструктор принимает класс с набором правил выбора параметров
    def __init__(self, picker, actions, sent) -> None:
        super().__init__()
        self.picker = picker
        # ToDo: ввести в объект АРМ злоумышленника для реализации атак
        # from RequestsFactory import Host
        # self.maliciousHost = Host(['11.11.11.69', '1', '1'])
        # ToDo: реализовать генерацию запросов на атаки
        self.actions = actions
        self.gen_msg_counter = 0
        self.sent = sent
        self.terminated = False
        self.interrupted = False

    # Метод генерирует и складывает в очередь случайные запросы на отправку/получение/атаку
    def produce(self, iterations, messages, requests, safeprint, verbose=False, terminated=False):
        self.terminated = False
        self.interrupted = False
        i = 0
        self.picker.dbreader.connect_sql_db()
        while i < iterations:
            if self.interrupted:
                print("Выполнение потока-генератора прервано")
                return
            import time
            time.sleep(5)
            action_type = random.choice(self.actions)
            if action_type == 'Отправка':
                s = self.picker.get_sender_id()
                tau = self.picker.get_protocol_id(s)
                j = self.picker.get_host_id(s, tau)
                r = self.picker.get_recipient_id(s, tau)
                # TODO: реализовать подгрузку сообщений в/из БД
                phi = Message(self.gen_msg_counter, s, r, tau)
                messages[self.gen_msg_counter] = phi
                q = Request(action_type, j, self.gen_msg_counter)
                self.gen_msg_counter += 1
                requests.put(q)
                i += 1
            elif action_type == 'Получение':
                send_request_generated = False
                if self.sent:
                    msg_id = self.sent.pop(0)
                    phi = messages[msg_id]
                    r = phi.recipient
                    j = self.picker.get_host_id(r, phi.protocol)
                    q = Request(action_type, j, msg_id)
                    requests.put(q)
                    i += 1
                    send_request_generated = True
            elif action_type == 'Атака':
                # TODO: обновить секцию с атаками
                if self.sent:
                    msg_id = self.sent[random.randint(0, len(self.sent) - 1)]
                    phi = messages[msg_id]
                    q = Request(action_type, -1, msg_id)
                    requests.put(q)
                    i += 1
            with safeprint:
                print("[{0}]==========Генерация===========".format(i))
                print('Запрос типа "{0}"'.format(action_type))
                if action_type == 'Отправка':
                    if verbose:
                        print('\tОтправитель: {0}'.format(self.picker.dbreader.get_username(s)))
                        print('\tПротокол: {0}'.format(self.picker.dbreader.get_protocol_name(tau)))
                        print('\tУзел отправителя: {0}'.format(self.picker.dbreader.get_ipaddress(j)))
                        print('\tПолучатель: {0}'.format(self.picker.dbreader.get_username(r)))
                        print('\tФлаг: {0:08b}'.format(phi.flag))
                    print('Задание на отправку успешно сформировано и помещено в очередь')
                    print('Сгенерировано сообщений: {0}'.format(self.gen_msg_counter))
                elif action_type == 'Получение':
                    if send_request_generated:
                        if verbose:
                                print('\tФлаг: {0:08b}'.format(phi.flag))
                                print('\tПолучатель: {0}'.format(r))
                                print('\tУзел получателя: {0}'.format(j))
                        print('Задание на получение успешно сформировано и помещено в очередь')
                    else:
                        print('Стек сообщений пуст')
                elif action_type == 'Атака':
                    if self.sent:
                        if verbose:
                            print('\tФлаг для захвата: {0:08b}'.format(phi.flag))
                        print('Задание на атаку успешно сформировано и помещено в очередь')
                    else:
                        print('Стек сообщений пуст')
                print("==============================")
        self.terminated = True