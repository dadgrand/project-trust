import aiosqlite
import asyncio

db_path = 'database/users.db'

async def create_table_users(db_path: str) -> None:
    """Создаёт таблицу users."""

    query = """
    create table if not exists users (
        id integer primary key autoincrement,
        user_id text not null unique
    )
    """

    async with aiosqlite.connect(db_path) as db:
        await db.execute(query)
        await db.commit()

async def create_table_questionnaire(db_path: str) -> None:
    """Создаёт таблицу questionnaire для хранения анкет пользователей."""

    query = """
    create table if not exists questionnaire (
        id integer primary key autoincrement,
        user_id text not null unique,
        preferred_name TEXT NULL,
        assistance_preference TEXT NULL,
        age TEXT NULL,
        gender TEXT NULL,
        weight TEXT NULL,
        height TEXT NULL,
        favorite_sports TEXT NULL,
        sports_activity TEXT NULL,
        weekly_sport_hours TEXT NULL,
        injuries TEXT NULL,
        dietary_preferences TEXT NULL,
        wakeup_time TEXT NULL,
        sleep_time TEXT NULL,
        sleep_quality TEXT NULL,
        schedule TEXT NULL,
        desired_income TEXT NULL,
        improvement_areas TEXT NULL,
        motivation TEXT NULL,
        best_quality TEXT NULL,
        worst_quality TEXT NULL,
        shopping_preference TEXT NULL,
        spending_habits TEXT NULL,
        time_management_skill TEXT NULL,
        procrastination_level TEXT NULL,
        daily_social_media_time TEXT NULL,
        daily_screen_time TEXT NULL,
        reduce_phone_time TEXT NULL,
        hobbies_interests TEXT NULL,
        learning_preference TEXT NULL,
        weekly_desired_activities TEXT NULL,
        stress_management TEXT NULL,
        family_friends_time TEXT NULL,
        increase_social_time TEXT NULL,
        communication_frequency TEXT NULL,
        increase_known_people_communication TEXT NULL,
        increase_unknown_people_communication TEXT NULL,
        breathing_techniques TEXT NULL,
        belief_system TEXT NULL,
        receive_motivational_notifications TEXT NULL,
        self_improvement_commitment TEXT NULL,
        schedule_detailness TEXT NULL,
        communication_style TEXT NULL,
        nightly_survey_participation TEXT NULL,
        progress_reports TEXT NULL,
        live_session_participation TEXT NULL,
        journaling_interest TEXT NULL,
        responsibility TEXT NULL,
        self_improvement_desire TEXT NULL
    )"""

    async with aiosqlite.connect(db_path) as db:
        await db.execute(query)
        await db.commit()