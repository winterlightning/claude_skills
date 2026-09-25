"""A diagonal dental explorer with an arcing hook and short angled branch. Bounds (6,6)-(42,42); smooth tangent curve continues the diagonal shaft.
Construction reference: Lucide wrench: coherent diagonal tool silhouette; source hook curvature retained.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '34b397e2-5944-4499-8303-bd0af66a4a03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/tooth_34b397e2-5944-4499-8303-bd0af66a4a03.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='angled-dental-explorer-curved-tip'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "health"
    categories = ("health", "primitives")
    aliases=()
    keywords=('tooth',)
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('tool',(6,42),[('L',(18,24)),('L',(26,12)),('C',(34,6),(29,8),(31,6)),('C',(42,12),(38,6),(40,10))])
        line('branch',(18,24),(28,34));join('tool','branch')
