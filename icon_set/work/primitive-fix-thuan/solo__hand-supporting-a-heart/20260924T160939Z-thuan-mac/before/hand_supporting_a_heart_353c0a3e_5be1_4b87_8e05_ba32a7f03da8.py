"""Hand Holding Heart.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
A clear heart sits above an open supporting hand. Fine finger divisions are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-heart.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '353c0a3e-5be1-4b87-8e05-ba32a7f03da8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/romance pride lgbt heart hand holding_353c0a3e-5be1-4b87-8e05-ba32a7f03da8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-supporting-a-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hand', 'supporting', 'a', 'heart')

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

        path('thumb',(6,30),[('L',(14,24)),('L',(20,24)),('L',(24,24)),('A',(24,32),4,4,True),('L',(18,32))])
        path('palm',(6,42),[('L',(26,42)),('L',(36,34)),('A',(36,22),6,6,False),('L',(24,32))]);join('thumb','palm')

        path('heart',(20,24),[('L',(10,14)),('C',(14,6),(6,10),(10,6)),('C',(20,10),(18,6),(20,8)),('C',(26,6),(20,8),(22,6)),('C',(30,14),(30,6),(34,10)),('L',(20,24))],True);join('heart','thumb')
