"""Diagonal scalpel with parallel handle and curved blade. Exact extremes6,6,42,42. Lucide wrench informs rounded tool end and consistent handle width; no exact local scalpel match. Circular cap tangent to handle; blade intentionally narrows to a cutting point. No omissions.
Reviewer: clean centerlines and consistent stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '729f7ed8-419e-4844-bcf8-46e3b3ffd38b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/scalpel_729f7ed8-419e-4844-bcf8-46e3b3ffd38b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='scalpel-with-curved-cutting-edge'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('scalpel', 'with', 'curved', 'cutting', 'edge')

    def build(self):
        self.path('handle',(6,42),[(21,24),(33,8),((41,14),5,5,True),(29,30)])
        self.add_bezier('cutting-edge',(29,30),((23,38),(14,42),(6,42)))
        # Recombine the handle primitives and blade edge as one closed outline.
        self.contours.clear()
        self.add_contour('scalpel','handle-0','handle-1','handle-2','handle-3','cutting-edge',closed=True)
        self.add_line('joint',(21,24),(29,30));self.relate('connect','joint','scalpel')

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

