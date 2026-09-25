"""fire-flame-curved: An asymmetric flame tip flows into one rounded bowl, with a deliberate inward notch on the left.
Lucide construction: flame; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '30104018-8e47-4b2e-9d72-f1246987add3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fire-flame-curved/20260924T165054Z-thuan-mac/reference/fire flame curved_30104018-8e47-4b2e-9d72-f1246987add3.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'fire-flame-curved'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('fire', 'flame', 'curved')
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

        path('flame',(24,4),[('C',(40,28),(34,12),(40,20)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('C',(14,16),(8,23),(10,19)),('C',(19,22),(15,19),(17,21)),('C',(24,4),(25,17),(27,10))],True)
