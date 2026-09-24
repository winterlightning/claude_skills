from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aff444cb-feb6-5274-9888-02b69d31bff2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/pen_aff444cb-feb6-5274-9888-02b69d31bff2.svg'
AUTHOR = 'gpt-6'


class DiagonalPenWithCurvedClip(Solo48):
    icon_id = 'diagonal-pen-with-curved-clip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('pen', 'writing', 'nib', 'cap', 'clip', 'stationery', 'ink', 'tool')

    def build(self) -> None:
        # Diagonal rounded barrel and conical nib; the clip curves out to the right.
        self.add_bezier('cap',(26,8),((28,6),(28,6),(30,6)),((33,6),(36,9),(36,12)),((36,14),(35,15),(34,16)))
        points=[(34,16),(30,20),(18,32),(6,42),(10,24),(26,8)]
        for n,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'body-{n}',a,b)
        self.add_contour('pen','cap',*[f'body-{n}' for n in range(1,6)],closed=True)
        self.add_line('band',(22,12),(30,20));self.relate('connect','band','pen')
        self.add_bezier('clip-top',(30,20),((38,20),(42,20),(42,28)))
        self.add_arc('clip-bottom',(42,28),(36,34),radius_x=6)
        self.add_contour('clip','clip-top','clip-bottom');self.relate('connect','clip','pen');self.relate('connect','clip','band')
