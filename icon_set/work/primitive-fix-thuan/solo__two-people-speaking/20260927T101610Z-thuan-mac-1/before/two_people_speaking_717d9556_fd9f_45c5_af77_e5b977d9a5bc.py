"""Two People Speaking.

Symbol plan: Two equal circular heads and rounded shoulder silhouettes follow human_ref/user.svg. One curved speech mark replaces the two tightly packed source marks. Each detached head has exactly 4 units of visible clearance to its own shoulders.
Lucide construction: user; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '717d9556-fd9f-45c5-af77-e5b977d9a5bc'
SOURCE_PATH = 'pictographic-primitives/chat/conversation speak_717d9556-fd9f-45c5-af77-e5b977d9a5bc.svg'
AUTHOR = 'gpt-6'


class TwoPeopleSpeaking(Solo48):
    icon_id = 'two-people-speaking'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'chat'
    categories = ('primitives', 'chat')
    aliases = ()
    keywords = ('two', 'people', 'speaking')

    def build(self):
        # human_ref/user.svg: circular heads and smooth shoulders; gap 24-(12+4)=8 centerline / 4 ink.
        head_y,head_r,body_top=12,4,24
        for n,x in [('left',10),('right',38)]:
            self.circle(n+'-head',x,head_y,head_r)
            self.path(n+'-body',(x-6,40),(x-6,30),(x,body_top,6,6,True),(x+6,30,6,6,True),(x+6,40))
        self.add_arc('speech',(23,8),(23,16),radius_x=5,radius_y=5,sweep=True)

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            member=f"{name}-{i+1}"
            if len(step)==2:
                self.add_line(member, point, step)
                point=step
            else:
                x,y,rx,ry,sweep=step
                self.add_arc(member, point, (x,y), radius_x=rx, radius_y=ry, sweep=sweep)
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self, name, x, y, r):
        self.path(name,(x-r,y),(x+r,y,r,r,True),(x-r,y,r,r,True),closed=True)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
