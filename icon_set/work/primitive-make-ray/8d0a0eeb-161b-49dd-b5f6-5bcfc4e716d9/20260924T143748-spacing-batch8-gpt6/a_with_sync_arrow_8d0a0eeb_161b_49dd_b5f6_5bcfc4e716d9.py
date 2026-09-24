"""A surrounded by opposed sync arrows.
Plan: Room for the opposed orbits. The A counter and compact arrowheads remain visible in both themes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9'
SOURCE_PATH = 'pictographic-primitives/other/a with sync arrow_8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'a-with-sync-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('a with sync arrow',)

    def build(self):
        # Opposed half-ellipse arrows, rotated by 180 degrees; centered capital A.
        self.add_arc('upper-orbit',(6,19),(42,19),radius_x=18,radius_y=13)
        self.add_polyline('upper-tip',(39,19),(42,19),(42,16))
        self.relate('connect','upper-orbit','upper-tip')
        self.add_arc('lower-orbit',(42,29),(6,29),radius_x=18,radius_y=13)
        self.add_polyline('lower-tip',(9,29),(6,29),(6,32))
        self.relate('connect','lower-orbit','lower-tip')
        self.add_polyline('letter-a',(17,30),(18,28),(24,16),(30,28),(31,30))
        self.add_line('a-bar',(18,28),(30,28))
        self.relate('connect','letter-a','a-bar')

PLAN = 'A surrounded by opposed sync arrows. Room for the opposed orbits.'
OMISSIONS = 'Arrowhead wings shortened.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/refresh-cw.svg', 'icon_set/references/lucide/atomic-debug/refresh-cw.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/a_with_sync_arrow_8d0a0eeb_161b_49dd_b5f6_5bcfc4e716d9.py'
