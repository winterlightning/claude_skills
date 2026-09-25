"""Rounded door backplate with projecting lever and lower round lock. Omit lock slash and double lever edge so openings remain clear; deliberate rightward projection.
No useful exact Lucide hardware match; supplied backplate and projecting lever establish subject.
Keyshape VRECT_L on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hotels/do not disturb_7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/do not disturb_7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/do not disturb_7eee6aa4-0ac9-47c7-b9fc-9f0cef4c83b0.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'door-lever-on-backplate-batch-013'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('door', 'lever', 'on', 'backplate')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_arc('plate-top',(8,15),(30,15),radius_x=11)
        self.add_polyline('plate-bottom',(30,24),(30,44),(8,44),(8,15))
        self.relate('connect','plate-top','plate-bottom')
        self.add_polyline('lever',(18,24),(30,24),(40,24))
        self.relate('connect','lever','plate-bottom')
        circle('lock',19,34,2)
