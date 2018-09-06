import os
import io
import json

import tornado.ioloop
from tornado import gen
import tornado.web

from PIL import Image

PORT = os.getenv("HYPY_PORT", 4649)

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        try:
            data = self.request.files['file'][0]['body']
            img = Image.open(io.BytesIO(data))
            print(img)
        except:
            err_msg = '''
            
            The curl command is not wrong?
            
            $ curl -X POST -F file=@{your_brilliant_datafile} {endpoint/syamu}
            
            take it easy! :)
            
            '''
            d = {"msg":err_msg}
            self.write(json.dumps(d))
            img = None

        return img

application = tornado.web.Application([
    (r'/syamu', MainHandler)
])

if __name__ == '__main__':
    application.listen(PORT)
    tornado.ioloop.IOLoop.current().start()