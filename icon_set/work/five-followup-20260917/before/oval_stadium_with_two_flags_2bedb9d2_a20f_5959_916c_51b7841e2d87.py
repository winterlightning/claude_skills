'oval-stadium-with-two-flags: Wide open arena with a low curved stadium wall and two complete repeated pennants, anchored on the rear rim. Original redrawn in place after the nine-icon meaning review.'
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
        # Symbol plan: Wide open arena with a low curved stadium wall and two complete repeated pennants, anchored on the rear rim.

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
        path('rim',(4,29),[('C',(12,24),(4,26),(8,25)),('C',(20,22),(16,23),(18,22)),('L',(28,22)),('C',(36,24),(30,22),(32,23)),('C',(44,29),(40,25),(44,26)),('A',(24,36),20,7,True),('A',(4,29),20,7,True)],True)
        path('wall',(4,29),[('L',(6,38)),('C',(24,46),(8,44),(16,46)),('C',(42,38),(32,46),(40,44)),('L',(44,29))]);join('rim','wall')
        for i,(x,y) in enumerate([(4, 29), (36, 24)]):
         poly('flag-'+str(i),(x,2),(x+8,9),(x,16),closed=True)
         line('pole-'+str(i),(x,16),(x,y));join('pole-'+str(i),'flag-'+str(i));join('pole-'+str(i),'rim')
