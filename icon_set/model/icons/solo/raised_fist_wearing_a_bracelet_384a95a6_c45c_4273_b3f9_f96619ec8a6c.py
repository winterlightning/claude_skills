"""romance pride lgbt bracelet fist. Revision: Shape four rounded knuckles with short finger grooves, restore a curved thumb, and keep the broad bracelet. Omit bracelet striping.
Construction: Shared human_ref minimal anatomy; Lucide hand: round fingers and coherent palm. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '384a95a6-c45c-4273-b3f9-f96619ec8a6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/romance pride lgbt bracelet fist_384a95a6-c45c-4273-b3f9-f96619ec8a6c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='raised-fist-wearing-a-bracelet'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('romance', 'pride', 'lgbt', 'bracelet', 'fist')

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

        path('fist',(14,36),[('L',(14,31)),('C',(8,23),(9,28),(8,26)),('L',(8,18)),('L',(8,10)),('A',(16,10),4,4,True),('L',(16,8)),('A',(24,8),4,4,True),('A',(32,8),4,4,True),('L',(32,10)),('A',(40,10),4,4,True),('L',(40,22)),('C',(34,31),(40,27),(34,28)),('L',(34,36))])
        path('thumb',(8,18),[('L',(18,18)),('A',(24,24),6,6,True),('L',(24,26))])
        path('bracelet',(12,36),[('L',(14,36)),('L',(34,36)),('L',(36,36)),('A',(36,44),4,4,True),('L',(12,44)),('A',(12,36),4,4,True)],True)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
