"""Gardening Shears and Plant.

Plan: Pruning shears beside a leafy stem, a gardening scene. Bounds6,6,42,42. Single leaf and broad blades.
Construction reference: scissors.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a757f97f-925d-4ec4-a7e5-e647c6df42dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pruner_a757f97f-925d-4ec4-a7e5-e647c6df42dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pruning-shears-leafy-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pruning', 'shears', 'leafy', 'stem')

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

        line('stem',(6,42),(6,24))
        path('leaf',(6,24),[('C',(18,6),(6,10),(12,6)),('C',(6,24),(18,18),(12,24))],True);join('leaf','stem')
        poly('blades',(28,6),(32,24),(42,14))
        path('handles',(32,24),[('L',(24,36)),('C',(30,42),(20,42),(28,42)),('L',(32,24)),('L',(42,36)),('L',(42,42))]);join('blades','handles')
