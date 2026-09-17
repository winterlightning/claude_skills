'one-world-trade-center: Make the tower tall and slender, with its spire and tapering triangular glass facets. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f65e361-4e52-4b05-8bdc-819e8fa55e14'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/one world trade center_7f65e361-4e52-4b05-8bdc-819e8fa55e14.svg'
AUTHOR = 'gpt-6'


class OneWorldTradeCenter(Solo48):
    icon_id = 'one-world-trade-center'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('one world trade center', 'new york', 'skyscraper', 'tower', 'freedom tower', 'landmark', 'building', 'usa')

    def build(self):
        # Symbol plan: Make the tower tall and slender, with its spire and tapering triangular glass facets.

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
        poly('tower',(12,44),(16,12),(32,12),(36,44),(12,44))
        line('spire',(24,2),(24,12));line('facet',(16,12),(28,44))
        join('tower','spire');join('tower','facet')
