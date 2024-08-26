import pandas as pd
from pathlib import Path
from datetime import datetime
from services.formater import EXPORT_DATETIME_FORMAT

TABLES = ["CUSTOMER", "CHARGE", "MONTHLY_CHARGE", "CHARGE_MONTHLY_CHARGE"]


def export_as_csv(app_db):
    desk_path = Path.home() / "Desktop"
    now = datetime.now().strftime(EXPORT_DATETIME_FORMAT)
    Path.mkdir(desk_path / f"back_up_quotamer_{now}")

    for table in TABLES:
        data: pd.DataFrame = app_db.get_all_from(table)
        data.to_csv(desk_path / f"back_up_quotamer_CSV_{now}" / f"{table}_{now}.csv")


def export_as_sql(app_db):
    pass


def export_as_json(app_db):
    desk_path = Path.home() / "Desktop"
    now = datetime.now().strftime(EXPORT_DATETIME_FORMAT)
    Path.mkdir(desk_path / f"back_up_quotamer_JSON_{now}", exist_ok=True)

    for table in TABLES:
        data: pd.DataFrame = app_db.get_all_from(table)
        data.to_json(desk_path / f"back_up_quotamer_JSON_{now}" / f"{table}_{now}.json", orient="records")


def import_as_csv(app_db):
    pass


def import_as_sql(app_db):
    pass


def import_as_json(app_db):
    pass
