"""Symmetric cow head with broad muzzle and drooping leaf ears. Paired arcs use shared mirrored dimensions; eyes omitted as in the source. No useful local Lucide cow match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb85044f-327b-4e51-b138-6ce8832a4242'
SOURCE_PATH = 'pictographic-primitives/animals/cow_cb85044f-327b-4e51-b138-6ce8832a4242.svg'
AUTHOR = 'gpt-6'


class CowHead(Solo48):
    icon_id = 'cow-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('cow', 'cattle', 'head', 'ears', 'muzzle', 'farm', 'bovine', 'dairy')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # Visible bounds: (0, 0, 48, 48); centerline inset 2.
        self.add_arc('crown', (14, 16), (34, 16), radius_x=10, radius_y=8, sweep=True)
        self.add_line('cheek-left', (14, 16), (16, 37))
        self.add_line('cheek-right', (34, 16), (32, 37))
        self.add_arc('muzzle-bottom', (32, 37), (16, 37), radius_x=8, radius_y=5, sweep=True)
        self.add_contour('head', 'cheek-left', closed=False)
        self.add_contour('right', 'cheek-right', 'muzzle-bottom', closed=False)
        self.relate("connect", 'crown', 'head')
        self.relate("connect", 'crown', 'right')
        self.relate("connect", 'head', 'right')
        self.add_arc('muzzle-top', (16, 37), (32, 37), radius_x=8, radius_y=5, sweep=True)
        self.relate("connect", 'muzzle-top', 'head')
        self.relate("connect", 'muzzle-top', 'right')
        self.add_arc('horn-left', (24, 8), (6, 6), radius_x=19, radius_y=6, sweep=True)
        self.relate("connect", 'horn-left', 'crown')
        self.add_arc('ear-left', (14, 16), (6, 27), radius_x=8, radius_y=11, sweep=False)
        self.add_arc('ear-bottom-left', (6, 27), (13, 28), radius_x=7, radius_y=1, sweep=False)
        self.relate("connect", 'ear-left', 'ear-bottom-left')
        self.relate("connect", 'ear-left', 'crown')
        self.relate("connect", 'ear-left', 'head')
        self.add_arc('horn-right', (24, 8), (42, 6), radius_x=19, radius_y=6, sweep=False)
        self.relate("connect", 'horn-right', 'crown')
        self.add_arc('ear-right', (34, 16), (42, 27), radius_x=8, radius_y=11, sweep=True)
        self.add_arc('ear-bottom-right', (42, 27), (35, 28), radius_x=7, radius_y=1, sweep=True)
        self.relate("connect", 'ear-right', 'ear-bottom-right')
        self.relate("connect", 'ear-right', 'crown')
        self.relate("connect", 'ear-right', 'right')
