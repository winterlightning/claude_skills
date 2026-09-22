"""Round camera lens on a short pedestal, symmetric about x=24.
VRECT_L bounds follow the circular housing and base. Source supplies two
concentric rings; Lucide webcam supplies the shared bottom node and stem/base
construction. Simplify the source's broad rounded foot to an open T pedestal.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bacf81f7-d345-4811-883f-80c90e127362'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/eardrum_bacf81f7-d345-4811-883f-80c90e127362.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-lens-on-short-pedestal'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Digital Web Camera', 'Round Lens on Short Pedestal')
    keywords = ('lens', 'camera', 'round', 'pedestal', 'device', 'opening', 'stand')

    def build(self):
        for label, radius in [('housing',16), ('lens',6)]:
            top, bottom = (24,20-radius), (24,20+radius)
            self.add_arc(label+'-right',top,bottom,radius_x=radius)
            self.add_arc(label+'-left',bottom,top,radius_x=radius)
            self.add_contour(label,label+'-right',label+'-left',closed=True)
        self.add_line('stem',(24,36),(24,44))
        self.add_line('base-left',(14,44),(24,44))
        self.add_line('base-right',(24,44),(34,44))
        self.add_contour('base','base-left','base-right')
        self.relate('connect','housing','stem')
        self.relate('connect','stem','base')
