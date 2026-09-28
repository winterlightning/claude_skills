'Television: natural wide screen, smooth corners and 10 units between screen and foot.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea5bd386-4f06-5935-9cb1-e87243d819f7'
SOURCE_PATH = 'pictographic-primitives/tv/modern tv flat screen_ea5bd386-4f06-5935-9cb1-e87243d819f7.svg'
AUTHOR = 'gpt-6'

class ModernTvFlatScreen(Solo48):
    icon_id = 'modern-tv-flat-screen'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    categories = ('tv', 'primitives')
    aliases = ()
    keywords = ('modern', 'tv', 'flat', 'screen')

    def build(self):
        # Television: natural wide screen, smooth corners and 10 units between screen and foot.
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

        r('screen',4,8,44,30,4)
        l('stand',(24,30),(24,40))
        l('foot',(14,40),(34,40))
        link('connect','stand','screen')
        link('connect','stand','foot')
