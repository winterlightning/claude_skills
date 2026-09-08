"""Triceratops side head with two horns and swept frill. Centerlines (5,2)-(43,46). Lucide bird informs coherent round head; omit neck crease."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab37d703-44f6-4eec-9a9a-969ad9012fc3'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur triceratop head_ab37d703-44f6-4eec-9a9a-969ad9012fc3.svg'
AUTHOR = 'gpt-6'


class TriceratopsHeadSide(Solo48):
    icon_id = 'triceratops-head-side'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('triceratops', 'dinosaur', 'head', 'horns', 'profile', 'prehistoric', 'reptile', 'frill')

    def build(self) -> None:
        self.add_arc('frill',(31,2),(43,23),radius_x=12,radius_y=21)
        self.add_arc('rear-head',(43,23),(24,42),radius_x=19)
        self.add_line('jaw',(24,42),(13,40))
        self.add_polyline('beak',(13,40),(5,36),(10,32),(5,30))
        self.add_arc('nose',(5,30),(9,23),radius_x=10)
        self.add_arc('nose-horn',(9,23),(6,13),radius_x=16)
        self.add_line('nose-horn-return',(6,13),(15,23))
        self.add_line('forehead',(15,23),(25,23))
        self.add_arc('brow-horn',(25,23),(20,6),radius_x=32,sweep=False)
        self.add_arc('brow-horn-return',(20,6),(32,19),radius_x=25)
        self.add_arc('frill-notch',(32,19),(31,2),radius_x=20,sweep=False)
        self.add_contour('head','frill','rear-head','jaw')
        self.relate('connect','head','beak')
        self.add_contour('front','nose','nose-horn','nose-horn-return','forehead','brow-horn','brow-horn-return','frill-notch')
        self.relate('connect','front','head')
        self.relate('connect','front','beak')
        self.add_arc('neck',(24,42),(32,46),radius_x=16,sweep=False)
        self.relate('connect','head','neck')
