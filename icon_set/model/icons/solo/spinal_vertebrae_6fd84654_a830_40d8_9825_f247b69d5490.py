"""Spinal Vertebrae.

Plan: Two identical broad vertebral contours in a vertical series, shared width and 26-unit step. Reduce three rows to two to preserve open bone bodies. Bounds (8,4)-(40,44). No useful Lucide anatomy match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fd84654-a830-40d8-9825-f247b69d5490'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty vertebra_6fd84654-a830-40d8-9825-f247b69d5490.svg'
AUTHOR = 'gpt-6'


class SpinalVertebrae(Solo48):
    icon_id = 'spinal-vertebrae'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('spinal', 'vertebrae')

    def build(self):
        # Two broad vertebrae replace three compressed rows; same definition.
        for i in range(2):
            y=4+26*i
            p=f'vertebra-{i}'
            self.add_arc(p+'-upper',(14,y),(34,y),radius_x=10,radius_y=2,sweep=False)
            self.add_arc(p+'-right-top',(34,y),(40,y+6),radius_x=6)
            self.add_arc(p+'-right-bottom',(40,y+6),(32,y+14),radius_x=8)
            self.add_line(p+'-base',(32,y+14),(16,y+14))
            self.add_arc(p+'-left-bottom',(16,y+14),(8,y+6),radius_x=8)
            self.add_arc(p+'-left-top',(8,y+6),(14,y),radius_x=6)
            self.add_contour(p,p+'-upper',p+'-right-top',p+'-right-bottom',p+'-base',p+'-left-bottom',p+'-left-top',closed=True)
