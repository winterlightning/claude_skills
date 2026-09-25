"""Sea-serpent head with broad snout, raised crown and smooth wide S-neck. Exact SQUARE extremes. No useful local Lucide match. Omit eye, zigzag mouth and narrow fin divisions; keep main crest silhouette.
Reviewer: clean centerlines and consistent stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6e9efaa-5911-4b52-b4b0-7f1573743591'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/03-d6e9efaa-5911-4b52-b4b0-7f1573743591.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='sea-serpent-head'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    aliases=()
    keywords=('sea', 'serpent', 'head')

    def build(self):
        # Crest is retained as the raised crown, with minor fin divisions omitted for clearance.
        # Neck curves have matching vertical endpoint tangents and generous width.
        self.add_bezier('inner-neck',(14,42),((14,32),(28,32),(28,24)))
        self.path('head',(28,24),[((22,18),6,6,False),(18,18),(18,26),(10,26),((6,22),4,4,True),(6,14),((10,10),4,4,True),(18,10),(22,6),((42,26),20,20,True)])
        self.add_bezier('outer-neck',(42,26),((42,34),(28,34),(28,42)))
        self.contours.clear()
        self.add_contour('serpent','inner-neck',*[f'head-{j}' for j in range(10)],'outer-neck')

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

