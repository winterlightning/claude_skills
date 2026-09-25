"""Circular head under a heavy fringe with one central notch. SQUARE preserves the dome and circular lower face. Shared human reference informed the round jaw. Omit facial features as in the source; central notch mirrors about x24.

Symbol plan: SQUARE; visible bounds (4, 4, 44, 44). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b41f40e-b8c1-475b-aecb-1278f6553288'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fringe_6b41f40e-b8c1-475b-aecb-1278f6553288.svg'
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
    icon_id = 'head-with-heavy-fringe-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('head', 'hair', 'fringe', 'bangs', 'face', 'hairstyle', 'portrait')

    def build(self):
        _path(self,'hair',(6,24),[('A',(42,24),18),('L',(28,24)),('L',(24,16)),('L',(20,24)),('L',(6,24))],True)
        self.add_arc('jaw',(42,24),(6,24),radius_x=18)
        self.relate('connect','jaw','hair')
