"""Handled Diya Oil Lamp.

Plan: Teardrop flame above shallow bowl with right loop handle and pedestal foot; bounds (6,6)-(42,42).
Construction: Lucide flame: continuous teardrop run; source handled bowl and foot.
Reduction: Omitted wick interior; broad pedestal baseline keeps the foot legible without a tiny trapped pocket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ce61eef0-26c7-53d5-8b7f-008e608029a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/karthika deepam_ce61eef0-26c7-53d5-8b7f-008e608029a0.svg'
AUTHOR = 'gpt-6'


class HandledDiyaOilLamp(Solo48):
    icon_id = 'handled-diya-oil-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('handled', 'diya', 'oil', 'lamp')

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
        path('flame',(18,6),[('C',(23,12),(19,9),(23,9)),('A',(13,12),5,5,True),('C',(18,6),(13,9),(17,9))],True)
        path('bowl',(6,26),[('L',(30,26)),('L',(30,34)),('L',(18,34)),('C',(6,26),(12,34),(8,30))],True)
        # Open handle attaches to the two endpoints of the bowl's right wall.
        path('handle',(30,26),[('A',(42,30),12,4,True),('A',(30,34),12,4,True)])
        self.relate('connect','handle','bowl')
        self.add_line('stand',(18,34),(18,42))
        self.add_polyline('foot',(10,42),(18,42),(26,42))
        self.relate('connect','stand','bowl');self.relate('connect','stand','foot')
