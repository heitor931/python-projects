from prettytable import PrettyTable

table = PrettyTable()

table.add_column("name", ["Heitor", "Zánia", "Hélio", "Ayla", "Heloíza"])
table.add_column("age", [34, 32, 6, 2, 0])
table.add_autoindex()

print(table)