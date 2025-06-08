import pickle
import pathlib

from typing import Dict, Tuple, List

def read_dict(path: pathlib.Path) -> Dict[str, str]:
    """ Заванатажує довідник з файла

    path -- шлях до довідника
    """
    if path.exists():
        try:
            with open(path, 'rb') as f:
                return pickle.load(f)
        except Exception as ex:
            print("Loading Contacts error: {ex}, creating new dictionary")
            return {}
    else:
        # Якщо довідника ще нема, то повертаємо поржній
        return {}
    
def write_dict(path: pathlib.Path, dict: Dict[str, str]):
    """ Записує довідник в файл

    path -- шлях до довідника
    dict -- словник довідника
    """
    with open(path, "wb") as f:
        pickle.dump(dict, f)

def main():
    script_path = pathlib.Path(__file__)
    dict_path = script_path.with_name('contacts.pickle')
    dict = read_dict(dict_path)

    # Декоратор записує словник у файл при вдалому завершенні функції
    def writter(func):
        def inner(name: str, phone: str) -> Tuple[bool, str]:
            res = func(name, phone)
            if res[0]:
                write_dict(dict_path, dict)
            return res
        return inner  

    # Декоратор виводить повідомлення про результат операції 
    def verbose(func):
        def inner(name: str | None = None, phone: str | None = None) -> Tuple[bool, str]:
            res = func(name, phone)
            print(res[1])
            return res
        return inner    
    
    # Декоратор приводить команди до нижнього регістру та намагається визначити коианду по перших двох літерах
    def validate(func):
        def inner(prompt: str) -> List[str]:
            res: List[str] = func(prompt)
            if len(res) > 0:
                res[0] = res[0].strip().lower()
                if res[0].startswith('ad'):
                    res[0] = 'add'
                elif res[0].startswith('al'):
                    res[0] = 'all'
                elif res[0].startswith('ch'):
                    res[0] = 'change'
                elif res[0].startswith('ph'):
                    res[0] = 'phone'
                elif res[0].startswith('ex'):
                    res[0] = 'exit'
                elif res[0].startswith('cl'):
                    res[0] = 'close'
                elif res[0].startswith('qu'):
                    res[0] = 'quit'
                elif res[0].startswith('he'):
                    res[0] = 'hello'
                elif res[0].startswith('hi'):
                    res[0] = 'hello'
                    
            if len(res) > 1:
                res[1] = res[1].strip()
            if len(res) > 2:
                res[2] = res[2].strip()
            
            return res
        return inner    

    # Handler: add name phone - додає новий контакт
    @writter
    @verbose
    def add(name: str, phone: str) -> Tuple[bool, str]:
        dict[name] = phone
        return True, f"Phone {phone} to {name} added"

    # Handler: change name phone - змінює існуючий контакт
    @writter
    @verbose
    def change(name: str, phone: str) -> Tuple[bool, str]:
        if name in dict:
            dict[name] = phone
            return True, f"Contact {name}: {phone} changed"
        else:
            return False, f"Contact {name} not found"
        
    # Handler: all - виводить всі контакти
    @verbose
    def print_all(*args) -> Tuple[bool, str]:
        print("")
        for name, phone in dict.items():
            print(f"{name}: {phone}")
        return True, "OK\n" 

    # Handler: phone name - виводить вказаний контакт
    @verbose
    def print_phone(name: str, *args):
        if name in dict:
            print(f"{name}: {dict[name]}")   
            return True, "OK\n"
        else:
            return False, f"Contact {name} not found"
        
    @validate    
    def parse_input(prompt: str) -> List[str]: 
        msg = input("Enter a command: ")
        cmd = msg.split() 
        return cmd

    print("Welcome to the assistant bot!")
    while True:
        repl = parse_input("Enter a command: ")
        match repl:
            case ['add', name, phone]:
                add(name, phone)
            case ['change', name, phone]:
                change(name, phone)
            case ['all']:
                print_all()
            case ['phone', name]:
                print_phone(name)
            case ['exit'] | ['quit'] | ['close']:
                print("Good bye!")
                break
            case ['hello']:
                print("How can I help you?")
            case _:
                print(f"in-correct command: {repl}")
    

if __name__ == "__main__":
    main()