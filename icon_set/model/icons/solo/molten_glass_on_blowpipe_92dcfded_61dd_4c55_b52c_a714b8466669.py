"""Molten Glass on Blowpipe.

Plan: Large glass bulb with diagonal blowpipe and one rising heat stroke. Remove inner reflection and second heat wave. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92dcfded-61dd-4c55-b52c-a714b8466669'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/glass blowing 1_92dcfded-61dd-4c55-b52c-a714b8466669.svg'
AUTHOR = 'gpt-6'

class MoltenGlassOnBlowpipe(Solo48):
    icon_id = 'molten-glass-on-blowpipe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hobbies"
    aliases = ()
    keywords = ('molten', 'glass', 'on', 'blowpipe')

    def build(self):
        self.add_arc('bulb-upper',(30,32),(18,22),radius_x=12,radius_y=10,sweep=False)
        self.add_arc('bulb-left',(18,22),(6,32),radius_x=12,radius_y=10,sweep=False)
        self.add_arc('bulb-bottom',(6,32),(30,32),radius_x=12,radius_y=10,sweep=False)
        self.add_contour('bulb','bulb-upper','bulb-left','bulb-bottom',closed=True)
        self.add_line('pipe',(30,32),(42,6));self.relate('connect','pipe','bulb')
        self.add_arc('heat',(10,6),(10,14),radius_x=4)
