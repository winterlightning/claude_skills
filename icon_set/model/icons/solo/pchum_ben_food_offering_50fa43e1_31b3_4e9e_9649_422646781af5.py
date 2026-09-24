"""pchum ben acnestor day. Revision: Smooth bottle shoulders, broaden leaf and parcel so their openings survive. Retain one representative leaf and food parcel; omit bottle bands, second leaf and second parcel.
Construction: Lucide milk: symmetric shoulders and rounded base. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '50fa43e1-31b3-4e9e-9649-422646781af5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/pchum ben acnestor day_50fa43e1-31b3-4e9e-9649-422646781af5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pchum-ben-food-offering'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='holidays'
    aliases=()
    keywords=('pchum', 'ben', 'acnestor', 'day')

    def build(self):
        # Each contour owns its shape. Repeated parts share dimensions and axes.
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for j,s in enumerate(steps):
                k=f'{n}-{j}';kind,q,*v=s
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
                elif kind=='C': self.add_bezier(k,p,(v[0],v[1],q))
                members.append(k);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*p):self.add_polyline(n,*p)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b):self.relate('connect',a,b)

        path('bottle',(10,6),[('L',(18,6)),('L',(18,14)),('C',(22,22),(18,18),(22,18)),('L',(22,38)),('A',(18,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,22)),('C',(10,14),(6,18),(10,18)),('L',(10,6))],True)
        path('leaf',(33,6),[('C',(42,17),(38,8),(42,12)),('C',(32,24),(42,23),(36,24)),('C',(33,6),(30,20),(30,13))],True)
        poly('parcel',(32,33),(39,33),(42,42),(30,42),(32,33))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
