"""wind-state: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfffa211-4688-49bd-87eb-16a4c14d3a9b'
SOURCE_PATH = 'pictographic-primitives/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Wind(Solo48):
    icon_id = 'wind-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('wind', 'state')

    def build(self):
        # Plan: HRECT_L; one coherent repeated wave with equal line spacing; retain directional lifted tips.
        # Reference: Geometric repeated cubic flow.
        # One repeated wave definition owns the curve flow and line spacing.
        for i,y in enumerate((8,21,34)):
            self.add_bezier(f'wave-{i}',(4,y+3),((8,y+1),(10,y),(14,y)),((22,y),(24,y+6),(34,y+6)),((39,y+6),(44,y+5),(44,y+1)))
