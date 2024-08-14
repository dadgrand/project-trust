import aiosqlite
import asyncio

from utils.questionnaire import questionnaire
from datetime import date

db_path = '/Users/pabgrand/Documents/туда сюда/project-trust/database/data.db'


# ~~~~~ Работа с таблицей users ~~~~~ #
async def create_user(db_path: str, user_id: str) -> None:
    """Добавляет в таблицу нового пользователя (user_id)."""

    query = f"""
    insert into users (user_id) values ({user_id})
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


async def delete_user(db_path: str, user_id: str) -> None:
    """Удаляет из таблицы пользователя (user_id)."""

    query = f"""
    delete from users where user_id = {user_id}
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


# ~~~~~ Работа с таблицей questionnaire ~~~~~ #
async def create_questionnaire(db_path: str, user_id: str, **user_data) -> None:
    """Создаёт анкету для пользователя и заполняет её ответами пользователя."""

    columns = ', '.join(user_data.keys())
    placeholders = ', '.join('?' * len(user_data))
    values = tuple(user_data.values())

    query = f"""
    insert into questionnaire (user_id, {columns}) values ({user_id}, {placeholders})
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query, values)
            await db.commit()


async def edit_questionnaire(db_path: str, user_id: str, column_name: str, column_value: str) -> None:
    """Изменяет значение в анкете по column_name."""

    query = f"""
    update questionnaire set {column_name} = {column_value} where user_id = {user_id}
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


async def show_questionnaire(db_path: str, user_id: str) -> str:
    """Выводит данные анкеты пользователя."""
    global questionnaire

    query = f"""
    select * from questionnaire where user_id = {user_id}
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            user_data = await cursor.fetchone()

            if user_data:
                for question, answer in zip(questionnaire, user_data[1:]):
                    print(f"{question}: {answer}")
            else:
                print("Упс.. Ваша анкета не найдена. Желаете заполнить?")
                return "questionnaire_does_not_exists"


async def delete_questionnaire(db_path: str, user_id: str) -> None:
    """Удаляет данные анкеты пользователя."""

    query = f"""
    delete from questionnaire where user_id = {user_id}
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()


# ~~~~~ Работа с таблицей schedule ~~~~~ #
async def create_task(db_path: str, user_id: str, start_time: str, end_time: str) -> None:
    """Создаёт задачу в расписании пользователя."""

    query = f"""
    insert into schedule (user_id, date, start_time, end_time) values ({user_id}, {date}, {start_time}, {end_time})
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()

async def delete_tasks(db_path: str, user_id: str) -> None:
    """Удаляет все задачи пользователя по текущей дате."""

    query = f"""
    delete from schedule where user_id = {user_id} and date = {date}
    """

    async with aiosqlite.connect(db_path) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
            await db.commit()



