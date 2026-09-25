"""Do Not Disturb Door Handle.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Tall backplate with projecting lever and lower lock circle.
Reduction: Omit slash in small lock circle; retain integrated door hardware.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hotels/do not disturb_7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/do not disturb_7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/do not disturb_7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'door-lever-on-backplate-batch-014-13'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hotels"
    aliases = ()
    keywords = ('door', 'lever', 'handle', 'backplate', 'lock', 'hardware')

    def build(self):
        self.add_line('plate-1', (6, 42), (6, 18))
        self.add_arc('plate-2', (6, 18), (30, 18), radius_x=12, radius_y=12, sweep=True)
        self.add_line('plate-3', (30, 18), (30, 42))
        self.add_line('plate-close', (30, 42), (6, 42))
        self.add_contour('plate', 'plate-1', 'plate-2', 'plate-3', 'plate-close', closed=True)
        self.add_line('lever', (18, 18), (42, 18))
        self.add_arc('lock-1', (18, 27), (21, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('lock-2', (21, 30), (18, 33), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('lock-3', (18, 33), (15, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('lock-4', (15, 30), (18, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('lock', 'lock-1', 'lock-2', 'lock-3', 'lock-4', closed=True)
        self.relate("connect", 'plate', 'lever')
