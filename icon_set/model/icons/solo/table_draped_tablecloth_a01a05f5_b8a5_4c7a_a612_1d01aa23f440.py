'Table with Tablecloth.\nPlan: Flat cloth top, sloping sides and scalloped hem above two shared table legs. Bounds4,8..44,40.\nReference: No useful Lucide furniture-table match; source cloth silhouette and shared leg attachments.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a01a05f5-b8a5-4c7a-a612-1d01aa23f440'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tablecloth_a01a05f5-b8a5-4c7a-a612-1d01aa23f440.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'table-draped-tablecloth'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('table', 'draped', 'tablecloth')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('cloth',(8,8),[(40,8),(44,28),((36,28),4,2,True),((24,28),6,2,False),((12,28),6,2,True),((4,28),4,2,False),(8,8)],True)
        for x in (12,36):self.add_line(f'leg-{x}',(x,28),(x,40));self.relate('connect',f'leg-{x}','cloth')

# Additional original reference represented by this completed drawing.
SOURCE_REFERENCES = globals().get("SOURCE_REFERENCES", []) + [('38c2df08-0c21-4678-8b69-c177f845ce5d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tablecloth_38c2df08-0c21-4678-8b69-c177f845ce5d.svg')]
