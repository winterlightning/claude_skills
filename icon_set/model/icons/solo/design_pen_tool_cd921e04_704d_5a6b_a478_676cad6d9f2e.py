"""A pen nib beneath a Bezier control diamond and guide arms.
Symbol plan and construction: pen-tool: closed nib and identifying slit; supplied reference: mirrored Bezier handles.
Keyshape: SQUARE gives the diamond and nib separate vertical bands.
Omissions: Tiny vent circle and short cuff extensions.
Review: The enlarged control diamond joins real handle nodes. Shared left/right guide parameters maintain symmetry; the vent was removed rather than crowded between nib walls."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd921e04-704d-5a6b-a478-676cad6d9f2e'
SOURCE_PATH = 'pictographic-primitives/design/design pen tool_cd921e04-704d-5a6b-a478-676cad6d9f2e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'design-pen-tool'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('design', 'pen', 'tool')



    def build(self):
        # Wider control diamond shares genuine handle endpoints.
        self.add_polyline('control',(24,6),(30,12),(24,18),(18,12),closed=True)
        for name,left in [('left',True),('right',False)]:
            x,tip=(6,18) if left else (42,30)
            self.add_line('handle-'+name,(x,12),(tip,12))
            self.add_bezier('guide-'+name,(x,26),((x,20),(tip,16),(tip,12)))
            self.relate('connect','guide-'+name,'handle-'+name)
            self.relate('connect','control','handle-'+name)
            self.relate('connect','control','guide-'+name)
        self.add_polyline('nib',(24,26),(36,32),(32,42),(16,42),(12,32),closed=True)
        self.add_line('slit',(24,26),(24,34))
        self.relate('connect','slit','nib')
