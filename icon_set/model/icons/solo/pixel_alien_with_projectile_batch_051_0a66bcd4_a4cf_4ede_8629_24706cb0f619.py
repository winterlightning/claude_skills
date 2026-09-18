"""Stepped arcade alien with paired eyes and a detached projectile. HRECT_L preserves its wide silhouette. Omit lower foot notches and shorten the crown to keep eyes and projectile clear. No useful exact Lucide match.

Symbol plan: HRECT_L; visible bounds (2, 6, 46, 42). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a66bcd4-a4cf-4ede-8629-24706cb0f619'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gamasutra 2_0a66bcd4-a4cf-4ede-8629-24706cb0f619.svg'
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
    icon_id = 'pixel-alien-with-projectile-batch-051'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('alien', 'pixel', 'invader', 'game', 'projectile', 'arcade', 'space')

    def build(self):
        self.add_polyline('alien',(4,30),(4,18),(10,18),(10,8),(38,8),(38,18),(44,18),(44,30),closed=True)
        for x in (20,28): self.add_dot('eye-'+str(x),(x,20))
        self.add_dot('projectile',(24,40))
