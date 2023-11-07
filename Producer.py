from RequestsFactory import Message, Request
import random
import datetime
# Класс - генератор запросов на отправку/получение/атаку
class Producer:
    # конструктор принимает класс с набором правил выбора параметров
    def __init__(self, picker, sent, maliciousHost) -> None:
        super().__init__()
        self.picker = picker
        self.maliciousHost = maliciousHost
        # self.actions = ['Отправка', 'Получение', 'Атака']
        self.actions = ['Отправка', 'Получение']
        self.msg_counter = 0
        self.sent = sent

    # Метод генерирует и складывает в очередь случайные запросы на отправку/получение/атаку
    def produce(self, iterations, messages, requests, safeprint, verbose=False, terminated=False):
        i = 0
        while i < iterations:
            import time
            time.sleep(5)
            type = random.randint(0, len(self.actions) - 1)
            if type == 0:
                s = self.picker.getSender()
                tau = self.picker.getProtocol(self.picker.users[s])
                j = self.picker.getHost(self.picker.users[s], tau)
                r = self.picker.getRecipient(tau)
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
                    j = self.picker.getHost(self.picker.users[r], phi.protocol)
                    q = Request(type, j, msg_id)
                    # requests.append(q)
                    requests.put(q)
                    i += 1
                    send_request_generated = True
            elif type == 2:
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
                        print('\tОтправитель: {0}'.format(self.picker.users[s].name))
                        print('\tПротокол: {0}'.format(self.picker.protocols[tau]))
                        print('\tУзел отправителя: {0}'.format(self.picker.hosts[j].ip))
                        print('\tПолучатель: {0}'.format(self.picker.users[r].name))
                        print('\tФлаг: {0:08b}'.format(phi.flag))
                    print('Задание на отправку успешно сформировано и помещено в очередь')
                elif type == 1:
                    if send_request_generated:
                        if verbose:
                                print('\tФлаг: {0:08b}'.format(phi.flag))
                                print('\tПолучатель: {0}'.format(self.picker.users[r].name))
                                print('\tУзел получателя: {0}'.format(self.picker.hosts[j].ip))
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