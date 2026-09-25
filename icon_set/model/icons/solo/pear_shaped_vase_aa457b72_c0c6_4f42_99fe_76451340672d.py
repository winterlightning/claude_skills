'pear-shaped-vase: Restore a narrow flared mouth, inward neck and smooth pear-shaped belly with a flat foot. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa457b72-c0c6-4f42-99fe-76451340672d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg'
AUTHOR = 'gpt-6'


class PearShapedVase(Solo48):
    icon_id = 'pear-shaped-vase'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    aliases = ()
    keywords = ('vase', 'bottle', 'ceramic', 'vessel', 'decor', 'flared lip', 'pear shape')

    def build(self):
        # Symbol plan: Restore a narrow flared mouth, inward neck and smooth pear-shaped belly with a flat foot.

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
        path('vase',(16,4),[('L',(32,4)),('C',(28,14),(32,8),(28,8)),('C',(36,32),(28,20),(36,24)),('C',(29,44),(36,39),(33,44)),('L',(19,44)),('C',(12,32),(15,44),(12,39)),('C',(20,14),(12,24),(20,20)),('C',(16,4),(20,8),(16,8))],True)
