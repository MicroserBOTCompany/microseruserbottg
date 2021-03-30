from telethon import TelegramClient

API_KEY="API ID YAZINIZ"

API_HASH="API HASH YAZINIZ"

#my.telegram.org adresinden alın

bot = TelegramClient('userbot',API_KEY,API_HASH)

bot.start()

#Bu komut dosyası botunuzu çalıştırmaz, sadece bir oturum oluşturur.
