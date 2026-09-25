"""Delivery Person Holding Open Box.

Plan: SQUARE (6,6)-(42,42). Right-facing courier with circular head and cap,
a bent supporting arm, open box and upright rear flap. The human full_body_ref.png
seated/reaching pose informs the torso and bent arm. Head radius4 center (10,10),
torso junction (10,22): 8u centerline / exactly 4u detached ink gap.
Lucide package-open informs the flap; use a side view matching the source.
Reduction: plain circular head, single cap brim, one supporting arm, no fingers; flap reduced to its open bent edge to avoid a narrow outlined strip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cf7fe47-0bae-52b2-a6ad-0ac50b09764f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/construction/folding pocket knife_2cf7fe47-0bae-52b2-a6ad-0ac50b09764f.svg'
AUTHOR = "gpt-6"

class DeliveryPersonHoldingOpenBox(Solo48):
    icon_id = 'delivery-person-holding-open-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('delivery', 'person', 'holding', 'open', 'box')

    def build(self):
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path("head",(10,6),[("A",(10,14),4,4,True),("A",(10,6),4,4,True)],True)
        self.add_line("cap",(10,6),(18,6))
        self.relate("connect","head","cap")
        self.add_line("torso",(10,22),(10,42))
        self.add_polyline("arm",(10,22),(20,34),(26,34))
        self.relate("connect","torso","arm")
        self.mark_human_figure("courier",head="head",torso="torso",torso_junction="start")
        path("box",(26,26),[("L",(42,26)),("L",(42,34)),("A",(38,38),4,4,True),("L",(30,38)),("A",(26,34),4,4,True),("L",(26,26))],True)
        self.relate("connect","box","arm")
        self.add_polyline("flap",(42,26),(34,14),(30,18))
        self.relate("connect","flap","box")
