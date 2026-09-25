"""Circular face with paired closed-eye strokes and angular nose. SQUARE accommodates a round human head. Omit ears and cropped neck. Shared human user.svg informed circular head construction.

Symbol plan: SQUARE; visible bounds (4, 4, 44, 44). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b362ca85-0c66-4cb9-a489-7e694adccbba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/freckle_b362ca85-0c66-4cb9-a489-7e694adccbba.svg'
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
    icon_id = 'front-facing-head-with-closed-eyes-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('face', 'head', 'ears', 'nose', 'eyes', 'portrait', 'person')

    def build(self):
        _circle(self,'face',24,24,18)
        for side in (-1,1):
            x=24+side*8
            self.add_line('eye-'+str(side),(x-1,20),(x+1,20))
        self.add_polyline('nose',(24,24),(24,31),(27,31))
