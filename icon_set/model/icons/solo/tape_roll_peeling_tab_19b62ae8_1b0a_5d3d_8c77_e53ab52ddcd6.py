"""A concentric tape roll with squared peeling tab; tab extends asymmetrically toward lower right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19b62ae8-1b0a-5d3d-8c77-e53ab52ddcd6'
SOURCE_PATH = 'pictographic-primitives/tools/duct tape_19b62ae8-1b0a-5d3d-8c77-e53ab52ddcd6.svg'
AUTHOR = 'gpt-6'

class TapeRollPeelingTab(Solo48):
    icon_id = 'tape-roll-peeling-tab'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('tape', 'duct tape', 'roll', 'adhesive', 'sticky', 'peel', 'repair', 'packing')

    def build(self) -> None:

        def circle(n, x, y, r):
            self.add_arc(n+'-a', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(n+'-b', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        circle('roll',22,22,16)
        circle('core',22,22,7)
        self.add_polyline('tab',(38,22),(42,42),(22,38))
        self.relate('connect','tab','roll')
