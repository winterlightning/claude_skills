"""shipper. Revision: Restore two complete circular wheels, soften cargo corners, preserve angled windshield and cargo divider. Omit window crossbar.
Construction: Lucide truck: complete circular wheels, shared chassis and rounded cargo corners. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6bb7f733-561a-4d2b-a952-3879ff5bb90f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/shipper_6bb7f733-561a-4d2b-a952-3879ff5bb90f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='plain-box-delivery-truck'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('shipper',)

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

        circle('rear-wheel',12,34,6);circle('front-wheel',36,34,6)
        path('cargo',(6,34),[('L',(4,34)),('L',(4,12)),('A',(8,8),4,4,True),('L',(24,8)),('L',(24,16)),('L',(24,34)),('L',(18,34))])
        path('cab',(24,16),[('L',(34,16)),('L',(44,26)),('L',(44,34)),('L',(42,34))])
        line('sill',(24,34),(30,34))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
