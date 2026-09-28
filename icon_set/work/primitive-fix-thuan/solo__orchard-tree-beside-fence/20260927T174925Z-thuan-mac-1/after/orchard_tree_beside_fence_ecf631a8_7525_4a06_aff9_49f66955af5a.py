"""Fruit Tree and Fence.

Plan: Orchard tree and nearby fence form one landscape. Bounds6,6,42,42. Omit tiny fruit circles.
Construction reference: No useful local Lucide match.
Final review: Omitted small fruit; shortened fence rails for tree clearance.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ecf631a8-7525-4a06-aff9-49f66955af5a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__orchard-tree-beside-fence/20260927T174925Z-thuan-mac-1/reference/orchard_ecf631a8-7525-4a06-aff9-49f66955af5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'orchard-tree-beside-fence'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('orchard', 'tree', 'beside', 'fence')

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

        path('crown',(24,28),[('A',(20,16),7,7,True),('A',(30,6),10,10,True),('A',(40,16),10,10,True),('C',(42,22),(42,18),(42,20)),('C',(30,30),(42,28),(36,30)),('L',(24,28))],True)
        line('trunk',(30,30),(30,42));join('crown','trunk')
        line('fence-left',(6,26),(6,42))
        line('fence-right',(16,34),(16,42))
        line('fence-top',(6,34),(16,34));line('fence-low',(6,42),(16,42))
        for post in ('fence-left','fence-right'):
            for rail in ('fence-top','fence-low'):join(post,rail)
        self.add_dot('fruit',(30,17))
