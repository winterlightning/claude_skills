"""Speaking Tube with Two Mouthpieces.

Symbol plan: Two opposed flared mouthpieces joined by one tangent S curve. A taller envelope separates the mouths from the tube; detached sound rays are omitted.
Lucide construction: paint-roller; original and atomic-debug inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f582c39-9c53-57a7-a698-2c3f1da5c23b'
SOURCE_PATH = 'pictographic-primitives/chat/conversation spy_7f582c39-9c53-57a7-a698-2c3f1da5c23b.svg'
AUTHOR = 'gpt-6'


class SpeakingTubeWithTwoMouthpieces(Solo48):
    icon_id = 'speaking-tube-with-two-mouthpieces'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'chat'
    categories = ('primitives', 'chat')
    aliases = ()
    keywords = ('speaking', 'tube', 'with', 'two', 'mouthpieces')

    def build(self):
        self.path('upper-mouth',(8,4),(20,6),(20,10),(20,14),(8,16),(8,4),closed=True)
        self.path('tube',(20,10),(33,10),(40,17,7,7,True),(33,24,7,7,True),(15,24),(8,31,7,7,False),(15,38,7,7,False),(28,38))
        self.path('lower-mouth',(40,32),(28,34),(28,38),(28,42),(40,44),(40,32),closed=True)
        self.relate('connect','tube','upper-mouth');self.relate('connect','tube','lower-mouth')

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
