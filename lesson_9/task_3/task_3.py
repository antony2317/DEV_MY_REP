from collections import Counter


def most_common_word(line):
    words = line.split()
    word_counter = Counter(words)
    most_common = word_counter.most_common(1)
    if most_common:
        return most_common[0]
    return None, 0


input_file = 'zen.txt'
output_file = 'zen1.txt'

try:
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            word, count = most_common_word(line)
            if word:
                outfile.write(f'{word} {count}\n')
            else:
                outfile.write('Нет слов в строке\n')
    print(f"Обработка завершена. Результат записан в {output_file}")
except FileNotFoundError:
    print(f"Ошибка: файл {input_file} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
