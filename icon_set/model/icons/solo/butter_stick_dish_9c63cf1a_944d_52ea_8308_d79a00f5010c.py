"""Stick of Butter on Dish."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c63cf1a-944d-52ea-8308-d79a00f5010c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear butter_9c63cf1a-944d-52ea-8308-d79a00f5010c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'butter-stick-dish'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('butter', 'stick', 'dish')

    def build(self):
        # Plan: Butter block in perspective above a shallow dish. Shared corners define the top and two sides; Lucide sandwich informs simple food layers. Separate plate edge and small corner details simplified to a broad open serving dish.
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

        poly('butter',(10,16),(28,8),(38,12),(38,22),(20,30),(10,26),(10,16),closed=True)
        poly('top',(10,16),(20,21),(38,12));join('top','butter')
        line('edge',(20,21),(20,30));join('edge','top');join('edge','butter')
        path('dish',(4,34),[('C',(12,40),(4,40),(8,40)),('L',(36,40)),('C',(44,34),(40,40),(44,40))])
