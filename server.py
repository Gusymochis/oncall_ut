import tornado.ioloop
import tornado.web
import parse_csv as parse
import tornado.template
import os

cwd = os.getcwd()

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    attrib = parse.get_oncall()
    print "date=%s" % attrib['date']
    print "img=%s" % attrib['user1'][1]
    print "img=%s" % attrib['user2'][1]

    #v_img1=attrib['user1'][1]
    #v_img2=attrib['user2'][1]
    self.render("index.html", data=attrib)

application = tornado.web.Application([
  (r"/", MainHandler),
  (r"/(.*\.css)", tornado.web.StaticFileHandler, {"path": cwd}),
  (r"/attr/pictures/(.*)", tornado.web.StaticFileHandler, {"path": "./attr/pictures"}),
])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
