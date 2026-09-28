"""Pair of Hanging Baubles.

Plan: Two staggered baubles on vertical suspension strings, each own circular outline. Bounds (6,6)-(42,42).
Construction: Source pair of hanging circular ornaments; circles constructed from cardinal arcs.
Reduction: Separated overlapping baubles to preserve independent round openings; caps reduced to suspension strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '960048c4-db60-5bf1-ae5c-55d326a355ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas tree ornaments_960048c4-db60-5bf1-ae5c-55d326a355ec.svg'
AUTHOR = 'gpt-6'


class IconPairOfHangingBaubles(Solo48):
    icon_id = 'pair-of-hanging-baubles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('pair', 'of', 'hanging', 'baubles')

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
        path('left',(6,18),[('A',(14,10),8,8,True),('A',(22,18),8,8,True),('A',(6,18),8,8,True)],True)
        path('right',(26,34),[('A',(34,26),8,8,True),('A',(42,34),8,8,True),('A',(26,34),8,8,True)],True)
        self.add_line('string-left',(14,6),(14,10));self.add_line('string-right',(34,6),(34,26))
        self.relate('connect','string-left','left');self.relate('connect','string-right','right')
