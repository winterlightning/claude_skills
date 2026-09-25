"""Traditional Mooncake Side View."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da36c485-0e4c-5eee-bd30-d4c501f9d52e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mooncake side_da36c485-0e4c-5eee-bd30-d4c501f9d52e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'traditional-mooncake-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('traditional', 'mooncake', 'side', 'view')

    def build(self):
        # Plan: Thick mooncake in perspective with scalloped top, fluted side walls and central decoration. Shared upper/lower flute nodes and a centered top dot. Fine radiating marks reduced; no useful exact Lucide match.
        # Envelope: HRECT_L; visible ink (2, 6, 46, 42) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('top',(4,18),[('C',(12,10),(4,12),(8,10)),('C',(24,8),(14,10),(16,8)),('C',(36,10),(32,8),(34,10)),('C',(44,18),(40,10),(44,12)),('C',(36,26),(44,24),(40,26)),('C',(24,28),(34,26),(32,28)),('C',(12,26),(16,28),(14,26)),('C',(4,18),(8,26),(4,24))],True)
        path('side',(4,18),[('L',(4,30)),('C',(12,38),(4,36),(8,38)),('C',(24,40),(14,38),(16,40)),('C',(36,38),(32,40),(34,38)),('C',(44,30),(40,38),(44,36)),('L',(44,18))]);join('side','top')
        for j,(a,b) in enumerate((((12,26),(12,38)),((24,28),(24,40)),((36,26),(36,38)))):line('flute-'+str(j),a,b);join('flute-'+str(j),'top');join('flute-'+str(j),'side')
        self.add_dot('decoration',(24,18))
