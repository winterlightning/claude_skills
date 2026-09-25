"""Fresh Cauliflower Floret.

Plan: Lobed cauliflower crown with branching base. Bounds6,6,42,42. Omit fine crown texture.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b41dda21-b80f-4717-8407-aa466a10e230'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cauliflower_b41dda21-b80f-4717-8407-aa466a10e230.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cauliflower-crown-on-stalk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('cauliflower', 'crown', 'on', 'stalk')

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

        path('crown',(14,30),[('A',(6,22),8,8,True),('A',(14,14),8,8,True),('C',(24,6),(14,8),(18,6)),('C',(34,14),(30,6),(34,8)),('A',(42,22),8,8,True),('A',(34,30),8,8,True),('L',(14,30))],True)
        poly('stalk',(16,30),(20,42),(28,42),(32,30));join('stalk','crown')
