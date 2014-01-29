import tornado.ioloop
import tornado.web
import new_parse_csv
import tornado.template
import os

cwd = os.getcwd()

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    #self.write(parse_csv.get_oncall())
    self.render("index.html", names=new_parse_csv.get_oncall())

application = tornado.web.Application([
  (r"/", MainHandler),
  (r"/(.*\.css)", tornado.web.StaticFileHandler, {"path": cwd}),
  (r"/(.*\.png)", tornado.web.StaticFileHandler, {"path": cwd}),
])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
