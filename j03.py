import sys
from datetime import datetime

def parse_log_line(line: str):
    line_list = line.split()
    # Якщо в рядку щонайменш чотири елементи, то вважаємо його коректним
    if len(line_list) > 3:
        return {
            'timestamp': datetime.fromisoformat(line_list[0] + 'T' + line_list[1]),
            'level': line_list[2],
            'message': ' '.join(line_list[3:])}
    else:
        # Якщо ні, то повертаємо порожній словник та виводимо повідомлення
        # Тут можлива інша обробка ситуації
        print(f"line {line} in-correct, ignored")
        return {}

def load_log(path: str):
    # При обробці відного файлу можливі проблеми, тому try
    try:
        with open(path, "r") as f:
            # В процесі обробки файлу ігноруємо записи, де число елементів не дорівнює 3
            return [item for item in [parse_log_line(line) for line in f.readlines()] if len(item) == 3]
    except Exception as ex:
    # Якщо виникла проблема - повертаємо порожній список
    # Тут можлива інша обробка ситуації
        print(ex)
        return []
    
def count_logs_by_level(log):
    dict = {}
    for record in log:
        level = record['level']
        if  level in dict:
            dict[level] += 1
        else:
            dict[level] = 1
    return dict

def filter_logs_by_level(log, level):
    return [item for item in log if item['level'] == level]

def display_log_counts(counts):
    print('')
    print(f"{'Level':16}:{'Count':>16}")
    print('-' * 33)
    for k, v in counts.items():
        print(f"{k:16}:{v:>16}")
    print('-' * 33)

def display_log(log):
    print('')
    print(f"{'Timestamp':20} : {'Level':10} : {'Message':64}")
    print('-' * 100)
    for record in log:
        print(f"{record['timestamp'].isoformat():20} : {record['level']:10} : {record['message']:64}")
    print('-' * 100)
    
def display_usage():
    print('')
    print("""Usage       
    script path_to_log [level]
    """)


def main(command):
    match command:
        # Якщо тільки задано шлях
        case [path]:
            log = load_log(path)
            counts = count_logs_by_level(log)
            display_log_counts(counts)
        # Якщо задано шлях та рівень
        case [path, level]:
            log = load_log(path)
            counts = count_logs_by_level(log)
            display_log_counts(counts)
            
            log_by_level = filter_logs_by_level(log, level)
            display_log(log_by_level)
        # Якщо не формат, то виводимо підказку
        case _:
            display_usage()

            
if __name__ == "__main__":
    main(sys.argv[1:])