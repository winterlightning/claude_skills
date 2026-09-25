"""A right arrow between two open brackets.

Plan: Mirrored brackets enclose an independent directional arrow.
Construction: log-in: open bracket with directed shaft
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0bd98d1c-2291-4610-be55-e9292563a85a'
SOURCE_PATH = 'icon_set/work/todo-references/right to bracket_0bd98d1c-2291-4610-be55-e9292563a85a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-to-bracket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('right', 'to', 'bracket')

    def build(self):
        for side in (0,1):
            def p(x,y):return (48-x if side else x,y)
            n=f'bracket-{side}'
            self.add_line(n+'-top',p(14,6),p(10,6))
            self.add_arc(n+'-upper',p(10,6),p(6,10),radius_x=4,sweep=bool(side))
            self.add_line(n+'-wall',p(6,10),p(6,38))
            self.add_arc(n+'-lower',p(6,38),p(10,42),radius_x=4,sweep=bool(side))
            self.add_line(n+'-bottom',p(10,42),p(14,42))
            self.add_contour(n,*(n+s for s in ('-top','-upper','-wall','-lower','-bottom')))
        self.arrow('right',(15,24),(32,24),(24,16),(24,32))

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
