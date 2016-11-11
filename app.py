import  analisis_data
import web

data = analisis_data.Analisis()
data.data_read("data.csv")

render = web.template.render('views/')

urls = ('/','index',
        '/datos(.*)','datos',
        '/mapa','mapa')

class index:
    def GET(self):
        return render.index()

class datos:
    def GET(self, datos):
        datos = data.data_get()
        return  render.datos(datos)

class mapa:
    def GET(self):
        return render.mapa()

if __name__ == '__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
