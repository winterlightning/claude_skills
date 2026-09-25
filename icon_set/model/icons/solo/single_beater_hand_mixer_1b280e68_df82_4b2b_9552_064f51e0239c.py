"""Electric Hand Mixer."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b280e68-df82-4b2b-9552-064f51e0239c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mixer_1b280e68-df82-4b2b-9552-064f51e0239c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-beater-hand-mixer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('mixer', 'hand mixer', 'beater', 'appliance', 'baking', 'kitchen', 'handle')

    def build(self):
        # Plan: Hand mixer with rounded motor, recessed grip mark and one oval beater. Lucide blender appliance simplicity. Handle hole reduced to slot, beater wire omitted. Asymmetric envelope (6,6)-(42,42).
        self.add_line('top',(14,6),(32,6))
        self.add_bezier('shoulder',(32,6),((39,6),(42,12),(42,18)))
        self.add_polyline('bottom',(42,18),(42,24),(14,24),(6,24),(6,14))
        self.add_arc('corner',(6,14),(14,6),radius_x=8)
        for a,b in (('top','shoulder'),('shoulder','bottom'),('bottom','corner'),('corner','top')):self.relate('connect',a,b)
        self.add_line('grip',(24,15),(31,15))
        self.add_line('shaft',(14,24),(14,32));self.relate('connect','shaft','bottom')
        self.add_arc('beater-r',(14,32),(14,42),radius_x=6,radius_y=5)
        self.add_arc('beater-l',(14,42),(14,32),radius_x=6,radius_y=5)
        self.add_contour('beater','beater-r','beater-l',closed=True);self.relate('connect','shaft','beater')
