from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd95930dd-4c35-5a2d-ad85-faa5674be25f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-steamed-dumpling/20260929T091731Z-thuan-mac/reference/chef gear dumplings_d95930dd-4c35-5a2d-ad85-faa5674be25f.svg'
AUTHOR = "gpt-6"

# Original/rejected comparison: The front dumplings became plain circles, so the cluster read as fruit or balls.
# Revision: Restore flattened dumpling bases, soft domes and short pinched folds on all three buns.
# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.
class Drawing(Solo48):
    icon_id = 'three-steamed-dumpling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('chef', 'gear', 'dumplings')

    def build(self):
        path(self,'back-dumpling',(12,23),('C',(12,14),(15,6),(24,6)),('C',(33,6),(36,14),(36,23)))
        path(self,'back-fold-left',(20,7),('C',(22,11),(19,12),(19,15)))
        path(self,'back-fold-right',(28,7),('C',(26,11),(29,12),(29,15)))
        path(self,'front-left',(24,28),('C',(18,17),(4,21),(4,34)),('C',(4,41),(8,43),(16,43)),('L',(25,42)))
        path(self,'front-right',(24,28),('C',(27,21),(42,20),(44,32)),('C',(47,43),(35,44),(28,43)),('C',(21,42),(19,35),(24,28)),closed=True)
        path(self,'left-fold-a',(11,23),('C',(13,26),(11,28),(11,29)))
        path(self,'left-fold-b',(18,23),('L',(18,28)))
        path(self,'right-fold-a',(29,24),('C',(30,27),(28,28),(28,30)))
        path(self,'right-fold-b',(37,24),('C',(36,27),(38,28),(38,30)))
        contacts(self)

# Exact drawing accepted under the user-authorized visual-exception workflow.
Drawing.exception = {'reason': 'Keep all three flattened dumpling bodies and their attached pinched folds. Small fold openings and occluded intersections retain the food identity at 48px.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'ec28599b112bc8696b2b413ae870146e56dd7500a039623be668a9e2d92787bf'}
