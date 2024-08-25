
def export_data(output_format:str):
    match output_format:
        case "CSV":
            export_as_csv()
        case "SQL":
            export_as_sql()
        case "JSON":
            export_as_json()


def export_as_csv():
    pass


def export_as_sql():
    pass


def export_as_json():
    pass


def import_data(input_format:str):
    match input_format:
        case "CSV":
            import_as_csv()
        case "SQL":
            import_as_sql()
        case "JSON":
            import_as_json()


def import_as_csv():
    pass


def import_as_sql():
    pass


def import_as_json():
    pass
