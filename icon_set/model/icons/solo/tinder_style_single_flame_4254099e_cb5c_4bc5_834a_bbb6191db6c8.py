"""Fire Flame Symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4254099e-cb5c-4bc5-834a-bbb6191db6c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/tinder logo_4254099e-cb5c-4bc5-834a-bbb6191db6c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tinder-style-single-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('flame', 'fire', 'logo', 'tinder', 'burning', 'heat', 'symbol')

    def build(self):
        # Plan: Single broad asymmetric flame with left notch. One smooth outer run and circular lower base, following Lucide flame construction. Bounds (8,4)-(40,44).
        self.add_bezier('flame',(24,4),((27,16),(22,20),(20,23)),((15,22),(11,19),(11,15)),((9,19),(8,24),(8,28)),((8,37),(15,44),(24,44)),((33,44),(40,37),(40,28)),((40,18),(32,8),(24,4)))
        self.add_contour('outline','flame',closed=True)
