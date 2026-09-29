from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '11de53db-91e8-4ba6-95b4-7e2d64d91005'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thunderstorm-cloud/20260929T091731Z-thuan-mac/reference/weather cloud rain thunder_11de53db-91e8-4ba6-95b4-7e2d64d91005.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The shallow cloud and attached bolt read as a mushroom-shaped electric symbol; distinct cloud lobes and detached weather marks were lost.
# Revision: Restore an asymmetric multi-lobed cloud with a separate zigzag lightning bolt and one rain stroke.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'thunderstorm-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('weather', 'cloud', 'rain', 'thunder')

    def build(self):
        path(self,'cloud',(12,25),('C',(1,25),(1,13),(12,13)),('C',(12,2),(27,2),(31,10)),('C',(37,8),(41,12),(40,17)),('C',(48,20),(44,25),(37,25)),('L',(12,25)),closed=True)
        poly(self,'lightning',(27,30),(20,38),(28,38),(22,46))
        line(self,'rain-left',(12,33),(7,41))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Preserve the multi-lobed cloud with a detached lightning bolt and single rain stroke. Compact cloud/bolt clearance and the taller envelope remain legible.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'd0019828178e9ad2efe9f59cb20aa803d312cbf97ea8bf9eb31d6a5e3747ee54'}
