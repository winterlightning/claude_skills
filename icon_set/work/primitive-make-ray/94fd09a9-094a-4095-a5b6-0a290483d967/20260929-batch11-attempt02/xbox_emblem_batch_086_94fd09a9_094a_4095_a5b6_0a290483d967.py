"""Rejected emblem makes four equivalent triangular sectors. Restore small top, broad bottom and taller side panels around curved X-shaped opening. No written reviewer feedback.
Construction: Lucide sticky-note fold junction and glasses rounded lobes where relevant.
Portraits use human_ref/user.svg circular facial construction; no body for the nightcap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='94fd09a9-094a-4095-a5b6-0a290483d967'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__xbox-emblem-batch-086/20260929T124811Z-thuan-mac/reference/logo xbox_94fd09a9-094a-4095-a5b6-0a290483d967.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='xbox-emblem-batch-086'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('logo', 'xbox')
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

        # A broad lower spherical panel, smaller crown, mirrored swept side panels.
        path('top',(16,6),[('A',(32,6),20,20,True),('L',(24,13)),('L',(16,6))],True)
        path('left',(7,15),[('C',(4,24),(5,17),(4,20)),('C',(6,32),(4,27),(5,30)),('C',(16,23),(9,28),(13,25)),('C',(7,15),(13,19),(10,16))],True)
        path('right',(41,15),[('C',(44,24),(43,17),(44,20)),('C',(42,32),(44,27),(43,30)),('C',(32,23),(39,28),(35,25)),('C',(41,15),(35,19),(38,16))],True)
        path('bottom',(12,40),[('C',(24,29),(15,35),(20,30)),('C',(36,40),(28,30),(33,35)),('A',(12,40),20,20,True)],True)
