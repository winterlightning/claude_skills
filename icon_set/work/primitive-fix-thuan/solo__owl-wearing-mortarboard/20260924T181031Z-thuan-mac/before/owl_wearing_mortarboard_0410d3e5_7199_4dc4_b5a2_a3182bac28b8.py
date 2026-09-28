'owl-wearing-mortarboard: Restore the owl body and large paired eyes under a broad diamond mortarboard with tassel. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0410d3e5-7199-4dc4-b5a2-a3182bac28b8'
SOURCE_PATH = 'pictographic-primitives/school-learning/study owl_0410d3e5-7199-4dc4-b5a2-a3182bac28b8.svg'
AUTHOR = 'gpt-6'


class OwlWearingMortarboard(Solo48):
    icon_id = 'owl-wearing-mortarboard'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "education/school"
    aliases = ()
    keywords = ('owl', 'mortarboard', 'graduation', 'education', 'bird', 'study')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+'-'+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Symbol plan: Restore the owl body and large paired eyes under a broad diamond mortarboard with tassel.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        poly('cap',(2,12),(24,4),(46,12),(24,20),(2,12))
        line('tassel',(2,12),(2,24));join('cap','tassel')
        circle('left-eye',14,30,4);circle('right-eye',34,30,4)
        path('breast',(10,30),[('C',(24,44),(0,40),(14,44)),('C',(38,30),(34,44),(48,40))])
        join('breast','left-eye');join('breast','right-eye')
        poly('beak',(20,30),(24,34),(28,30));join('beak','left-eye');join('beak','right-eye')
