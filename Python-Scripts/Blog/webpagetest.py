import webapp2

form = """
<form action="/form">
    <input name="q">
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, DUDU!')
        self.response.write(form)


class TestPage(webapp2.RequestHandler):
    def get(self):
        self.response.wirte('123')

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.response.out.write(self.request)


app = webapp2.WSGIApplication([
    ('/', MainPage), ('/form',  TestPage)
], debug=True)
