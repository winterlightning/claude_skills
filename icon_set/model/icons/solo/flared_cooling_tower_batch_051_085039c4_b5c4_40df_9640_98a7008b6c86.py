"""Cooling tower with flared concave walls and an upper rim. VRECT_L preserves its height. Omit base curvature in favor of a stable baseline. No useful exact Lucide match.

Symbol plan: VRECT_L; visible bounds (6, 2, 42, 46). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '085039c4-b5c4-40df-9640-98a7008b6c86'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gaffer_085039c4-b5c4-40df-9640-98a7008b6c86.svg'
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
    icon_id = 'flared-cooling-tower-batch-051'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('tower', 'cooling', 'industrial', 'plant', 'structure', 'flared', 'building')

    def build(self):
        _path(self,'tower',(16,4),[('L',(32,4)),('L',(32,14)),('A',(40,44),80,80,False),('L',(8,44)),('A',(16,14),80,80,False),('L',(16,4))],True)
        self.add_line('rim',(16,14),(32,14))
        self.relate('connect','rim','tower')
