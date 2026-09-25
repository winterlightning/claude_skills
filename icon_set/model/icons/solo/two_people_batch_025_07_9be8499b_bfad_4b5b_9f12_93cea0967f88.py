"""Two equal busts using shared human user.svg proportions, repeated head and shoulder parameters.
Keyshape ink bounds: (2, 6, 46, 42).
Construction reference: Lucide users; source render establishes subject.
Reduction: Equal-height arrangement emphasizes a balanced pair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9be8499b-bfad-4b5b-9f12-93cea0967f88'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two people_9be8499b-bfad-4b5b-9f12-93cea0967f88.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/two people_9be8499b-bfad-4b5b-9f12-93cea0967f88.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'two-people-batch-025-07'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('two', 'people')

    def build(self):
        for tag,cx in [('left',12),('right',36)]:
         cy,r=12,4
         self.add_arc(tag+'-head-a',(cx-r,cy),(cx+r,cy),radius_x=r)
         self.add_arc(tag+'-head-b',(cx+r,cy),(cx-r,cy),radius_x=r)
         self.add_contour(tag+'-head',tag+'-head-a',tag+'-head-b',closed=True)
         self.add_line(tag+'-side-a',(cx-8,40),(cx-8,32))
         self.add_arc(tag+'-shoulders',(cx-8,32),(cx+8,32),radius_x=8)
         self.add_line(tag+'-side-b',(cx+8,32),(cx+8,40))
         self.add_contour(tag+'-body',tag+'-side-a',tag+'-shoulders',tag+'-side-b')
