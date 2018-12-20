import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

# form_html = """
# <form>
# <h2>Add a Food</h2>
# <input type="text" name="food">
# %s
# <button>Add</button>
# </form>
# """

# item_html = "<li>%s</li>"

# hidden_html = """
# <input type="hidden" name="food" value="%s">
# """

# shopping_list_html = """
# <br>
# <br>
# <h2>Shopping List</h2>
# <ul>
# %s
# </ul>
# """


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        # n = self.request.get("n")
        # if n:
        #     n = int(n)

        items = self.request.get_all("food")
        self.render("shopping_list.html", items=items)
        # self.render("shopping_list.html", name="Zihan")

        # output = form_html
        # output_hidden = ""

        # items = self.request.get_all("food")
        # if items:
        #     output_items = ""
        #     for item in items:
        #         output_hidden += hidden_html % item
        #         output_items += item_html % item

        #     output_shopping = shopping_list_html % output_items
        #     output += output_shopping

        # output = output % output_hidden

        # self.write(output)


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
