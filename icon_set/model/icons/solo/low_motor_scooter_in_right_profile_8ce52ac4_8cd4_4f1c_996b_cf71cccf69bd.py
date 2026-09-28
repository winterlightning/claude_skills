"""sidecar. Revision: Restore long low scooter cowl and seat, smooth rear wheel, and angled fork. Omit small headlamp.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ce52ac4-8cd4-4f1c-996b-cf71cccf69bd'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/sidecar_8ce52ac4-8cd4-4f1c-996b-cf71cccf69bd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='low-motor-scooter-in-right-profile'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('sidecar',)

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

        path('body',(4,31),[('A',(12,23),8,8,True),('L',(20,23)),('L',(25,23)),('C',(31,19),(28,23),(29,21)),('L',(34,15))])
        path('floor',(4,31),[('L',(12,31)),('L',(20,31)),('A',(25,26),5,5,False),('L',(25,23))])
        path('rear-wheel',(4,31),[('A',(20,31),8,9,False)])
        path('seat',(12,23),[('L',(12,19)),('A',(16,15),4,4,True),('L',(20,15)),('L',(20,23))])
        poly('fork',(27,8),(32,8),(34,15),(37,26))
        circle('front-wheel',37,33,7)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
