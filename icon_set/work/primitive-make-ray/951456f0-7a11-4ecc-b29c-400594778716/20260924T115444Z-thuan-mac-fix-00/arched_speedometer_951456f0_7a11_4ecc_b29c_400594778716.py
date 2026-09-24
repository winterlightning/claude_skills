"""Round the arched dial into its base and detach sparse dial marks from the rim. Retain circular needle hub and diagonal pointer.
Construction: Lucide gauge: coherent circular dial and diagonal needle.
Omissions: Reduce five fine ticks to two spaced marks.
Keyshape HRECT_L: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '951456f0-7a11-4ecc-b29c-400594778716'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arched-speedometer/20260924T115444Z-thuan-mac/reference/odometer_951456f0-7a11-4ecc-b29c-400594778716.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'arched-speedometer'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('arched', 'speedometer')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        path('dial',(4,28),[('A',(24,8),20,20,True),('A',(44,28),20,20,True),('L',(44,34)),('A',(38,40),6,6,True),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,28))],True)
        circle('hub',24,28,3)
        line('needle',(27,28),(33,22));join('needle','hub')
        self.add_dot('tick-top',(24,17));self.add_dot('tick-left',(13,25))
