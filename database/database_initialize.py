import aiosqlite
import asyncio

db_path = '/Users/pabgrand/Documents/туда сюда/project-trust/database/data.db'


async def create_table_users(db_path: str) -> None:
    """Создаёт таблицу users."""

    query = """
    create table if not exists users (
        id integer primary key autoincrement,
        user_id text not null unique
    )
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


async def create_table_questionnaire(db_path: str) -> None:
    """Создаёт таблицу questionnaire для хранения анкет пользователей."""

    query = """
    create table if not exists questionnaire (
        questionnaire_id integer primary key autoincrement,
        user_id text not null unique,
        preferred_name text, /* 1. Как вам удобно чтобы я вас называл? */
        assistance_type text, /* 2. Вы хотите чтобы я просто структурировал ваши планы или предлагал различные житейские техники? */
        age text, /* 3. Ваш Возраст? */
        gender text, /* 4. Ваш Пол? */
        weight text, /* 5. Ваш Вес? */
        height text, /* 6. Ваш Рост? */
        favorite_sports text, /* 7. Любимые виды спорта? */
        exercise_frequency text, /* 8. Вы занимаетесь спортом, ходите в зал? */
        exercise_hours_per_week text, /* 9. Сколько бы часов в неделю вы готовы тратить на спорт/зал? */
        injuries text, /* 10. У вас есть какие-то травмы? */
        eating_habits text, /* 11. Сколько раз в день вы едите? У вас есть диетические предпочтения? Что вы не едите? */
        wake_up_time text, /* 12. Во сколько вы просыпаетесь? Хотите ли просыпаться раньше? */
        sleep_time text, /* 13. Во сколько засыпаете? Хотите засыпать раньше? */
        sleep_quality text, /* 14. Как бы вы оценили качество сна? */
        work_schedule text, /* 15. Напишите свое учебное/рабочее расписание */
        desired_income text, /* 16. Сколько вы хотите зарабатывать в месяц? */
        improvement_areas text, /* 17. Отметьте сферы жизни в которых вы бы хотели быть лучше */
        motivation text, /* 18. Что вас мотивирует? */
        best_quality text, /* 19. Ваше лучшее качество? */
        worst_quality text, /* 20. Ваше худшее качество? */
        shopping_preference text, /* 21. Вы любите шоппинг? */
        spending_habits text, /* 22. Вы бы хотели меньше тратить? */
        time_management_skill text, /* 23. Как бы вы оценили свой скилл тайм-менеджмента? */
        procrastination_level text, /* 24. Оцените по 10 бальной, насколько вы прокрастинатор? */
        social_media_time text, /* 25. Сколько времени в день вы тратите на социальные сети? */
        screen_time text, /* 26. Сколько у вас часов экранного времени в день? */
        reduce_screen_time text, /* 27. Вы бы хотели сидеть меньше в телефоне и соц. сетях? */
        hobbies_interests text, /* 28. Какие у вас хобби и интересы? */
        learning_style text, /* 29. Как вы любите учить информацию - читать, смотреть, слушать, делать? */
        new_activities_time text, /* 30. Сколько часов в неделю вы бы уделяли вещам которые сейчас не делаете но хотели бы делать? Определите по часам каждую - Хобби, изучения новых знаний, овладеваете новыми полезными привычками? */
        stress_management text, /* 31. Как вы справляетесь со стрессом? */
        social_time text, /* 32. Сколько времени вы проводите с семьей и друзьями в день и неделю? */
        increase_social_time text, /* 33. Вы бы хотели проводить больше социального времени с ними? */
        communication_frequency text, /* 34. Со сколькью людьми вы общаетесь в день, неделю, месяц? */
        increase_acquaintance_communication text, /* 35. Вы бы хотели общаться с большим количеством знакомых людей? */
        increase_stranger_communication text, /* 36. Вы бы хотели общаться с большим количеством незнакомых вам людей? */
        breathing_techniques text, /* 37. Вы знаете какие-то дыхательные техники? Используете их? Хотите чтобы я их советовал? */
        spirituality text, /* 38. Вы верите в высшие силы? Потустороннию энергию? Следуете какой-то религии? */
        motivational_notifications text, /* 39. Вы бы хотели получать мотивационные уведомления от меня? */
        commitment_level text, /* 40. Насколько сильно вы готовы отдаться процессу становления новой версии себя? По сто бальной шкале. */
        schedule_detail_level text, /* 41. Насколько детально вы бы хотели чтобы я вам помогал составлять расписание вашего дня? Поминутно, по-получасово, почасово, ещё как то? */
        communication_style text, /* 42. Каким языком вы хотели бы чтобы я с вами общался? Вежливо, настойчиво, как реальный робот лол, по-дружески, с приколом? */
        daily_questionnaire text, /* 43. Вы готовы проходить опросник каждый вечер, для детализации и улучшения программы? */
        progress_reports text, /* 44. Вы хотите получать итоги недели, месяца, года чтобы видеть свой прогресс? */
        live_sessions text, /* 45. Вы не против участвовать в прямых эфирах - разборах с наставником? (Рандомно выбирается кто-то из зрителей) Пожалуйста, будьте честны по поводу прожитых дней. */
        journaling text, /* 46. Вы хотите вести ежедневник? Поверьте, это чит код. */
        take_responsibility text, /* 47. Вы готовы брать ответственность за свою жизнь? */
        desire_for_improvement text /* 48. Вы точно хотите стать лучше? */
    );
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


async def create_table_schedule(db_path: str) -> None:
    """Создаёт таблицу questionnaire для хранения расписаний пользователей."""

    query = """
    create table if not exists schedule (
        task_id integer primary key autoincrement,
        user_id text not null,
        date date not null,
        start_time time default null,
        end_time time default null,
        is_tagged boolean default false
    )
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


async def list_tables(db_path: str) -> None:
    """Выводит список названий таблиц в базе данных."""

    query = """
    SELECT name FROM sqlite_master WHERE type='table';
    """

    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.cursor() as cursor:
                await cursor.execute(query)
                tables = await cursor.fetchall()

                if tables:
                    print("Таблицы в базе данных:")
                    for table in tables:
                        print(table[0])  # Выводим только название таблицы
                else:
                    print("База данных пуста. Таблицы не найдены.")

    except Exception as e:
        print(f"Ошибка при получении списка таблиц: {e}")

async def delete_table(db_path: str, table_name: str) -> None:
    """Удаляет таблицу."""

    query = f"""
    drop table if exists "{table_name}"
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


def main():
    asyncio.run(list_tables(db_path))


if __name__ == '__main__':
    main()