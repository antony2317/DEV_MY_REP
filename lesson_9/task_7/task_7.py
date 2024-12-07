def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def encrypt_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            for line_number, line in enumerate(lines, start=1):
                encrypted_line = caesar_cipher(line.strip(), line_number)
                outfile.write(encrypted_line + '\n')
        print(f"Файл успешно зашифрован. Результат сохранён в '{output_filename}'.")
    except FileNotFoundError:
        print("Ошибка: входной файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


input_file = 'input.txt'
output_file = 'output.txt'

encrypt_file(input_file, output_file)
