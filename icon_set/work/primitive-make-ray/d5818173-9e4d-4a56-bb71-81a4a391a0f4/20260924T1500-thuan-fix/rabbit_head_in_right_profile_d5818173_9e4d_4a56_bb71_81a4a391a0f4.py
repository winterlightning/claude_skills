"""angora. Revision: Round the two ear tips and define the muzzle with a calm jaw-to-neck curve. Omit tiny mouth and eye.
Construction: Lucide rabbit: rounded upright ears and coherent projecting muzzle. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d5818173-9e4d-4a56-bb71-81a4a391a0f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rabbit-head-in-right-profile/20260924T150007Z-thuan-mac/reference/angora_d5818173-9e4d-4a56-bb71-81a4a391a0f4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='rabbit-head-in-right-profile'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('angora',)

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

        path('rabbit',(8,44),[('C',(14,29),(8,38),(14,36)),('L',(14,23)),('C',(10,7),(8,19),(8,11)),('C',(14,4),(10,4),(12,4)),('C',(23,20),(20,7),(23,12)),('L',(23,7)),('C',(29,5),(23,4),(27,4)),('C',(31,20),(32,8),(31,15)),('C',(37,28),(34,21),(36,24)),('C',(40,32),(39,29),(40,30)),('C',(31,36),(40,37),(35,38)),('C',(34,44),(30,40),(34,41))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
