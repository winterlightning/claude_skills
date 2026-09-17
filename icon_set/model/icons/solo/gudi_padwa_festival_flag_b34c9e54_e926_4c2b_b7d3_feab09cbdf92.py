"""Gudi Padwa Festival Flag.

Plan: Pole with pot finial and hanging rounded garland on left, wave flag at right. Bounds (8,4)-(40,44).
Construction: Lucide flag: coherent waves with shared vertical pole. Source ceremonial pot and hanging ornament.
Reduction: Omitted small garland interior stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'b34c9e54-e926-4c2b-b7d3-feab09cbdf92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/gudi padwa_b34c9e54-e926-4c2b-b7d3-feab09cbdf92.svg'
AUTHOR = 'gpt-6'


class GudiPadwaFestivalFlag(Solo48):
    icon_id = 'gudi-padwa-festival-flag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('gudi', 'padwa', 'festival', 'flag')

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
        path('pot',(8,14),[('L',(8,8)),('A',(12,4),4,4,True),('L',(16,4)),('A',(20,8),4,4,True),('L',(20,14)),('L',(14,14)),('L',(8,14))],True)
        path('garland',(8,14),[('L',(8,24)),('A',(14,30),6,6,False),('A',(20,24),6,6,False),('L',(20,18)),('L',(20,14))])
        self.relate('connect','pot','garland')
        self.add_polyline('pole',(14,30),(14,40),(14,44));self.relate('connect','pole','garland')
        path('flag',(20,18),[('C',(40,20),(28,14),(30,24)),('L',(40,40)),('C',(14,40),(30,44),(24,36))])
        self.relate('connect','flag','garland');self.relate('connect','flag','pole')
