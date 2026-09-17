"""Bulleted List with Circles.
Plan: Three circle bullets and three identical rows share a constant15-unit vertical step. Ink (4,4)-(44,44).
Reference construction: list.
Reduction: Use one text line per bullet; omit paired lines and the trailing short line.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ecbf3f8-017b-5c12-95dc-25c14dcbc02a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/paragraph bullets_5ecbf3f8-017b-5c12-95dc-25c14dcbc02a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bulleted-list-with-circles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('bulleted', 'list', 'with', 'circles')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,y in enumerate((9,24,39)):
            circle(f'bullet-{j}',9,y,3)
            self.add_line(f'row-{j}',(21,y),(42,y))
