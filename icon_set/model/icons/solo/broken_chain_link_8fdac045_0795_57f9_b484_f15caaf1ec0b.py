"""Broken Chain Link.
Plan: Mirrored half-capsules leave a central break; top and bottom emphasis strokes are detached. Ink (2,6)-(46,42).
Reference construction: unlink.
Reduction: Use one emphasis stroke above and below the gap instead of three.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8fdac045-0795-57f9-b484-f15caaf1ec0b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/link broken_8fdac045-0795-57f9-b484-f15caaf1ec0b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'broken-chain-link'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('broken', 'chain', 'link')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('left-top',(20,16),(12,16))
        self.add_arc('left-end',(12,16),(12,32),radius_x=8,sweep=False)
        self.add_line('left-bottom',(12,32),(20,32))
        self.add_contour('left-link','left-top','left-end','left-bottom')
        self.add_line('right-top',(28,16),(36,16))
        self.add_arc('right-end',(36,16),(36,32),radius_x=8)
        self.add_line('right-bottom',(36,32),(28,32))
        self.add_contour('right-link','right-top','right-end','right-bottom')
        self.add_line('break-top',(24,8),(24,9))
        self.add_line('break-bottom',(24,39),(24,40))
