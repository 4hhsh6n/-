player_1 = {}
player_stats = {'Firewey': 'amazon', 'Dewedor': 'necromancer'}
#name = player_stats["Firewey"] - получение
#player_stats['Firewey'] = 'barbarian - изменение
#player_stats['Mark'] = 'bard' - добавление
#del player_stats['Firewey'] - удаление
#player_stats['Not exists'] - специальная ошибка
#print('not exists' in player_stats) - Вывод False (оператор in)
#print('Firewey' in player_stats) - Вывод True (оператор in )
#print(player_stats.keys()) - вернет объект со всеми ключами словаря
#print(player_stats.values()) - вернет объект со всеми значениями словаря
for key in player_stats.keys():
    print(key)
print(player_stats)
