"""Standard Mail Envelope.

Plan: Symmetric envelope, flap and lower seams. Bounds4,10,44,38. Shared seam nodes maintain true contact.
Construction reference: mail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ee84a73-bec7-4c14-9550-87c854a35f45'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mail_7ee84a73-bec7-4c14-9550-87c854a35f45.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standard-mail-envelope'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('standard', 'mail', 'envelope')

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

        poly('body',(4,10),(44,10),(44,38),(4,38),closed=True)
        poly('flap',(4,10),(16,22),(24,30),(32,22),(44,10));join('body','flap')
        line('left-seam',(4,38),(16,22));line('right-seam',(44,38),(32,22))
        for n in ('left-seam','right-seam'): join(n,'body');join(n,'flap')
