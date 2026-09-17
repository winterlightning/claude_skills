"""Person and Business Growth Chart.

Plan: SQUARE centerline extremes (6,6)-(42,42). A left foreground bust and
an interrupted presentation board form one scene. Chart rises to the right.
Lucide presentation informs the board and stand. human_ref/user.svg owns bust
proportions; circular head r4 at (10,23), shoulder apex y35 gives exact 4u ink gap.
Reduction: omit tiny chart markers; retain trend and complete person/board scene.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aca4af14-d513-5480-b973-52f14722c981'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/business/customer relationship management performance metrics_aca4af14-d513-5480-b973-52f14722c981.svg'
AUTHOR = "gpt-6"

class PersonAndBusinessGrowthChart(Solo48):
    icon_id = 'person-and-business-growth-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('person', 'and', 'business', 'growth', 'chart')

    def build(self):
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        circle("head",10,23,4)
        path("shoulders",(6,42),[("L",(6,39)),("A",(10,35),4,4,True),("A",(14,39),4,4,True),("L",(14,42))])
        path("board",(14,10),[("A",(18,6),4,4,True),("L",(38,6)),("A",(42,10),4,4,True),("L",(42,30)),("A",(38,34),4,4,True),("L",(30,34)),("L",(23,34))])
        self.add_polyline("growth",(23,24),(33,15))
        self.add_polyline("arrow",(25,15),(33,15),(33,23))
        self.relate("connect","growth","arrow")
        self.add_line("stand",(30,34),(30,42))
        self.add_polyline("foot",(23,42),(30,42),(37,42))
        self.relate("connect","board","stand")
        self.relate("connect","stand","foot")
