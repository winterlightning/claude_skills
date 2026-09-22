"""Dining table between inward-facing chairs and a bowl. HRECT_L spans chair backs and feet. Chairs mirror about x24 with shared seat nodes; central pedestal simplifies four table legs. Source supplies dining arrangement; Lucide armchair supplies shared seat/leg construction. Bowl retained, thin tabletop thickness omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '9cde1498-b4f8-473c-bf34-8b315d13a18e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/lunchroom_9cde1498-b4f8-473c-bf34-8b315d13a18e.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'dining-table-two-chairs-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Dining Table Between Two Chairs with Bowl',)
    keywords = ('dining', 'table', 'two', 'chairs', 'bowl')
    def build(self):
        axis = 24
        for label, x, inward in [('left',4,1), ('right',44,-1)]:
            seat = (x,32)
            self.add_line(label+'-back',(x,8),seat)
            self.add_line(label+'-rear-leg',seat,(x,40))
            self.add_polyline(label+'-seat',seat,(x+inward*8,32),(x+inward*8,40))
            self.relate('connect',label+'-back',label+'-rear-leg',label+'-seat')
        self.add_line('table-left',(12,20),(axis,20))
        self.add_line('table-right',(axis,20),(36,20))
        self.add_line('pedestal',(axis,20),(axis,40))
        self.relate('connect','table-left','table-right','pedestal')
        self.add_bezier('bowl',(16,8),((16,16),(20,20),(24,20)),((28,20),(32,16),(32,8)))
        self.add_line('rim',(32,8),(16,8))
        self.add_contour('dish','bowl','rim',closed=True)
        self.relate('connect','dish','table-left','table-right','pedestal')
