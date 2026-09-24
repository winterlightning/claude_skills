'oval-stadium-with-two-flags: Wide elliptical stadium with an inner playing area, curved front wall and two compact rectangular flags. Original redrawn in place after the nine-icon meaning review.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2bedb9d2-a20f-5959-916c-51b7841e2d87'
SOURCE_PATH = 'pictographic-primitives/building/stadium classic_2bedb9d2-a20f-5959-916c-51b7841e2d87.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2bedb9d2-a20f-5959-916c-51b7841e2d87', 'pictographic-primitives/building/stadium classic_2bedb9d2-a20f-5959-916c-51b7841e2d87.svg'),)

class OvalStadiumWithTwoFlags(Solo48):
    icon_id = 'oval-stadium-with-two-flags'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('oval', 'stadium', 'with', 'two', 'flags')

    def build(self):
        # Symbol plan: Wide elliptical stadium with an inner playing area, curved front wall and two compact rectangular flags.

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
        path('rim',(4,27),[('C',(20,18),(4,21),(12,18)),('L',(28,18)),('C',(36,20),(31,18),(34,19)),('C',(44,27),(41,22),(44,24)),('C',(39,33),(44,30),(42,32)),('C',(24,36),(35,35),(29,36)),('C',(9,33),(19,36),(13,35)),('C',(4,27),(6,32),(4,30))],True)
        path('field',(9,33),[('C',(24,26),(12,28),(18,26)),('C',(39,33),(30,26),(36,28))]);join('field','rim')
        path('wall',(4,27),[('L',(6,38)),('C',(24,46),(7,44),(16,46)),('C',(42,38),(32,46),(41,44)),('L',(44,27))]);join('rim','wall')
        for i,(x,y) in enumerate([(4, 27), (36, 20)]):
         poly('flag-'+str(i),(x,2),(x+8,2),(x+8,10),(x,10),closed=True)
         line('pole-'+str(i),(x,10),(x,y));join('pole-'+str(i),'flag-'+str(i));join('pole-'+str(i),'rim')
