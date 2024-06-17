from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.start_state import router
from aiogram import F
from bot_graph import BotStates
from keyboards.keyboard_for_choosing_models import keyboard_for_choosing_models
from keyboards.keyboard_for_leaf_vertex import keyboard_for_leaf_vertex


# Роутер для обработка запроса "LogReg"
# handlers/logreg.py
@router.message(BotStates.choosing_model_state, F.text.lower() == "логистическая регрессия")
async def log_reg_chosen(message: Message, state: FSMContext):
    await message.answer(
        text="Вы выбрали `логистическую регрессию`! Теперь отправьте боту Вашу новость",
        reply_markup=keyboard_for_leaf_vertex()
    )
    await state.update_data(navigator="LogReg")
    await state.set_state(BotStates.logreg_state)


# Роутер для обработка запроса "RandomForest"
# handlers/random_forest.py
@router.message(BotStates.choosing_model_state,
                F.text.lower() == "lstm")
async def random_forest_chosen(message: Message, state: FSMContext):
    await message.answer(
        text="Вы выбрали `lstm`! Теперь отправьте боту Вашу новость",
        reply_markup=keyboard_for_leaf_vertex()
    )
    await state.update_data(navigator="lstm")
    await state.set_state(BotStates.randomforest_state)


# Роутер для обработки некорректных вводов
# handlers/incorrect model.py
@router.message(BotStates.choosing_model_state,
                F.text.lower() != "назад")
async def task_chosen_incorrectly(message: Message):
    await message.answer(
        text="Некорректный ввод.\n\n"
             "Пожалуйста, выберите модель из списка ниже:",
        reply_markup=keyboard_for_choosing_models()
    )
