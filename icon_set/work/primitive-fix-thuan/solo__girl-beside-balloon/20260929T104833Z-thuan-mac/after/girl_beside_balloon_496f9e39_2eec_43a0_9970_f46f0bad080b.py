"""Girl beside a pear-shaped balloon with a trailing string.

Plan: SQUARE, centerline bounds (6,6)-(42,42). Circular head above a
rounded shoulder/dress contour, paired legs and a detached balloon.
Human full_body_ref.png informs rounded figure proportions. Head bottom16,
shoulder top24 gives exactly 8 centerline / 4 ink units. Lucide balloon
original and atomic geometry inform its round top and tapered underside.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '496f9e39-2eec-43a0-9970-f46f0bad080b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__girl-beside-balloon/20260929T104833Z-thuan-mac/reference/girl ballon_496f9e39-2eec-43a0-9970-f46f0bad080b.svg'
AUTHOR = 'gpt-6'


class GirlBesideBalloon(Solo48):
    icon_id = 'girl-beside-balloon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people'
    aliases = ()
    keywords = ('girl', 'balloon', 'child', 'dress')

    def build(self):
        self.add_arc('head-top',(9,11),(19,11),radius_x=5)
        self.add_arc('head-bottom',(19,11),(9,11),radius_x=5)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('shoulders',(11,24),(17,24))
        self.add_bezier('dress-right',(17,24),((20,24),(21,30),(22,35)),((22,36),(20,36),(18,36)))
        self.add_line('hem',(18,36),(10,36))
        self.add_bezier('dress-left',(10,36),((8,36),(6,36),(6,35)),((7,30),(8,24),(11,24)))
        self.add_contour('dress','shoulders','dress-right','hem','dress-left',closed=True)
        for x in (10,18):
            self.add_line(f'leg-{x}',(x,36),(x,42))
            self.relate('connect',f'leg-{x}','dress')
        self.add_arc('balloon-top',(28,13),(42,13),radius_x=7)
        self.add_bezier('balloon-right',(42,13),((42,18),(38,22),(35,24)))
        self.add_bezier('balloon-left',(35,24),((32,22),(28,18),(28,13)))
        self.add_contour('balloon','balloon-top','balloon-right','balloon-left',closed=True)
        self.add_bezier('string',(35,24),((35,28),(34,30),(31,31)))
        self.relate('connect','string','balloon')
