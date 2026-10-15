color = str("")

for contador in range(1,7):
    match color:
        case str("verde"):
            print("ambar")
            color = "ambar"
        case str("ambar"):
            print("rojo")
            color = "rojo"
        case str("rojo"):
            print("verde")
            color = "verde"
        case _:
            print("rojo")
            color = "rojo"
