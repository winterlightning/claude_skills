"""Joined the circular skull to a continuous neck and rebuilt the shoulder as a smooth arc at an exact node.
Symbol plan: Circular skull and smooth quarter-circle shoulder; continuous neck remains anatomical. Human user.svg informs circular skull and rounded shoulder. No detached head.
Final reduction: No essential parts omitted.
References: human_ref/user.svg: circular head and smooth shoulder.
Keyshape reason: Upright human profile; continuous anatomical neck, no detached head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81b8e41d-b09d-4c1f-8f67-d8dbdac1f6ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/body skeleton_81b8e41d-b09d-4c1f-8f67-d8dbdac1f6ff.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='right-facing-human-profile'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('right', 'facing', 'human', 'profile')
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
        path('profile',(24,44),[(24,32),(24,28),((12,16),12,12,True),((24,4),12,12,True),((36,16),12,12,True),(40,22),(34,24),(34,32),(32,32)])
        path('shoulder',(8,44),[((24,32),16,12,True)]);join('profile','shoulder')
