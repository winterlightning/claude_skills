"""Mirrored bug with a plain rounded body, small head, two antennae and six legs. Lucide bug informs shared-endpoint leg attachments and paired radii."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7a8728f-7d41-4594-84ad-c41d60d742d9'
SOURCE_PATH = 'pictographic-primitives/animals/pet_d7a8728f-7d41-4594-84ad-c41d60d742d9.svg'
AUTHOR = 'gpt-6'


class RoundBug(Solo48):
    icon_id = 'round-bug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ('beetle',)
    keywords = ('bug', 'insect', 'beetle', 'small', 'antennae', 'legs', 'pest', 'nature')

    def build(self) -> None:
        self.add_arc('body-1', (12, 27), (18, 19), radius_x=6, radius_y=8, sweep=True)
        self.add_line('body-2', (18, 19), (30, 19))
        self.add_arc('body-3', (30, 19), (36, 27), radius_x=6, radius_y=8, sweep=True)
        self.add_line('body-4', (36, 27), (36, 34))
        self.add_arc('body-5', (36, 34), (30, 44), radius_x=6, radius_y=10, sweep=True)
        self.add_arc('body-6', (30, 44), (24, 46), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-7', (24, 46), (18, 44), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-8', (18, 44), (12, 34), radius_x=6, radius_y=10, sweep=True)
        self.add_line('body-9', (12, 34), (12, 27))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', closed=True)
        self.add_line('head-1', (18, 19), (18, 13))
        self.add_arc('head-2', (18, 13), (24, 7), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('head-3', (24, 7), (30, 13), radius_x=6, radius_y=6, sweep=True)
        self.add_line('head-4', (30, 13), (30, 19))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', closed=False)
        self.add_arc('antenna-left-1', (18, 13), (11, 2), radius_x=15, radius_y=15, sweep=False)
        self.add_contour('antenna-left', 'antenna-left-1', closed=False)
        self.add_arc('antenna-right-1', (30, 13), (37, 2), radius_x=15, radius_y=15, sweep=True)
        self.add_contour('antenna-right', 'antenna-right-1', closed=False)
        self.add_arc('leg-l1-1', (12, 27), (2, 24), radius_x=12, radius_y=12, sweep=False)
        self.add_contour('leg-l1', 'leg-l1-1', closed=False)
        self.add_arc('leg-r1-1', (36, 27), (46, 24), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('leg-r1', 'leg-r1-1', closed=False)
        self.add_line('leg-l2-1', (12, 34), (2, 34))
        self.add_contour('leg-l2', 'leg-l2-1', closed=False)
        self.add_line('leg-r2-1', (36, 34), (46, 34))
        self.add_contour('leg-r2', 'leg-r2-1', closed=False)
        self.add_arc('leg-l3-1', (18, 44), (5, 46), radius_x=15, radius_y=15, sweep=False)
        self.add_contour('leg-l3', 'leg-l3-1', closed=False)
        self.add_arc('leg-r3-1', (30, 44), (43, 46), radius_x=15, radius_y=15, sweep=True)
        self.add_contour('leg-r3', 'leg-r3-1', closed=False)
        self.relate("connect", 'body', 'head')
        self.relate("connect", 'head', 'antenna-left')
        self.relate("connect", 'head', 'antenna-right')
        self.relate("connect", 'body', 'leg-l1')
        self.relate("connect", 'body', 'leg-r1')
        self.relate("connect", 'body', 'leg-l2')
        self.relate("connect", 'body', 'leg-r2')
        self.relate("connect", 'body', 'leg-l3')
        self.relate("connect", 'body', 'leg-r3')
