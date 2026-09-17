"""Temple and Palm Tree.

Plan: Left palm with arching fronds beside tiered temple at right. Bounds (6,6)-(42,42).
Construction: Source Balinese scene; Lucide tree-palm open frond construction.
Reduction: Two broad roof tiers replace three; narrow trunk and walls use strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '2e14f161-71b4-40a8-a538-68bc9cdb799b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/nyepi_2e14f161-71b4-40a8-a538-68bc9cdb799b.svg'
AUTHOR = 'gpt-6'


class IconTempleAndPalmTree(Solo48):
    icon_id = 'temple-and-palm-tree'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('temple', 'and', 'palm', 'tree')

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
        path('trunk',(12,42),[('C',(16,10),(16,30),(16,20))])
        path('fronds',(6,18),[('C',(16,10),(6,8),(12,6)),('C',(20,12),(19,6),(20,8))]);self.relate('connect','trunk','fronds')
        path('roof-upper',(26,18),[('L',(34,6)),('L',(42,18)),('L',(34,18)),('L',(26,18))],True)
        self.add_line('tower',(34,18),(34,26));self.relate('connect','tower','roof-upper')
        path('roof-lower',(24,34),[('L',(28,26)),('L',(34,26)),('L',(38,26)),('L',(42,34)),('L',(34,34)),('L',(24,34))],True);self.relate('connect','tower','roof-lower')
        self.add_line('wall',(34,34),(34,42));self.relate('connect','wall','roof-lower')
