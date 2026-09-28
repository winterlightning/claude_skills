"""Restore a balanced dashed circular sweep and align the lower arrowhead with its counterclockwise tangent.
Construction: Lucide circle-dashed: spaced curved dashes; source counterclockwise arrow retained.
Omissions: Nine tiny dashes reduced to four separated runs.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '86ee206a-80e8-4959-a6ec-c45dd3bfc655'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-dashed-counterclockwise-circle/20260924T115444Z-thuan-mac/reference/diagram dash circle_86ee206a-80e8-4959-a6ec-c45dd3bfc655.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'arrow-dashed-counterclockwise-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('arrow', 'dashed', 'counterclockwise', 'circle')
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

        path('top',(12,10),[('C',(24,6),(16,7),(20,6))])
        path('right',(38,12),[('C',(42,24),(41,16),(42,20))])
        path('left',(7,18),[('C',(6,24),(6,20),(6,22)),('C',(7,30),(6,26),(6,28))])
        path('bottom',(12,38),[('C',(24,42),(16,41),(20,42)),('C',(36,34),(30,42),(33,38))])
        poly('head',(28,34),(36,34),(36,42));join('head','bottom')
