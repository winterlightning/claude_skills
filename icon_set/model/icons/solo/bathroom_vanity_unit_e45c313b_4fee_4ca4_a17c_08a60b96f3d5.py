"""Bathroom Vanity Unit.

Plan: Wide two-door cabinet beneath basin and arched faucet. Bounds (6,6)-(42,42).
Construction: Lucide bath fixture curves and source vanity cabinet.
Reduction: Sink reduced to a broad trapezoid resting on the cabinet; one door seam replaces multiple drawers and short feet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e45c313b-4fee-4ca4-a17c-08a60b96f3d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/reception toilet_e45c313b-4fee-4ca4-a17c-08a60b96f3d5.svg'
AUTHOR = 'gpt-6'


class IconBathroomVanityUnit(Solo48):
    icon_id = 'bathroom-vanity-unit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('bathroom', 'vanity', 'unit')

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
        path('cabinet',(6,26),[('L',(14,26)),('L',(22,26)),('L',(24,26)),('L',(42,26)),('L',(42,42)),('L',(24,42)),('L',(6,42)),('L',(6,26))],True)
        self.add_line('doors',(24,26),(24,42));self.relate('connect','doors','cabinet')
        path('basin',(8,18),[('L',(14,18)),('L',(28,18)),('L',(22,26)),('L',(14,26)),('L',(8,18))],True);self.relate('connect','basin','cabinet')
        path('tap',(14,18),[('L',(14,10)),('A',(22,10),4,4,True)]);self.relate('connect','tap','basin')
