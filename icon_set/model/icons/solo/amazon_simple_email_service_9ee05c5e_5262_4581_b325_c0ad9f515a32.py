'Email service: coherent envelope and network nodes, replacing tiny distorted node loops.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ee05c5e-5262-4581-b325-c0ad9f515a32'
SOURCE_PATH = 'icons-json/_uncategorized_02/amazon simple email service_9ee05c5e-5262-4581-b325-c0ad9f515a32.json'
AUTHOR = 'gpt-6'

class AmazonSimpleEmailService(Solo48):
    icon_id = 'amazon-simple-email-service'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'simple', 'email', 'service', '_uncategorized_02')

    def build(self):
        # Email service: coherent envelope and network nodes, replacing tiny distorted node loops.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        r('envelope',6,6,42,24,3)
        p('flap',(6,6),(24,17),(42,6))
        link('connect','flap','envelope')
        l('stem',(24,24),(24,33))
        p('network',(9,36),(9,33),(39,33),(39,36))
        link('connect','stem','envelope')
        link('connect','stem','network')
        for x in (9,24,39):
            c(f'node-{x}',x,39,3)
        link('connect','network','node-9')
        link('connect','network','node-39')
        l('middle',(24,33),(24,36))
        link('connect','middle','stem')
        link('connect','middle','network')
        link('connect','middle','node-24')
