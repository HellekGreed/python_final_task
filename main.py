import logging

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('homework.log', encoding='utf-8')
    handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    logger.addHandler(handler)
    logger.addHandler(console_handler)

    try:
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))
        logger.info(f"a = {a}, b = {b}, c = {c}")

        if a + b > c and a + c > b and b + c > a:
            logger.info("Треугольник существует")
            if a == b == c:
                logger.info("Треугольник равносторонний")
            elif a == b or a == c or b == c:
                logger.info("Треугольник равнобедренный")
            else:
                logger.info("Треугольник разносторонний")
        else:
            logger.error("Треугольник не существует")
    except Exception as e:
        logger.error("Error: %s", str(e))

if __name__ == "__main__":
    main()
