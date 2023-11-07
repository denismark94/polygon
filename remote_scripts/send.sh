sender="alice@polygon.mil.zs"
recipient="bob@polygon.mil.zs"
smtp_login="alice@plygon.mil.zs"
smtp_password="123qweR%"
subject="id:002"
text="secret key = ABCDEFG"
hint="-n Имя отправителя\n-f Адрес отпавителя\n-r Адрес получателя\n-u SMTP-логин\n-p SMTP-пароль\n-s Тема\n-t Текст\n-v Подробный вывод"
verbose=false
while [ -n "$1" ]
do
case "$1" in
-n) name="$2"
shift ;;
-f) sender="$2"
shift ;;
-r) recipient="$2"
shift ;;
-u) smtp_login="$2"
shift ;;
-p) smtp_password="$2"
shift ;;
-s) subject="$2"
shift ;;
-t) text="$2"
shift ;;
-v) verbose=true
shift;;
-h) echo -e "$hint"
exit 1;;
*) echo "$1 недопустимый флаг. Используйте -h" 
exit 1;;
esac
shift
done
#echo "Sender name: $name"
#echo "From: $sender"
#echo "To: $recipient"
#echo "SMTP login: $smtp_login"
#echo "SMTP password: $smtp_password"
#echo "Subject: $subject"
#echo "Text: $text"
if [ $verbose = true ]
then
    echo "======================================"
    echo "Конфигурация MuttRC"
fi
echo "set from = $sender
set imap_user = $smtp_login
set imap_pass = $smtp_password
set smtp_pass = $smtp_password
set realname = $name
set smtp_url = smtp://ns1.polygon.mil.zs:25/
set ssl_verify_host = no
set ssl_verify_dates = no
set ssl_starttls = no
set ssl_force_tls = no
set crypt_use_gpgme=no
" > ~/.muttrc
if [ $verbose = true ]
then
    echo "MuttRC успешно сконфигурирован"
    echo "======================================"
    echo "Отправка сообщения..."
fi
echo "$text" | mutt -s "$subject" $recipient &> /dev/null
status=$?

if [ $verbose = true ]
then
    if [ $status -eq 0 ]
    then
        echo "Сообщение успешно отправлено"
	exitcode=0
    else
        echo "Ошибка! Сообщение не отправлено"
	exitcode=1
    fi
    echo "======================================"
    echo "Очистка временных файлов..."
fi
if [ $verbose = true ]
then	echo "Очистка временных файлов успешно завершена"
fi
rm ~/.muttrc
exit $exitcode
