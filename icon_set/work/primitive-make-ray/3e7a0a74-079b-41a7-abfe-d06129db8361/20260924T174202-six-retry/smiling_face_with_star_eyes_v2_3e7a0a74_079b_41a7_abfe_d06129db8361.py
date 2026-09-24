"""Smiling face with star eyes.
Plan: SQUARE uses (6,6)-(42,42) for two large outlined stars and a curved lower face.
Design changes: Large five-point eyes form the upper head boundary, joined by a real bridge. The separate enclosing forehead is absorbed into this shared silhouette; smiling arc retained.
References: Original reference establishes star eyes. Lucide star original and atomic-debug reviewed for the alternating five-tip contour; stars share one definition. Human user.svg supplies circular facial vocabulary.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3e7a0a74-079b-41a7-abfe-d06129db8361'
SOURCE_PATH='pictographic-primitives/_uncategorized_17/face awesome_3e7a0a74-079b-41a7-abfe-d06129db8361.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smiling-face-with-star-eyes'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/expressions'
    aliases=()
    keywords=('star','eyes','smile')
    def build(self):
        # Large five-point stars form the upper face boundary; the lower face joins outer tips.
        for i,x in enumerate((13,35)):
            self.add_polyline(f'eye-{i}',(x,6),(x+4,12),(x+7,12),(x+4,16),(x+5,24),(x,22),(x-5,24),(x-4,16),(x-7,12),(x-4,12),closed=True)
        self.add_line('bridge',(20,12),(28,12))
        self.relate('connect','bridge','eye-0')
        self.relate('connect','bridge','eye-1')
        self.add_arc('jaw-left',(8,24),(24,42),radius_x=16,radius_y=18,sweep=False)
        self.add_arc('jaw-right',(24,42),(40,24),radius_x=16,radius_y=18,sweep=False)
        self.add_contour('jaw','jaw-left','jaw-right')
        self.relate('connect','jaw','eye-0')
        self.relate('connect','jaw','eye-1')
        self.add_arc('smile',(20,32),(28,32),radius_x=4,radius_y=1,sweep=False)