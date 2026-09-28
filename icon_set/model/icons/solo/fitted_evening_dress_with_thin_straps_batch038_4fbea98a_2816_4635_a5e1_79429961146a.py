"""Fresh batch-038 result for fitted-evening-dress-with-thin-straps.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape VRECT_L: ink extremes (6,2)-(42,46).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: shirt (outline economy only).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fbea98a-2816-4635-a5e1-79429961146a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/evening wear_4fbea98a-2816-4635-a5e1-79429961146a.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'fitted-evening-dress-with-thin-straps-batch038'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('fitted', 'evening', 'dress', 'with', 'thin', 'straps')

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
        # A wide sleeveless bodice gives the deep V real clearance from the waist.
        axis=24
        self.add_line('neck-left',(16,4),(axis,14))
        self.add_line('neck-right',(axis,14),(32,4))
        self.add_line('bust-right',(32,4),(40,12))
        self.add_arc('waist-right',(40,12),(40,28),radius_x=10,sweep=False)
        self.add_line('skirt-right',(40,28),(36,44))
        self.add_line('hem',(36,44),(12,44))
        self.add_line('skirt-left',(12,44),(8,28))
        self.add_arc('waist-left',(8,28),(8,12),radius_x=10,sweep=False)
        self.add_line('bust-left',(8,12),(16,4))
        self.add_contour('dress','neck-left','neck-right','bust-right','waist-right',
                         'skirt-right','hem','skirt-left','waist-left','bust-left',closed=True)
