"""Fresh Baked Croissant.

Plan: Crescent pastry with plump crown and tapered lower ends. Bounds4,8,44,40. Two broad segment seams.
Construction reference: croissant.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae9a3d91-41ba-425b-bb30-2096c8d8d30c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pastry_ae9a3d91-41ba-425b-bb30-2096c8d8d30c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-crescent-croissant'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('segmented', 'crescent', 'croissant')

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

        path('croissant',(4,40),[('C',(10,18),(4,30),(6,24)),('C',(24,8),(14,12),(18,8)),('C',(38,18),(30,8),(34,12)),('C',(44,40),(42,24),(44,30)),('C',(30,26),(36,36),(34,28)),('C',(18,26),(26,20),(22,20)),('C',(4,40),(14,28),(12,36))],True)
        line('left-seam',(10,18),(18,26));line('right-seam',(38,18),(30,26));join('croissant','left-seam');join('croissant','right-seam')
