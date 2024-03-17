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
        self.msg_counter = 0
        self.sent = sent

    # Метод генерирует и складывает в очередь случайные запросы на отправку/получение/атаку
    def produce(self, iterations, messages, requests, safeprint, verbose=False, terminated=False):
        i = 0
        self.picker.dbreader.connect_sql_db()
        while i < iterations:
            import time
            time.sleep(5)
            type = random.randint(0, len(self.actions) - 1)
            if type == 0:
                # s = self.picker.getSender()
                s = self.picker.get_sender_id()
                # tau = self.picker.getProtocol(self.picker.users[s])
                tau = self.picker.get_protocol_id(s)
                # j = self.picker.getHost(self.picker.users[s], tau)
                j = self.picker.get_host_id(s, tau)
                # r = self.picker.getRecipient(tau)
                r = self.picker.get_recipient_id(s, tau)
                # TODO: реализовать подгрузку сообщений в/из БД
                phi = Message(self.msg_counter, s, r, tau)
                messages[self.msg_counter] = phi
                q = Request(type, j, self.msg_counter)
                self.msg_counter += 1
                # requests.append(q)
                requests.put(q)
                i += 1
            elif type == 1:
                send_request_generated = False
                if self.sent:
                    msg_id = self.sent.pop(0)
                    phi = messages[msg_id]
                    r = phi.recipient
                    # j = self.picker.getHost(self.picker.users[r], phi.protocol)
                    j = self.picker.get_host_id(r, phi.protocol)
                    q = Request(type, j, msg_id)
                    # requests.append(q)
                    requests.put(q)
                    i += 1
                    send_request_generated = True
            elif type == 2:
                # TODO: обновить секцию с атаками
                if self.sent:
                    msg_id = self.sent[random.randint(0, len(self.sent) - 1)]
                    phi = messages[msg_id]
                    q = Request(type, -1, msg_id)
                    # requests.append(q)
                    requests.put(q)
                    i += 1
            with safeprint:
                print("==========Генерация===========")
                print('Запрос типа "{0}"'.format(self.actions[type]))
                if type == 0:
                    if verbose:
                        # print('\tОтправитель: {0}'.format(self.picker.users[s].name))
                        print('\tОтправитель: {0}'.format(s))
                        # print('\tПротокол: {0}'.format(self.picker.protocols[tau]))
                        print('\tПротокол: {0}'.format(tau))
                        # print('\tУзел отправителя: {0}'.format(self.picker.hosts[j].ip))
                        print('\tУзел отправителя: {0}'.format(j))
                        # print('\tПолучатель: {0}'.format(self.picker.users[r].name))
                        print('\tПолучатель: {0}'.format(r))
                        print('\tФлаг: {0:08b}'.format(phi.flag))
                    print('Задание на отправку успешно сформировано и помещено в очередь')
                elif type == 1:
                    if send_request_generated:
                        if verbose:
                                print('\tФлаг: {0:08b}'.format(phi.flag))
                                # print('\tПолучатель: {0}'.format(self.picker.users[r].name))
                                print('\tПолучатель: {0}'.format(r))
                                # print('\tУзел получателя: {0}'.format(self.picker.hosts[j].ip))
                                print('\tУзел получателя: {0}'.format(j))
                        print('Задание на получение успешно сформировано и помещено в очередь')
                    else:
                        print('Стек сообщений пуст')
                elif type == 2:
                    if self.sent:
                        if verbose:
                            print('\tФлаг для захвата: {0:08b}'.format(phi.flag))
                        print('Задание на атаку успешно сформировано и помещено в очередь')
                    else:
                        print('Стек сообщений пуст')
                print("==============================")
        terminated['value'] = True