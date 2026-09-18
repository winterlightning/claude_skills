"""Interlocking female and male symbols with cross and arrow. SQUARE fits the diagonal linked pair. Rear loop is open where hidden by the front loop; intentional asymmetry follows the source. Lucide venus-and-mars informed the stems and arrow.

Symbol plan: SQUARE; visible bounds (4, 4, 44, 44). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c536046d-ba8c-4f3d-ab8e-72b88649c323'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gender gay_c536046d-ba8c-4f3d-ab8e-72b88649c323.svg'
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
    icon_id = 'interlocking-female-and-male-symbols-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('gender', 'female', 'male', 'symbols', 'interlocking', 'circles', 'identity')

    def build(self):
        _path(self,'female',(14,18),[('A',(22,26),8),('A',(14,34),8),('A',(6,26),8),('A',(14,18),8)],True)
        _path(self,'male',(14,18),[('A',(22,10),8),('A',(30,18),8),('A',(22,26),8)])
        self.relate('connect','female','male')
        self.add_line('female-stem',(14,34),(14,42))
        self.add_line('cross',(8,42),(20,42))
        self.relate('connect','female-stem','female')
        self.relate('connect','cross','female-stem')
        self.add_line('male-stem',(30,18),(42,6))
        self.add_polyline('arrow',(32,6),(42,6),(42,16))
        self.relate('connect','male-stem','male')
        self.relate('connect','male-stem','arrow')
