"""Revision from the inspected source: The current seated figure has a pinhead beside two panels; the original centers a clearer head and reclining occupant among floating screens.

Changes: Enlarged and aligned the seated head and adjusted the shoulder to preserve the human clearance.
Full-body or bust construction follows icon_set/references/human_ref.
"""
'Human construction repair. Set head-outline to shoulder centerline separation to exactly 8u. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '885e5bb2-b144-41f7-a38d-f0aa93842fa0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reclining-with-floating-panels/20260927T083143Z-thuan-mac-1/reference/immersive reality chair_885e5bb2-b144-41f7-a38d-f0aa93842fa0.svg'
AUTHOR = "gpt-6"
HUMAN_CONSTRUCTION = 'stick-figure'

class PersonRecliningWithFloatingPanels(Solo48):
    icon_id = 'person-reclining-with-floating-panels'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('immersive', 'person', 'chair', 'panels', 'spatial', 'virtual-reality', 'relax')

    # Second spacing pass complete.
    def build(self):
        self.add_line('panel-1', (6, 10), (18, 6))
        self.add_line('panel-2', (18, 6), (18, 19))
        self.add_line('panel-3', (18, 19), (6, 15))
        self.add_line('panel-4', (6, 15), (6, 10))
        self.add_line('small-panel-1', (6, 28), (16, 30))
        self.add_line('small-panel-2', (16, 30), (16, 42))
        self.add_line('small-panel-3', (16, 42), (6, 40))
        self.add_line('small-panel-4', (6, 40), (6, 28))
        self.add_arc('heada', (34, 10), (34, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('headb', (34, 18), (34, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('person-1', (34, 26), *(((34.0, 28.75), (31.0, 31.75), (30, 34)),))
        self.add_line('person-2', (30, 34), (24, 34))
        self.add_line('person-3', (24, 34), (24, 42))
        self.add_line('chair-1', (42, 24), (42, 42))
        self.add_line('chair-2', (42, 42), (24, 42))
        self.add_contour('panel', *('panel-1', 'panel-2', 'panel-3', 'panel-4'), closed=True)
        self.add_contour('small-panel', *('small-panel-1', 'small-panel-2', 'small-panel-3', 'small-panel-4'), closed=True)
        self.add_contour('head', *('heada', 'headb'), closed=True)
        self.add_contour('person', *('person-1', 'person-2', 'person-3'), closed=False)
        self.add_contour('chair', *('chair-1', 'chair-2'), closed=False)
        self.relate('connect', *('person', 'chair'))
        self.mark_human_figure('person-1', head='head', torso='person-1', torso_junction='start')
