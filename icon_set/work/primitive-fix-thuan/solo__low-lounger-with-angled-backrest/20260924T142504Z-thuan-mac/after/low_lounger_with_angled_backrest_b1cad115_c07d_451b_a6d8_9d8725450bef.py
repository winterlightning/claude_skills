"""daybed. Revision: Smooth padded backrest into long seat; reposition leg contacts directly on underside. Preserve both legs.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b1cad115-c07d-451b-a6d8-9d8725450bef'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__low-lounger-with-angled-backrest/20260924T142504Z-thuan-mac/reference/daybed_b1cad115-c07d-451b-a6d8-9d8725450bef.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='low-lounger-with-angled-backrest'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('daybed',)

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

        path('seat',(4,12),[('A',(8,8),4,4,True),('C',(11,10),(9,8),(10,9)),('L',(23,22)),('L',(38,22)),('A',(44,28),6,6,True),('L',(44,32)),('L',(38,32)),('L',(16,32)),('L',(5,17)),('C',(4,12),(4,16),(4,14))],True)
        line('leg-left',(16,32),(14,40));line('leg-right',(38,32),(40,40))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
