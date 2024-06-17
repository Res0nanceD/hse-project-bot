# import pytest
# from aiogram.filters import Command
# from aiogram.methods import SendMessage
# from handlers.start_state import cmd_start, help_with_start
# from handlers.registration_state import receive_name
# from handlers.back import back_to_menu
# from handlers.main_menu_state import task_chosen_topic, task_chosen_sim, task_chosen_rate
# from handlers.choosing_models_state import log_reg_chosen, random_forest_chosen, task_chosen_incorrectly
# from handlers.text_analyse_state import log_reg_answer, rf_answer, sim_text_answer
# from handlers.prob_state import show_log_reg_prob, show_rf_prob
# from handlers.rating_state import app_rated_bad, app_rated_norm, app_rated_good
#
# from aiogram_tests import MockedBot
# from aiogram_tests.handler import CallbackQueryHandler
# from aiogram_tests.handler import MessageHandler
# from aiogram_tests.types.dataset import CALLBACK_QUERY
# from aiogram_tests.types.dataset import MESSAGE
#
#
# @pytest.mark.asyncio
# async def test_command_handler():
#     requester = MockedBot(request_handler=MessageHandler(cmd_start, Command(commands=["start"])))
#     requester.add_result_for(SendMessage, ok=True)
#     calls = await requester.query(MESSAGE.as_object(text="/start"))
#     answer_message = calls.send_message.fetchone().text
#     assert answer_message == "Для продолжения введите свое имя"
#
# @pytest.mark.asyncio
# async def test_message_handler():
#     requester = MockedBot(MessageHandler(cmd_start))
#     calls = await requester.query(MESSAGE.as_object(text="Hello!"))
#     answer_message = calls.send_message.fetchone().text
#     assert answer_message == "Hello!"
#
#а
#
# @pytest.mark.asyncio
# async def test_message_handler_with_state():
#     requester = MockedBot(MessageHandler(message_handler_with_state, state=States.state))
#     calls = await requester.query(MESSAGE.as_object(text="Hello, bot!"))
#     answer_message = calls.send_message.fetchone().text
#     assert answer_message == "Hello, from state!"
#
#
# @pytest.mark.asyncio
# async def test_callback_query_handler():
#     requester = MockedBot(CallbackQueryHandler(callback_query_handler, TestCallbackData.filter()))
#
#     callback_query = CALLBACK_QUERY.as_object(
#         data=TestCallbackData(id=1, name="John").pack(), message=MESSAGE.as_object(text="Hello world!")
#     )
#     calls = await requester.query(callback_query)
#
#     answer_text = calls.send_message.fetchone().text
#     assert answer_text == "Hello, John"
#
#     callback_query = CALLBACK_QUERY.as_object(
#         data=TestCallbackData(id=1, name="Mike").pack(), message=MESSAGE.as_object(text="Hello world!")
#     )
#     calls = await requester.query(callback_query)
#
#     answer_text = calls.send_message.fetchone().text
#     assert answer_text == "Hello, Mike"
#
#
# @pytest.mark.asyncio
# async def test_callback_query_handler_with_state():
#     requester = MockedBot(CallbackQueryHandler(callback_query_handler_with_state, TestCallbackData.filter()))
#
#     callback_query = CALLBACK_QUERY.as_object(data=TestCallbackData(id=1, name="John").pack())
#     calls = await requester.query(callback_query)
#
#     answer_text = calls.answer_callback_query.fetchone().text
#     assert answer_text == "Hello, from state!"
#
#
# @pytest.mark.asyncio
# async def test_handler_with_state_data():
#     requester = MockedBot(
#         MessageHandler(
#             message_handler_with_state_data, state=States.state_1, state_data={"info": "this is message handler"}
#         )
#     )
#
#     calls = await requester.query(MESSAGE.as_object())
#     answer_message = calls.send_message.fetchone()
#     assert answer_message.text == "Info from state data: this is message handler"