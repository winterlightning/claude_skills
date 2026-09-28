'settings-on: independent smooth-curve repair.\n\nConstruction: Capsule-like rounded enclosure with equal semicircular ends; centered interior where present.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0392b574-2d42-4e72-8939-91f0c4b24d2f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__settings-on/20260927T091411Z-thuan-mac-1/reference/settings on_0392b574-2d42-4e72-8939-91f0c4b24d2f.svg'
AUTHOR = "gpt-6"


class SettingsOn(Solo48):
    icon_id = 'settings-on'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('settings', 'on', 'interface-essential')
    keyshape = Keyshape.HRECT_M

    # Revision plan: Narrow the enclosure to the HRECT_M proportions and shift the on mark toward the right end. Lucide rectangle-horizontal informs the capsule.
    # Revision plan: Narrow the enclosure to the HRECT_M proportions and shift the on mark toward the right end. Lucide rectangle-horizontal informs the capsule.
    # Revision plan: Narrow the enclosure to the HRECT_M proportions and shift the on mark toward the right end. Lucide rectangle-horizontal informs the capsule.
    # Revision plan: Narrow the enclosure to the HRECT_M proportions and shift the on mark toward the right end. Lucide rectangle-horizontal informs the capsule.
    # Revision plan: Narrow the enclosure to the HRECT_M proportions and shift the on mark toward the right end. Lucide rectangle-horizontal informs the capsule.
    def build(self):
        # The source is a long horizontal capsule with its on marker to the right.
        self.add_line('top', (18, 10), (30, 10))
        self.add_arc('right-end', (30, 10), (30, 38), radius_x=14, radius_y=14, sweep=True)
        self.add_line('bottom', (30, 38), (18, 38))
        self.add_arc('left-end', (18, 38), (18, 10), radius_x=14, radius_y=14, sweep=True)
        self.add_contour('switch-shell', 'top', 'right-end', 'bottom', 'left-end', closed=True)
        self.add_line('on-marker', (33, 19), (33, 29))
