"""Two upright mechanical outlines separated by a gap. SQUARE fits the rounded bar and open hooked wall. Preserve the source ambiguity; do not invent a measuring mechanism. No useful exact Lucide match; earlier hold overridden by this batch request.

Symbol plan: SQUARE; visible bounds (4, 4, 44, 44). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49f64fa9-c95d-4a52-bec4-46556dd5120f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gap_49f64fa9-c95d-4a52-bec4-46556dd5120f.svg'
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
    icon_id = 'two-upright-shapes-with-gap-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('gap', 'bars', 'shapes', 'spacing', 'mechanical', 'outline', 'vertical')

    def build(self):
        _path(self,'bar',(10,6),[('L',(14,6)),('A',(18,10),4),('L',(18,38)),('A',(14,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,10)),('A',(10,6),4)],True)
        _path(self,'open-wall',(28,30),[('A',(32,26),4),('L',(34,26)),('L',(34,10)),('A',(38,6),4),('A',(42,10),4),('L',(42,42))])
