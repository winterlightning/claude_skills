"""Gear with Branching Options.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Six-lobed settings wheel attached to a three-arm options branch.
Reduction: Remove incidental terminal dots and center speck; preserve gear and branching diagram.
Construction reference: settings: alternating lobe and valley silhouette
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20a1fb0b-4458-4956-9328-ab0e436276f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'gear-with-branching-lines-batch-015-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('gear', 'branch', 'settings', 'diagram', 'options', 'workflow')

    def build(self):
        self.add_bezier('gear-1', (16, 8), ((20, 8), (19, 16), (23, 16)))
        self.add_bezier('gear-2', (23, 16), ((30, 12), (32, 18), (26, 24)))
        self.add_bezier('gear-3', (26, 24), ((32, 30), (30, 36), (23, 32)))
        self.add_bezier('gear-4', (23, 32), ((19, 32), (20, 40), (16, 40)))
        self.add_bezier('gear-5', (16, 40), ((12, 40), (13, 32), (9, 32)))
        self.add_bezier('gear-6', (9, 32), ((7, 34), (4, 34), (4, 30)))
        self.add_bezier('gear-7', (4, 30), ((4, 28), (6, 26), (6, 24)))
        self.add_bezier('gear-8', (6, 24), ((6, 22), (4, 20), (4, 18)))
        self.add_bezier('gear-9', (4, 18), ((4, 14), (7, 14), (9, 16)))
        self.add_bezier('gear-10', (9, 16), ((13, 16), (12, 8), (16, 8)))
        self.add_contour('gear', 'gear-1', 'gear-2', 'gear-3', 'gear-4', 'gear-5', 'gear-6', 'gear-7', 'gear-8', 'gear-9', 'gear-10', closed=True)
        self.add_polyline('branch', (44, 8), (40, 8), (40, 40), (44, 40), closed=False)
        self.add_line('middle-arm', (26, 24), (44, 24))
        self.relate("connect", 'middle-arm', 'branch')
        self.relate("connect", 'middle-arm', 'gear')
