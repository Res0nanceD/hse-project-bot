from aiogram.types import Message
from handlers.start_state import router


# Роутер для обработки некорректных вводов
@router.message()
async def incorrect_input(message: Message):
    await message.answer(
        text="Некорректный ввод.\n"
             "Пожалуйста, выберите одно из списка ниже:"
    )
