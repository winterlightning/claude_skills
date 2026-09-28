"""love-compatibility: Two overlapping hearts with matched lobe curves; rear heart disappears only at shared front-heart endpoints.
Lucide construction: heart; original and atomic-debug inspected.
Omissions: None
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '13ea8ba1-9370-50ce-9da5-f3a7facdf796'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__love-compatibility/20260924T165054Z-thuan-mac/reference/love compatibility_13ea8ba1-9370-50ce-9da5-f3a7facdf796.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'love-compatibility'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('love', 'compatibility')
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

        path('front',(31,22),[('C',(38,18),(33,19),(35,18)),('C',(44,25),(42,18),(44,21)),('C',(31,40),(44,31),(37,36)),('C',(21,32),(27,37),(23,35)),('C',(18,25),(19,29),(18,27)),('C',(24,18),(18,21),(20,18)),('C',(31,22),(27,18),(29,19))],True)
        path('rear',(21,32),[('L',(16,40)),('C',(4,20),(10,34),(4,27)),('C',(12,8),(4,12),(7,8)),('C',(21,12),(16,8),(19,10)),('C',(29,8),(23,10),(25,8)),('C',(38,18),(34,8),(38,12))]);join('rear','front')
