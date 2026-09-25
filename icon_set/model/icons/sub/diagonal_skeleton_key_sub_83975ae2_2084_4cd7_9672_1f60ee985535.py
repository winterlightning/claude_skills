"""Simple Skeleton Key Symbol: complete-source SUB32 candidate."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '83975ae2-2084-4cd7-9672-1f60ee985535'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/key 3_83975ae2-2084-4cd7-9672-1f60ee985535.svg'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'diagonal-skeleton-key-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'

    def build(self):

        # Round bow at upper right, diagonal shaft, two equal southeast teeth.
        # Lucide key-round and atomic-debug informed the round bow/diagonal axis.
        # Radius five has exact integer diagonal points (22,11) and (28,3).
        self.add_arc('bow-a', (22,11), (28,3), radius_x=5)
        self.add_arc('bow-b', (28,3), (22,11), radius_x=5)
        self.add_contour('bow', 'bow-a','bow-b', closed=True)
        self.add_line('shaft', (2,26), (22,11))
        self.relate('connect','shaft','bow')
        for name, start in [('tip',(2,26)), ('middle',(10,20))]:
            end = (start[0]+3, start[1]+4)
            self.add_line(name,start,end)
            self.relate('connect','shaft',name)

