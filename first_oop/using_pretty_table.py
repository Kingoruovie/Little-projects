from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokeman Name", ["Pikachu", "squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
