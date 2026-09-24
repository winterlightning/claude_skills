"""Bulb above a battery with a detached U-shaped circuit wire. SQUARE bounds.
Natural electrical scene, not a badge combination. Lucide lightbulb informs
pear-shaped bulb contour. Omit filament, minus and small battery step to retain
clearance; keep all three physical components and source arrangement.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ac0c54d-d3b5-4b3a-822d-460c4ff8f217'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/science electricity_9ac0c54d-d3b5-4b3a-822d-460c4ff8f217.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'light-bulb-and-battery-circuit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Light Bulb Electrical Circuit']
    keywords = ['bulb','battery','circuit','wire','electricity','science']
    def build(self):
        self.add_bezier('bulb-left',(12,26),((12,20),(6,22),(6,16)),((6,10),(10,6),(16,6)))
        self.add_bezier('bulb-right',(16,6),((22,6),(26,10),(26,16)),((26,22),(20,20),(20,26)))
        self.add_line('bulb-base',(20,26),(12,26))
        self.add_contour('bulb','bulb-left','bulb-right','bulb-base',closed=True)
        self.add_polyline('battery',(6,34),(27,34),(27,42),(6,42),closed=True)
        self.add_bezier('wire',(36,16),((42,16),(42,18),(42,22)))
        self.add_line('wire-right',(42,22),(42,36))
        self.add_arc('wire-turn',(42,36),(36,42),radius_x=6)
        self.add_contour('circuit-wire','wire','wire-right','wire-turn')
