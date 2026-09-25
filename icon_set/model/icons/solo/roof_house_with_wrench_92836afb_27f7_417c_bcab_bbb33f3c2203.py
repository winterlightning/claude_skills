"""A house roof above a double-ended wrench.

Plan: Roof apex centered above a horizontal shaft; wrench jaws mirror around x24 and y34.
Construction: wrench: open jaws attached to a continuous shaft
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92836afb-27f7-417c-bcab-bbb33f3c2203'
SOURCE_PATH = 'icon_set/work/todo-references/roof house with wrench_92836afb-27f7-417c-bcab-bbb33f3c2203.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'roof-house-with-wrench'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('roof', 'house', 'with', 'wrench')

    def build(self):
        self.add_polyline('roof',(4,18),(24,8),(44,18))
        for side in (0,1):
            def p(x,y):return (48-x if side else x,y)
            n=f'jaw-{side}'
            self.add_line(n+'-upper-lip',p(6,28),p(10,28))
            self.add_arc(n+'-upper',p(10,28),p(16,34),radius_x=6,sweep=not bool(side))
            self.add_arc(n+'-lower',p(16,34),p(10,40),radius_x=6,sweep=not bool(side))
            self.add_line(n+'-lower-lip',p(10,40),p(6,40))
            self.add_contour(n,*(n+s for s in ('-upper-lip','-upper','-lower','-lower-lip')))
        self.add_line('shaft',(16,34),(32,34))
        for side in (0,1):
            for suffix in ('-upper','-lower'):self.relate('connect','shaft',f'jaw-{side}'+suffix)

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
