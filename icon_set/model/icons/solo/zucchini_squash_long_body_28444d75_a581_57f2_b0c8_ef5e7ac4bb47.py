"""A long diagonal zucchini with gently widening rounded end, short stem and two lengthwise grooves. Bounds (6,6)-(42,42).
Construction reference: Lucide fish: long organic outline and smooth contour flow.
Omissions: Two close grooves reduced to one clear lengthwise groove."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '28444d75-a581-57f2-b0c8-ef5e7ac4bb47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/zucchini_28444d75-a581-57f2-b0c8-ef5e7ac4bb47.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='zucchini-squash-long-body'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "food"
    categories = ("primitives", "food")
    aliases=()
    keywords=('zucchini',)
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
        path('squash',(12,12),[('C',(25,12),(15,9),(19,7)),('C',(36,24),(29,17),(31,21)),('C',(42,35),(40,26),(42,30)),('C',(35,42),(42,40),(39,42)),('C',(19,36),(29,42),(24,40)),('L',(9,26)),('C',(12,12),(4,21),(7,16))],True)
        poly('stem',(12,12),(6,8),(8,6),(15,10));join('stem','squash')
        line('groove',(24,25),(29,30))
