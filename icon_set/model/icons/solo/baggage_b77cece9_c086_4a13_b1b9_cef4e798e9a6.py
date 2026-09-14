'Suitcase: balanced rounded case, equal wheels, and a 10-unit handle opening.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b77cece9-c086-4a13-b1b9-cef4e798e9a6'
SOURCE_PATH = 'icons-json/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.json'
AUTHOR = 'gpt-6'

class Baggage(Solo48):
    icon_id = 'baggage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('baggage', 'travel')

    def build(self):
        # Suitcase: balanced rounded case, equal wheels, and a 10-unit handle opening.
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

        r('case',6,16,42,38,4)
        p('handle',(16,16),(16,6),(32,6),(32,16))
        link('connect','handle','case')
        for x in (14,34):
            l(f'wheel-{x}',(x,38),(x,42))
            link('connect',f'wheel-{x}','case')
