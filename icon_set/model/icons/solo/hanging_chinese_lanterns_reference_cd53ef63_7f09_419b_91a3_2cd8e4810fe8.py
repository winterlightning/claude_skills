"""Hanging Chinese Lanterns.

Plan: Staggered rounded lanterns share overhead cord. Bounds (6,6)-(42,42). Repeated construction with unequal widths.
Construction: Source paired lanterns; rounded geometric containers built with tangent circular corners. No useful exact Lucide lantern match.
Reduction: Caps and collars become suspension and tassel strokes; omitted tiny bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'cd53ef63-7f09-419b-91a3-2cd8e4810fe8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/lantern festival_cd53ef63-7f09-419b-91a3-2cd8e4810fe8.svg'
AUTHOR = 'gpt-6'


class IconHangingChineseLanternsReference(Solo48):
    icon_id = 'hanging-chinese-lanterns-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('hanging', 'chinese', 'lanterns')

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
        path('cord',(6,6),[('C',(12,9),(8,7),(10,8)),('C',(35,9),(20,11),(28,11)),('C',(42,6),(38,8),(40,7))])
        self.add_line('suspend-left',(12,9),(12,18));self.relate('connect','suspend-left','cord')
        path('left',(12,18),[('L',(14,18)),('A',(18,22),4,4,True),('L',(18,24)),('A',(14,28),4,4,True),('L',(12,28)),('L',(10,28)),('A',(6,24),4,4,True),('L',(6,22)),('A',(10,18),4,4,True),('L',(12,18))],True)
        self.relate('connect','suspend-left','left');self.add_line('tassel-left',(12,28),(12,36));self.relate('connect','tassel-left','left')
        self.add_line('suspend-right',(35,9),(35,28));self.relate('connect','suspend-right','cord')
        path('right',(35,28),[('L',(38,28)),('A',(42,32),4,4,True),('L',(42,34)),('A',(38,38),4,4,True),('L',(35,38)),('L',(32,38)),('A',(28,34),4,4,True),('L',(28,32)),('A',(32,28),4,4,True),('L',(35,28))],True)
        self.relate('connect','suspend-right','right');self.add_line('tassel-right',(35,38),(35,42));self.relate('connect','tassel-right','right')
