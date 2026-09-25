"""Four Pointed Ninja Star.

Plan: Four diagonal blades and center hole. Bounds6,6,42,42; broad concave waists.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34a0e45f-101b-49ec-be4c-d97a89128d37'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antique shuriken_34a0e45f-101b-49ec-be4c-d97a89128d37.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-point-throwing-star'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('four', 'point', 'throwing', 'star')

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

        path('star',(6,6),[('C',(24,14),(16,12),(18,14)),('L',(42,6)),('C',(34,24),(36,16),(34,18)),('L',(42,42)),('C',(24,34),(32,36),(30,34)),('L',(6,42)),('C',(14,24),(12,32),(14,30)),('L',(6,6))],True)
        circle('hole',24,24,2)
