"""Sealed Letter Envelope.

Plan: Mirror flap around24. Bounds4,10,44,38; blank lower envelope.
Construction reference: mail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50118f35-5541-4d2d-9d74-c57099d07377'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mail_50118f35-5541-4d2d-9d74-c57099d07377.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sealed-envelope'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('sealed', 'envelope')

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

        path('body',(4,14),[('A',(8,10),4,4,True),('L',(40,10)),('A',(44,14),4,4,True),('L',(44,34)),('A',(40,38),4,4,True),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,14))],True)
        poly('flap',(4,14),(24,26),(44,14));join('body','flap')
