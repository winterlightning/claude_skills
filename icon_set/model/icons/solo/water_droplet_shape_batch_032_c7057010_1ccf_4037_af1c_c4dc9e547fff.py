"""A single outlined droplet stands upright with a sharply pointed tip and a broad rounded lower bowl. Its sides curve outward smoothly, enclosing a plain empty interior."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7057010-1ccf-4037-af1c-c4dc9e547fff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/drop_c7057010-1ccf-4037-af1c-c4dc9e547fff.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'water-droplet-shape-batch-032'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('water-droplet-shape',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Mirrored teardrop sides flow into a rounded bowl; extrema (8,4)-(40,44).

        self.add_bezier('right',(24,4),((30,14),(40,22),(40,28)),((40,37),(33,44),(24,44)))
        self.add_bezier('left',(24,44),((15,44),(8,37),(8,28)),((8,22),(18,14),(24,4)))
        self.add_contour('drop','right','left',closed=True)

SOURCE_REFERENCES = [('a26c2ef3-c469-4683-87b4-6bc44054199d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/water_a26c2ef3-c469-4683-87b4-6bc44054199d.svg')]
