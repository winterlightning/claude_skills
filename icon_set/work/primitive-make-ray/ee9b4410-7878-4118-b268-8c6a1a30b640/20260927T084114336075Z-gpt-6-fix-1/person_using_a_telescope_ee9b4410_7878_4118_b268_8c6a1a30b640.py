"""Revision from the inspected source: The rejected observer floated far from the eyepiece; the original leans the face toward the telescope.

Changes: Moved the head toward the eyepiece and aligned it more closely with the bending observer.
Full-body or bust construction follows icon_set/references/human_ref.
"""
"""Person Using a Telescope. Observer leans left toward a horizontal telescope on a tripod; omit lens divisions and the third leg for spacing.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide telescope: a coherent barrel and widely splayed support legs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ee9b4410-7878-4118-b268-8c6a1a30b640'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-using-a-telescope/20260927T083143Z-thuan-mac-1/reference/landmarks telescope person_ee9b4410-7878-4118-b268-8c6a1a30b640.svg'
AUTHOR = "gpt-6"


class PersonUsingATelescope(Solo48):
    icon_id = 'person-using-a-telescope'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('person', 'using', 'a', 'telescope')

    def build(self) -> None:
        self.add_line('barrel-1', (4, 8), (22, 10))
        self.add_line('barrel-2', (22, 10), (22, 18))
        self.add_line('barrel-3', (22, 18), (14, 20))
        self.add_line('barrel-4', (14, 20), (4, 20))
        self.add_line('barrel-5', (4, 20), (4, 8))
        self.add_contour('barrel', 'barrel-1', 'barrel-2', 'barrel-3', 'barrel-4', 'barrel-5', closed=True)
        self.add_line('tripod-1', (6, 40), (14, 25))
        self.add_line('tripod-2', (14, 25), (22, 40))
        self.add_contour('tripod', 'tripod-1', 'tripod-2', closed=False)
        self.add_line('support', (14, 25), (14, 20))
        self.relate("connect", 'tripod', 'support')
        self.relate("connect", 'barrel', 'support')
        self.add_arc('head-top', (30, 11), (36, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (36, 11), (30, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('observer-1', (44, 40), (44, 30))
        self.add_line('observer-2', (44, 30), (35, 23))
        self.add_line('observer-3', (35, 23), (27, 27))
        self.add_line('observer-4', (27, 27), (22, 23))
        self.add_contour('observer', 'observer-1', 'observer-2', 'observer-3', 'observer-4', closed=False)
        self.add_line('forearm', (22, 23), (14, 20))
        self.relate("connect", 'observer', 'forearm')
        self.relate("connect", 'barrel', 'forearm')
        self.relate("connect", 'support', 'forearm')
