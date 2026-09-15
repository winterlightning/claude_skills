'Shrimp: independent spacing revision.\n\nOpen broad curled tail; remove narrow inner return and tiny segment seam.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
# Variant of shrimp; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c9a4b76d-c47f-5b37-8116-0f507820f490'
SOURCE_PATH = 'pictographic-primitives/animals/shellfish shrimp_c9a4b76d-c47f-5b37-8116-0f507820f490.svg'
AUTHOR = 'gpt-6'

class Shrimp(Solo48):
    icon_id = 'shrimp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('shrimp', 'prawn', 'shellfish', 'seafood', 'sea', 'marine', 'curl', 'food')

    def build(self):
        self.add_polyline('head-top',(8, 14),(14, 14),(26, 14),closed=False)
        self.add_arc('back',(26, 14),(42, 30),radius_x=16,radius_y=16,sweep=True)
        self.add_arc('rump',(42, 30),(30, 42),radius_x=12,radius_y=12,sweep=True)
        self.add_polyline('tail',(30, 42),(6, 42),(6, 30),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'head-top']
        self.contours = [c for c in self.contours if c.contour_id != 'tail']
        self.add_contour('outer','head-top-1','head-top-2','back','rump','tail-1','tail-2',closed=False)
        self.add_arc('head-front',(8, 14),(20, 26),radius_x=12,radius_y=12,sweep=False)
        self.add_line('chin',(20, 26),(26, 26))
        self.add_contour('inner','head-front','chin',closed=False)
        self.add_polyline('antenna',(14, 14),(14, 6),(32, 6),closed=False)
        self.relate('connect','outer','inner')
        self.relate('connect','antenna','outer')
