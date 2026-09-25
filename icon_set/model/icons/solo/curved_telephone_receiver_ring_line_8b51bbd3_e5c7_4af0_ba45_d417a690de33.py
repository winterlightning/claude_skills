"""Ringing Telephone Receiver.

Plan: Diagonal handset with separate lower ringing arc; bounds6,6,42,42.
Construction reference: Lucide phone: continuous curved grip and two end pads
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b51bbd3-e5c7-4af0-ba45-d417a690de33'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/phone hangup_8b51bbd3-e5c7-4af0-ba45-d417a690de33.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-telephone-receiver-ring-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('curved', 'telephone', 'receiver', 'ring', 'line')

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

        path('phone',(6,14),[('C',(12,6),(6,10),(8,6)),('L',(20,14)),('L',(16,20)),('C',(28,32),(18,24),(24,30)),('L',(34,28)),('L',(42,36)),('C',(34,42),(42,40),(38,42)),('C',(6,14),(20,42),(6,28))],True)
        path('ring',(6,38),[('C',(10,42),(7,40),(8,41))])
