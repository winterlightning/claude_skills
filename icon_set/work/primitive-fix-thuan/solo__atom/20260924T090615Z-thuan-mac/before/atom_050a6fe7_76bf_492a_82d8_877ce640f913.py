"""Atom. Reduces the source three-orbit structure to two broad crossing orbits, retaining the atom silhouette and central nucleus; omits the tiny extra nucleus ring.

CIRCLE visible extremes (2, 2, 46, 46); centerlines (4, 4, 44, 44).
Lucide atom: two crossing orbital loops and a detached nucleus.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '050a6fe7-76bf-492a-82d8-877ce640f913'
SOURCE_PATH = 'pictographic-primitives/symbol/atom_050a6fe7-76bf-492a-82d8-877ce640f913.svg'
AUTHOR = 'gpt-6'


class Atom(Solo48):
    icon_id = 'atom'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('atom', 'science', 'physics', 'orbit', 'nucleus', 'chemistry', 'nuclear', 'electron')

    def build(self) -> None:
        self.add_arc('orbit-one-cap-a', (10, 22), (24, 8), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('orbit-one-cap-b', (24, 8), (26, 10), radius_x=10, radius_y=10, sweep=True)
        self.add_line('orbit-one-right', (26, 10), (38, 26))
        self.add_arc('orbit-one-cap-c', (38, 26), (24, 40), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('orbit-one-cap-d', (24, 40), (22, 38), radius_x=10, radius_y=10, sweep=True)
        self.add_line('orbit-one-left', (22, 38), (10, 22))
        self.add_contour('orbit-one', 'orbit-one-cap-a', 'orbit-one-cap-b', 'orbit-one-right', 'orbit-one-cap-c', 'orbit-one-cap-d', 'orbit-one-left', closed=True)
        self.add_arc('orbit-two-cap-a', (22, 10), (24, 8), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('orbit-two-cap-b', (24, 8), (38, 22), radius_x=10, radius_y=10, sweep=True)
        self.add_line('orbit-two-right', (38, 22), (26, 38))
        self.add_arc('orbit-two-cap-c', (26, 38), (24, 40), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('orbit-two-cap-d', (24, 40), (10, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_line('orbit-two-left', (10, 26), (22, 10))
        self.add_contour('orbit-two', 'orbit-two-cap-a', 'orbit-two-cap-b', 'orbit-two-right', 'orbit-two-cap-c', 'orbit-two-cap-d', 'orbit-two-left', closed=True)
        self.relate("connect", 'orbit-one', 'orbit-two')
        self.add_dot('nucleus', (24, 24))
