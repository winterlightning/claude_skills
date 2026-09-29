from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f80a174d-7812-44f5-9ee2-c2d09024d923'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-wheel-steam-locomotive/20260929T091731Z-thuan-mac/reference/steam engine_f80a174d-7812-44f5-9ee2-c2d09024d923.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The locomotive lost its large driving wheel, cab window, boiler proportions and flared chimney.
# Revision: Restore one large driving wheel, two smaller wheels, an upright cab, horizontal boiler and flared smokestack.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'three-wheel-steam-locomotive'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('steam', 'engine')

    def build(self):
        # The cab frame is itself the window; avoid nesting a second tiny rectangle inside it.
        line(self,'cab-roof',(4,7),(21,7))
        poly(self,'cab',(6,26),(6,7),(19,7),(19,27))
        path(self,'boiler',(19,18),('L',(39,18)),('A',3,3,True,(42,21)),('L',(42,30)),('L',(23,30)))
        poly(self,'stack',(31,18),(31,12),(29,7),(39,7),(37,12),(37,18))
        ellipse(self,'driver',12,35,9)
        ellipse(self,'driver-hub',12,35,3)
        for x in (28,40):
         ellipse(self,f'wheel-{x}',x,39,3)
         line(self,f'axle-{x}',(x,30),(x,36))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve one large driver, two small wheels, the tall cab and flared chimney. Compact vehicle attachments and the taller envelope remain clear at native size.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '541e86039afb68142fbec1d8064499d0142ea41a1cc661940ea43b15f44798e9'}
