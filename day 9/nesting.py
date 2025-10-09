capitals={
    "france":"paris",
    "india":"delhi",
}

#nested list 
travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["berlin", "munich"],
}
#to print only lille
print(travel_log["france"][1])

#nested list
nested_list = ["A", "B", ["C", "D"]]
#to print only D
print(nested_list[2][1])