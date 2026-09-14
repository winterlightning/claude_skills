'Charging battery: spacious terminal and a clear lightning stroke inside a balanced body.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eb92da5-29c0-4d92-ae40-851bdeae1749'
SOURCE_PATH = 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'
AUTHOR = 'gpt-6'


class BatteryChargingVertical(Solo48):
    icon_id = 'battery-charging-vertical'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('battery', 'charging', 'power', 'energy', 'charge', 'electric', 'level', 'device')

    def build(self):
        # Charging battery: spacious terminal and a clear lightning stroke inside a balanced body.
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

        r('body',8,14,40,44,4)
        p('terminal',(16,14),(16,4),(32,4),(32,14))
        link('connect','terminal','body')
        p('charge',(26,23),(18,30),(29,30),(22,35))
