import aiosqlite
import asyncio

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
    INSERT INTO questionnaire (user_id, {columns}) VALUES ({user_id}, {placeholders})
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

