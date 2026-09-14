'Switch plate: centered rocker, consistent corner radii and equal 8-unit rocker halves.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69a3714e-47a4-5c41-9c78-1b1b26a4a41c'
SOURCE_PATH = 'icons-json/interface-essential/switch on_69a3714e-47a4-5c41-9c78-1b1b26a4a41c.json'
AUTHOR = 'gpt-6'

class SwitchOn(Solo48):
    icon_id = 'switch-on'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('switch', 'on', 'interface-essential')

    def build(self):
        # Switch plate: centered rocker, consistent corner radii and equal 8-unit rocker halves.
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

        r('plate',6,6,42,42,4)
        r('switch',16,16,32,32,3)
        l('seam',(16,24),(32,24))
        link('connect','switch','seam')
