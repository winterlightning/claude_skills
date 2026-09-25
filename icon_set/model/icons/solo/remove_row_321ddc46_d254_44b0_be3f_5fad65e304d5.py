"""A deletion cross beside two spreadsheet row rules.

Plan: Two row rules share endpoints; cross is centered beside their gap.
Construction: table: straight repeated rules
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '321ddc46-d254-44b0-be3f-5fad65e304d5'
SOURCE_PATH = 'icon_set/work/todo-references/remove row_321ddc46-d254-44b0-be3f-5fad65e304d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'remove-row'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('remove', 'row')

    def build(self):
        self.add_line('row-top',(24,10),(44,10))
        self.add_line('row-bottom',(24,38),(44,38))
        self.add_polyline('cross-a',(4,18),(10,24),(16,30))
        self.add_polyline('cross-b',(4,30),(10,24),(16,18))
        for a in (1,2):
            for b in (1,2):self.relate('connect',f'cross-a-{a}',f'cross-b-{b}')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, l, t, r, b, rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i in range(8):
            a,z=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def arrow(self, name, start, tip, wing1, wing2):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',wing1,tip,wing2)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')

    def heart(self, name, x, top, half, bottom):
        # Mirrored lobes share dimensions and meet the pointed lower silhouette.
        self.add_bezier(name+'-left',(x,top+2),((x-half,top-5),(x-half-3,top+4),(x-half,top+7)),((x-half+2,top+10),(x, bottom),(x,bottom)))
        self.add_bezier(name+'-right',(x,bottom),((x,bottom),(x+half-2,top+10),(x+half,top+7)),((x+half+3,top+4),(x+half,top-5),(x,top+2)))
        self.add_contour(name,name+'-left',name+'-right',closed=True)
