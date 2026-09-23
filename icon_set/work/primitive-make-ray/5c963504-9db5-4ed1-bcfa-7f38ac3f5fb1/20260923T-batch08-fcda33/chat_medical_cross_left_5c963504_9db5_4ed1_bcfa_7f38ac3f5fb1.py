"""chat medical cross left. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; SQUARE bounds (4, 4, 44, 44).
Construction reference: Lucide message-square-plus, round joins and coherent symbol contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1'
SOURCE_PATH = 'icon_set/work/todo-references/chat medical cross left_5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chat-medical-cross-left'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('chat', 'medical', 'cross', 'left')

    def build(self):

        # Rounded speech enclosure with a left tail; a centred medical cross.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        self.add_line('tail-1',(38,34),(22,34))
        self.add_line('tail-2',(22,34),(14,42))
        self.add_line('tail-3',(14,42),(14,34))
        self.add_line('tail-4',(14,34),(10,34))
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('bubble','top','tr','right','br','tail-1','tail-2','tail-3','tail-4','bl','left','tl',closed=True)
        self.add_line('cross-horizontal',(16,20),(24,20))
        self.add_line('cross-right',(24,20),(32,20))
        self.add_line('cross-top',(24,15),(24,20))
        self.add_line('cross-bottom',(24,20),(24,25))
        self.relate('connect','cross-horizontal','cross-right','cross-top','cross-bottom')

