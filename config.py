import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7489275442:AAEsqqvoQu-KcbduarihcCopYuMIW0Us8d8")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25213176"))

#Your API Hash from my.telegram.o
API_HASH = os.environ.get("API_HASH", "a720bfef89e315cc1d7c2ff628c3a69a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kidsop:kidsop@cluster0.6v96naz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
