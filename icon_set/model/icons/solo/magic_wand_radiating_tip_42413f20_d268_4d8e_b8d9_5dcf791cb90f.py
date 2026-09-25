"""Magic Wand with Sparkles.
Plan: Diagonal wand and five correctly oriented rays in an open radial burst around its tip. Centerline extremes (6,6)-(42,42).
Reference: Lucide wand: diagonal stem with detached straight radial strokes.
Reduction: Seven rays reduced to five.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42413f20-d268-4d8e-b8d9-5dcf791cb90f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/selection wand_42413f20-d268-4d8e-b8d9-5dcf791cb90f.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'magic-wand-radiating-tip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('magic', 'wand', 'with', 'sparkles')

    def build(self):

        self.add_line('wand',(6,42),(27,21))
        self.add_line('north',(28,6),(28,11))
        self.add_line('northeast',(37,11),(42,6))
        self.add_line('east',(37,22),(42,22))
        self.add_line('southeast',(36,31),(40,35))
        self.add_line('northwest',(14,7),(18,11))
