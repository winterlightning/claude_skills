"""Rejected peel is a cramped sliver and wink is heavy. Enlarge the folded quadrant and use a shallow wink. No written reviewer feedback.
Construction: Lucide sticky-note fold junction and glasses rounded lobes where relevant.
Portraits use human_ref/user.svg circular facial construction; no body for the nightcap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4e07c108-ee65-49d8-8b3f-7e814c8e1cc5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__winking-face-peeling-sticker/20260929T124811Z-thuan-mac/reference/retouch sticker_4e07c108-ee65-49d8-8b3f-7e814c8e1cc5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='winking-face-peeling-sticker'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('retouch', 'sticker')
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

        # Circular sticker with a large joined fold; facial marks occupy the unpeeled area.
        path('outline',(44,24),[('A',(24,4),20,20,False),('A',(4,24),20,20,False),('A',(24,44),20,20,False),('L',(44,24))],True)
        path('fold',(24,44),[('L',(24,36)),('A',(36,24),12,12,True),('L',(44,24))]);join('fold','outline')
        self.add_dot('eye',(14,18))
        path('wink',(26,17),[('A',(32,17),5,3,True)])
        path('smile',(12,28),[('A',(19,32),9,9,False)])
