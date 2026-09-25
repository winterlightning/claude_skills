"""Widen the gate from 8 to 12 centerline units and raise its lintel by one unit; remove the inner tower divider so the larger opening stays clear. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '437c1e1f-16fd-515d-8ae3-fa2eab4a2640'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_437c1e1f-16fd-515d-8ae3-fa2eab4a2640.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'castle-with-gate-tower'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('castle', 'fortress', 'gate', 'tower', 'battlement', 'spire', 'medieval', 'flag')

    def build(self):
        """Symbol plan: Widen the gate from 8 to 12 centerline units and raise its lintel by one unit; remove the inner tower divider so the larger opening stays clear. Reference: Lucide castle: one clear gate opening within the castle silhouette."""
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx, radius_y=rx if ry is None else ry, sweep=sweep)
        p('castle', (6, 42), (6, 24), (30, 24), (30, 16), (42, 16), (42, 42), (6, 42))
        p('roof', (30, 16), (36, 6), (42, 16))
        link('connect', 'castle', 'roof')
        p('gate', (14, 42), (14, 33), (26, 33), (26, 42))
        link('connect', 'gate', 'castle')
        l('pole', (6, 24), (6, 6))
        p('flag', (6, 6), (20, 6), (16, 14), (6, 14))
        link('connect', 'flag', 'pole')
        link('connect', 'pole', 'castle')
