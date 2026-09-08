"""Burj Al Arab: a vertical mast, projecting arm and a convex sail on a baseline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fef6ca45-0bb0-5b62-bc09-38dce2e48b1d'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/burj al arab uae_fef6ca45-0bb0-5b62-bc09-38dce2e48b1d.svg'
AUTHOR = 'gpt-6'


class BurjAlArab(Solo48):
    icon_id = 'burj-al-arab'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('burj al arab', 'dubai', 'uae', 'hotel', 'tower', 'sail', 'skyscraper', 'landmark', 'architecture')

    def build(self) -> None:
        # Centerline extremes: (8,2)-(40,46); intentional sail asymmetry.
        self.add_polyline('mast', (14,2), (14,10), (14,18), (14,46))
        self.add_arc('sail', (14,10), (36,46), radius_x=52, sweep=True)
        self.add_polyline('ground', (8,46), (14,46), (36,46), (40,46))
        self.add_line('arm', (8,18), (14,18))
        self.relate('connect','mast','sail')
        self.relate('connect','mast','ground')
        self.relate('connect','sail','ground')
        self.relate('connect','mast','arm')
