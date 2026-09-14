"""Angry Person. Retains all identifying parts, reconstructed on the integer grid.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide user-round: head/shoulder hierarchy; supplied source provides the frown and slanted brows.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dafb63e7-5f8a-47d0-a53c-945b0a5d235d'
SOURCE_PATH = 'pictographic-primitives/symbol/angry person_dafb63e7-5f8a-47d0-a53c-945b0a5d235d.svg'
AUTHOR = 'gpt-6'


class AngryPerson(Solo48):
    icon_id = 'angry-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('angry', 'person', 'face', 'mad', 'emotion', 'frown', 'user', 'upset')

    def build(self) -> None:
        self.add_line('head-top', (16, 6), (32, 6))
        self.add_arc('head-ne', (32, 6), (40, 12), radius_x=8, radius_y=8, sweep=True)
        self.add_line('head-right', (40, 12), (40, 22))
        self.add_arc('head-se', (40, 22), (24, 36), radius_x=16, radius_y=14, sweep=True)
        self.add_arc('head-sw', (24, 36), (8, 22), radius_x=16, radius_y=14, sweep=True)
        self.add_line('head-left', (8, 22), (8, 12))
        self.add_arc('head-nw', (8, 12), (16, 6), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('head', 'head-top', 'head-ne', 'head-right', 'head-se', 'head-sw', 'head-left', 'head-nw', closed=True)
        self.add_line('brow-left', (17, 13), (20, 15))
        self.add_line('brow-right', (28, 15), (31, 13))
        self.add_arc('frown', (20, 26), (28, 26), radius_x=4, radius_y=2, sweep=True)
        self.add_arc('shoulder-left', (8, 42), (24, 36), radius_x=16, radius_y=8, sweep=True)
        self.add_arc('shoulder-right', (24, 36), (40, 42), radius_x=16, radius_y=8, sweep=True)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')
        self.relate("connect", 'head', 'shoulders')
