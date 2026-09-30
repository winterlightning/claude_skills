"""Cropped waist with mirrored hips, waistband and high-cut briefs. VRECT_L accommodates the tall torso. Omit navel and fine garment seams. Shared full_body_ref.png informed economical anatomy; no useful exact Lucide match.

Symbol plan: VRECT_L; visible bounds (6, 2, 42, 46). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4107e406-bbc1-4ebd-9934-68f5e7cbf1f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/girdle_4107e406-bbc1-4ebd-9934-68f5e7cbf1f6.svg'
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
    icon_id = 'waist-wearing-briefs-batch-051'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('waist', 'hips', 'underwear', 'briefs', 'torso', 'body', 'clothing')

    def build(self):
        for side in (-1,1):
            x=lambda a:24+side*a
            self.add_polyline('hip-'+str(side),(x(12),4),(x(8),14),(x(12),24),(x(16),32),(x(16),44))
        self.add_line('waistband',(12,24),(36,24))
        self.add_polyline('briefs',(8,32),(24,44),(40,32))
        for side in (-1,1):
            self.relate('connect','waistband','hip-'+str(side))
            self.relate('connect','briefs','hip-'+str(side))
