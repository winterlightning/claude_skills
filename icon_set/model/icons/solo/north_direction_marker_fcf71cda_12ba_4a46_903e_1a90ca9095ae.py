'north-direction-marker: Use a true upward navigation needle above an upright capital N. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcf71cda-12ba-4a46-903e-1a90ca9095ae'
SOURCE_PATH = 'pictographic-primitives/navigation/compass north_fcf71cda-12ba-4a46-903e-1a90ca9095ae.svg'
AUTHOR = 'gpt-6'


class NorthDirectionMarker(Solo48):
    icon_id = 'north-direction-marker'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "navigation"
    aliases = ()
    keywords = ('north', 'direction', 'compass', 'navigation', 'arrow', 'orientation', 'marker')

    def build(self):
        # Symbol plan: Use a true upward navigation needle above an upright capital N.

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
        poly('needle',(24,4),(36,22),(24,18),(12,22),(24,4))
        poly('north',(16,44),(16,30),(32,44),(32,30))
