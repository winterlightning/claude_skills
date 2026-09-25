"""drop: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3057870d-1409-44b0-8369-04ad03f65bba'
SOURCE_PATH = 'pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Drop(Solo48):
    icon_id = 'drop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('drop', 'smileys', 'sub icon')

    def build(self):
        # Plan: VRECT_L; mirrored shoulders meet a circular bowl with vertical tangents.
        # Reference: Lucide droplet: a coherent pointed crest and round bowl.
        axis = 24
        self.add_bezier('left',(axis,4),((19,11),(8,22),(8,28)))
        self.add_arc('bowl',(8,28),(40,28),radius_x=16,sweep=False)
        self.add_bezier('right',(40,28),((40,22),(29,11),(axis,4)))
        self.add_contour('outline','left','bowl','right',closed=True)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('01d89380-da3f-4d8c-ae1a-a259c8c619ae', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/drop_01d89380-da3f-4d8c-ae1a-a259c8c619ae.svg')]
