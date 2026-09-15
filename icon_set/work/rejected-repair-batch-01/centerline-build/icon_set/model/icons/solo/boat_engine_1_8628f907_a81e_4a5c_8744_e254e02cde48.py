'Outboard motor: tangent engine corners, an 8-unit drive shaft and clear propeller.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8628f907-a81e-4a5c-8744-e254e02cde48'
SOURCE_PATH = 'pictographic-primitives/transportation/boat engine 1_8628f907-a81e-4a5c-8744-e254e02cde48.svg'
AUTHOR = 'gpt-6'

class BoatEngine1(Solo48):
    icon_id = 'boat-engine-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('boat', 'engine', 'transportation')

    def build(self):
        # Outboard motor: tangent engine corners, an 8-unit drive shaft and clear propeller.
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

        r('engine',16,4,40,20,4)
        l('tiller',(8,16),(16,16))
        link('connect','tiller','engine')
        p('shaft',(24,20),(24,40),(28,44),(32,44),(32,20))
        link('connect','shaft','engine')
        l('propeller',(32,36),(40,36))
        l('propeller-end',(40,30),(40,42))
        link('connect','shaft','propeller')
        link('connect','propeller','propeller-end')
