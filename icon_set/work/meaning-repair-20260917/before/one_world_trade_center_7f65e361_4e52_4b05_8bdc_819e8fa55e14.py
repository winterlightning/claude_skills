"""One World Trade Center: tapering shaft and diagonal facet; tiny triangular cap reduced to spire."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f65e361-4e52-4b05-8bdc-819e8fa55e14'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/one world trade center_7f65e361-4e52-4b05-8bdc-819e8fa55e14.svg'
AUTHOR = 'gpt-6'


class OneWorldTradeCenter(Solo48):
    icon_id = 'one-world-trade-center'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('one world trade center', 'new york', 'skyscraper', 'tower', 'freedom tower', 'landmark', 'building', 'usa')

    def build(self) -> None:
        # Centerline extremes: (8,4)-(40,44).
        self.add_polyline('shaft',(8,44),(15,12),(24,12),(33,12),(40,44),(23,44),(8,44),closed=True)
        self.add_line('spire',(24,4),(24,12))
        self.add_line('facet',(33,12),(23,44))
        self.relate('connect','shaft','spire')
        self.relate('connect','shaft','facet')
