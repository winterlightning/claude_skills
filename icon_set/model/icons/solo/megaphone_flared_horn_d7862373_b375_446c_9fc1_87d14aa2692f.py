"""Public Announcement Megaphone.

Plan: Angled megaphone bounds4,8,44,40. Sloping horn preserves source perspective; attached handle and rounded rear.
Construction reference: Lucide megaphone: three parts joined at shared endpoints; intentional perspective
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7862373-b375-446c-9fc1-87d14aa2692f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/advertising megaphone_d7862373-b375-446c-9fc1-87d14aa2692f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'megaphone-flared-horn'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('megaphone', 'flared', 'horn')

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

        path('housing',(8,18),[('L',(14,18)),('L',(16,28)),('L',(8,30)),('A',(4,26),4,4,True),('L',(4,22)),('A',(8,18),4,4,True)],True)
        poly('horn',(14,18),(38,8),(44,32),(23,29),(16,28));join('horn','housing')
        poly('handle',(8,30),(8,40),(23,40),(23,29));join('handle','housing');join('handle','horn')
