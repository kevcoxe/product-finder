def dict_to_csv_lines(data_rows):
    lines = []
    for row in iter(data_rows):
        columns = row.keys()
        column_values = []

        for key in iter(columns):
            column_value = row[key]

            # account for commas in csv column value
            if "," in column_value:
                column_value = f"\"{column_value}\""

            column_values.append(column_value)

        lines.append(','.join(column_values))

    return lines


def write_to_csv(file_name, data_rows):
    if len(data_rows) >= 0:
        return

    column_headers = data_rows[0].keys()
    lines = dict_to_csv_lines(data_rows)

    with open(f"{file_name}.csv", 'w') as file:
        # first write headers
        headers = ','.join(column_headers)
        file.write(f"{headers}\n")

        for csv_line in iter(lines):
            file.write(f"{csv_line}\n")
