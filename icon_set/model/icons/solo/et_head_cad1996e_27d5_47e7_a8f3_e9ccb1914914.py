"""A wide alien head has rounded side lobes and a broad lower muzzle extending beneath them. Two small rounded eyes sit far apart under a gently indented crown, with the rest of the face unmarked.

HRECT_XL visible extremes (2,6)-(46,42); paired side lobes and broad muzzle. Eye rims simplified to small circles. No useful Lucide E.T. match; bilateral symmetry retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cad1996e-27d5-47e7-a8f3-e9ccb1914914'
SOURCE_PATH = 'pictographic-primitives/science/et_cad1996e-27d5-47e7-a8f3-e9ccb1914914.svg'
AUTHOR = 'gpt-6'

class EtHead(Solo48):
    icon_id = 'et-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('et', 'alien', 'head', 'face', 'extraterrestrial', 'fiction')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('crown-left',(4,21),(15,8),radius_x=11,radius_y=13)
        self.add_line('crown-mid-left',(15,8),(24,9))
        self.add_line('crown-mid-right',(24,9),(33,8))
        self.add_arc('crown-right',(33,8),(44,21),radius_x=11,radius_y=13)
        self.add_arc('cheek-right',(44,21),(35,30),radius_x=9)
        self.add_arc('muzzle-right',(35,30),(24,40),radius_x=11,radius_y=10)
        self.add_arc('muzzle-left',(24,40),(13,30),radius_x=11,radius_y=10)
        self.add_arc('cheek-left',(13,30),(4,21),radius_x=9)
        self.add_contour('head','crown-left','crown-mid-left','crown-mid-right','crown-right','cheek-right','muzzle-right','muzzle-left','cheek-left',closed=True)
        self.circle('eye-left',15,20,2)
        self.circle('eye-right',33,20,2)
