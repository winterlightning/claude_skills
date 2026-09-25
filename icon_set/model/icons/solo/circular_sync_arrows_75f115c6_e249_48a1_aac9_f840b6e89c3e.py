"""Two opposing circular sync arrows share radius 20 and diagonal arrowheads.
Construction: refresh-cw: two coherent arcs with attached heads
Reduction: No omissions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75f115c6-e249-48a1-aac9-f840b6e89c3e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sync arrow_75f115c6-e249-48a1-aac9-f840b6e89c3e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-sync-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('circular', 'sync', 'arrows')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('upper',(4,24),[('A',(24,4),20,20,True),('A',(40,12),20,20,True)])
        poly('upper-tip',(31,12),(40,12),(40,16));join('upper','upper-tip')
        path('lower',(44,24),[('A',(24,44),20,20,True),('A',(8,36),20,20,True)])
        poly('lower-tip',(17,36),(8,36),(8,32));join('lower','lower-tip')
