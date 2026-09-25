"""Fresh batch-038 result for curving-bank-above-water-waves.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape HRECT_L: ink extremes (2,6)-(46,42).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: none (no useful exact landscape match).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1dae8789-528e-488c-917c-ccf5c29fd630'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/estuary_1dae8789-528e-488c-917c-ccf5c29fd630.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'curving-bank-above-water-waves-batch038'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('curving', 'bank', 'above', 'water', 'waves')

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
        # The bank flows tangentially into the first wave; the sea spans below.
        self.add_line('ledge',(44,8),(32,8))
        self.add_arc('bank-upper',(32,8),(24,16),radius_x=8,sweep=False)
        self.add_line('bank-lower',(24,16),(24,24))
        for row,y in enumerate((24,38)):
            parts=[]
            for i in range(2 if row == 0 else 0,4):
                n=f'water-{row}-{i}'
                self.add_arc(n,(4+i*10,y),(14+i*10,y),radius_x=5,radius_y=2,sweep=bool(i%2))
                parts.append(n)
            if row == 0:
                self.add_contour('bank-water','ledge','bank-upper','bank-lower',*parts)
            else:
                self.add_contour('sea',*parts)
