"""Partly occluded record rim meets a broad hand in the lower right. Merge fine fingers into one extended group plus thumb; omit the obscured spindle hole and sheen. Centerline extremes (6,6)-(42,42). Human reference: full_body_ref.png continuous round-ended limbs; Lucide hand and disc. No detached head."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='65e3fe01-2acf-45bd-91bb-84820fe24a5a'
SOURCE_PATH='pictographic-primitives/music/modern music dj tape_65e3fe01-2acf-45bd-91bb-84820fe24a5a.svg'
AUTHOR='gpt-6'

class DjHandOnRecord(Solo48):
    icon_id='dj-hand-on-record'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('dj', 'turntable', 'record', 'scratch', 'hand', 'vinyl', 'mixing', 'music')

    def build(self):
        self.add_arc('record-top',(20,6),(6,20),radius_x=14,sweep=False)
        self.add_bezier('record-bottom',(6,20),((6,24),(7,28),(9,31)))
        self.add_contour('record','record-top','record-bottom')
        points=((28,18),(42,32),(42,42),(26,42),(14,36))
        for n,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'hand-outer-{n}',a,b)
        self.add_arc('thumb-bottom',(14,36),(9,31),radius_x=5)
        self.add_arc('thumb-top',(9,31),(14,26),radius_x=5)
        self.add_line('thumb-web',(14,26),(24,30))
        self.add_line('finger-inner',(24,30),(20,24))
        self.add_bezier('fingertips',(20,24),((14,18),(22,12),(28,18)))
        self.add_contour('hand',*[f'hand-outer-{n}' for n in range(1,5)],'thumb-bottom','thumb-top','thumb-web','finger-inner','fingertips',closed=True)
        self.relate('connect','record','hand')
