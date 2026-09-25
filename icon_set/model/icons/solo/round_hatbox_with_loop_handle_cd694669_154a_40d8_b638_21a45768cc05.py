"""Rebuilt the lid with tangent corners and attached the handle at exact shared endpoints.
Symbol plan: Cylinder with oval lid and broad semicircular loop handle seated at actual shared lid endpoints. Lucide cylinder informs equal curved top and bottom.
Final reduction: Double lid band omitted; top rear rim has a short flat span to support legal exact handle nodes.
References: Lucide cylinder original and atomic-debug: equal cylindrical side curves.
Keyshape reason: Tall handled cylinder.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd694669-154a-40d8-b638-21a45768cc05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hatbox_cd694669-154a-40d8-b638-21a45768cc05.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-hatbox-with-loop-handle'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('round', 'hatbox', 'with', 'loop', 'handle')
    def build(self):

        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                m=f"{n}-{i}"
                if len(step)==2:
                    self.add_line(m,p,step);p=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(m,p,end,radius_x=rx,radius_y=ry,sweep=sweep);p=end
                members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[((x,y-r),r,r,True),((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('lid',(8,24),[((16,16),8,8,True),(32,16),((40,24),8,8,True),((24,32),16,8,True),((8,24),16,8,True)],True)
        path('body',(8,24),[(8,36),((24,44),16,8,False),((40,36),16,8,False),(40,24)]);join('body','lid')
        path('handle',(16,16),[(16,12),((32,12),8,8,True),(32,16)]);join('handle','lid')
