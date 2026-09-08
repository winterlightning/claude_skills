"""An unrolled parchment with two writing lines; bounds (2,2)-(46,46).

Construction reference: Lucide scroll-text: opposing round curls and two separated text rules.
Centerline extremes are the declared keyshape's exact bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0872fa36-cb40-4048-bfff-5fa6453c601b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/greek script_0872fa36-cb40-4048-bfff-5fa6453c601b.svg'
AUTHOR = 'astra-chatgpt'


class WrittenScroll(Solo48):
    icon_id = 'written-scroll'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('scroll', 'parchment', 'manuscript', 'script', 'ancient', 'document', 'writing', 'papyrus')

    def build(self) -> None:
        self.add_arc("top-roll-a", (2, 8), (8, 2), radius_x=6)
        self.add_arc("top-roll-b", (8, 2), (14, 8), radius_x=6)
        self.add_line("left-wall-a", (14, 8), (14, 14))
        self.add_line("left-wall-b", (14, 14), (14, 40))
        self.add_arc("bottom-roll-a", (14, 40), (20, 46), radius_x=6, sweep=False)
        self.add_arc("bottom-roll-b", (20, 46), (26, 40), radius_x=6, sweep=False)
        self.add_line("roll-rise", (26, 40), (26, 34))
        self.add_line("roll-top-1", (26, 34), (40, 34))
        self.add_line("roll-top-2", (40, 34), (46, 34))
        self.add_line("roll-top-3", (46, 34), (46, 40))
        self.add_arc("bottom-corner", (46, 40), (40, 46), radius_x=6)
        self.add_line("bottom-edge", (40, 46), (20, 46))
        self.add_contour("scroll-lower", "top-roll-a", "top-roll-b", "left-wall-a", "left-wall-b", "bottom-roll-a", "bottom-roll-b", "roll-rise", "roll-top-1", "roll-top-2", "roll-top-3", "bottom-corner", "bottom-edge")
        self.add_polyline("roll-lip", (2, 8), (2, 14), (14, 14))
        self.add_line("top-edge", (8, 2), (34, 2))
        self.add_arc("top-corner", (34, 2), (40, 8), radius_x=6)
        self.add_line("right-wall", (40, 8), (40, 34))
        self.add_contour("scroll-upper", "top-edge", "top-corner", "right-wall")
        self.relate("connect", "scroll-lower", "roll-lip")
        self.relate("connect", "scroll-lower", "scroll-upper")
        self.add_line("writing-top", (23, 17), (31, 17))
        self.add_line("writing-bottom", (23, 25), (29, 25))
