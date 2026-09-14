'VR headset: true circular head and a symmetric rounded visor, removing wavy fitted edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0284d3a8-c0bf-450e-8702-f6e30af3b263'
SOURCE_PATH = 'icons-json/technology/reality vr_0284d3a8-c0bf-450e-8702-f6e30af3b263.json'
AUTHOR = 'gpt-6'

class RealityVr(Solo48):
    icon_id = 'reality-vr'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('reality', 'vr', 'technology')

    def build(self):
        # VR headset: smooth head arcs end at the visor, removing tiny overlap pockets.
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

        a('head-top',(10,14),(38,14),14,8)
        a('head-bottom',(38,32),(10,32),14,10)
        r('goggles',6,14,42,32,4)
        link('connect','head-top','goggles')
        link('connect','head-bottom','goggles')
