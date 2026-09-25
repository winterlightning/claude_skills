"""Looping Sewing Thread.

Plan: One thread makes a broad open upper curl, central loop and lower tail. Reduce multiple overlaps to one visible crossing. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44e88e9d-a0d5-432e-b08f-05a0b1522e97'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/crafts sewing_44e88e9d-a0d5-432e-b08f-05a0b1522e97.svg'
AUTHOR = 'gpt-6'

class LoopingSewingThread(Solo48):
    icon_id = 'looping-sewing-thread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ()
    keywords = ('looping', 'sewing', 'thread')

    def build(self):
        self.add_arc('curl',(14,18),(14,6),radius_x=6,sweep=False)
        self.add_arc('turn',(14,6),(24,16),radius_x=10)
        self.add_line('diagonal',(24,16),(36,28))
        self.add_arc('right',(36,28),(36,42),radius_x=6,radius_y=7)
        self.add_arc('lower',(36,42),(24,30),radius_x=12)
        self.add_arc('left-loop',(24,30),(6,30),radius_x=9)
        self.add_arc('loop-up',(6,30),(14,22),radius_x=8)
        
        self.add_contour('thread','curl','turn','diagonal','right','lower','left-loop','loop-up')
