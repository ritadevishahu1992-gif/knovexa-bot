from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "YOUR TOKEN ID HERE"


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("Class 8", callback_data="class_8"),
            InlineKeyboardButton("Class 9", callback_data="class_9")
        ],
        [
            InlineKeyboardButton("Class 10", callback_data="class_10"),
            InlineKeyboardButton("Class 11", callback_data="class_11")
        ],
        [
            InlineKeyboardButton("Class 12", callback_data="class_12")
        ]
    ]

    await update.message.reply_text(
        "👋 Welcome to Knovexa!\n\n"
        "🎓 Select your class:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# CLASS SELECTION
# =========================

async def class_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    selected_class = query.data.replace("class_", "")
    context.user_data["class"] = selected_class

    keyboard = [
        [
            InlineKeyboardButton("📐 Mathematics", callback_data="maths"),
            InlineKeyboardButton("🔬 Science", callback_data="science")
        ],
        [
            InlineKeyboardButton("🌍 Social Science", callback_data="sst"),
            InlineKeyboardButton("📖 English", callback_data="english")
        ],
        [
            InlineKeyboardButton("🔙 Change Class", callback_data="change_class")
        ]
    ]

    await query.edit_message_text(
        f"🎓 Class {selected_class}\n\n"
        "📚 Select your subject:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# SUBJECT SELECTION
# =========================

async def subject_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    subject = query.data
    context.user_data["subject"] = subject

    subject_names = {
        "maths": "📐 Mathematics",
        "science": "🔬 Science",
        "sst": "🌍 Social Science",
        "english": "📖 English"
    }

    keyboard = [
        [
            InlineKeyboardButton("Chapter 1", callback_data="chapter_1"),
            InlineKeyboardButton("Chapter 2", callback_data="chapter_2")
        ],
        [
            InlineKeyboardButton("Chapter 3", callback_data="chapter_3"),
            InlineKeyboardButton("Chapter 4", callback_data="chapter_4")
        ],
        [
            InlineKeyboardButton("Chapter 5", callback_data="chapter_5"),
            InlineKeyboardButton("Chapter 6", callback_data="chapter_6")
        ],
        [
            InlineKeyboardButton("🔙 Change Subject", callback_data="change_subject")
        ]
    ]

    await query.edit_message_text(
        f"🎓 Class {context.user_data.get('class')}\n"
        f"{subject_names.get(subject)}\n\n"
        "📖 Select your chapter:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# CHAPTER SELECTION
# =========================

async def chapter_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    chapter = query.data.replace("chapter_", "")
    context.user_data["chapter"] = chapter

    keyboard = [
        [
            InlineKeyboardButton("📚 Notes", callback_data="notes"),
            InlineKeyboardButton("📝 Questions", callback_data="questions")
        ],
        [
            InlineKeyboardButton("✅ Quiz", callback_data="quiz")
        ],
        [
            InlineKeyboardButton("🔙 Change Chapter", callback_data="change_chapter")
        ]
    ]

    await query.edit_message_text(
        f"🎓 Class {context.user_data.get('class')}\n"
        f"📖 Chapter {chapter}\n\n"
        "What do you want?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# CONTENT
# =========================

async def content_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    option = query.data

    # ---------- NOTES ----------

    if option == "notes":

        notes = """
📚 CLASS 8 MATHEMATICS
📖 CHAPTER 1 — RATIONAL NUMBERS

🔹 Rational Number

A rational number can be written in the
form p/q, where p and q are integers
and q ≠ 0.

Examples:
1/2
-3/4
5/7

🔹 Numerator

The upper number is called the numerator.

🔹 Denominator

The lower number is called the denominator.

⚠️ The denominator cannot be zero.

🔹 Important Properties

1️⃣ Closure Property

The sum, difference and product of
two rational numbers are rational numbers.

2️⃣ Commutative Property

a + b = b + a

a × b = b × a

3️⃣ Associative Property

(a + b) + c = a + (b + c)

(a × b) × c = a × (b × c)

4️⃣ Additive Identity

a + 0 = a

5️⃣ Multiplicative Identity

a × 1 = a

⭐ Example

1/2 + 1/3

= 3/6 + 2/6

= 5/6
"""

        keyboard = [
            [
                InlineKeyboardButton(
                    "📝 Questions",
                    callback_data="questions"
                ),
                InlineKeyboardButton(
                    "✅ Quiz",
                    callback_data="quiz"
                )
            ]
        ]

        await query.edit_message_text(
            notes,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ---------- QUESTIONS ----------

    elif option == "questions":

        await query.edit_message_text(
            "📝 CLASS 8 — MATHS\n"
            "📖 CHAPTER 1\n\n"
            "Practice Questions\n\n"

            "1️⃣ What is a rational number?\n\n"

            "2️⃣ Why can't the denominator be zero?\n\n"

            "3️⃣ Write three examples of rational numbers.\n\n"

            "4️⃣ Find:\n"
            "1/2 + 1/3\n\n"

            "5️⃣ State the additive identity of "
            "rational numbers."
        )


    # ---------- QUIZ ----------

    elif option == "quiz":

        keyboard = [
            [
                InlineKeyboardButton(
                    "A) 1/2",
                    callback_data="quiz_wrong"
                ),
                InlineKeyboardButton(
                    "B) 5/6",
                    callback_data="quiz_correct"
                )
            ],
            [
                InlineKeyboardButton(
                    "C) 2/5",
                    callback_data="quiz_wrong"
                )
            ]
        ]

        await query.edit_message_text(
            "✅ QUICK QUIZ\n\n"
            "What is:\n"
            "1/2 + 1/3 ?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ---------- CORRECT ----------

    elif option == "quiz_correct":

        await query.edit_message_text(
            "🎉 Correct!\n\n"
            "1/2 + 1/3 = 5/6"
        )


    # ---------- WRONG ----------

    elif option == "quiz_wrong":

        await query.edit_message_text(
            "❌ Not quite!\n\n"
            "Correct answer: 5/6"
        )


# =========================
# CHANGE CLASS
# =========================

async def change_class(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("Class 8", callback_data="class_8"),
            InlineKeyboardButton("Class 9", callback_data="class_9")
        ],
        [
            InlineKeyboardButton("Class 10", callback_data="class_10"),
            InlineKeyboardButton("Class 11", callback_data="class_11")
        ],
        [
            InlineKeyboardButton("Class 12", callback_data="class_12")
        ]
    ]

    await query.edit_message_text(
        "🎓 Select your class:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# BOT SETUP
# =========================

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    CallbackQueryHandler(
        class_selected,
        pattern="^class_"
    )
)

app.add_handler(
    CallbackQueryHandler(
        subject_selected,
        pattern="^(maths|science|sst|english)$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        chapter_selected,
        pattern="^chapter_"
    )
)

app.add_handler(
    CallbackQueryHandler(
        content_selected,
        pattern="^(notes|questions|quiz|quiz_correct|quiz_wrong)$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        change_class,
        pattern="^change_class$"
    )
)

print("🚀 Knovexa is running...")

app.run_polling()