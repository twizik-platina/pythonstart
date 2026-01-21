file = open("INPUT.TXT")
data = file.read().split()
file.close()

t_room = int(data[0])
t_cond = int(data[1])
rejim = data[2]

if rejim == "freeze":
    if t_room > t_cond:
        result = t_cond
    else:
        result = t_room
elif rejim == "heat":
    if t_room < t_cond:
        result = t_cond
    else:
        result = t_room
elif rejim == "auto":
    result = t_cond
elif rejim == "fan":
    result = t_room

output = open("OUTPUT.TXT", "w")
output.write(f"{result}")
output.close()