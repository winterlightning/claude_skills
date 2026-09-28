"""Short Sleeve Dress.

Plan: Retained the round-neck dress, short sleeves, waist and flared skirt. Simplified the gently curved hem to a broad baseline.
Construction reference: Lucide shirt neckline/sleeve construction; source-specific dress waist and skirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f4db51e-f5e5-4d53-a35b-a7aefa4efb3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dressing_5f4db51e-f5e5-4d53-a35b-a7aefa4efb3b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'short-sleeved-dress-with-flared-skirt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('short', 'sleeved', 'dress', 'with', 'flared', 'skirt')

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

        path('dress',(18,4),[('A',(30,4),6,6,False),('L',(34,6)),('L',(40,14)),('L',(34,20)),('L',(30,16)),('L',(30,26)),('L',(38,44)),('L',(10,44)),('L',(18,26)),('L',(18,16)),('L',(14,20)),('L',(8,14)),('L',(14,6)),('L',(18,4))],True)
        line('waist',(18,26),(30,26));join('waist','dress')
