from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "Address" , "height", ]
table.add_row(["Sworup", 22, "Pokhara",6.2])
table.add_row(["Aastha", 21, "Kathmandu", 5.5])
table.align="l"
print(table)
