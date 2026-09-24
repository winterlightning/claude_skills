"""Clockwise return clock with full circular curvature, open lower gap and diagonal arrowhead.
Construction: refresh-cw: circular arrow construction
Reduction: No omissions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ae0f802-0947-49ab-948b-a13314a05022'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/snooze return repeat_4ae0f802-0947-49ab-948b-a13314a05022.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clock-with-clockwise-return-arrow'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('clock', 'with', 'clockwise', 'return', 'arrow')
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

        path('rim',(24,44),[('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True)])
        poly('tip',(36,32),(36,40),(27,40));join('rim','tip')
        poly('hands',(24,13),(24,24),(32,24))
