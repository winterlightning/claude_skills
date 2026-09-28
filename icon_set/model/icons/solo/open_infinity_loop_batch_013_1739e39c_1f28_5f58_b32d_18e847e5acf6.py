"""Smooth open infinity loop: equal broad lobes and separated descending strand ends. Mirror paired lobes about center; use coherent cubic tangents from Lucide infinity.
Lucide infinity: flowing mirrored lobe curves; preserve separated strand ends.
Keyshape HRECT_M on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1739e39c-1f28-5f58-b32d-18e847e5acf6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-infinity-loop-batch-013'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('open', 'infinity', 'loop')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_bezier('rising',(18,15),((16,12),(15,10),(12,10)),((6,10),(4,16),(4,24)),((4,32),(6,38),(12,38)),((21,38),(27,10),(36,10)),((42,10),(44,16),(44,24)),((44,32),(42,38),(36,38)),((33,38),(31,36),(29,33)))
