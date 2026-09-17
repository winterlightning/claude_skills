"""Shining Easter Eggs.

Plan: Two unequal egg contours, upright rear and round foreground, with three rays. Bounds (6,6)-(42,42).
Construction: Lucide egg cubic crown and rounded base. Source supplies paired eggs and radiance.
Reduction: Separated unequal eggs preserve their openings; omitted decorative bands and reduced five rays to three.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '13cb93f6-c485-4531-8105-41c9f2431b89'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/easter egg_13cb93f6-c485-4531-8105-41c9f2431b89.svg'
AUTHOR = 'gpt-6'


class IconShiningEasterEggs(Solo48):
    icon_id = 'shining-easter-eggs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('shining', 'easter', 'eggs')

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
        path('egg-back',(13,16),[('C',(20,35),(17,16),(20,28)),('A',(6,35),7,7,True),('C',(13,16),(6,28),(9,16))],True)
        path('egg-front',(36,26),[('C',(42,36),(40,26),(42,31)),('A',(30,36),6,6,True),('C',(36,26),(30,31),(32,26))],True)
        self.add_line('ray-top',(13,6),(13,7));self.add_line('ray-left',(40,14),(42,16));self.add_line('ray-right',(27,8),(30,6))
