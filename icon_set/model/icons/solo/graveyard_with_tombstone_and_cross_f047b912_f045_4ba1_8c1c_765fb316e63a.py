"""Graveyard with Tombstone and Cross.

Plan: Round tombstone left and taller cross right on one rolling mound. Bounds (6,6)-(42,42).
Construction: Source grave/cross scene; Lucide simple round cap construction.
Reduction: Removed small incised cross to keep the stone opening generous; retained cemetery cross.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'f047b912-f045-4ba1-8c1c-765fb316e63a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/graveyard_f047b912-f045-4ba1-8c1c-765fb316e63a.svg'
AUTHOR = 'gpt-6'


class GraveyardWithTombstoneAndCross(Solo48):
    icon_id = 'graveyard-with-tombstone-and-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('graveyard', 'with', 'tombstone', 'and', 'cross')

    def build(self) -> None:

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
        path('stone',(6,42),[('L',(6,28)),('A',(22,28),8,8,True),('L',(22,40))])
        path('ground',(6,42),[('C',(22,40),(12,38),(17,38)),('C',(34,38),(26,38),(30,38)),('C',(42,42),(38,38),(40,40))])
        self.relate('connect','stone','ground')
        self.add_polyline('upright',(34,6),(34,16),(34,38))
        self.add_polyline('crossbar',(26,16),(34,16),(42,16))
        self.relate('connect','upright','crossbar');self.relate('connect','upright','ground')
