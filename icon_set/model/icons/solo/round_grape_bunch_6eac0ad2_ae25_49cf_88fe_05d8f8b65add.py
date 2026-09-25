"""Bunch of Grapes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6eac0ad2-ae25-49cf-88fe-05d8f8b65add'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/sugar apple_6eac0ad2-ae25-49cf-88fe-05d8f8b65add.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-grape-bunch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('grape', 'fruit', 'bunch', 'berry', 'vine', 'produce', 'food', 'sub icon')

    def build(self):
        # Plan: Three large round grapes on triangular lattice, shortened detached stem. Lucide grape circular repetition; overlap removed to keep clear interiors. Symmetric envelope (8,4)-(40,44).
        for i,(x,y) in enumerate(((14,20),(34,20),(24,38))):
         self.add_arc(f't-{i}',(x-6,y),(x+6,y),radius_x=6)
         self.add_arc(f'b-{i}',(x+6,y),(x-6,y),radius_x=6)
         self.add_contour(f'grape-{i}',f't-{i}',f'b-{i}',closed=True)
        self.add_line('stem',(24,4),(24,7))


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('2fc0acbf-1d1b-470d-a272-1cf68f822b5a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/grape_2fc0acbf-1d1b-470d-a272-1cf68f822b5a.svg')]
