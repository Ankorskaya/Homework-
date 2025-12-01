from PIL import Image

filename = "example.jpg"
image = Image.open(filename)
pixels = image.load()
width, height = image.size
depth = len(image.getbands())
img_type = image.format

print(f"Ширина: {width}")
print(f"Высота: {height}")
print(f"Глубина: {depth}")
print(f"Формат: {img_type}")

while True:
    choice = input("Выбрать эффект(1)   Сохранить(2) ")

    if choice == "1":
        print("Выберите эффект:")
        print("1 — Черно-белое")
        print("2 — Отразить по вертикали")
        print("3 — Отразить по горизонтали")
        effect = input("Введите номер эффекта: ")

        if effect == "1":
            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y][:3]
                    gray = (r + g + b) // 3
                    pixels[x, y] = (gray, gray, gray)
            print("Эффект применён: черно-белое")

        elif effect == "2":
            for y in range(height):
                for x in range(width // 2):
                    left = pixels[x, y]
                    right = pixels[width - x - 1, y]
                    pixels[x, y], pixels[width - x - 1, y] = right, left
            print("Эффект применён: вертикальное отражение")

        elif effect == "3":
            for y in range(height // 2):
                for x in range(width):
                    top = pixels[x, y]
                    bottom = pixels[x, height - y - 1]
                    pixels[x, y], pixels[x, height - y - 1] = bottom, top
            print("Эффект применён: горизонтальное отражение")

        else:
            print("Нет такого эффекта.")
            continue

    if choice == "2":
        while True:
            save_name = input("Введите имя для сохранения (например, result.png): ")

            try:
                image.save(save_name)
                print(f"Изображение сохранено как {save_name}")
                quit()

            except Exception as e:
                print("Ошибка сохранения:", e)
                print("Попробуйте другое имя.\n")
