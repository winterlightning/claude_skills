"""Fountain Pen Writing.
Plan: Diagonal barrel has a rounded cap and a broad nib meeting a wavy writing stroke. Ink (6,2)-(42,46).
Reference construction: pen-line; pen-tool.
Reduction: Join the nib to the barrel and omit the short nib slit. Keep the writing stroke attached to the nib tip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '15a1b25b-3e18-4376-b972-0dc3b619ed70'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pen write_15a1b25b-3e18-4376-b972-0dc3b619ed70.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'fountain-pen-writing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('fountain', 'pen', 'writing')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('barrel-left',(20,26),(30,6))
        self.add_bezier('cap-start',(30,6),((31,4),(32,4),(34,4)))
        self.add_arc('cap',(34,4),(40,10),radius_x=6)
        self.add_bezier('cap-end',(40,10),((40,12),(39,12),(38,14)))
        self.add_line('barrel-right',(38,14),(30,30))
        self.add_line('nib-right',(30,30),(18,40))
        self.add_line('nib-left',(18,40),(20,26))
        self.add_contour('pen','barrel-left','cap-start','cap','cap-end','barrel-right','nib-right','nib-left',closed=True)
        self.add_line('seam',(20,26),(30,30));self.relate('connect','seam','pen')
        self.add_bezier('writing',(8,44),((12,36),(14,44),(18,40)))
        self.relate('connect','writing','pen')
