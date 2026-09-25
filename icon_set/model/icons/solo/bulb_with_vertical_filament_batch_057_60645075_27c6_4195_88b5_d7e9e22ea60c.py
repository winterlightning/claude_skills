"""Symmetric circular crown narrows to flat base; isolated upright filament. Lucide lightbulb informs circular top and minimal lower structure. No extra screw ridges."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '60645075-27c6-4195-88b5-d7e9e22ea60c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/glow plug warning_60645075-27c6-4195-88b5-d7e9e22ea60c.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'bulb-with-vertical-filament-batch-057'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bulb', 'light', 'filament', 'lamp', 'illumination', 'electric')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        self.add_arc('crown', (8, 20), (40, 20), radius_x=16)
        self.add_arc('lower-right', (40, 20), (36, 32), radius_x=20)
        base_run = chain('base', (36, 32), (32, 44), (16, 44), (12, 32))
        self.add_arc('lower-left', (12, 32), (8, 20), radius_x=20)
        self.add_contour('bulb', 'crown', 'lower-right', *base_run, 'lower-left', closed=True)
        self.add_line('filament', (24, 17), (24, 28))
