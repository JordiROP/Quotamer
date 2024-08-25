import json
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
lang_dir = current_dir / ".." / "assets" / "lang"
register_lang = lang_dir / "register.json"


class LanguageManager:
    @staticmethod
    def get_register_tab_fields():
        with open(register_lang, "r", encoding="utf8") as register_tab_lang:
            return json.load(register_tab_lang)
