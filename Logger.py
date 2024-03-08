# Отдельный файл для конфигурации логирования
import logging
logging.basicConfig(
    filename='./log/log_file.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)
