"""Molecule (science), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14a03156-aefb-4868-8884-03d2980af425'
SOURCE_PATH = 'pictographic-primitives/science/molecule_14a03156-aefb-4868-8884-03d2980af425.svg'
AUTHOR = 'gpt-6'

class Molecule(Solo48):
    icon_id = 'molecule'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('molecule', 'science')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_arc('sym-e0',(19, 13),(29, 13),radius_x=5,radius_y=5,large_arc=False,sweep=True)
        self.add_arc('sym-e1',(29, 13),(19, 13),radius_x=5,radius_y=5,large_arc=False,sweep=True)
        self.add_arc('sym-e2',(33, 35),(44, 35),radius_x=5,radius_y=5,large_arc=False,sweep=True)
        self.add_bezier('sym-e3',(44, 35),*(((44, 38.03756612), (41.53756612, 40), (38.5, 40)), ((35.46243388, 40), (33.0, 38.03756612), (33, 35))))
        self.add_arc('sym-e4',(15, 35),(4, 35),radius_x=5,radius_y=5,large_arc=False,sweep=False)
        self.add_bezier('sym-e5',(4, 35),*(((4, 38.03756612), (6.46243388, 40), (9.5, 40)), ((12.53756612, 40), (15.0, 38.03756612), (15, 35))))
        self.add_line('sym-e6',(33, 35),(15, 35))
        self.add_line('sym-e7',(38, 30),(28, 17))
        self.add_line('sym-e8',(10, 30),(20, 17))
        self.add_contour('sym-c0',*('sym-e0', 'sym-e1'),closed=True)
        self.add_contour('sym-c1',*('sym-e2', 'sym-e3'),closed=True)
        self.add_contour('sym-c2',*('sym-e4', 'sym-e5'),closed=True)
        self.add_contour('sym-c3',*('sym-e6',),closed=False)
        self.add_contour('sym-c4',*('sym-e7',),closed=False)
        self.add_contour('sym-c5',*('sym-e8',),closed=False)
        self.relate('connect',*('sym-c1', 'sym-c3'))
        self.relate('connect',*('sym-c2', 'sym-c3'))
        self.relate('connect',*('sym-c2', 'sym-c5'))
        self.relate('connect',*('sym-c1', 'sym-c4'))
        self.relate('connect',*('sym-c0', 'sym-c5'))
        self.relate('connect',*('sym-c0', 'sym-c4'))
        self.relate('connect',*('sym-c2', 'sym-c3'))
        self.relate('connect',*('sym-c1', 'sym-c3'))
