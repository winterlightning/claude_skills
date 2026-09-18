"""Clustered berry with central drupe and short stem. VRECT_L includes the stem above four rounded outer lobes. Four shared-radius lobes replace six crowded source lobes; omit the stem fork after clearance review. No useful exact Lucide match.

Symbol plan: VRECT_L; visible bounds (6, 2, 42, 46). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac0aabf7-0c09-4997-9ab6-af64655e476d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fruit blackberry raspberry boysenberrry_ac0aabf7-0c09-4997-9ab6-af64655e476d.svg'
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
    icon_id = 'clustered-berry-with-branching-stem-batch-051'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('berry', 'raspberry', 'blackberry', 'fruit', 'lobes', 'stem', 'food')

    def build(self):
        # Four outer lobes share radius10 and Pythagorean (6,8) endpoints;
        # centers (18,22),(30,22),(18,34),(30,34). Central drupe radius4.
        _path(self,'berry',(24,14),[('A',(38,28),10),('A',(24,42),10),('A',(10,28),10),('A',(24,14),10)],True)
        _circle(self,'center',24,28,4)
        self.add_line('stem',(24,14),(24,4))
        self.relate('connect','stem','berry')
