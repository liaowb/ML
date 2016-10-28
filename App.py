import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = 8888
    application.listen(port)
    print("server on http://127.0.0.1:%s/" %(port))
    tornado.ioloop.IOLoop.instance().start()