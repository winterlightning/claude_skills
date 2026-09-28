"""Public Announcement Megaphone.

Plan: Megaphone bounds4,8,44,40. Rounded rear joins flared horn with downward handle. Shared attachment coordinates.
Construction reference: Lucide megaphone: joined rear housing, flared horn and attached handle
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bac73377-8266-4be0-ab30-2c147588004d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/ligula_bac73377-8266-4be0-ab30-2c147588004d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'megaphone-reference-bac73377'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('megaphone', 'reference', 'bac73377')

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

        path('housing',(8,16),[('L',(16,16)),('L',(16,28)),('L',(8,28)),('A',(4,24),4,4,True),('L',(4,20)),('A',(8,16),4,4,True)],True)
        poly('horn',(16,16),(44,8),(44,36),(23,30),(16,28));join('horn','housing')
        poly('handle',(8,28),(8,40),(23,40),(23,30));join('handle','housing');join('handle','horn')
