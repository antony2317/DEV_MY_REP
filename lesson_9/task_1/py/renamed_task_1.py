import os
import shutil
from collections import defaultdict


def sort_files_by_extension(folder_path):
    extensions_info = defaultdict(lambda: {'count': 0, 'size': 0})

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension.lstrip('.').lower()

        if not file_extension:
            continue

        extension_folder = os.path.join(folder_path, file_extension)
        os.makedirs(extension_folder, exist_ok=True)

        source_path = os.path.join(folder_path, file)
        destination_path = os.path.join(extension_folder, file)
        shutil.move(source_path, destination_path)

        file_size = os.path.getsize(destination_path)
        extensions_info[file_extension]['count'] += 1
        extensions_info[file_extension]['size'] += file_size

    return extensions_info


def rename_one_file_in_subdirs(folder_path):
    for subdir in os.listdir(folder_path):
        subdir_path = os.path.join(folder_path, subdir)

        if os.path.isdir(subdir_path):
            files_in_subdir = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
            if files_in_subdir:
                old_file_name = files_in_subdir[0]
                old_file_path = os.path.join(subdir_path, old_file_name)
                new_file_name = f"renamed_{old_file_name}"
                new_file_path = os.path.join(subdir_path, new_file_name)

                os.rename(old_file_path, new_file_path)
                print(f"Файл {old_file_name} был переименован в {new_file_name}")
                break


def main():
    os_name = os.name
    print(f"Имя вашей операционной системы: {os_name}")

    current_folder = os.getcwd()
    print(f"Путь до текущей папки: {current_folder}")

    print("\nРассортировка файлов по расширениям...")
    extensions_info = sort_files_by_extension(current_folder)

    for ext, info in extensions_info.items():
        size_in_mb = info['size'] / (1024 * 1024)
        print(
            f"В папке с расширением '{ext}' перемещено {info['count']} файлов, их суммарный размер – {size_in_mb:.2f} МБ")

    print("\nПереименование одного файла в подпапках...")
    rename_one_file_in_subdirs(current_folder)


if __name__ == "__main__":
    main()
