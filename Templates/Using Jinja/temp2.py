import os
import webapp2
import jinja2

form_html="""
<form>
<h2>Add a food</h2>
<input type="text" name="food">
<input type="hidden" name="food" value="eggs"
<button>Add</button>
</form>
"""

hidden_html="""
<input tpye="hidden" name="food" value="%s">
"""
item_html="<li>%s</li>"

shopping_list_html="""
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

    def render_str(self,template,**params):
        t=jinja_env.get_template(template)
        return t.render(params)

    def render(self,template,**kw):
        self.write(self.render_str(template, **kw))
    

class MainPage(Handler):
    def get(self):
        n=self.request.get("n")
        if n:
            n=int(n)
        self.render("shoo_list.html",n=n)
        

        # items=self.request.get_all("food")
        # if items:
        #     output_items=""
        #     for item in items:
        #         output_hidden+=hidden_html%item
        #         output_items+=item_html%item

        #     output_shopping=shopping_list_html % output_items
        #     output+=output_shopping
        
        # output=output % output_hidden
        # self.write(output)
        
class FizzBuzzHandler(Handler):
    def get(self):
        n=self.request.get('n',0)
        n=n and int(n)
        self.render('fizzbuzz.html',n=n)
app=webapp2.WSGIApplication([('/',MainPage),],debug=True)