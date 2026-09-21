"""French Baguette Bread Loaf.

Plan: Diagonal rounded loaf with three scores attached to crust. Bounds6,6,42,42.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec98192c-cf34-4d21-8f1f-3f5139450985'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baguette_ec98192c-cf34-4d21-8f1f-3f5139450985.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-baguette-with-three-scoring-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('diagonal', 'baguette', 'with', 'three', 'scoring', 'marks')

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

        path('loaf',(6,34),[('C',(10,24),(6,30),(8,26)),('L',(24,10)),('C',(34,6),(28,6),(30,6)),('A',(42,14),8,8,True),('C',(38,24),(42,18),(40,22)),('L',(24,38)),('C',(14,42),(20,42),(18,42)),('A',(6,34),8,8,True)],True)
        line('score-a',(12,22),(18,28));line('score-b',(22,12),(28,18));join('score-a','loaf');join('score-b','loaf')
