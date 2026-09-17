'mountain-forest-trail: Give the scene a winding foreground trail, a triangular mountain and a recognizable pine tree. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eadab1c1-488b-4bcd-b945-526f25489491'
SOURCE_PATH = 'pictographic-primitives/nature/outdoors landscape_eadab1c1-488b-4bcd-b945-526f25489491.svg'
AUTHOR = 'gpt-6'


class MountainForestTrail(Solo48):
    icon_id = 'mountain-forest-trail'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-02"
    aliases = ()
    keywords = ('landscape', 'mountains', 'trail', 'pine', 'forest', 'hiking', 'outdoors', 'path')

    def build(self):
        # Symbol plan: Give the scene a winding foreground trail, a triangular mountain and a recognizable pine tree.

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
        poly('mountain',(4,20),(12,4),(20,20),closed=True)
        poly('pine',(36,12),(44,28),(28,28),closed=True)
        line('trunk',(36,28),(36,36));join('pine','trunk')
        path('trail',(14,32),[('C',(8,44),(25,36),(4,37))])
