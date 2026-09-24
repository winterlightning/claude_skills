"""Heart tattoo on the shoulder with a diagonal tattoo tool. Shared human reference: smooth minimal shoulder and arm; no detached head. Lucide syringe informs straight needle and crossbars. Arm extends below tattoo; omit minor skin folds. Tool and heart retain intentional contact from the source.
Reviewer: clean centerlines and consistent stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='09849323-30e8-4e89-80f9-b5adff38e1bd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__shoulder-heart-tattooing/20260924T163012Z-thuan-mac/reference/tattoo arm tattoo_09849323-30e8-4e89-80f9-b5adff38e1bd.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='shoulder-heart-tattooing'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('shoulder', 'heart', 'tattooing')

    def build(self):
        self.path('heart',(21,29),[((18,26),3,3,False),((15,29),3,3,False),((18,35),6,8,False),(21,38),(24,35),((27,29),6,8,False),((24,26),3,3,False),((21,29),3,3,False)],True)
        self.add_arc('shoulder',(6,14),(18,26),radius_x=12,radius_y=12)
        self.relate('connect','shoulder','heart')
        self.add_line('arm-left',(6,28),(6,42))
        self.add_line('arm-right',(24,35),(26,42));self.relate('connect','arm-right','heart')
        self.add_polyline('needle',(36,10),(30,18),(24,26));self.relate('connect','needle','heart')
        self.add_polyline('bar-top',(30,6),(36,10),(42,14))
        self.add_polyline('bar-bottom',(26,15),(30,18),(34,21))
        self.relate('connect','needle','bar-top');self.relate('connect','needle','bar-bottom')

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

