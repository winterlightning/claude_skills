"""Mythical Dragon Head.

Plan: Mirrored pointed ears, fierce brow silhouette, angled eye marks, rounded narrowing muzzle and long whiskers. Bounds (6,6)-(42,42).
Construction: Source dragon face; no useful exact Lucide dragon head match.
Reduction: Nostrils become one muzzle dot; omitted the second whiskers, and incorporated brows into the outer contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '6f473e98-64f6-48ab-8e8a-b9679130547e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/takengei_6f473e98-64f6-48ab-8e8a-b9679130547e.svg'
AUTHOR = 'gpt-6'


class IconMythicalDragonHead(Solo48):
    icon_id = 'mythical-dragon-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('mythical', 'dragon', 'head')

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
        path('head',(8,24),[('C',(14,16),(8,20),(12,18)),('L',(6,6)),('C',(20,12),(14,6),(18,8)),('C',(28,12),(22,10),(26,10)),('C',(42,6),(30,8),(34,6)),('L',(34,16)),('C',(40,24),(36,18),(40,20)),('C',(34,34),(40,28),(36,30)),('A',(24,42),10,8,True),('A',(14,34),10,8,True),('C',(8,24),(12,30),(8,28))],True)
        self.add_line('eye-left',(18,24),(20,26));self.add_line('eye-right',(30,24),(28,26))
        self.add_dot('nose',(24,33))
        self.add_line('whisker-left',(14,34),(6,38));self.add_line('whisker-right',(34,34),(42,38))
        self.relate('connect','whisker-left','head');self.relate('connect','whisker-right','head')
