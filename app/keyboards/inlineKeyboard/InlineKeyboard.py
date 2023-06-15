from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LetsGoInlineKeyboard = InlineKeyboardMarkup()
LetsGoInlineKeyboardB1 = InlineKeyboardButton(text='Да, погнали 🤘',
                                              callback_data='LetsGo')
LetsGoInlineKeyboard.add(LetsGoInlineKeyboardB1)

AcceptCallInlineKeyboard = InlineKeyboardMarkup()
AcceptCallInlineKeyboardB1 =\
    InlineKeyboardButton(text='📞 Ответить на звонок',
                         callback_data='AcceptCall')
AcceptCallInlineKeyboard.add(AcceptCallInlineKeyboardB1)

IWantLikeThisInlineKeyboard = InlineKeyboardMarkup()
IWantLikeThisInlineKeyboardB1 = \
    InlineKeyboardButton(text='Как круто! Хочу так же!',
                         callback_data='WantLikeThis')
IWantLikeThisInlineKeyboard.add(IWantLikeThisInlineKeyboardB1)

WhatInMaraphone = InlineKeyboardMarkup()
WhatInMaraphoneB1 = InlineKeyboardButton(text='А что будет на самом марафоне?',
                                         callback_data='WhatInMaraphone')
WhatInMaraphone.add(WhatInMaraphoneB1)

SoHard = InlineKeyboardMarkup()
SoHardB1 = InlineKeyboardButton(text='Как круто! Но это, наверное, сложно😓',
                                callback_data='SoHard')
SoHard.add(SoHardB1)

WhatPrice = InlineKeyboardMarkup()
WhatPriceB1 = InlineKeyboardButton(text='Как круто! А сколько стоит участие?',
                                   callback_data='Price')
WhatPrice.add(WhatPriceB1)

WantToBuy = InlineKeyboardMarkup()
WantToBuyB1 = InlineKeyboardButton(text='Хочу на марафон! 😍',
                                   callback_data='Buy')
WantToBuy.add(WantToBuyB1)
IThinkItsNotForMe = InlineKeyboardMarkup()
InlineKeyboardButtonB1 = \
    InlineKeyboardButton(text="""Мне кажется, что это не для меня 🤔""",
                         callback_data='NotForMe')
IThinkItsNotForMe.add(WantToBuyB1, InlineKeyboardButtonB1)

MeditateOrMaraphone = InlineKeyboardMarkup()
Kb1 = InlineKeyboardButton(text='Послушать медитацию 🧘‍♀️',
                           callback_data='Meditation')
Kb2 = InlineKeyboardButton(text='А что будет на самом марафоне? 🤔',
                           callback_data='WhatInMaraphone')
MeditateOrMaraphone.add(Kb1).insert(Kb2)
