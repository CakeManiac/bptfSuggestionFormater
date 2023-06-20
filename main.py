num =107

def main():
    f = open('data.txt', 'r')
    data = f.read().split('|')
    f.close()
    name = ""
    
    final = "" #f"[b]SQUAD 1  | CHALLENGE 22 | SUGGESTION {str(num)}[/b]\n"
    itemCount =0
    saleCount = 0

    for line in data:
        if line[0] == 'n':
            name = line[1:]
            final += f'\n[b]{name}[/b]\n'
            continue
        if line[0] == 'i':
            item = line[1:]
            itemCount +=1
            saleCount = 0
            final += f'\n[u]Item {itemCount}[/u]\n' + f'{item}'
            continue
        if line[0] == 's':
            sale = line[1:]
            saleCount +=1
            final += f'\n[u]Sale {saleCount}[/u]\n' + f'{sale}'
            continue
        if line[0] == 'p':
            price = line[1:]
            final += f'[color=#990000]{price}[/color]\n'
            continue
        if line[0] == 't':
            price = line[1:]
            final += f'\n[b]Total[/b]\n[color=#990000]{price}[/color]\n'
            continue

    print(final)
    f = open('out.txt', 'w')
    f.write(final)
    f.close()
    input()

while True:
    main()
    num +=1