import logging

from app.task_manager import TaskManager

logging.basicConfig(filename="task.log", level=logging.INFO, encoding="utf-8")

logger = logging.getLogger(__name__)

manager = TaskManager()
manager.load_from_json()


logger.info("Цикл запущен!")
while True:
    print("Task Manager".center(32, "-"))
    print(
        "1. Все задачи\n"
        "2. Добавить задачу\n"
        "3. Редактировать задачу\n"
        "4. Удалить задачу\n"
        "5. Найти задачу\n"
        "0. Выход\n"
    )

    action = input("Выберете действие: ")

    if action == "0":
        logger.info("Цикл завершён!")

        break

    elif action == "1":
        logger.info("ДЕЙСТВИЕ 1: ВСЕ ЗАДАЧИ")

        tasks = manager.get_all_tasks()

        if not manager.tasks:
            print("Задач нет")

        else:
            for task in tasks:
                print(task)

    elif action == "2":
        logger.info("ДЕЙСТВИЕ 2: ДОБАВИТЬ ЗАДАЧУ")

        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        prioity = input("Введите приоритет задачи: ")

        try:
            manager.add_task(title, description, prioity)
            manager.save_to_json()

            print("Успешно добвалено!")

            logger.info("Задача успешно добавлена")

        except ValueError as e:
            print(f"Ошибка: {e}")

            logger.error(e)

    elif action == "3":
        logger.info("ДЕЙСТВИЕ 3: ИЗМЕНИТЬ ЗАДАЧУ")

        try:
            task_id = int(input("Введите ID задачи, которую хотите изменить: "))

            new_title = input("Введите новое название: ") or None
            new_desc = input("Введите новое описание: ") or None
            new_priority = input("Введите новый приоритет: ") or None

            manager.update_task(task_id, new_title, new_desc, new_priority)
            manager.save_to_json()

            print("Успешно!")

            logger.info("Задача успешно обнавлена!")

        except ValueError as e:
            print(f"Ошибка: {e}")

            logger.error(e)

    elif action == "4":
        logger.info("ДЕЙСТВИЕ 4: УДАЛИТЬ ЗАДАЧУ")

        try:
            task_id = int(input("Введите ID задания, которое хотите удалить: "))

            manager.delete_task(task_id)
            manager.save_to_json()

            print("Успешно!")

            logger.info("Задача успешно удалена!")

        except ValueError as e:
            print(f"Ошибка: {e}")

            logger.error(e)

    elif action == "5":
        logger.info("ДЕЙСТВИЕ 5: НАЙТИ ЗАДАЧУ")

        try:
            task_id = int(input("Введите ID задания: "))

            task = manager.get_task_by_id(task_id)

            print(task)

            logger.info(f"Задача найдена: {task}")

        except ValueError as e:
            print(f"Ошибка {e}")

            logger.error(e)

    else:
        print("Неверный ввод")
