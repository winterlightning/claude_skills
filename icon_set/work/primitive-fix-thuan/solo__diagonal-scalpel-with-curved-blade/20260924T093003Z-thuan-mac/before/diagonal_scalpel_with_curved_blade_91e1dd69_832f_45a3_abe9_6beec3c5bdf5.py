"""Surgical Scalpel Tool.

Symbol plan: Diagonal broad scalpel handle with tangent semicircular cap and asymmetric pointed blade. One collar replaces two tightly spaced source bands; Lucide pencil informs handle.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91e1dd69-832f-45a3-abe9-6beec3c5bdf5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/razor cut_91e1dd69-832f-45a3-abe9-6beec3c5bdf5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'diagonal-scalpel-with-curved-blade'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('surgical', 'scalpel', 'tool')

    def build(self):
        self.add_line('handle-upper',(10,20),(26,8))
        self.add_arc('cap',(26,8),(38,24),radius_x=10)
        self.add_line('handle-lower',(38,24),(22,36))
        self.add_arc('blade-lower',(22,36),(6,42),radius_x=28)
        self.add_line('blade-upper',(6,42),(10,20))
        self.add_contour('outline','handle-upper','cap','handle-lower','blade-lower','blade-upper',closed=True)
        self.add_line('collar',(10,20),(22,36))
        self.relate('connect','collar','outline')
