"""Capped circular head and broad open shoulders following human user.svg; circular jaw and shoulder ink touch with zero gap.
Keyshape ink bounds: (6, 2, 42, 46).
Construction reference: Lucide user; source render establishes subject.
Reduction: Cap boundary straightened; seam kept short and separated.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '991efad5-dac4-455d-92c1-cfb4bb736b92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person_991efad5-dac4-455d-92c1-cfb4bb736b92.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/person_991efad5-dac4-455d-92c1-cfb4bb736b92.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'capped-person-bust-batch-025-08'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('capped', 'person', 'bust')

    human_construction = "bust"

    def build(self):
        self.add_arc('head-top',(14,14),(34,14),radius_x=10)
        self.add_arc('head-bottom',(34,14),(14,14),radius_x=10)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('cap',(14,14),(34,14))
        self.relate('connect','cap','head')
        self.add_arc('shoulders',(8,44),(40,44),radius_x=16,radius_y=16)
        self.add_line('seam',(24,44),(24,41))
        self.relate('connect','head','shoulders')
