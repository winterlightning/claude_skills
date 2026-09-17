"""Rabbit under Moon and Cloud.

Plan: Seated right-facing rabbit under crescent and cloud; extrema (6,6)-(42,42).
Construction: Lucide rabbit: swept ear, round haunch and short foot.
Reduction: One long ear, no eye or hind-leg seam; open crescent and cloud strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'fd9eb502-f6e2-4998-aa9a-b1268976dd8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/chinese moon festival rabbit_fd9eb502-f6e2-4998-aa9a-b1268976dd8f.svg'
AUTHOR = 'gpt-6'


class IconRabbitUnderMoonAndCloud(Solo48):
    icon_id = 'rabbit-under-moon-and-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('rabbit', 'under', 'moon', 'and', 'cloud')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('rabbit',(30,26),[('C',(40,30),(37,24),(40,26)),('L',(34,36)),('L',(34,42)),('L',(18,42)),('A',(10,34),8,8,True),('C',(24,30),(10,27),(18,28)),('C',(12,18),(18,28),(12,22)),('C',(30,26),(22,18),(26,22))],True)
        path('moon',(12,6),[('A',(6,12),6,6,False)])
        path('cloud',(28,14),[('C',(36,8),(25,8),(31,4)),('C',(42,14),(42,6),(42,12)),('L',(28,14))],True)
