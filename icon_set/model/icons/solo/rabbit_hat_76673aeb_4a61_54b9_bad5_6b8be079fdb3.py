'Rabbit hat: clear upright and folded ears above a balanced hat with a single rim.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76673aeb-4a61-54b9-bad5-6b8be079fdb3'
SOURCE_PATH = 'icons-json/products/rabbit hat_76673aeb-4a61-54b9-bad5-6b8be079fdb3.json'
AUTHOR = 'gpt-6'

class RabbitHat(Solo48):
    icon_id = 'rabbit-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('rabbit', 'hat', 'products')

    def build(self):
        # Rabbit hat: clear upright and folded ears above a balanced hat with a single rim.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

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

        l('rim',(6,30),(42,30))
        p('hat',(12,30),(14,42),(34,42),(36,30))
        link('connect','rim','hat')
        r('upright-ear',16,6,24,30,4)
        a('folded-ear-a',(24,12),(36,18),12,6)
        a('folded-ear-b',(36,18),(24,18),6,3)
        self.add_contour('folded-ear','folded-ear-a','folded-ear-b')
        link('connect','upright-ear','rim')
        link('connect','folded-ear','upright-ear')
