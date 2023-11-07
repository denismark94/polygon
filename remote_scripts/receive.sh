user="bob"
password="123qweR%"
id="013"
hint="-u SMTP-логин\n-p SMTP-пароль\n-i ID сообщения\n-e Стереть почту пользователя с сервера\n-v Подробный вывод"
erase=false
verbose=false
flag='n\a'
while [ -n "$1" ]
do
case "$1" in
-u) user="$2"
shift ;;
-p) password="$2"
shift ;;
-i) id="$2"
shift ;;
-e) erase=true ;;
-v) verbose=true ;;
-h) echo -e "$hint"
exit 1;;
*) echo "$1 is illegal option. Use -h" 
exit 1;;
esac
shift
done
if [ $verbose = true ]
then
    echo "==========================="
    echo "Конфигурация Fetchmail..."
fi
echo "poll ns1.polygon.mil.zs
proto IMAP
user $user
pass $password
mda \"/usr/bin/procmail -m ~/.procmailrc\"" > .fetchmailrc
chmod 0700 .fetchmailrc
if [ $verbose = true ]
then
    echo "Fetchmail успешно сконфигурирован"
    echo "==========================="
    echo "Конфигурация Procmail..."
fi
echo "MAILDIR=\"./mailbox/\"
DEFAULT=\"./mailbox/\"" > .procmailrc
mkdir ./mailbox
if [ $verbose = true ]
then
    echo "Procmail успешно сконфигурирован"
    echo "==========================="
    echo "Получение почты..."
fi
if [ $erase = true ]
then
    fetchmail -a -s -t 10 &> /dev/null
else
    fetchmail -a -s -k -t 10 &> /dev/null
fi
status=$?
case "$status" in
0)
    if [ $verbose = true ]
    then
        echo "Почтовые сообщения успешно загружены"
        echo "==========================="
        echo "Поиск сообщения c id = $id..."
	
    fi
    filename=`grep -rl ./mailbox -e "id:$id"`
    if [ -n "$filename" ]
    then
	flag=`tail -n 1 $filename`
	if [ $verbose = true ]
	then	echo "Флаг: $flag"
        fi
	exit_code=0
    else
	if [ $verbose = true ]
	then	echo "Сообщение с ID=$id не найдено"
	fi
	exit_code=3
    fi
    ;;
1) 
    if [ $verbose = true ]
    then	echo "Сообщений для пользователя $user на сервере нет" 
    fi
    exit_code=1
    ;;
2)
    if [ $verbose = true ]
    then	echo "Ошибка! Загрузить сообщения не удалось"
    fi 
    exit_code=2
    ;;
esac
if [ $verbose = true ]
then
    echo "==========================="
    echo "Очистка временных файлов..."
fi
rm -R ./mailbox
rm .fetchmailrc
rm .procmailrc
if [ $verbose = true ]
then
    echo "Очистка временных файлов успешно завершена"
    echo "==========================="
fi
echo "$flag"
exit $exit_code
#EXIT CODES:
# 0 - OK
# 1 - EMPTY MAILBOX
# 2 - ERROR
# 3 - ID NOT FOUND
