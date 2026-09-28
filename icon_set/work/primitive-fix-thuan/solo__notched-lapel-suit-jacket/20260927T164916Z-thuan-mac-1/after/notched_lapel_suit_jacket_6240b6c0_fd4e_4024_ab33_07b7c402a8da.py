"""Formal Suit Jacket.

Plan: Suit silhouette with wide sleeves and V lapels. Bounds6,6,42,42. Omit pocket and buttons.
Construction reference: shirt.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6240b6c0-fd4e-4024-ab33-07b7c402a8da'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__notched-lapel-suit-jacket/20260927T164916Z-thuan-mac-1/reference/blazer 1_6240b6c0-fd4e-4024-ab33-07b7c402a8da.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'notched-lapel-suit-jacket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('notched', 'lapel', 'suit', 'jacket')

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

        poly('jacket',(16,6),(32,6),(42,14),(42,34),(34,34),(34,42),(14,42),(14,34),(6,34),(6,14),closed=True)
        poly('lapel-left',(16,6),(17,14),(21,16),(24,24));poly('lapel-right',(32,6),(31,14),(27,16),(24,24));join('lapel-left','jacket');join('lapel-right','jacket');join('lapel-left','lapel-right');line('opening',(24,24),(24,42));join('opening','lapel-left');join('opening','lapel-right');join('opening','jacket')
