from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import token

bot = Bot(token)
dp = Dispatcher(bot)

buttons = [
    KeyboardButton("О нас"),
    KeyboardButton("Объекты"),
    KeyboardButton("Контакты"),
]

butts = ReplyKeyboardMarkup().add(*buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Здравствуйте!", reply_markup=butts)

@dp.message_handler(text="О нас")
async def about_us(message:types.Message):
    await message.answer("Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в объектах расположенных во всех наиболее привлекательных районах городов Ош и Джалал-Абад. У нас максимально выгодные условия, гибкий (индивидуальный) подход при реализации жилой и коммерческой недвижимости. Мы занимаем лидирующие позиции по количеству объектов по югу Кыргызстана. Наша миссия: Мы обеспечиваем население удобным жильем для всей семьи, проявляя лояльность и индивидуальный подход и обеспечивая высокий уровень обслуживания. Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и опыт профессионалов своего дела.")

@dp.message_handler(text="Объекты")
async def about_us(message:types.Message):
    await message.answer("ЖК «Малина-Лайф» г.Ош, ул Монуева 1 Сроки начала строительства: 11 Сроки завершения строительства: 2 Жилой комплекс «Малина Лайф» – эксклюзивный проект бизнес-класса c отличной экологией и богатой инфраструктурой. В шаговой доступности находится вся инфраструктура города Ош: гипермаркеты «Фрунзе» и «Глобус», рынок «Келечек», река «Ак-Буура» и набережная для прогулок всей семьей. Также, на расстоянии двухсот метров расположены парк им. Навои и проспект Масалиева – одна из основных автомагистралей города. Любители престижа и высокого уровня жизни оценят уникальный архитектурный облик и безупречно продуманные планировочные решения квартир.")

@dp.message_handler(text="Контакты")
async def about_us(message:types.Message):
    await message.answer("г.Ош, ул.Аматова 1, \nБизнес центр Томирис \ncontact@vg-stroy.com \n+996 709 620088 \n+996 772 620088 \n+996 550 620088 \nwww.vg-stroy.com")

executor.start_polling(dp)