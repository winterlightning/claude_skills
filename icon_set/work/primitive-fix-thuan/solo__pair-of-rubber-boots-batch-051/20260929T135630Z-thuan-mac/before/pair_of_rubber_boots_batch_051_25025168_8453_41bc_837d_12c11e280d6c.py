"""Overlapping rubber boots facing right. SQUARE balances two shafts and rounded ankle turns. Rear boot is partly hidden. Omit sole, squared heel and hidden edges; no useful exact Lucide match.

Symbol plan: SQUARE; visible bounds (4, 4, 44, 44). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25025168-8453-41bc-837d-12c11e280d6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/galoshes_25025168-8453-41bc-837d-12c11e280d6c.svg'
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
    icon_id = 'pair-of-rubber-boots-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('boots', 'pair', 'rubber', 'galoshes', 'footwear', 'rain', 'shoes')

    def build(self):
        _path(self,'front',(6,16),[('L',(20,16)),('L',(20,26)),('A',(28,34),8,8,False),('L',(34,34)),('L',(34,42)),('L',(6,42)),('L',(6,16))],True)
        _path(self,'back',(16,6),[('L',(30,6)),('L',(30,16)),('A',(38,24),8,8,False),('L',(42,24)),('L',(42,32))])
