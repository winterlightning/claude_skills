"""Full Beard and Mustache.

Plan: Symmetric broad beard with pointed chin and integrated mustache top. Bounds6,6,42,42. Remove hair strands.
Construction reference: human_ref/user.svg.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79b021f5-047e-42ed-b099-1d623460924c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beard_79b021f5-047e-42ed-b099-1d623460924c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-beard-with-a-broad-mustache'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('pointed', 'beard', 'with', 'a', 'broad', 'mustache')

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

        path('beard',(6,6),[('L',(6,22)),('C',(24,42),(6,32),(18,38)),('C',(42,22),(30,38),(42,32)),('L',(42,6)),('C',(24,18),(36,20),(30,20)),('C',(6,6),(18,20),(12,20))],True)
