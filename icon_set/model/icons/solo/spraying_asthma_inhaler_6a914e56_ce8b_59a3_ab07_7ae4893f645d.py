"""Spraying Asthma Inhaler.

Plan: L-shaped housing and exposed canister; repeated spray strokes. Upright canister keeps clearance; asymmetric mouthpiece faces right. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a914e56-ce8b-59a3-ab07-7ae4893f645d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/inhaler spray_6a914e56-ce8b-59a3-ab07-7ae4893f645d.svg'
AUTHOR = 'gpt-6'


class SprayingAsthmaInhaler(Solo48):
    icon_id = 'spraying-asthma-inhaler'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('spraying', 'asthma', 'inhaler')

    def build(self):
        points=[(6,16),(22,16),(22,30),(30,30),(30,42),(12,42)]
        for j,(a,b) in enumerate(zip(points,points[1:])):
            self.add_line(f'housing-{j}',a,b)
        self.add_arc('heel',(12,42),(6,36),radius_x=6)
        self.add_line('housing-left',(6,36),(6,16))
        self.add_contour('body',*[f'housing-{j}' for j in range(5)],'heel','housing-left',closed=True)
        self.add_polyline('canister',(6,16),(6,6),(22,6),(22,16))
        self.relate('connect','body','canister')
        self.add_line('spray-top',(39,26),(42,24))
        self.add_line('spray-middle',(39,34),(42,34))
