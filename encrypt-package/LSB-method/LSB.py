from PIL import Image


def encode_message(image_path, message, output_path):
    # Открываем изображение
    image = Image.open(image_path)
    pixels = image.load()

    # Конвертируем сообщение в двоичную строку
    binary_message = ''.join([format(ord(char), '08b') for char in message]) + '00000000'  # Стоп символ (нулевой байт)

    # Встраиваем сообщение в изображение, изменяя младший бит пикселей
    message_index = 0
    for y in range(image.height):
        for x in range(image.width):
            if message_index < len(binary_message):
                r, g, b = pixels[x, y]

                # Меняем младший бит красного канала
                r = (r & ~1) | int(binary_message[message_index])
                message_index += 1

                # Меняем младший бит зеленого канала, если сообщение ещё не закончено
                if message_index < len(binary_message):
                    g = (g & ~1) | int(binary_message[message_index])
                    message_index += 1

                # Меняем младший бит синего канала, если сообщение ещё не закончено
                if message_index < len(binary_message):
                    b = (b & ~1) | int(binary_message[message_index])
                    message_index += 1

                # Обновляем пиксель с новыми значениями
                pixels[x, y] = (r, g, b)
            else:
                # Если всё сообщение встроено, сохраняем изображение и выходим
                image.save(output_path)
                print("Message encoded successfully!")
                return


def decode_message(image_path):
    # Открываем изображение
    image = Image.open(image_path)
    pixels = image.load()

    # Извлекаем двоичное сообщение из младших битов каждого пикселя
    binary_message = ""
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    # Преобразуем двоичное сообщение в текст до стоп символа (00000000)
    decoded_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == '00000000':  # Стоп символ
            break
        decoded_message += chr(int(byte, 2))

    return decoded_message


# Пример использования
encode_message("input_image.png", "Секретное сообщение", "encoded_image.png")
print("Decoded message:", decode_message("encoded_image.png"))