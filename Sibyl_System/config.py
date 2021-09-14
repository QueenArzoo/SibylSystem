from typing import Union, Optional

API_ID: int = 12345
API_HASH: str = "XYZ"
STRING_SESSION: str = "XYZ:XYZ:XYZ...."
Sibyl_logs: Union[str, int] = 123456789
Sibyl_approved_logs: Union[str, int] = 123456789
GBAN_MSG_LOGS: Optional[Union[str, int]] = None
BOT_TOKEN: str = "123456:shsiajskzkxhxj"
MONGO_DB_URL: str = ""
SIBYL = get_user_list("elevated_users.json", "SIBYL")
INSPECTORS = get_user_list("elevated_users.json", "INSPECTORS")
ENFORCERS = get_user_list("elevated_users.json", "ENFORCERS")
