"""Previous video control: left stop bar and left-pointing triangle. Lucide skip-back informs a single coherent triangle and straight bar. Mirror triangle vertically about y24; no omissions.
Keyshape VRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d97ce210-8c87-47ca-ad69-8c331dcbc800'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__controls-previous-video/20260924T164246Z-thuan-mac/reference/controls previous_d97ce210-8c87-47ca-ad69-8c331dcbc800.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='controls-previous-video'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('controls', 'previous', 'video')

    def build(self):
        self.add_line('bar',(8,4),(8,44))
        self.add_polyline('triangle',(40,4),(40,44),(18,24),closed=True)

    def path(self,name,start,commands,closed=False):
        members=[];here=start
        for j,(kind,end,*args) in enumerate(commands):
            eid=f'{name}-{j}'
            if kind=='L':self.add_line(eid,here,end)
            elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
