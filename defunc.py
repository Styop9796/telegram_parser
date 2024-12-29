from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sync import TelegramClient
import os
import time
from telethon.errors import UserPrivacyRestrictedError, PeerFloodError


""""
def inviting(client, channel, users):
    client(InviteToChannelRequest(
        channel=channel,
        users=[users]
    ))"""


def inviting(client, channelname, user):
    try:
        if not client.is_connected():
            client.connect()


        print(f": {user}")


        user_entity = client.get_input_entity(user)
        channel_entity = client.get_input_entity(channelname)

        client(InviteToChannelRequest(channel_entity, [user_entity]))
        print(f"Успешно приглашенный : {user}")

    except UserPrivacyRestrictedError:
        print(f"Пользователь {user} имеет ограничения на конфиденциальность. Пропуская...")
    except PeerFloodError:
        print("Количество запросов в Telegram ограничено. Попробуйте еще раз позже.")
        return
    except ValueError as e:
        print(f"Недействительный объект для {user}: {e}")
    except Exception as e:
        print(f"Ошибка при приглашении {user}: {e}")



def parsing(client, index: int, id: bool, name: bool):
    all_participants = []
    all_participants = client.get_participants(index)
    if name:
        with open('usernames.txt', 'r+') as f:
            usernames = f.readlines()
            for user in all_participants:
                if user.username:
                    if ('Bot' not in user.username) and ('bot' not in user.username):
                        if (('@' + user.username + '\n') not in usernames):
                            f.write('@' + user.username + '\n')
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
    if id:
        with open('userids.txt', 'r+') as f:
            userids = f.readlines()
            for user in all_participants:
                if (str(user.id) + '\n') not in userids:
                    f.write(str(user.id) + '\n')


def config():
    while True:
        os.system('cls||clear')

        with open('options.txt', 'r+') as f:
            if not f.readlines():
                f.write("NONEID\n"
                        "NONEHASH\n"
                        "True\n"
                        "True\n")
                continue
                
        options = getoptions()
        sessions = []
        for file in os.listdir('.'):
            if file.endswith('.session'):
                sessions.append(file)

        key = str(input("1 - Обновить api_id [{0}]\n"
                "2 - Обновить api_hash [{1}]\n"
                "3 - Парсить user-id [{2}]\n"
                "4 - Парсить user-name [{3}]\n"
                "5 - Добавить аккаунт юзербота[{4}]\n"
                "6 - Сбросить настройки\n"
                "e - Выход\n"
                "Ввод: ".format(
                    options[0].replace('\n', ''),
                    options[1].replace('\n', ''),
                    options[2].replace('\n', ''),
                    options[3].replace('\n', ''),
                    len(sessions)
                )))


        if key == '1':
            os.system('cls||clear')
            options[0] = str(input("Введите API_ID: ")) + "\n"

        elif key == '2':
            os.system('cls||clear')
            options[1] = str(input("Введите API_HASH: ")) + "\n"

        elif key == '3':
            if options[2] == 'True\n':
                options[2] = 'False\n'
            else:
                options[2] = 'True\n'

        elif key == '4':
            if options[3] == 'True\n':
                options[3] = 'False\n'
            else:
                options[3] = 'True\n'
        
        elif key == '5':
            os.system('cls||clear')
            if options[0] == "NONEID\n" or options[1] == "NONEHASH":
                print("Проверьте api_id и api_hash")
                time.sleep(2)
                continue

            print("Аккаунты:\n")
            for i in sessions:
                print(i)

            phone = str(input("Введите номер телефона аккаунта: "))
            client = TelegramClient(phone, int(options[0].replace('\n', '')), 
                                    options[1].replace('\n', '')).start(phone)
            
        elif key == '6':
            os.system('cls||clear')
            answer = input("Вы уверены?\nAPI_ID и API_HASH будут удалены\n"
                           "1 - Удалить\n2 - Назад\n"
                           "Ввод: ")
            if answer == '1':    
                options.clear()
                print("Настройки очищены.")
                time.sleep(2)
            else:
                continue

        elif key == 'e':
            os.system('cls||clear')
            break

        with open('options.txt', 'w') as f:
            f.writelines(options)


def getoptions():
    with open('options.txt', 'r') as f:
        options = f.readlines()
    return options
