"""Closed the baby head, integrated the ears into its silhouette, and rebuilt the top curl.
Symbol plan: Closed circular baby face, integrated ears and one top curl; Lucide baby informs circular face and curl; human user.svg supplies circular anatomy. Facial dots omitted because source is blank.
Final reduction: Facial dots omitted because the source face is blank.
References: Lucide baby original and atomic-debug; human_ref/user.svg circular anatomy.
Keyshape reason: Radial head and ears; no body or detached gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ec01feb-4215-413d-9fe1-82f8e7660a71'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baby boy_4ec01feb-4215-413d-9fe1-82f8e7660a71.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='round-baby-head-with-one-curl'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('round', 'baby', 'head', 'with', 'one', 'curl')
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
        path('head',(8,20),[((24,4),16,16,True),((40,20),16,16,True),((44,24),4,4,True),((40,28),4,4,True),((24,44),16,16,True),((8,28),16,16,True),((4,24),4,4,True),((8,20),4,4,True)],True)
        path('curl',(24,4),[((30,10),6,6,True),((24,16),6,6,True),((18,10),6,6,True)]);join('curl','head')
