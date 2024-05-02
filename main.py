import json
import pickle

def add_friends(friends_dict, person1, person2):
    if person1 in friends_dict:
        friends_dict[person1].append(person2)
    else:
        friends_dict[person1] = [person2]

def main():
    friends_dict = {}
    num_entries = int(input("Введіть кількість пар друзів: "))

    for _ in range(num_entries):
        person1 = input("Введіть ім'я першої людини: ")
        person2 = input("Введіть ім'я другої людини: ")
        add_friends(friends_dict, person1, person2)

    with open("friends.pkl", "wb") as f:
        pickle.dump(friends_dict, f)
    print("Дані збережено у файлі friends.pkl")

    with open("friends.pkl", "rb") as f:
        loaded_friends_dict = pickle.load(f)

    with open("friends.json", "w") as f:
        json.dump(loaded_friends_dict, f)
    print("Дані збережено у файлі friends.json")

    print("Дані про друзів:")
    for person, friends in loaded_friends_dict.items():
        print(f"{person}: {friends}")

if __name__ == "__main__":
    main()
