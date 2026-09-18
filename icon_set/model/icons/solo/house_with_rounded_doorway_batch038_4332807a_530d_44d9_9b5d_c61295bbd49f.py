"""Fresh batch-038 result for house-with-rounded-doorway.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape SQUARE: ink extremes (4,4)-(44,44).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4332807a-530d-44d9-9b5d-c61295bbd49f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/exterior_4332807a-530d-44d9-9b5d-c61295bbd49f.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'house-with-rounded-doorway-batch038'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/expressions" 
    aliases = ()
    keywords = ('house', 'with', 'rounded', 'doorway')

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
        # One open doorway contour, with a mirrored roof and rounded base.
        self.add_polyline('roof',(6,22),(24,6),(42,22))
        self.add_line('wall-r',(42,22),(42,38))
        self.add_arc('corner-r',(42,38),(38,42),radius_x=4)
        self.add_line('base-r',(38,42),(29,42))
        self.add_line('door-r',(29,42),(29,29))
        self.add_arc('door-top',(29,29),(19,29),radius_x=5,sweep=False)
        self.add_line('door-l',(19,29),(19,42))
        self.add_line('base-l',(19,42),(10,42))
        self.add_arc('corner-l',(10,42),(6,38),radius_x=4)
        self.add_line('wall-l',(6,38),(6,22))
        self.add_contour('walls','wall-r','corner-r','base-r','door-r','door-top','door-l','base-l','corner-l','wall-l')
        self.relate('connect','roof','walls')
