def read_rows(lines):
    rows = []
    headers = None

    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line.startswith('\ufeff'):
            cleaned_line = cleaned_line.lstrip('\ufeff')

        if not cleaned_line:
            continue

        fields = [f.strip() for f in cleaned_line.split(',')]

        if headers is None:
            headers = fields
            continue

        if len(fields) != len(headers):
            continue
        row_dict = {}
        for i in range(len(headers)):
            row_dict[headers[i]] = fields[i]
        rows.append(row_dict)
    return rows
def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind is not None:
            counts[kind] = counts.get(kind, 0) + 1
    return counts
def total_minutes(rows, kind):
    total = 0.0
    has_matches = False

    for row in rows:
        if row.get('тип') == kind:
            has_matches = True
            minutes_str = row.get('минуты', '')
            minutes_str = minutes_str.replace(',', '.')
            try:
                total += float(minutes_str)
            except ValueError:
                continue
    if not has_matches:
        return 0.0
    return round(total, 1)
def to_csv(counts):
    output = "тип,количество\n"
    for kind in sorted(counts.keys()):
        output += f"{kind},{counts[kind]}\n"
    return output
