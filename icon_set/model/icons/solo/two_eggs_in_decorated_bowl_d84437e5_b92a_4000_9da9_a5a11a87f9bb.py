"""Two Eggs in Decorated Bowl.

Plan: Two eggs over round bowl, shared paired egg definition and rim endpoints. Bounds (6,6)-(42,42).
Construction: Lucide egg cubic dome and circular bowl silhouette; source paired eggs.
Reduction: One shallow curved decorative stroke replaces repeated waves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'd84437e5-b92a-4000-9da9-a5a11a87f9bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/easter egg basket_d84437e5-b92a-4000-9da9-a5a11a87f9bb.svg'
AUTHOR = 'gpt-6'


class IconTwoEggsInDecoratedBowl(Solo48):
    icon_id = 'two-eggs-in-decorated-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('two', 'eggs', 'in', 'decorated', 'bowl')

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
        path('rim',(6,24),[('L',(8,24)),('L',(20,24)),('L',(28,24)),('L',(40,24)),('L',(42,24))])
        path('bowl',(6,24),[('A',(42,24),18,18,False)]);self.relate('connect','rim','bowl')
        for x in [14,34]:
         path('egg'+str(x),(x-6,24),[('C',(x,6),(x-6,12),(x-3,6)),('C',(x+6,24),(x+3,6),(x+6,12))]);self.relate('connect','egg'+str(x),'rim')
        path('decoration',(20,32),[('C',(24,33),(21,32),(22,33)),('C',(28,32),(26,33),(27,32))])
