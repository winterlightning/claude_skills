'Organizational hierarchy cube.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/organizational_hierarchy_cube.py'
AUTHOR = 'gpt-6'

class OrganizationalHierarchyCube(Solo48):
    icon_id = 'organizational-hierarchy-cube'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ('hierarchy-cube', 'organization-chart', 'org-chart')
    keywords = ('hierarchy', 'organization', 'structure', 'node', 'tree', 'distribute', 'cube', 'network')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_6 = (24, 6)
        p_34_11 = (34, 11)
        p_34_21 = (34, 21)
        p_24_26 = (24, 26)
        p_14_21 = (14, 21)
        p_14_11 = (14, 11)
        p_24_16 = (24, 16)
        p_24_30 = (24, 30)
        p_6_30 = (6, 30)
        p_42_30 = (42, 30)
        p_6_42 = (6, 42)
        p_24_42 = (24, 42)
        p_42_42 = (42, 42)
        self.add_line('cube-outline-1', p_24_6, p_34_11)
        self.add_line('cube-outline-2', p_34_11, p_34_21)
        self.add_line('cube-outline-3', p_34_21, p_24_26)
        self.add_line('cube-outline-4', p_24_26, p_14_21)
        self.add_line('cube-outline-5', p_14_21, p_14_11)
        self.add_line('cube-outline-6', p_14_11, p_24_6)
        self.add_line('cube-y-left', p_14_11, p_24_16)
        self.add_line('cube-y-right', p_34_11, p_24_16)
        self.add_line('cube-y-down', p_24_16, p_24_26)
        self.add_line('parent-stem', p_24_26, p_24_30)
        self.add_line('bus-left', p_6_30, p_24_30)
        self.add_line('bus-right', p_24_30, p_42_30)
        self.add_line('child-left-stem', p_6_30, p_6_42)
        self.add_line('child-centre-stem', p_24_30, p_24_42)
        self.add_line('child-right-stem', p_42_30, p_42_42)
        self.add_contour('cube-outline', 'cube-outline-1', 'cube-outline-2', 'cube-outline-3', 'cube-outline-4', 'cube-outline-5', 'cube-outline-6', closed=True)
        self.relate('connect', 'cube-outline', 'cube-y-left')
        self.relate('connect', 'cube-outline', 'cube-y-right')
        self.relate('connect', 'cube-outline', 'cube-y-down')
        self.relate('connect', 'cube-outline', 'parent-stem')
        self.relate('connect', 'cube-y-left', 'cube-y-right')
        self.relate('connect', 'cube-y-left', 'cube-y-down')
        self.relate('connect', 'cube-y-right', 'cube-y-down')
        self.relate('connect', 'cube-y-down', 'parent-stem')
        self.relate('connect', 'parent-stem', 'bus-left')
        self.relate('connect', 'parent-stem', 'bus-right')
        self.relate('connect', 'parent-stem', 'child-centre-stem')
        self.relate('connect', 'bus-left', 'bus-right')
        self.relate('connect', 'bus-left', 'child-left-stem')
        self.relate('connect', 'bus-left', 'child-centre-stem')
        self.relate('connect', 'bus-right', 'child-centre-stem')
        self.relate('connect', 'bus-right', 'child-right-stem')
