"""Four Petal Flower.

Plan: Four mirrored rounded petals and small center. Bounds6,6,42,42.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9004bc2-cb80-4030-aa94-9badd784e12f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dogwood_d9004bc2-cb80-4030-aa94-9badd784e12f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-rounded-petals-around-small-center'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('four', 'rounded', 'petals', 'around', 'small', 'center')

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

        path('flower',(16,16),[('C',(24,6),(10,6),(18,6)),('C',(32,16),(30,6),(38,6)),('C',(42,24),(42,10),(42,18)),('C',(32,32),(42,30),(42,38)),('C',(24,42),(38,42),(30,42)),('C',(16,32),(18,42),(10,42)),('C',(6,24),(6,38),(6,30)),('C',(16,16),(6,18),(6,10))],True)
        circle('center',24,24,2)
