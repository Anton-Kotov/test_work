
def send_message():
    user_string = input('user_message: ')

    nums_dict = {
        '1': ['.', ',', '?', '!', ':', ';', '1'],
        '2': ['а', 'б', 'в', 'г', '2'],
        '3': ['д', 'е', 'ж', 'з', '3'],
        '4': ['и', 'й', 'к', 'л', '4'],
        '5': ['м', 'н', 'о', 'п', '5'],
        '6': ['р', 'с', 'т', 'у', '6'],
        '7': ['ф', 'х', 'ц', 'ч', '7'],
        '8': ['ш', 'щ', 'ъ', 'ы', '8'],
        '9': ['ь', 'э', 'ю', 'я', '9'],
        '0': [' ', '0']
    }

    final_string = ''

    for el in user_string.split():

        if len(el) > 1 and el[0] != el[-1]:             # проверка правильности ввода данных
            return None

        if len(el) > len(nums_dict[el[0]]):             # проверка на превышение символов
            num_c = len(el) % len(nums_dict[el[0]])
        else:
            num_c = len(el)

        final_string += nums_dict[el[0]][num_c - 1]

    return final_string





