"""cricket: A side-view cricket retains the long wing, curved antenna, two low feet and tall folded jumping leg. Natural directional asymmetry is preserved.
Lucide construction: bug; original and atomic-debug inspected.
Omissions: Small wing seam and extra antenna omitted for readable separation.
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f676f8b4-b6a7-4e6b-ab0e-87feab8269f5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cricket/20260924T172457Z-thuan-mac/reference/insect cricket body_f676f8b4-b6a7-4e6b-ab0e-87feab8269f5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'cricket'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('cricket',)
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(12,18),[('L',(20,20)),('L',(40,26)),('C',(28,32),(38,31),(34,32)),('C',(16,30),(22,32),(19,32)),('C',(12,18),(12,28),(10,23))],True)
        path('antenna',(12,18),[('C',(4,8),(6,16),(4,14))]);join('antenna','body')
        poly('hind-leg',(20,20),(34,8),(44,40));join('hind-leg','body')
        poly('front-leg',(16,30),(12,40),(4,40));poly('middle-leg',(28,32),(32,40),(24,40));join('front-leg','body');join('middle-leg','body')
