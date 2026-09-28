'Luggage: smooth equal corners, widened handle opening and matching feet.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b930759-f290-469b-a412-4c466c1f838c'
SOURCE_PATH = 'pictographic-primitives/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.svg'
AUTHOR = 'gpt-6'

class Luggage(Solo48):
    icon_id = 'luggage'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('luggage', 'state')

    def build(self):
        # Luggage: smooth equal corners, widened handle opening and matching feet.
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

        r('case',8,14,40,40,4)
        p('handle',(16,14),(16,4),(32,4),(32,14))
        link('connect','handle','case')
        for x in (12,36):
            l(f'wheel-{x}',(x,40),(x,44))
            link('connect',f'wheel-{x}','case')
