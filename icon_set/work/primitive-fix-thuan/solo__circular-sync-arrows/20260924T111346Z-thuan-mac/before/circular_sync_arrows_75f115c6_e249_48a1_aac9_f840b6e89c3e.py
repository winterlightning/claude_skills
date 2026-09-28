"""Rotating Circular Sync Arrows.

Plan: Two opposing semicircular runs and squared open arrowheads, shared radius18 and center24. Bounds6,6,42,42.
Construction reference: refresh-cw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75f115c6-e249-48a1-aac9-f840b6e89c3e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sync arrow_75f115c6-e249-48a1-aac9-f840b6e89c3e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-sync-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('circular', 'sync', 'arrows')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('upper',(6,19),[('A',(24,6),18,13,True),('A',(42,19),18,13,True)])
        poly('upper-head',(30,19),(42,19),(42,8));join('upper','upper-head')
        path('lower',(42,29),[('A',(24,42),18,13,True),('A',(6,29),18,13,True)])
        poly('lower-head',(6,40),(6,29),(18,29));join('lower','lower-head')
