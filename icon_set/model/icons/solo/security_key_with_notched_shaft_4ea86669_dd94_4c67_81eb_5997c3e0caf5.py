"""Security key with circular left bow, smooth rounded shoulders and notched shaft. Lucide key-round informs integrated bow and shaft. Mirror bow shoulders around y24; key tooth intentionally asymmetric. One large tooth replaces small repeated teeth.
Reviewer: clean centerlines and consistent stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ea86669-dd94-4c67-81eb-5997c3e0caf5'
SOURCE_PATH = 'pictographic-primitives/other/crypto encryption key_4ea86669-dd94-4c67-81eb-5997c3e0caf5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='security-key-with-notched-shaft'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=('security', 'key', 'with', 'notched', 'shaft')

    def build(self):
        self.path('key',(30,16),[((18,10),12,6,False),((4,24),14,14,False),((18,38),14,14,False),((30,32),12,6,False),(34,32),(34,24),(40,24),(44,20),(40,16),(30,16)],True)
        self.circle('hole',16,24,3)

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

