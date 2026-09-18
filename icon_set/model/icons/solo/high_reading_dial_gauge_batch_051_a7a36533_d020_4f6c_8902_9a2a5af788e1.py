"""Domed speedometer with rising needle. HRECT_M keeps a broad dial; omit fine ticks and hub. Lucide gauge original and atomic-debug informed the dome and diagonal.

Symbol plan: HRECT_M; visible bounds (2, 8, 46, 40). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7a36533-d020-4f6c-8902-9a2a5af788e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gauge high_a7a36533-d020-4f6c-8902-9a2a5af788e1.svg'
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
    icon_id = 'high-reading-dial-gauge-batch-051'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('gauge', 'dial', 'needle', 'speedometer', 'meter', 'reading', 'instrument')

    def build(self):
        _path(self,'rim',(4,30),[('A',(44,30),20),('L',(44,38)),('L',(4,38)),('L',(4,30))],True)
        self.add_line('needle',(24,29),(31,22))
