"""Shearling Wool Pelt.

Plan: Retained the scalloped fleece and blank central face opening. Simplified small wool lobes and enlarged clearances.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '858c52c0-c021-48ac-aa6d-6739fbb88ad4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shearling_858c52c0-c021-48ac-aa6d-6739fbb88ad4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scalloped-fleece-with-plain-face-opening'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('scalloped', 'fleece', 'with', 'plain', 'face', 'opening')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('fleece',(12,12),[('C',(24,6),(10,6),(18,6)),('C',(36,12),(30,6),(38,6)),('C',(42,24),(42,12),(42,18)),('C',(36,36),(42,30),(42,36)),('C',(24,42),(36,42),(30,42)),('C',(12,36),(18,42),(12,42)),('C',(6,24),(6,36),(6,30)),('C',(12,12),(6,18),(6,12))],True)
        path('face',(18,18),[('L',(30,18)),('L',(30,26)),('A',(24,32),6,6,True),('A',(18,26),6,6,True),('L',(18,18))],True)
