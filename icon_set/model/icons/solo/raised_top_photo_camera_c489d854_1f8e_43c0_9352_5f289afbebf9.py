"""camera settings rotate. Revision: Round raised housing transitions symmetrically and center the lens in the body. No defining parts omitted.
Construction: Lucide camera: mirrored smooth shoulder transitions and one centered lens. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c489d854-1f8e-43c0-9352-5f289afbebf9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/camera settings rotate_c489d854-1f8e-43c0-9352-5f289afbebf9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='raised-top-photo-camera'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('camera', 'settings', 'rotate')

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

        path('shell',(8,14),[('L',(11,14)),('C',(17,10),(14,14),(15,12)),('C',(21,8),(18,8),(19,8)),('L',(27,8)),('C',(31,10),(29,8),(30,8)),('C',(37,14),(33,12),(34,14)),('L',(40,14)),('A',(44,18),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,18)),('A',(8,14),4,4,True)],True)
        circle('lens',24,25,6)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
