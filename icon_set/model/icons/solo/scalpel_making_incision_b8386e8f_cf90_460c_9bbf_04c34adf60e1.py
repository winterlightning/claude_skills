"""Scalpel making an incision between two separated surface strokes. Lucide wrench informs rounded tool cap; blade narrows to incision point. Shared diagonal handle directions and a smooth cutting-edge curve. Omit small bevel marks.
Reviewer: clean centerlines and consistent stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8386e8f-cf90-460c-9bbf-04c34adf60e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/incision_b8386e8f-cf90-460c-9bbf-04c34adf60e1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='scalpel-making-incision'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('scalpel', 'making', 'incision')

    def build(self):
        self.path('handle',(14,32),[(24,20),(33,8),((41,14),5,5,True),(32,26)])
        self.add_bezier('edge',(32,26),((29,30),(20,32),(14,32)))
        self.contours.clear()
        self.add_contour('scalpel',*[f'handle-{j}' for j in range(4)],'edge',closed=True)
        self.add_line('joint',(24,20),(32,26));self.relate('connect','joint','scalpel')
        self.add_line('surface-left',(6,42),(12,42))
        self.add_line('surface-right',(24,42),(42,42))

    def path(self, name, start, steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            eid=f'{name}-{j}'
            if len(step)==2:
                self.add_line(eid,here,step); end=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)

