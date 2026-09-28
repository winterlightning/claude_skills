"""Four curved links, each ending in a rounded ball at a corner, interlock at the centre in a square knot.

Plan: Four curved terminal links attach to a central diamond knot using shared nodes.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected flower-2: rotational repeat; tangent terminal curves.
Simplification: Interweaving bands reduce to a diamond knot with four curved links and round terminals.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '912f29e9-3e6b-45a8-8e4a-679dc1578b19'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__joomla-logo/20260927T070927Z-thuan-mac-1/reference/joomla logo_912f29e9-3e6b-45a8-8e4a-679dc1578b19.svg'
AUTHOR = "gpt-6"


class JoomlaLogo(Solo48):
    icon_id = 'joomla-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('joomla', 'cms', 'knot', 'logo', 'brand', 'web', 'open-source')

    def build(self):
        # Four rounded terminals and two crossing diagonal straps recall the woven J.
        for label,x,y in (('nw',9,9),('ne',39,9),('se',39,39),('sw',9,39)):
            self.add_arc(label+'-left',(x,y+3),(x,y-3),radius_x=3)
            self.add_arc(label+'-right',(x,y-3),(x,y+3),radius_x=3)
            self.add_contour(label,label+'-left',label+'-right',closed=True)
        self.add_bezier('rising',(9,12),((17,14),(31,34),(39,36)))
        self.add_bezier('falling',(39,12),((31,14),(17,34),(9,36)))
        self.relate('connect','rising','falling')
        self.relate('connect','nw','rising');self.relate('connect','se','rising')
        self.relate('connect','ne','falling');self.relate('connect','sw','falling')
