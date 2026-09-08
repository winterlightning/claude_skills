"""An open necklace with a circular pendant. Symmetric U chain; no useful direct Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '304c082c-7604-5a82-9d4c-a7d6655317a1'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/accessories necklace_304c082c-7604-5a82-9d4c-a7d6655317a1.svg'
AUTHOR = 'astra-chatgpt'

class NecklaceWithRoundPendant(Solo48):
    icon_id = 'necklace-with-round-pendant'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('necklace', 'with', 'round', 'pendant')

    def build(self) -> None:
        # Centerline extremes (5,2)-(43,46); mirror about x=24.
        self.add_line("chain-left", (5,2), (5,15))
        self.add_arc("chain-left-bend", (5,15), (24,34), radius_x=19, sweep=False)
        self.add_arc("chain-right-bend", (24,34), (43,15), radius_x=19, sweep=False)
        self.add_line("chain-right", (43,15), (43,2))
        self.add_contour("chain", "chain-left", "chain-left-bend", "chain-right-bend", "chain-right")
        self.add_arc("pendant-right", (24,34), (24,46), radius_x=6)
        self.add_arc("pendant-left", (24,46), (24,34), radius_x=6)
        self.add_contour("pendant", "pendant-right", "pendant-left", closed=True)
        self.relate("connect", "chain", "pendant")
