"""Two overlapping washers with a circular bore in front; the cramped rear bore is omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3113de9a-2721-4232-87f3-a6b659676a57'
SOURCE_PATH = 'pictographic-primitives/tools/hardware nuts round_3113de9a-2721-4232-87f3-a6b659676a57.svg'
AUTHOR = 'gpt-6'

class TwoRoundWashers(Solo48):
    icon_id = 'two-round-washers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('washer', 'washers', 'ring', 'hardware', 'fastener', 'round', 'nut', 'metal')

    def build(self) -> None:

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        circle('front',18,18,12)
        circle('front-bore',18,18,3)
        self.add_arc('back-outer',(30,18),(18,30),radius_x=12,large_arc=True)
        self.relate('connect','back-outer','front')
