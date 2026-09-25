"""Large foreground and smaller rear busts, circular heads and smooth shoulders; shared human user.svg.
Keyshape ink bounds: (2, 6, 46, 42).
Construction reference: Lucide users; source render establishes subject.
Reduction: Separate silhouettes retain depth by relative head and shoulder sizes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '482de8d8-4394-4977-8b8b-6abf5b4074e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two users_482de8d8-4394-4977-8b8b-6abf5b4074e7.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/two users_482de8d8-4394-4977-8b8b-6abf5b4074e7.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'two-user-profiles-batch-025-06'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('two', 'user', 'profiles')

    def build(self):
        for tag,cx,cy,r,left,right in [('front',14,14,6,4,24),('rear',38,16,4,32,44)]:
         self.add_arc(tag+'-head-a',(cx-r,cy),(cx+r,cy),radius_x=r)
         self.add_arc(tag+'-head-b',(cx+r,cy),(cx-r,cy),radius_x=r)
         self.add_contour(tag+'-head',tag+'-head-a',tag+'-head-b',closed=True)
         top=cy+r+8
         self.add_arc(tag+'-shoulders',(left,top+6),(right,top+6),radius_x=(right-left)//2,radius_y=6)
         self.add_line(tag+'-left',(left,40),(left,top+6))
         self.add_line(tag+'-right',(right,top+6),(right,40))
         self.add_contour(tag+'-body',tag+'-left',tag+'-shoulders',tag+'-right')
