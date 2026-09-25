"""Align Objects Left.

Plan: Three outlined bars share a left edge beside a vertical guide; heights8, pitch16 and shortening widths. Envelope 8,4–40,44.
Construction reference: align-start-horizontal (local original and atomic-debug inspected).
Simplification: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c30d475-aa27-4179-9e42-3e04f097ab0a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/objects align left_4c30d475-aa27-4179-9e42-3e04f097ab0a.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'left-object-alignment'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('align', 'objects', 'left')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, left, top, right, bottom, r=2):
            pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for j,a in enumerate(pts):
                b=pts[(j+1)%8]; eid=f'{name}-{j}'; members.append(eid)
                if j%2: self.add_arc(eid,a,b,radius_x=r)
                else: self.add_line(eid,a,b)
            self.add_contour(name,*members,closed=True)

        self.add_line('guide',(8,4),(8,44))
        for j,right in enumerate((40,34,28)):
            rect(f'bar-{j}',17,4+j*16,right,12+j*16,2)
