"""Left-facing crocodile with open wedge jaws and scalloped body. Extrema (6,8)-(42,40). Tiny teeth omitted to keep the open jaw readable; profile asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b3f8555-9dd9-5eed-9e14-306ed68ff106'
SOURCE_PATH = 'pictographic-primitives/animals/reptile hippo_4b3f8555-9dd9-5eed-9e14-306ed68ff106.svg'
AUTHOR = 'gpt-6'


class OpenMouthCrocodile(Solo48):
    icon_id = 'open-mouth-crocodile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('crocodile', 'alligator', 'mouth', 'jaws', 'open', 'reptile', 'teeth', 'bite')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('skull',(4, 16),*(((4, 12.25786848), (6.96800053, 8.93412832), (12, 8)),))
        self.add_bezier('brow',(12, 8),*(((17.5228475, 8), (22.0, 12.4771525), (22, 18)),))
        self.add_arc('ridge',(22, 18),(32, 18),radius_x=5,radius_y=4,large_arc=False,sweep=True)
        self.add_bezier('back',(32, 18),*(((39.18226645, 19.82633427), (44, 25.59406833), (44, 32)),))
        self.add_line('tail',(44, 32),(44, 40))
        self.add_bezier('belly-right',(44, 40),*(((36.31773355, 39.34773776), (31.7343768, 37.28783274), (32, 35)),))
        self.add_arc('belly-left',(32, 35),(18, 35),radius_x=9,radius_y=8,large_arc=False,sweep=True)
        self.add_bezier('jaw-lower',(18, 35),*(((14.50610396, 37.10575251), (8.90635852, 37.48750394), (4, 36)),))
        self.add_line('mouth-lower',(4, 36),(15, 29))
        self.add_arc('mouth-hinge',(15, 29),(15, 23),radius_x=4,radius_y=4,large_arc=False,sweep=False)
        self.add_line('mouth-upper',(15, 23),(4, 16))
        self.add_line('eye',(26, 25),(26, 25))
        self.add_contour('outline',*('skull', 'brow', 'ridge', 'back', 'tail', 'belly-right', 'belly-left', 'jaw-lower', 'mouth-lower', 'mouth-hinge', 'mouth-upper'),closed=False)
