import asyncio
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self, ):
        self.write("Hello world!")

def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ]
    )
#end def


async def main():
    app = make_app()
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()
#end aysnc def

if __name__ == "__main__":
    asyncio.run(main())
#endif

