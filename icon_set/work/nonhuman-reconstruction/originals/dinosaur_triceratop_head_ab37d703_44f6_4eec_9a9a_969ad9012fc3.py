"""Triceratops side head with two horns and swept frill. Centerlines (6,6)-(42,42). Lucide bird informs coherent round head; omit neck crease."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab37d703-44f6-4eec-9a9a-969ad9012fc3'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur triceratop head_ab37d703-44f6-4eec-9a9a-969ad9012fc3.svg'
AUTHOR = 'gpt-6'


class TriceratopsHeadSide(Solo48):
    icon_id = 'triceratops-head-side'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('triceratops', 'dinosaur', 'head', 'horns', 'profile', 'prehistoric', 'reptile', 'frill')

    def build(self) -> None:
        self.add_arc('frill',(31,6),(42,23),radius_x=12,radius_y=21)
        self.add_bezier('rear-head', (42, 23), *(((42, 33.11497493), (34.10096577, 41.4676421), (24, 42)),))
        self.add_line('jaw',(24,42),(13,40))
        self.add_polyline('beak',(13,40),(6,36),(10,32),(6,30))
        self.add_arc('nose',(6,30),(9,23),radius_x=10)
        self.add_bezier('nose-horn', (9, 23), *(((6.91000584, 20.09586881), (6, 16.57500539), (6, 13)),))
        self.add_line('nose-horn-return',(6,13),(15,23))
        self.add_line('forehead',(15,23),(25,23))
        self.add_arc('brow-horn',(25,23),(20,6),radius_x=32,sweep=False)
        self.add_arc('brow-horn-return',(20,6),(32,19),radius_x=25)
        self.add_arc('frill-notch',(32,19),(31,6),radius_x=20,sweep=False)
        self.add_contour('head','frill','rear-head','jaw')
        self.relate('connect','head','beak')
        self.add_contour('front','nose','nose-horn','nose-horn-return','forehead','brow-horn','brow-horn-return','frill-notch')
        self.relate('connect','front','head')
        self.relate('connect','front','beak')
        self.add_bezier('neck', (24, 42), *(((26.62364472, 42), (29.37635528, 42), (32, 42)),))
        self.relate('connect','head','neck')
