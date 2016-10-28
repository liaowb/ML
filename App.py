#coding:utf-8
import tornado.ioloop
import tornado.web
import Route

url = Route.getAppRoute()
application =  tornado.web.Application(
    url
)

if __name__ == "__main__":
    port = 8888
    application.listen(port)
    print("server on http://127.0.0.1:%s/" %(port))
    tornado.ioloop.IOLoop.instance().start()