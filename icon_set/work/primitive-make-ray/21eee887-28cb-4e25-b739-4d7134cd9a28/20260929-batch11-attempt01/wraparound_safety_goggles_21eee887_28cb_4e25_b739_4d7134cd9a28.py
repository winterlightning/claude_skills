"""Rejected lens has square corners and a sharp nose notch. Restore rounded wraparound lens and smooth nose bridge. No written reviewer feedback.
Construction: Lucide sticky-note fold junction and glasses rounded lobes where relevant.
Portraits use human_ref/user.svg circular facial construction; no body for the nightcap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='21eee887-28cb-4e25-b739-4d7134cd9a28'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__wraparound-safety-goggles/20260929T124811Z-thuan-mac/reference/safety goggles_21eee887-28cb-4e25-b739-4d7134cd9a28.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='wraparound-safety-goggles'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('safety', 'goggles')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        # Paired curved lens lobes and smooth central bridge; outer protective rim shares axis 24.
        path('rim',(14,40),[('L',(12,40)),('A',(4,32),8,8,True),('L',(4,16)),('A',(12,8),8,8,True),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,32)),('A',(36,40),8,8,True),('L',(34,40))])
        path('lens',(16,17),[('L',(32,17)),('A',(35,20),3,3,True),('L',(35,27)),('A',(31,31),4,4,True),('C',(24,26),(27,31),(28,26)),('C',(17,31),(20,26),(21,31)),('A',(13,27),4,4,True),('L',(13,20)),('A',(16,17),3,3,True)],True)
