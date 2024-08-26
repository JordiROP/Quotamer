import json
import streamlit as st
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
lang_dir = current_dir / ".." / "assets" / "lang"
register_lang = lang_dir / "register.json"


class LanguageManager:
    register_tab = json.load(open(register_lang, "r", encoding="utf8"))

    @classmethod
    def screen_json_file(cls, screen: str):
        match screen:
            case "REGISTER":
                return cls.register_tab

    @classmethod
    def get_field(cls, screen: str, field: str, subfield: None | str = None):
        language = st.session_state.language
        if subfield:
            return cls.screen_json_file(screen).get(field).get(language).get(subfield)
        else:
            return cls.screen_json_file(screen).get(field).get(language)
