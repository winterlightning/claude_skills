'opera-house-shells-on-water: Restore overlapping curved sail roofs over a low waterfront base, with a separate water ripple. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3eff9550-c341-4d47-a50c-db9b48c3be68'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/sydney opera house_3eff9550-c341-4d47-a50c-db9b48c3be68.svg'
AUTHOR = 'gpt-6'

class OperaHouseShellsOnWater(Solo48):
    icon_id = 'opera-house-shells-on-water'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('sydney opera house', 'australia', 'shells', 'sails', 'harbour', 'water', 'landmark', 'cloud')

    def build(self):
        # Symbol plan: Restore overlapping curved sail roofs over a low waterfront base, with a separate water ripple.

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
        path('roofs',(4,32),[('L',(4,22)),('C',(16,28),(10,22),(14,25)),('L',(12,14)),('C',(28,26),(20,14),(26,20)),('L',(24,6)),('C',(40,32),(36,10),(40,24)),('L',(44,32)),('L',(4,32))],True)
        path('water',(4,44),[('C',(24,44),(11,40),(17,44)),('C',(44,44),(31,40),(37,44))])
