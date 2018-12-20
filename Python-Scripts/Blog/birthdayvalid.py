import webapp2
import cgi

form = """
<form method = "post">

Please input your birthdate
    <label> year
        <input type="text" name="year" value="%(year)s">
    </label>

    <label> month
        <input type="text" name="month" value="%(month)s">
    </label>

    <label> day
        <input type="text" name="day" value="%(day)s">
    </label>

    <div style="color: red">%(error)s</div>

    <input type="submit">
</form>
"""

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


def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day


month_abb = dict((m[:3].lower(), m) for m in months)


def valid_month(month):
        if month:
            short_month = month[:3].lower()
            return month_abb.get(short_month)
            # cap_month = month.capitalize()
            # if cap_month in months:
            #     return cap_month


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2017:
            return year


def escape_html(s):
    cgi.escape(s, quote=True)


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", year="", month="", day=""):
        self.response.out.write(form % {"error": escape_html(error),
                                        "year": escape_html(year),
                                        "month": escape_html(month),
                                        "day": escape_html(day)})

    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, DUDU!')
        # self.response.write(form)
        self.write_form()

    def post(self):
        user_year = self.request.get('year')
        user_month = self.request.get('month')
        user_day = self.request.get('day')

        year = valid_year(user_year)
        month = valid_month(user_month)
        day = valid_day(user_day)

        if not (year and month and day):
            # self.response.out.write(form)
            self.write_form("Invalid Birthdate!",
                            user_day, user_month, user_year)
        else:
            self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Correct!")


# class TestPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.wirte('123')

#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.response.out.write(self.request)


app = webapp2.WSGIApplication([
    ('/', MainPage)
    # , ('/form',  TestPage)
    , ('/thanks', ThanksHandler)
], debug=True)
