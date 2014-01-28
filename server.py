import tornado.ioloop
import tornado.web
import new_parse_csv

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write(new_parse_csv.get_oncall())

application = tornado.web.Application([
  (r"/", MainHandler),
])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
