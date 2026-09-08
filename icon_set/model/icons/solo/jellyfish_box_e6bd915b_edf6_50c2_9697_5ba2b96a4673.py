"""Jellyfish with a broad domed bell and three wavy hanging tentacles. Centerline extremes (5,2)-(43,46). No useful local Lucide jellyfish match. Shallow scallops reduced to a calm rim to keep tentacle junctions open."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6bd915b-edf6-50c2-9697-5ba2b96a4673'
SOURCE_PATH = 'pictographic-primitives/animals/jellyfish box_e6bd915b-edf6-50c2-9697-5ba2b96a4673.svg'
AUTHOR = 'gpt-6'


class Jellyfish(Solo48):
    icon_id = 'jellyfish'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('jellyfish', 'sea', 'ocean', 'marine', 'tentacles', 'bell', 'medusa', 'swim')

    def build(self) -> None:
        self.add_arc('bell-left', (5, 22), (24, 2), radius_x=19, radius_y=20, sweep=True)
        self.add_arc('bell-right', (24, 2), (43, 22), radius_x=19, radius_y=20, sweep=True)
        self.add_line('rim-0', (43, 22), (34, 22))
        self.add_line('rim-1', (34, 22), (24, 22))
        self.add_line('rim-2', (24, 22), (14, 22))
        self.add_line('rim-3', (14, 22), (5, 22))
        self.add_contour('bell', 'bell-left', 'bell-right', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_arc('tentacle-0-upper', (14, 22), (12, 34), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('tentacle-0-lower', (12, 34), (14, 46), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('tentacle-0', 'tentacle-0-upper', 'tentacle-0-lower', closed=False)
        self.relate("connect", 'bell', 'tentacle-0')
        self.add_arc('tentacle-1-upper', (24, 22), (22, 34), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('tentacle-1-lower', (22, 34), (24, 46), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('tentacle-1', 'tentacle-1-upper', 'tentacle-1-lower', closed=False)
        self.relate("connect", 'bell', 'tentacle-1')
        self.add_arc('tentacle-2-upper', (34, 22), (32, 34), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('tentacle-2-lower', (32, 34), (34, 46), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('tentacle-2', 'tentacle-2-upper', 'tentacle-2-lower', closed=False)
        self.relate("connect", 'bell', 'tentacle-2')
