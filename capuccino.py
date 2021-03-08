import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_spoons(cup_qnt: float) -> float:
    return (14 * cup_qnt) / 7

def get_water(cup_qnt: float, cup_size: float) -> float:
    if cup_qnt > 1:
        return (float(14.285714285714) * cup_size / 100) * cup_qnt
    else:
        return cup_size / 7

def get_milk(cup_qnt: float, cup_size: float) -> float:
    if cup_qnt > 1:
        return (float(85.714285714286) * cup_size / 100) * cup_qnt
    else:
        return cup_size - get_water(cup_qnt, cup_size)

def show_recipe(cup_qnt: float, cup_size: float) -> None:
    print(f'''
    Ingredientes: \n\n
    [+] {get_spoons(cup_qnt):.0f} colheres de pó de capuccino.
    [+] {get_water(cup_qnt, cup_size):.2f}ml de água.
    [+] {get_milk(cup_qnt, cup_size):.2f}ml de leite.
    ''')

def show_steps(cup_qnt, cup_size) -> None:
    print(f'''
    Modo de Preparo: \n\n
    [!] Esquente {get_water(cup_qnt, cup_size):.2f}ml de água (sem deixar ferver!).
    [!] Adicione {get_spoons(cup_qnt):.0f} colheres (de sopa) de pó de capuccino e misture bem.
    [!] Pegue essa mistura e coloque na geladeira, até que esfrie.
    [!] Após a mistura esfriar, coloque no liquidificador e bate junto com {get_milk(cup_qnt, cup_size):.2f}ml de leite (o liquidificador deixa mais cremoso).
    [!] E pronto, seu capuccino gelado está pronto (use canudo de metal, bambu, madeira e papel). Receita by: Rafaelvis Presley!.
    ''')

def main():
    cup_qnt = int(input('Digite a quantidade de copos: '))
    cup_size = float(input('Digite o tamanho dos copos em ml: '))
    clear_screen()
    show_recipe(cup_qnt, cup_size)
    show_steps(cup_qnt, cup_size)
    input('Pressione ENTER para continuar...')

if __name__ == '__main__':
    main()