"""Dress silhouette owns mirrored sleeve and flared skirt, with circular neckline and curved hem. Lucide shirt informs integrated sleeves and neck; omit seams."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5f1f8cde-daf5-41ca-9527-37d72bc3c33c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gown_5f1f8cde-daf5-41ca-9527-37d72bc3c33c.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'short-sleeve-flared-dress-batch-057'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dress', 'clothing', 'fashion', 'sleeves', 'garment', 'wardrobe')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        axis = 24
        left = [(16, 4), (12, 4), (8, 16), (16, 20), (18, 24), (10, 40)]
        left_run = chain('left', *left)
        self.add_arc('hem', (10, 40), (38, 40), radius_x=14, radius_y=4, sweep=False)
        right_run = chain('right', *[(2 * axis - x, y) for x, y in reversed(left)])
        self.add_arc('neck', (32, 4), (16, 4), radius_x=8)
        self.add_contour('dress', *left_run, 'hem', *right_run, 'neck', closed=True)
