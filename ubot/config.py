import os

from dotenv import load_dotenv

load_dotenv()



DEVS = [
    6096141441 #DEVAIU
]

KYNAN = list(map(int, os.getenv("KYNAN", "6096141441").split()))

API_ID = int(os.environ.get("API_ID", "17250424"))

API_HASH = os.environ.get("API_HASH", "753bc98074d420ef57ddf7eb1513162b")

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002314438515"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001608847572 -1001982790377 -1001538826310 -1001861414061 -1001876092598").split()))

USER_ID = list(map(int, os.getenv("USER_ID", "6096141441").split()))

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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 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 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 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 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",
).split()

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7741660290:AAFeXv7RxG8AoO8RXwgNTmsmvxdeNdgkAxk")

OWNER_ID = int(os.environ.get("OWNER_ID", "6096141441"))

MAX_BOT = int(os.environ.get("MAX_BOT", "45"))

SKY = int(os.environ.get("SKY", "-1002314438515"))

MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://uputra:uputra@cluster0.n94m27s.mongodb.net/?retryWrites=true&w=majority",
)
