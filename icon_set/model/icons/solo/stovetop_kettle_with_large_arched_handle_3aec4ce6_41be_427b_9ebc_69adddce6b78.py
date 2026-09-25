"""Traditional Stovetop Tea Kettle.

Plan: Stovetop kettle with broad body, pointed left spout and large arch handle. Bounds (4,8)-(44,40). Lid knob removed to leave a clear handle opening.
Construction reference: Lucide coffee: vessel silhouette; no exact kettle match. Handle follows common axis above body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '3aec4ce6-41be-427b-9ebc-69adddce6b78'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/tea kettle 1_3aec4ce6-41be-427b-9ebc-69adddce6b78.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'stovetop-kettle-with-large-arched-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('traditional', 'stovetop', 'tea', 'kettle')

    def build(self):
        path(self,'body',(14,24),('L',(36,24)),('L',(44,34)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(14,40)),('A',4,4,True,(10,36)),('L',(10,32)),('L',(4,22)),('L',(8,22)),('L',(14,24)),closed=True)
        path(self,'handle',(14,24),('L',(14,19)),('A',11,11,True,(25,8)),('A',11,11,True,(36,19)),('L',(36,24)))
        contacts(self)
