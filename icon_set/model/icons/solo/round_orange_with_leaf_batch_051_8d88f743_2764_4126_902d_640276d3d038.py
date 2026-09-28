"""Round orange with a pointed lens leaf. VRECT_M fits the leaf above the round fruit. Lucide citrus informed economy of citrus construction; supplied source determines whole-fruit silhouette. Omit separate stem line where the leaf attaches.

Symbol plan: VRECT_M; visible bounds (8, 2, 40, 46). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d88f743-2764-4126-902d-640276d3d038'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fruit orange_8d88f743-2764-4126-902d-640276d3d038.svg'
AUTHOR = 'gpt-6'

def _circle(icon, name, x, y, r):
    icon.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
    icon.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def _path(icon, name, start, commands, closed=False):
    members=[]; p=start
    for i,c in enumerate(commands):
        n=f'{name}-{i}'; q=c[1]
        if c[0]=='L': icon.add_line(n,p,q)
        else: icon.add_arc(n,p,q,radius_x=c[2],radius_y=c[3] if len(c)>3 else c[2],sweep=c[4] if len(c)>4 else True)
        p=q; members.append(n)
    icon.add_contour(name,*members,closed=closed)

class Batch051Icon(Solo48):
    icon_id = 'round-orange-with-leaf-batch-051'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('orange', 'fruit', 'leaf', 'stem', 'citrus', 'food', 'produce')

    def build(self):
        _path(self,'fruit',(24,16),[('A',(38,30),14),('A',(24,44),14),('A',(10,30),14),('A',(24,16),14)],True)
        # Broad lens rather than the first draft's pinched triangular opening.
        _path(self,'leaf',(24,16),[('A',(38,4),14,12),('A',(24,16),14,12)],True)
        self.relate('connect','fruit','leaf')
