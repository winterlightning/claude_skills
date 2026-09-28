"""Diagonal Security Key.
Plan: Circular bow and thin diagonal shaft share a rational circle attachment; two teeth repeat along the upper shaft. Ink (4,4)-(44,44).
Reference construction: key-round.
Reduction: Reduce the shaft and stepped teeth to single strokes; the circular outline provides the bow opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82ed92a8-489d-4970-b274-02f570b13f51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/login key_82ed92a8-489d-4970-b274-02f570b13f51.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-security-key'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('diagonal', 'security', 'key')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        pts=[(16,22),(22,24),(26,32),(16,42),(6,32),(16,22)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'bow-{j}',a,b,radius_x=10)
        self.add_contour('bow',*(f'bow-{j}' for j in range(5)),closed=True)
        self.add_polyline('shaft',(22,24),(31,15),(39,7),(40,6),(42,6))
        self.relate('connect','bow','shaft')
        for n,a,b in [('tooth-1',(31,15),(37,21)),('tooth-2',(39,7),(42,10))]:
         self.add_line(n,a,b);self.relate('connect',n,'shaft')
