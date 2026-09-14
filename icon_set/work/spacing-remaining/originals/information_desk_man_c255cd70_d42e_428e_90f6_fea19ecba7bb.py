'Information desk: circular head with exact 4-unit ink gap above the shoulders and a clear desk band.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c255cd70-d42e-428e-90f6-fea19ecba7bb'
SOURCE_PATH = 'icons-json/wayfinding/information desk man_c255cd70-d42e-428e-90f6-fea19ecba7bb.json'
AUTHOR = 'gpt-6'

class InformationDeskMan(Solo48):
    icon_id = 'information-desk-man'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('information', 'desk', 'man', 'wayfinding')

    def build(self):
        # Information desk: circular head with exact 4-unit ink gap above the shoulders and a clear desk band.
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

        # Shared full_body_ref.png: round head, simple body, exactly 4 units of ink gap.
        c('head',24,11,5)
        p('shoulders',(12,32),(16,24),(32,24),(36,32))
        r('desk',6,32,42,40,2)
        link('connect','desk','shoulders')
        for x in (10,38):
            l(f'leg-{x}',(x,40),(x,42))
            link('connect',f'leg-{x}','desk')
