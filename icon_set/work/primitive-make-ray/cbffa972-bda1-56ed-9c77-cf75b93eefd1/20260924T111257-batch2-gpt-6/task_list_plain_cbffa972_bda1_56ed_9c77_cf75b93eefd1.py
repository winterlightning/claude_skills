"""A task list has three empty square checkboxes and matching text lines.
Symbol plan: Portrait page and three repeated checkbox/text rows at pitch 11. This candidate preserves the full composition for inspection; three 8-unit square openings plus MIC gaps cannot fit within the page interior.
Keyshape visible bounds: (6, 2, 42, 46).
Construction references: Lucide clipboard-list: paired row alignment; supplied reference: three empty squares, three lines and plain rounded page..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cbffa972-bda1-56ed-9c77-cf75b93eefd1'
SOURCE_PATH = 'pictographic-primitives/work/task list plain_cbffa972-bda1-56ed-9c77-cf75b93eefd1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'task-list-plain'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('task', 'list', 'plain')
    def build(self):
        self.box('page',8,4,40,44,4)
        # Three equal square checkbox rows retain the reference arrangement.
        left,top,side,step=16,10,6,11
        for i in range(3):
            y=top+i*step
            self.add_polyline(f'checkbox-{i}',(left,y),(left+side,y),(left+side,y+side),(left,y+side),closed=True)
            self.add_line(f'text-{i}',(30,y+side//2),(32,y+side//2))

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)
