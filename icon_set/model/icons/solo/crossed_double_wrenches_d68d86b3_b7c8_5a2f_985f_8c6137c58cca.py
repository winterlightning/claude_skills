"""Two outlined double-ended wrenches overlap diagonally; broad open jaws and a continuous foreground handle preserve the tool silhouettes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd68d86b3-b7c8-5a2f-985f-8c6137c58cca'
SOURCE_PATH = 'pictographic-primitives/tools/tools wrench_d68d86b3-b7c8-5a2f-985f-8c6137c58cca.svg'
AUTHOR = 'gpt-6'

class CrossedDoubleWrenches(Solo48):
    icon_id = 'crossed-double-wrenches'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('wrenches', 'wrench', 'crossed', 'spanner', 'repair', 'maintenance', 'mechanic', 'tools')

    def build(self) -> None:
        points=[(30,6),(24,12),(24,18),(18,24),(12,24),(6,30),(6,36),(12,30),(18,36),(12,42),(18,42),(24,36),(24,30),(30,24),(36,24),(42,18),(42,12),(36,18),(30,12),(36,6),(30,6)]
        arcs={0:(6,False),4:(6,False),7:(6,True),10:(6,False),14:(6,False),17:(6,True)}
        ids=[]
        for j,(a,b) in enumerate(zip(points,points[1:])):
            n='front-'+str(j);ids.append(n)
            if j in arcs:
                r,sw=arcs[j];self.add_arc(n,a,b,radius_x=r,sweep=sw)
            else:self.add_line(n,a,b)
        self.add_contour('front',*ids,closed=True)
        for name,flip in [('rear-upper',False),('rear-lower',True)]:
            def p(x,y):return (48-x,48-y) if flip else (x,y)
            pts=[(18,24),(12,18),(6,12),(6,6),(12,12),(18,6),(18,12),(24,18)]
            ids=[]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                n=name+'-'+str(j);ids.append(n)
                a=p(*a);b=p(*b)
                if j==1:self.add_arc(n,a,b,radius_x=6)
                else:self.add_line(n,a,b)
            self.add_contour(name,*ids)
            self.relate('connect',name,'front')
