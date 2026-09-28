"""Round Bottom Chemistry Flask.

Plan: Symmetric neck and round belly; bounds8,4,40,44. Wide single lip replaces the source double lip.
Construction reference: flask-round.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db5d0816-6bfc-489d-95c5-5623b4efb1c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/beaker_db5d0816-6bfc-489d-95c5-5623b4efb1c5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-bottom-flask-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('round', 'bottom', 'flask', 'solo')

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

        path('flask',(18,4),[('L',(18,16)),('C',(8,28),(12,18),(8,22)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('C',(30,16),(40,22),(36,18)),('L',(30,4))])
        poly('lip',(14,4),(18,4),(30,4),(34,4));join('lip','flask')
