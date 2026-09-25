"""Two Teeth with Braces.

Plan: Two simplified molars joined by orthodontic wire. Reduce brackets to clear upright attachment bars, preserving the paired teeth. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac9c677b-473a-4138-92bb-0d16f69a0b08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dental brace_ac9c677b-473a-4138-92bb-0d16f69a0b08.svg'
AUTHOR = 'gpt-6'


class TwoTeethWithBraces(Solo48):
    icon_id = 'two-teeth-with-braces'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('two', 'teeth', 'with', 'braces')

    def build(self):
        for i in range(2):
            x=4+24*i;p=f'tooth-{i}'
            self.add_arc(p+'-top',(x,16),(x+16,16),radius_x=8)
            self.add_line(p+'-r1',(x+16,16),(x+16,24))
            self.add_line(p+'-r2',(x+16,24),(x+16,36))
            self.add_arc(p+'-root-r',(x+16,36),(x+8,36),radius_x=4)
            self.add_arc(p+'-root-l',(x+8,36),(x,36),radius_x=4)
            self.add_line(p+'-l2',(x,36),(x,24))
            self.add_line(p+'-l1',(x,24),(x,16))
            self.add_contour(p,p+'-top',p+'-r1',p+'-r2',p+'-root-r',p+'-root-l',p+'-l2',p+'-l1',closed=True)
        self.add_polyline('wire',(4,24),(12,24),(20,24),(28,24),(36,24),(44,24))
        for i in range(2):self.relate('connect','wire',f'tooth-{i}')
        for i in range(2):
            x=12+24*i
            self.add_polyline(f'bracket-{i}',(x,20),(x,24),(x,28))
            self.relate('connect',f'bracket-{i}','wire')
