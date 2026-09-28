"""water bottle. Revision: Smooth symmetric shoulders and shallow waist; retain cap seam and broad label band. Omit lower decorative seam.
Construction: Lucide milk: paired shoulders and rounded base. Preserve source-facing direction and arrangement.
Keyshape VRECT_M; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eaae1a7b-a649-5e77-afca-1508b1d56891'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/water bottle_eaae1a7b-a649-5e77-afca-1508b1d56891.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='plastic-water-bottle-with-waist-and-label-band'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases=()
    keywords=('water', 'bottle')

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

        path('bottle',(18,4),[('L',(30,4)),('L',(30,12)),('C',(38,22),(30,16),(38,17)),('L',(38,30)),('C',(36,35),(38,32),(36,33)),('C',(38,40),(36,37),(38,38)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('C',(12,35),(10,38),(12,37)),('C',(10,30),(12,33),(10,32)),('L',(10,22)),('C',(18,12),(10,17),(18,16)),('L',(18,4))],True)
        line('cap-seam',(18,12),(30,12))
        for y in (22,30):line('label-'+str(y),(10,y),(38,y));join('label-'+str(y),'bottle')

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
