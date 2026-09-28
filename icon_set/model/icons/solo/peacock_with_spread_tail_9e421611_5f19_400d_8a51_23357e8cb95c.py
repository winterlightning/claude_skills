'peacock-with-spread-tail: Connect both sides of the spread fan directly to the body with mirrored sweeping curves. Original redrawn in place after the nine-icon meaning review.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e421611-5f19-400d-8a51-23357e8cb95c'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feathers up_9e421611-5f19-400d-8a51-23357e8cb95c.svg'
AUTHOR = 'gpt-6'

class PeacockWithSpreadTail(Solo48):
    icon_id = 'peacock-with-spread-tail'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('peacock', 'with', 'spread', 'tail')
    keyshape = Keyshape.FREE

    def build(self):
        # Symbol plan: Connect both sides of the spread fan directly to the body with mirrored sweeping curves.

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
        path('fan',(16,34),[('C',(2,26),(7,38),(2,34)),('C',(8,12),(2,20),(4,15)),('C',(24,4),(12,7),(18,4)),('C',(40,12),(30,4),(36,7)),('C',(46,26),(44,15),(46,20)),('C',(32,34),(46,34),(41,38))])
        path('bird',(24,16),[('C',(30,22),(28,16),(28,20)),('L',(28,26)),('L',(28,28)),('C',(32,34),(28,30),(32,31)),('C',(28,40),(32,38),(30,40)),('L',(20,40)),('C',(16,34),(18,40),(16,38)),('C',(20,28),(16,31),(20,30)),('L',(20,24)),('C',(24,16),(20,20),(20,16))],True)
        for n,a,b in [('feather-left',(2,26),(9,26)),('feather-right',(46,26),(39,26)),('feather-upper-left',(8,12),(12,16)),('feather-upper-right',(40,12),(36,16))]:line(n,a,b);join(n,'fan')
        line('crest',(24,16),(24,13));join('crest','bird')
        line('foot-left',(20,40),(18,44));line('foot-right',(28,40),(30,44));join('foot-left','bird');join('foot-right','bird')

        join('fan','bird')
