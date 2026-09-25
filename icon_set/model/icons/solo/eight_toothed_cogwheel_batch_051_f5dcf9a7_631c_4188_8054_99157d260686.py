"""Eight-toothed cogwheel and circular bore. SQUARE preserves cardinal teeth; shared quarter definition produces rotational and reflection symmetry. Lucide settings informed radial repetition. Diagonal teeth were widened to maintain at least8 centerline clearance; omit fine corner rounding.

Symbol plan: SQUARE; visible bounds (4, 4, 44, 44). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5dcf9a7-631c-4188-8054-99157d260686'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gear_f5dcf9a7-631c-4188-8054-99157d260686.svg'
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
    icon_id = 'eight-toothed-cogwheel-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('gear', 'cogwheel', 'teeth', 'mechanical', 'settings', 'wheel', 'machine')

    def build(self):
        # Eight identical teeth, cardinal and diagonal, mirrored in each quadrant.
        quarter=[(20,6),(28,6),(28,12),(30,12),(34,8),(40,14),(36,18),(36,20)]
        points=[]
        for turn in range(4):
            for x,y in quarter:
                for _ in range(turn): x,y=48-y,x
                points.append((x,y))
        self.add_polyline('gear',*points,closed=True)
        _circle(self,'bore',24,24,3)
