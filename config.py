from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("29961447"))
API_HASH = getenv("be2e07ad90b5c8b5d368cb4efd302568")

BOT_TOKEN = getenv("7959845792:AAG5xEToJNEt3ufVPR_oRxev7NsRl8WSFqg", None)
DURATION_LIMIT = int(getenv("85", "90"))

OWNER_ID = int(getenv("6108061450"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("1BVtsOMMBu6xG-rxQyMzjdpbqngGXqHq9dOnw1yIQzYHCKicvYPSJwsbL3xcro6XnYuW_DuwvBWnKlAqWELxaWTXFTiyE-qXlazrK06iwJB4njVaiH2D-juDZ3jA0pdbhf_Mcw9V6bHpZ25XrO8i-4cQCDLcHQPbV6uoOXiOWnefbbC3bpoYV0_wyjW0bOaEhXVEbKbBIJeTNcstsyMe2tClXKcTPq_yWdtTPanyQfp-WWcz7ptAnnHOsLppFcYVj0q34z4YBr-ihdpWHU_hTcFzyrdDyVaM3pAUAACb_C8CmRoS3aXQfVd_avXkCaVmQWAvagPQE5HoZaZkVtWs58jkHTWSgwXU=", None)

SUPPORT_CHAT = getenv("https://t.me/Animes_India_bots_support_group", "https://t.me/tbcbotschat")
SUPPORT_CHANNEL = getenv("https://t.me/Animes_India_bot", "https://t.me/tbc_bots")

SUDO_USERS = list(map(int, getenv("5446367898", "5090817443").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
