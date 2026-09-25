"""Fresh batch-038 result for short-jacket-with-round-neckline.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape HRECT_L: ink extremes (2,6)-(46,42).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e8d6067-2207-46f7-b55a-8cee6a9b1108'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/epauliere_0e8d6067-2207-46f7-b55a-8cee6a9b1108.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'short-jacket-with-round-neckline-batch038'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('short', 'jacket', 'with', 'round', 'neckline')

    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def eye(name, x, y, up=False):
            self.add_arc(name, (x-2,y), (x+2,y), radius_x=2, radius_y=1, sweep=up)
        def mouth(y=32, sad=False, width=6, depth=2):
            self.add_arc('mouth',(24-width,y),(24+width,y),radius_x=width,radius_y=depth,sweep=sad)
        def drop(name,x,y):
            self.add_line(name+'-left',(x,y),(x-4,y+8))
            self.add_arc(name+'-base',(x-4,y+8),(x+4,y+8),radius_x=4,sweep=False)
            self.add_line(name+'-right',(x+4,y+8),(x,y))
            self.add_contour(name,name+'-left',name+'-base',name+'-right',closed=True)
        # Rounded shoulder shell, shared neckline/centre opening, paired sleeve seams.
        self.add_arc('neck-left',(16,8),(24,16),radius_x=8,sweep=False)
        self.add_arc('neck-right',(24,16),(32,8),radius_x=8,sweep=False)
        self.add_line('shoulder-r',(32,8),(34,8))
        self.add_arc('shoulder-curve-r',(34,8),(44,18),radius_x=10)
        self.add_line('side-r',(44,18),(44,40))
        for i,(x1,x2) in enumerate(zip((44,34,24,14),(34,24,14,4))):
            self.add_line('hem-'+str(i),(x1,40),(x2,40))
        self.add_line('side-l',(4,40),(4,18))
        self.add_arc('shoulder-curve-l',(4,18),(14,8),radius_x=10)
        self.add_line('shoulder-l',(14,8),(16,8))
        self.add_contour('jacket','neck-left','neck-right','shoulder-r','shoulder-curve-r','side-r','hem-0','hem-1','hem-2','hem-3','side-l','shoulder-curve-l','shoulder-l',closed=True)
        self.add_line('opening',(24,16),(24,40))
        self.relate('connect','opening','jacket')
        for i,x in enumerate((14,34)):
            self.add_line('sleeve-'+str(i),(x,28),(x,40))
            self.relate('connect','sleeve-'+str(i),'jacket')
