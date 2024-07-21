import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7489275442KcbduarihcCopYuMIW0Us8d8")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "253176"))

#Your API Hash from my.telegram.o
API_HASH = os.environ.get("API_HASH", "")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv::k@cluster0.6v96naz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&ssl=true")
