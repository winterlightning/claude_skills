"""The Leaning Tower of Pisa with sloping floor bands; the doorway and upper mast are omitted for clear spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a3f8c8c-6f0b-50d0-bd62-91718e949e17'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/pisa tower_9a3f8c8c-6f0b-50d0-bd62-91718e949e17.svg'
AUTHOR = 'gpt-6'


class LeaningTowerOfPisa(Solo48):
    icon_id = 'leaning-tower-of-pisa'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('pisa', 'tower', 'italy', 'leaning', 'landmark', 'campanile', 'travel', 'architecture')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46); tower leans right.
        self.add_polyline('shaft',(11,46),(13,36),(15,26),(17,16),(19,2),(35,6),(33,20),(31,30),(29,40),(28,46),(11,46),closed=True)
        self.add_line('upper-floor',(17,16),(33,20))
        self.add_line('middle-floor',(15,26),(31,30))
        self.add_line('lower-floor',(13,36),(29,40))
        for part in ('upper-floor','middle-floor','lower-floor'):
            self.relate('connect',part,'shaft')
        self.add_polyline('ground',(5,46),(11,46),(28,46),(43,46))
        self.relate('connect','ground','shaft')
