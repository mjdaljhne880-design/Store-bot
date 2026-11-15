import telebot
from telebot import types

# التوكن الخاص ببوتك
TOKEN = "9089097503:AAGlPLiTZtDxHHp5q0MQOThWCwZ_f0YE-Qo"

# الآيدي الرقمي الخاص بك (المشرف) لاستقبال الإشعارات
ADMIN_ID = 7151931897

bot = telebot.TeleBot(TOKEN)

# تخزين مؤقت لحالات المستخدمين
user_states = {}

# 1. القائمة الرئيسية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_games = types.InlineKeyboardButton("🎮 ألعاب", callback_data="games_menu")
    btn_apps = types.InlineKeyboardButton("📱 تطبيقات", callback_data="apps_menu")
    btn_subs = types.InlineKeyboardButton("⭐ اشتراكات", callback_data="subs_menu")
    btn_accounts = types.InlineKeyboardButton("👥 حسابات", callback_data="accounts_menu")
    btn_social = types.InlineKeyboardButton("🌐 رشق سوشيال ميديا", callback_data="social_menu")
    btn_cards = types.InlineKeyboardButton("💳 بطاقات الهدايا", callback_data="cards_menu")
    
    markup.add(btn_games, btn_apps, btn_subs, btn_accounts, btn_social, btn_cards)
    
    welcome_text = (
        "⚡ **دليل الأقسام والخدمات**\n\n"
        "🛒 اختر القسم المطلوب من القائمة أدناه لفتح المتجر واستعراض الخدمات المتاحة.\n\n"
        "ℹ️ في حال لم تجد الخدمة المطلوبة، يرجى التواصل مع الدعم: @Mjd7Aljhne"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# 2. معالجة الأقسام والألعاب
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.message.chat.id
    
    if call.data == "games_menu":
        bot.answer_callback_query(call.id, "قسم الألعاب")
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🔥 شدات ببجي (PUBG Mobile)", callback_data="pubg_products"),
            types.InlineKeyboardButton("💎 جواهر فري فاير (Free Fire)", callback_data="ff_products"),
            types.InlineKeyboardButton("🂡 توكنز جواكر (Jawaker)", callback_data="jawaker_products"),
            types.InlineKeyboardButton("⭐ اشتراكات الألعاب (ببجي وفري فاير)", callback_data="subs_games_products"),
            types.InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="main_menu")
        )
        bot.edit_message_text(
            "🎮 **قسم الألعاب - اختر اللعبة أو القسم المطلوبة:**", 
            user_id, 
            call.message.message_id, 
            reply_markup=markup, 
            parse_mode="Markdown"
        )
        
    # --- قسم شدات ببجي ---
    elif call.data == "pubg_products":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("10 شدات - 40 ل.س", callback_data="buy_p_10"),
            types.InlineKeyboardButton("60 شدة - 147 ل.س", callback_data="buy_p_60"),
            types.InlineKeyboardButton("325 شدة - 750 ل.س", callback_data="buy_p_325"),
            types.InlineKeyboardButton("660 شدة - 1470 ل.س", callback_data="buy_p_660"),
            types.InlineKeyboardButton("🔙 رجوع للألعاب", callback_data="games_menu")
        )
        bot.edit_message_text("🔥 **اختر باقة شدات ببجي موبايل المطلوبة:**", user_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # --- قسم جواهر فري فاير ---
    elif call.data == "ff_products":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("110 جواهر - 155 ل.س", callback_data="buy_ff_110"),
            types.InlineKeyboardButton("210 جواهر - 320 ل.س", callback_data="buy_ff_210"),
            types.InlineKeyboardButton("583 جوهرة - 775 ل.س", callback_data="buy_ff_583"),
            types.InlineKeyboardButton("1188 جوهرة - 1550 ل.س", callback_data="buy_ff_1188"),
            types.InlineKeyboardButton("🔙 رجوع للألعاب", callback_data="games_menu")
        )
        bot.edit_message_text("💎 **اختر باقة جواهر فري فاير المطلوبة:**", user_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # --- قسم توكنز جواكر ---
    elif call.data == "jawaker_products":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("10000 توكنز - 180 ل.س", callback_data="buy_j_10k"),
            types.InlineKeyboardButton("50000 توكنز - 850 ل.س", callback_data="buy_j_50k"),
            types.InlineKeyboardButton("75000 توكنز - 1270 ل.س", callback_data="buy_j_75k"),
            types.InlineKeyboardButton("🔙 رجوع للألعاب", callback_data="games_menu")
        )
        bot.edit_message_text("🂡 **اختر باقة توكنز جواكر المطلوبة:**", user_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # --- قسم اشتراكات الألعاب ---
    elif call.data == "subs_games_products":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("ببجي برايم عادي (شهر) - 145 ل.س", callback_data="buy_sub_p_normal"),
            types.InlineKeyboardButton("ببجي برايم بلس (شهر) - 1420 ل.س", callback_data="buy_sub_p_plus"),
            types.InlineKeyboardButton("فري فاير عضوية أسبوعية - 360 ل.س", callback_data="buy_sub_ff_week"),
            types.InlineKeyboardButton("فري فاير عضوية شهرية - 1650 ل.س", callback_data="buy_sub_ff_month"),
            types.InlineKeyboardButton("🔙 رجوع للألعاب", callback_data="games_menu")
        )
        bot.edit_message_text("⭐ **اختر الاشتراك المطلوب:**", user_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    # اختيار أي منتج يوجه المستخدم لإرسال الـ ID
    elif call.data.startswith("buy_"):
        product_dict = {
            "buy_p_10": "10 شدات ببجي (40 ل.س)",
            "buy_p_60": "60 شدة ببجي (147 ل.س)",
            "buy_p_325": "325 شدة ببجي (750 ل.س)",
            "buy_p_660": "660 شدة ببجي (1470 ل.س)",
            "buy_ff_110": "110 جواهر فري فاير (155 ل.س)",
            "buy_ff_210": "210 جواهر فري فاير (320 ل.س)",
            "buy_ff_583": "583 جوهرة فري فاير (775 ل.س)",
            "buy_ff_1188": "1188 جوهرة فري فاير (1550 ل.س)",
            "buy_j_10k": "10000 توكنز جواكر (180 ل.س)",
            "buy_j_50k": "50000 توكنز جواكر (850 ل.س)",
            "buy_j_75k": "75000 توكنز جواكر (1270 ل.س)",
            "buy_sub_p_normal": "ببجي برايم عادي شهر (145 ل.س)",
            "buy_sub_p_plus": "ببجي برايم بلس شهر (1420 ل.س)",
            "buy_sub_ff_week": "فري فاير عضوية أسبوعية (360 ل.س)",
            "buy_sub_ff_month": "فري فاير عضوية شهرية (1650 ل.س)"
        }
        
        item_name = product_dict.get(call.data, "منتج رقمي")
        user_states[user_id] = {"item": item_name, "step": "waiting_id"}
        
        bot.answer_callback_query(call.id, f"تم اختيار: {item_name}")
        bot.send_message(
            user_id, 
            f"🛒 لقد اخترت: **{item_name}**\n\n"
            "🆔 **أرسل الآن الـ ID الخاص بك داخل اللعبة (أو البريد/المعلومات المطلوبة للاشتراك):**"
        )
        
    elif call.data == "main_menu":
        send_welcome(call.message)

# 3. استقبال الـ ID وتحويل العميل للدفع عبر الشام كاش
@bot.message_handler(func=lambda message: message.chat.id in user_states and user_states[message.chat.id]["step"] == "waiting_id")
def receive_player_id(message):
    user_id = message.chat.id
    user_states[user_id]["player_id"] = message.text
    user_states[user_id]["step"] = "waiting_payment"
    
    item = user_states[user_id]["item"]
    
    payment_text = (
        f"✅ تم حفظ الـ ID/المعلومات بنجاح.\n\n"
        f"📦 الطلب: **{item}**\n\n"
        f"💳 **طريقة الدفع (شام كاش):**\n"
        f"يرجى تحويل قيمة الطلب حصراً عبر محفظة **الشام كاش** على الرابط التالي:\n"
        f"🔗 `1063346d770c733ae4def51ae118af09`\n\n"
        f"📸 **بعد اتمام التحويل:** قم بإرسال صورة إيصال التحويل أو رقم العملية هنا في المراسلة ليتم التحقق منه وتنفيذ طلبك."
    )
    bot.send_message(user_id, payment_text, parse_mode="Markdown")

# 4. استقبال إيصال الدفع وإرسال الإشعار إلى آيدي المشرف الخاص بك حصراً
@bot.message_handler(content_types=['text', 'photo'], func=lambda message: message.chat.id in user_states and user_states[message.chat.id]["step"] == "waiting_payment")
def receive_payment_proof(message):
    user_id = message.chat.id
    data = user_states[user_id]
    user_name = message.from_user.first_name
    username = f"@{message.from_user.username}" if message.from_user.username else "لا يوجد معرف"
    
    admin_caption = (
        f"🚨 **طلب شراء جديد بانتظار التحقق من الدفع!**\n\n"
        f"📦 المنتج: {data['item']}\n"
        f"🆔 الـ ID / المعرف: `{data['player_id']}`\n"
        f"👤 العميل: {user_name}\n"
        f"🔗 معرف العميل: {username}\n"
        f"💬 آيدي العميل الرقمي: `{user_id}`"
    )
    
    if message.content_type == 'photo':
        photo_id = message.photo[-1].file_id
        bot.send_photo(ADMIN_ID, photo_id, caption=admin_caption, parse_mode="Markdown")
    else:
        admin_caption += f"\n💰 تفاصيل الدفع / رقم العملية: {message.text}"
        bot.send_message(ADMIN_ID, admin_caption, parse_mode="Markdown")
        
    bot.send_message(
        user_id, 
        "⏳ **تم إرسال إيصال الدفع بنجاح!**\nجاري مراجعة التحويل عبر الشام كاش وتنفيذ الشحن يدوياً في أقرب وقت."
    )
    
    del user_states[user_id]

print("Bot is running...")
bot.infinity_polling()
