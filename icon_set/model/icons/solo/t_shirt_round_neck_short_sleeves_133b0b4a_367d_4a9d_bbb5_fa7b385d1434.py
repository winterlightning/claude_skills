"""Short Sleeved T-shirt.

Plan: Retained the complete plain short-sleeved T-shirt silhouette. Preserved its distinct source UUID despite similarity to the neighboring tee.
Construction reference: Lucide shirt: complete connected garment and circular neck opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '133b0b4a-367d-4a9d-bbb5-fa7b385d1434'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/raiment_133b0b4a-367d-4a9d-bbb5-fa7b385d1434.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 't-shirt-round-neck-short-sleeves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('t', 'shirt', 'round', 'neck', 'short', 'sleeves')

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

        path('shirt',(18,6),[('A',(30,6),6,6,False),('L',(34,6)),('L',(42,16)),('L',(36,22)),('L',(32,18)),('L',(32,42)),('L',(16,42)),('L',(16,18)),('L',(12,22)),('L',(6,16)),('L',(14,6)),('L',(18,6))],True)
