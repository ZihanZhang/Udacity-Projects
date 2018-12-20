months = ['Janurary',
              'Feburary',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']

month_abb = dict((m[:3].lower(), m) for m in months)


def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abb.get(short_month)

print(valid_month('Aprilsdfsdfds'))