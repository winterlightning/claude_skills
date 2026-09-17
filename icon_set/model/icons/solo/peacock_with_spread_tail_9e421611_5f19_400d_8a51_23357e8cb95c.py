'peacock-with-spread-tail: Add a scalloped fan tail, separate feather eyes, a bird head with beak and small feet. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9e421611-5f19-400d-8a51-23357e8cb95c'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feathers up_9e421611-5f19-400d-8a51-23357e8cb95c.svg'
AUTHOR = 'gpt-6'


class PeacockWithSpreadTail(Solo48):
    icon_id = 'peacock-with-spread-tail'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('peacock', 'with', 'spread', 'tail')
    keyshape = Keyshape.FREE

    def build(self):
        # Symbol plan: Add a scalloped fan tail, separate feather eyes, a bird head with beak and small feet.

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
        path('fan',(10,38),[('C',(2,26),(4,38),(2,32)),('C',(10,12),(2,20),(3,12)),('C',(24,4),(10,4),(18,4)),('C',(38,12),(30,4),(38,4)),('C',(46,26),(45,12),(46,20)),('C',(38,38),(46,32),(44,38))])
        circle('head',24,18,2);circle('body',24,34,6)
        line('neck',(24,20),(24,28));line('beak',(26,18),(30,20));join('neck','head');join('neck','body');join('beak','head')
        for n,x,y in [('eye-l',11,22),('eye-r',37,24)]:dot(n,(x,y))
        poly('feet',(18,44),(24,40),(30,44));join('feet','body')
