"""One northeast navigation pointer, reflected across x+y=48; SQUARE extremes (6,6)-(42,42). Lucide navigation informs the single notched contour.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c48eb4da-b133-4db8-82b4-28dc717bca0a'
SOURCE_PATH = 'pictographic-primitives/navigation/compass arrow_c48eb4da-b133-4db8-82b4-28dc717bca0a.svg'
AUTHOR = 'gpt-6'


class NavigationArrow(Solo48):
    icon_id = 'navigation-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "navigation"
    categories = ("navigation", "primitives")
    aliases = ()
    keywords = ('navigation', 'arrow', 'direction', 'pointer', 'location', 'heading', 'travel')

    def build(self) -> None:
        tip = (42, 6)
        wing = (6, 22)
        tail = (48-wing[1], 48-wing[0])
        notch = (22, 26)
        self.add_polyline("pointer", wing, tip, tail, notch, closed=True)
