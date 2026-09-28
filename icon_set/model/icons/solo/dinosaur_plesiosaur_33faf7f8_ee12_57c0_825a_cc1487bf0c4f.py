"""A swimming plesiosaur with a long neck and two paddles."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33faf7f8-ee12-57c0-825a-cc1487bf0c4f'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur plesiosaur_33faf7f8-ee12-57c0-825a-cc1487bf0c4f.svg'
AUTHOR = 'gpt-6'


class Plesiosaur(Solo48):
    icon_id = 'plesiosaur'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('plesiosaur', 'dinosaur', 'marine', 'swimming', 'prehistoric', 'reptile', 'sea', 'extinct')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('head',(8,12),((6,12),(6,10),(6,9)),((6,7),(6,6),(8,6)))
        self.add_line('crown',(8, 6),(12, 6))
        self.add_bezier('nape',(12, 6),*(((14.21753356, 6), (16.5422399, 6.24779087), (18, 8)),))
        self.add_line('neck',(18, 8),(20, 24))
        self.add_arc('back',(20,24),(34,26),radius_x=18,radius_y=8)
        self.add_line('tail-1',(34,26),(42,32))
        self.add_line('tail-2',(42,32),(34,35))
        self.add_line('tail-3',(34,35),(34,42))
        self.add_bezier('rear-paddle',(34,42),((30,42),(29,39),(26,36)))
        self.add_line('belly',(26,36),(20,36))
        self.add_line('front-paddle-tip',(20, 36),(16, 42))
        self.add_bezier('front-paddle',(16, 42),*(((13.43487422, 42), (11.02084694, 39.93781809), (10, 36)),))
        self.add_line('throat',(10, 36),(8, 12))
        self.add_contour('reptile',*('head', 'crown', 'nape', 'neck', 'back', 'tail-1', 'tail-2', 'tail-3', 'rear-paddle', 'belly', 'front-paddle-tip', 'front-paddle', 'throat'),closed=True)
