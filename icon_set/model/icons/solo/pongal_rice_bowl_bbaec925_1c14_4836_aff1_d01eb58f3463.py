"""Pongal Rice Bowl.

Plan: Wide elliptical rice surface over deep rounded bowl. Extremes (4,8)-(44,40).
Construction: Lucide cooking-pot coherent vessel contour; source ellipse and garnish.
Reduction: One curved garnish mark replaces overlapping garnish and grain marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'bbaec925-1c14-4836-aff1-d01eb58f3463'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/pongal_bbaec925-1c14-4836-aff1-d01eb58f3463.svg'
AUTHOR = 'gpt-6'


class IconPongalRiceBowl(Solo48):
    icon_id = 'pongal-rice-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('pongal', 'rice', 'bowl')

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
        path('rim',(4,20),[('A',(44,20),20,12,True),('A',(4,20),20,12,True)],True)
        path('bowl',(4,20),[('C',(24,40),(4,34),(12,40)),('C',(44,20),(36,40),(44,34))]);self.relate('connect','rim','bowl')
        path('rice',(19,19),[('C',(29,19),(21,16),(27,16))])
