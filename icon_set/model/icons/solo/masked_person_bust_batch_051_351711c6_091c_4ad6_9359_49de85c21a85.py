"""Portrait wearing a broad eye mask with two dot-sized eyes. VRECT_M gives the mask a clear band and a circular jaw. Shared user.svg informed circular jaw construction. Omit shoulders and neck to prioritize the identifying mask; eye slits reduced to dots.

Symbol plan: VRECT_M; visible bounds (8, 2, 40, 46). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '351711c6-091c-4ad6-9359-49de85c21a85'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fraudster_351711c6-091c-4ad6-9359-49de85c21a85.svg'
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
    icon_id = 'masked-person-bust-batch-051'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('person', 'mask', 'bust', 'eyes', 'disguise', 'portrait', 'avatar')

    def build(self):
        # An enlarged portrait gives the mask its own clear band and two visible eyes.
        _path(self,'head',(10,14),[('A',(38,14),14,10),('L',(38,30)),('A',(10,30),14),('L',(10,14))],True)
        for y in (14,30):
            self.add_line('mask-edge-'+str(y),(10,y),(38,y))
            self.relate('connect','head','mask-edge-'+str(y))
        for x in (20,28): self.add_dot('eye-'+str(x),(x,22))
