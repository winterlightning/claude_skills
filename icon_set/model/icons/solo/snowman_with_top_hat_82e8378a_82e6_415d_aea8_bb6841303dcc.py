"""Snowman with Top Hat.

Plan: Small snowball head and larger rounded body beneath top hat; symmetrical arms. Bounds (6,6)-(42,42).
Construction: Source snow sculpture; rounded coherent head/body silhouette. No useful exact Lucide snowman match.
Reduction: Blank face retained; twig branches omitted to preserve head and arm clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '82e8378a-82e6-415d-aea8-bb6841303dcc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/snowman_82e8378a-82e6-415d-aea8-bb6841303dcc.svg'
AUTHOR = 'gpt-6'


class IconSnowmanWithTopHat(Solo48):
    icon_id = 'snowman-with-top-hat-82e8378a-82e6-415d-aea8-bb6841303dcc'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('snowman', 'with', 'top', 'hat')

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
        path('snow',(18,14),[('C',(16,24),(13,17),(13,22)),('C',(12,33),(13,27),(12,30)),('A',(24,42),12,9,False),('A',(36,33),12,9,False),('C',(32,24),(36,30),(35,27)),('C',(30,14),(35,22),(35,17))])
        path('hat',(18,14),[('L',(18,6)),('L',(30,6)),('L',(30,14)),('L',(18,14))],True)
        self.relate('connect','snow','hat')
        self.add_line('brim-left',(18,14),(12,14));self.add_line('brim-right',(30,14),(36,14));self.relate('connect','brim-left','hat');self.relate('connect','brim-left','snow');self.relate('connect','brim-right','hat');self.relate('connect','brim-right','snow')
        for side in [-1,1]:
         def p(x,y):return(24+side*x,y)
         self.add_line('arm'+str(side),p(12,33),p(18,28));self.relate('connect','arm'+str(side),'snow')
