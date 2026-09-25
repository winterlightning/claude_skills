"""A circular award medal with two curved ribbon tails.

Plan: Medal circle and mirrored tails share exact circle nodes; paired ribbons derive from axis 24.
Construction: ribbon: continuous loop and paired fabric ends
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b54db383-db23-4859-92c2-e71b7abb5e7a'
SOURCE_PATH = 'pictographic-primitives/other/ribbon_b54db383-db23-4859-92c2-e71b7abb5e7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ribbon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases = ()
    keywords = ('ribbon',)

    def build(self):
        # Smaller medal gives the mirrored fabric tails broad negative spaces.
        points=[(12,18),(24,6),(36,18),(24,30)]
        for i in range(4): self.add_arc(f'medal-{i}',points[i],points[(i+1)%4],radius_x=12)
        self.add_contour('medal',*(f'medal-{i}' for i in range(4)),closed=True)
        for side in (0,1):
            def p(x,y): return (48-x if side else x,y)
            n=f'tail-{side}'
            self.add_polyline(n,p(12,18),p(6,38),p(14,36),p(16,42),p(24,30))
            self.relate('connect','medal',n)
        self.relate('connect','tail-0','tail-1')

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
