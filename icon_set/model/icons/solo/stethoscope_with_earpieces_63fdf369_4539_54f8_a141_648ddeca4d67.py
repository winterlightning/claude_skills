"""Stethoscope with Earpieces.

Plan: U-frame with quarter-circle split at hose attachment; flexible lower U and chestpiece. Lucide stethoscope informs tangent tubing. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63fdf369-4539-54f8-a141-648ddeca4d67'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/instrument_63fdf369-4539-54f8-a141-648ddeca4d67.svg'
AUTHOR = 'gpt-6'


class StethoscopeWithEarpieces(Solo48):
    icon_id = 'stethoscope-with-earpieces'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('stethoscope', 'with', 'earpieces')

    def build(self):
        self.add_line('ear-left',(8,4),(8,16))
        self.add_arc('frame-left',(8,16),(16,24),radius_x=8,sweep=False)
        self.add_arc('frame-right',(16,24),(24,16),radius_x=8,sweep=False)
        self.add_line('ear-right',(24,16),(24,4))
        self.add_contour('frame','ear-left','frame-left','frame-right','ear-right')
        self.add_line('hose-down',(16,24),(16,34))
        self.add_arc('hose-loop',(16,34),(36,34),radius_x=10,sweep=False)
        self.add_line('hose-up',(36,34),(36,26))
        self.add_contour('hose','hose-down','hose-loop','hose-up')
        self.add_arc('chest-right',(36,26),(36,18),radius_x=4,sweep=False)
        self.add_arc('chest-left',(36,18),(36,26),radius_x=4,sweep=False)
        self.add_contour('chestpiece','chest-right','chest-left',closed=True)
        self.relate('connect','frame','hose')
        self.relate('connect','hose','chestpiece')
        self.add_line('left-ear-tip',(8,4),(12,4))
        self.add_line('right-ear-tip',(20,4),(24,4))
        self.relate('connect','frame','left-ear-tip')
        self.relate('connect','frame','right-ear-tip')
