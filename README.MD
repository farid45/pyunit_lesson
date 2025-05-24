#Тестирование: PyUnit

## Задание:

1. Создай новый тест класс и в нем покрой юнит-тестами функцию log() в учебном калькуляторе. Используй фикстуры и параметризацию.

Протестируй следующие сценарии:

— Тест на обычное правильное использование функции.

— Тест на неправильные типы входных данных (например, если вместо чисел передается строка).

— Тест на то, что функция бросает ошибку InvalidInputException, если вводные данные не входят в ОДЗ функции.


## Установка:

### Linux - Ubuntu

#### Устанавливаем python, git, и прочии зависимости.

#### Для Debian/Ubuntu
```
sudo apt install python3 git
```
#### Для ArchLinux
```
(sudo) pacman -S  python python-pip
```
или
```
yay -S python python-pip git
```

#### Для Fedora
```
sudo dnf install python3 git
```

### macOS

#### Установить brew, так будет проще.

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install macfuse openssl
```



#### Grab файлы 
```
git clone https://github.com/farid45/pyunit_lesson.git
cd pyunit_lesson
```

#### Создать venv и установить зависимости
```
python3 -m venv pyunit
source pyunit/bin/activate
pip3 install -r requirements.txt
```

---------------------------------------------------------------------------------------------------------------

### Windows

#### Установить python + git
- Установите Python и git.
- Если вы устанавливаете Python из магазина Microsoft Store, «установка python setup.py» завершится неудачно, но этот шаг не требуется.
- WIN+R ```cmd```

#### Grab файлы и установка
```
git clone https://github.com/farid45/pyunit_lesson.git
cd pyinit_lesson
pip3 install -r requirements.txt
```

### Запуск тестирования:

#### В зависимости от операционной системы, различия по запуску не значительные. (В данном случае показываю пример запуска на MacOs)
```
python -m unittest
```
