"""Front car section with a flowing roof-to-hood transition and circular wheel.
Plan: Front car section with a flowing roof-to-hood transition and circular wheel.
Construction: Lucide truck: tangential round corners and circular wheel; source gives cropped front section.
Omissions: Hub circle omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '3db3961f-b690-449d-b4da-3a42295c5b5d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/fender_3db3961f-b690-449d-b4da-3a42295c5b5d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='front-car-section-with-wheel'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('front', 'car', 'section', 'with', 'wheel')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        circle('wheel',30,34,6)
        path('upper-body',(4,8),[('L',(13,8)),('C',(29,18),(21,8),(23,18)),('L',(38,18)),('A',(44,24),6,6,True),('L',(44,28)),('C',(36,34),(44,32),(40,34))]);join('upper-body','wheel')
        path('lower-body',(4,20),[('L',(4,30)),('A',(8,34),4,4,False),('L',(24,34))]);join('lower-body','wheel')
