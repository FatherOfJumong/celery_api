


def translate_to_dict(cursor, data):
    if not data:
        return None

    cols = [i[0] for i in cursor.description]

    def create_row(row):
        return dict(zip(cols, row))

    return create_row(data)
