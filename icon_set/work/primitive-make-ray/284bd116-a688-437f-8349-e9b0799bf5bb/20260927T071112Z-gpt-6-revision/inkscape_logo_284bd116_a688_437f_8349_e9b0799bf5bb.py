"""The Inkscape mountain peaks above a two-lobed, dripping ink silhouette.
Plan: Mirror the lower ink flow around the summit axis and keep a small snow mark with a clear opening.
SOLO48 SQUARE centreline bounds (6,6)-(42,42). The full wavy snow line is reduced because its narrow bands fail clearance.
Lucide mountain informed the angular summit; flower-2 informed smooth paired lower curves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '284bd116-a688-437f-8349-e9b0799bf5bb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__inkscape-logo/20260927T070909Z-thuan-mac-1/reference/inkscape logo_284bd116-a688-437f-8349-e9b0799bf5bb.svg'
AUTHOR = "gpt-6"


class InkscapeLogo(Solo48):
    icon_id = 'inkscape-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('inkscape', 'vector', 'drawing', 'logo', 'brand', 'open-source', 'mountain')

    def build(self):
        # Peaked mountain with a mirrored, two-lobed dripping ink base.
        self.add_polyline('peak',(6,24),(24,6),(42,24))
        curves=(
            ('right-shoulder',(42,24),((42,28),(34,28),(29,30))),
            ('right-notch',(29,30),((26,33),(40,33),(36,36))),
            ('right-drip',(36,36),((38,40),(29,42),(24,42))),
            ('left-drip',(24,42),((19,42),(10,40),(12,36))),
            ('left-notch',(12,36),((8,33),(22,33),(19,30))),
            ('left-shoulder',(19,30),((14,28),(6,28),(6,24))),
        )
        for name,start,segment in curves:
            self.add_bezier(name,start,segment)
        self.add_contour('ink-base',*(name for name,_,_ in curves))
        self.relate('connect','peak','ink-base')
        # The source snow line rises to a smaller central peak.
        self.add_polyline('snow',(21,22),(24,18),(27,22))
