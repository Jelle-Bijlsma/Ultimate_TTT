import tttField

fields = []
maxFields = 10

for fieldNum in range(0, maxFields):
    fields.append(tttField.Playfield())

print(type(fields))
print(type(fields[0]))
