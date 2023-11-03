import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_frame = pandas.DataFrame(data)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

nato = True

while nato:
    try:
        name = input("Type your name: ").upper()
        nato_list = [nato_dict[item] for item in name]
        print(nato_list)
    except KeyError:
        print("Type only letters please")

