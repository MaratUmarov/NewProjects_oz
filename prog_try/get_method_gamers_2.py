players_dict = {

     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}

help_dict = {"Rest": "отдыхают",
             "Training": "тренируются",
             "Travel": "путешествуют"}

team_order = ["A", "B", "C"]

# Запустим цикл по словарю состояний и одновременно будем вести счёт состояний, чтобы на каждой итерации выбирать одну из команд:
index = 0
for state in help_dict:
    print(f"Все члены команды из команды {team_order[index]}, которые {help_dict[state]}:")
    for _ , player in players_dict.items():
        if player["status"] == state and player["team"] == team_order[index]:
            print(player["name"])
    index += 1
