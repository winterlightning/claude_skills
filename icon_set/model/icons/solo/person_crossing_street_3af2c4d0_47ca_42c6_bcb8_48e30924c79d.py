'person-crossing-street: Restore a walking stride with an upright torso and a row of crossing stripes beneath the pedestrian. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3af2c4d0-47ca-42c6-bcb8-48e30924c79d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking cross street_3af2c4d0-47ca-42c6-bcb8-48e30924c79d.svg'
AUTHOR = 'gpt-6'

class PersonCrossingStreet(Solo48):
    icon_id = 'person-crossing-street'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'crossing', 'street', 'walking', 'pedestrian', 'road')

    def ring(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def branches(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{i}'
                self.add_line(key, a, b)
                members.append(key)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for i, (name, a, b) in enumerate(parts):
            for other, c, d in parts[i + 1:]:
                if a in (c, d) or b in (c, d):
                    self.relate('connect', name, other)

    def build(self):
        # Symbol plan: Restore a walking stride with an upright torso and a row of crossing stripes beneath the pedestrian.

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
        circle('head',24,6,4)
        poly('torso',(24,18),(24,22),(22,28))
        poly('arms',(10,23),(24,18),(32,25),(39,25));join('arms','torso')
        poly('legs',(12,35),(22,28),(32,35));join('legs','torso')
        for i,x in enumerate((4,16,28,40)):line('stripe-'+str(i),(x,44),(x+4,44))
        self.mark_human_figure('walker',head='head',torso='torso-1',torso_junction='start')
