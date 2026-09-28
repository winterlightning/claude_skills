"""Moai stone head in left profile with long nose and flared neck base.
VRECT_L 8,4..40,44. Asymmetry preserves face direction. Head and base share
attachment nodes. Omit a detached eye; keep angular nose and heavy chin.
Reference supplies sculpted profile; no useful exact local Lucide match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='2052b61a-5eec-4705-984f-d20c6c071198'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/moai_2052b61a-5eec-4705-984f-d20c6c071198.svg'
AUTHOR='gpt-6-astra'
class Drawing(Solo48):
    icon_id='moai-head-with-long-angular-nose'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=('moai statue','Easter Island statue')
    keywords=('moai','statue','head','stone','nose','sculpture','monument')
    def build(self):
        points=[(14,36),(14,28),(8,28),(20,12),(10,12),(10,4),(32,4)]
        for i,(a,b) in enumerate(zip(points,points[1:])):self.add_line(f'upper-{i}',a,b)
        self.add_arc('crown',(32,4),(36,8),radius_x=4)
        self.add_line('back',(36,8),(36,28))
        self.add_bezier('chin',(36,28),((36,36),(26,36),(14,36)))
        self.add_contour('head',*[f'upper-{i}' for i in range(6)],'crown','back','chin',closed=True)
        self.add_polyline('base',(14,36),(10,44),(40,44),(36,28))
        self.relate('connect','head','base')
