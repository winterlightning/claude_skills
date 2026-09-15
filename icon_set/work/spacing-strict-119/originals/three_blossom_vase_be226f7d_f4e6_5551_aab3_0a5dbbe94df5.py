"""Three scalloped blossoms above a rounded vase; small side leaf omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be226f7d-f4e6-5551-aab3-0a5dbbe94df5'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration flower vase_be226f7d-f4e6-5551-aab3-0a5dbbe94df5.svg'
AUTHOR = 'gpt-6'

class ThreeBlossomVase(Solo48):
    icon_id = 'three-blossom-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'flowers', 'blossoms', 'bouquet', 'leaf', 'plant', 'decor')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('left0',(8, 6),*(((8, 4.34314575), (9.34314575, 4), (11.0, 4)), ((12.65685425, 4), (14.0, 4.34314575), (14, 6))))
        self.add_arc('left1',(14, 6),(14, 11),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('left2',(14, 11),(8, 11),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_bezier('left3',(8, 11),*(((8, 10.44417642), (8, 9.50552269), (8, 8.5)), ((8, 7.49447731), (8, 6.55582358), (8, 6))))
        self.add_bezier('right0',(34, 6),*(((34.0, 4.34314575), (35.34314575, 4), (37.0, 4)), ((38.65685425, 4), (40, 4.34314575), (40, 6))))
        self.add_bezier('right1',(40, 6),*(((40, 6.55582358), (40, 7.49447731), (40, 8.5)), ((40, 9.50552269), (40, 10.44417642), (40, 11))))
        self.add_arc('right2',(40, 11),(34, 11),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('right3',(34, 11),(34, 6),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('front0',(21, 23),(27, 23),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('front1',(27, 23),(27, 29),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('front2',(27, 29),(21, 29),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('front3',(21, 29),(21, 23),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_line('left-stem',(11, 14),(21, 23))
        self.add_line('right-stem',(37, 14),(27, 23))
        self.add_line('pot-top-1',(24, 32),(34, 32))
        self.add_line('pot-top-2',(34, 32),(34, 42))
        self.add_bezier('pot-r',(34, 42),*(((32.5422399, 43.69026141), (30.21753356, 44), (28, 44)),))
        self.add_line('pot-base',(28, 44),(20, 44))
        self.add_bezier('pot-l',(20, 44),*(((17.78246644, 44), (15.4577601, 43.69026141), (14, 42)),))
        self.add_line('pot-side-1',(14, 42),(14, 32))
        self.add_line('pot-side-2',(14, 32),(24, 32))
        self.add_contour('left',*('left0', 'left1', 'left2', 'left3'),closed=True)
        self.add_contour('right',*('right0', 'right1', 'right2', 'right3'),closed=True)
        self.add_contour('front',*('front0', 'front1', 'front2', 'front3'),closed=True)
        self.add_contour('pot',*('pot-top-1', 'pot-top-2', 'pot-r', 'pot-base', 'pot-l', 'pot-side-1', 'pot-side-2'),closed=True)
        self.relate('connect',*('left-stem', 'left'))
        self.relate('connect',*('left-stem', 'front'))
        self.relate('connect',*('right-stem', 'right'))
        self.relate('connect',*('right-stem', 'front'))
        self.relate('connect',*('pot', 'front'))
