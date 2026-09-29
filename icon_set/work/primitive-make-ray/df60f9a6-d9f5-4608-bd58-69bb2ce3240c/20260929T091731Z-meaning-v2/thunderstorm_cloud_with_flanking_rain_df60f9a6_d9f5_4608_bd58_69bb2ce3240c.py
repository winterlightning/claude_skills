from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'df60f9a6-d9f5-4608-bd58-69bb2ce3240c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thunderstorm-cloud-with-flanking-rain/20260929T091731Z-thuan-mac/reference/weather cloud thunder rain_df60f9a6-d9f5-4608-bd58-69bb2ce3240c.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The shallow cloud and attached bolt read as a mushroom-shaped electric symbol; distinct cloud lobes and detached weather marks were lost.
# Revision: Restore an asymmetric multi-lobed cloud with a separate zigzag lightning bolt and rain strokes on both sides.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'thunderstorm-cloud-with-flanking-rain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('weather', 'cloud', 'thunder', 'rain')

    def build(self):
        path(self,'cloud',(12,25),('C',(1,25),(1,13),(12,13)),('C',(12,2),(27,2),(31,10)),('C',(37,8),(41,12),(40,17)),('C',(48,20),(44,25),(37,25)),('L',(12,25)),closed=True)
        poly(self,'lightning',(27,30),(20,38),(28,38),(22,46))
        line(self,'rain-left',(12,33),(7,41))
        line(self,'rain-right',(41,33),(36,41))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve the multi-lobed cloud, detached lightning bolt and both flanking rain strokes. Compact cloud/bolt clearance and the taller envelope remain legible.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'df75ea98cac81aff4c323ab11442eebc932dfba03a47e3e2ef4cac0eb0424b5a'}
