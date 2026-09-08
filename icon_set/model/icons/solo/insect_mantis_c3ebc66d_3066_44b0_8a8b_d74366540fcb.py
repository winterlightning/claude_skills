"""Connected mantis head: arched antennae join the brow, and hooked forelegs join the eyes. Mirrored on x=24; SQUARE extremes (2,2)-(46,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3ebc66d-3066-44b0-8a8b-d74366540fcb'
SOURCE_PATH = 'pictographic-primitives/animals/insect mantis_c3ebc66d-3066-44b0-8a8b-d74366540fcb.svg'
AUTHOR = 'gpt-6'


class PrayingMantisHead(Solo48):
    icon_id = 'praying-mantis-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('mantis', 'praying mantis', 'insect', 'head', 'claws', 'antennae', 'bug', 'predator')

    def build(self) -> None:
        # Mantis head and forelegs; centerline extremes (2,2)-(46,46). Mirrored eyes and hooked forelegs, with long swept antennae; fine mouthparts omitted.
        self.add_arc('eye-left-0', (11, 15), (14, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-left-1', (14, 18), (11, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-left-2', (11, 21), (8, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-left-3', (8, 18), (11, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('eye-left', 'eye-left-0', 'eye-left-1', 'eye-left-2', 'eye-left-3', closed=True)
        self.add_arc('eye-right-0', (37, 15), (40, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-right-1', (40, 18), (37, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-right-2', (37, 21), (34, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-right-3', (34, 18), (37, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('eye-right', 'eye-right-0', 'eye-right-1', 'eye-right-2', 'eye-right-3', closed=True)
        self.add_line('brow-left', (11, 15), (20, 15))
        self.add_line('brow-center', (20, 15), (28, 15))
        self.add_line('brow-right', (28, 15), (37, 15))
        self.add_contour('brow', 'brow-left', 'brow-center', 'brow-right')
        self.relate("connect", 'brow', 'eye-left')
        self.relate("connect", 'brow', 'eye-right')
        self.add_polyline('face', (11, 21), (24, 29), (37, 21), closed=False)
        self.relate("connect", 'face', 'eye-left')
        self.relate("connect", 'face', 'eye-right')
        self.add_arc('antenna-left', (20, 8), (2, 8), radius_x=9, radius_y=6, sweep=False)
        self.add_arc('claw-upper-left', (11, 21), (2, 33), radius_x=9, radius_y=12, sweep=False)
        self.add_arc('claw-lower-left', (2, 33), (7, 46), radius_x=5, radius_y=13, sweep=False)
        self.add_contour('claw-left', 'claw-upper-left', 'claw-lower-left')
        self.relate('connect', 'claw-left', 'eye-left')
        self.relate('connect', 'claw-left', 'face')
        self.add_line('claw-tip-left', (7, 46), (15, 34))
        self.relate("connect", 'claw-left', 'claw-tip-left')
        self.add_arc('antenna-right', (28, 8), (46, 8), radius_x=9, radius_y=6, sweep=True)
        self.add_arc('claw-upper-right', (37, 21), (46, 33), radius_x=9, radius_y=12, sweep=True)
        self.add_arc('claw-lower-right', (46, 33), (41, 46), radius_x=5, radius_y=13, sweep=True)
        self.add_contour('claw-right', 'claw-upper-right', 'claw-lower-right')
        self.relate('connect', 'claw-right', 'eye-right')
        self.relate('connect', 'claw-right', 'face')
        self.add_line('claw-tip-right', (41, 46), (33, 34))
        self.relate("connect", 'claw-right', 'claw-tip-right')
        self.add_line('antenna-stem-left', (20, 15), (20, 8))
        self.relate('connect', 'antenna-stem-left', 'brow')
        self.relate('connect', 'antenna-stem-left', 'antenna-left')
        self.add_line('antenna-stem-right', (28, 15), (28, 8))
        self.relate('connect', 'antenna-stem-right', 'brow')
        self.relate('connect', 'antenna-stem-right', 'antenna-right')
