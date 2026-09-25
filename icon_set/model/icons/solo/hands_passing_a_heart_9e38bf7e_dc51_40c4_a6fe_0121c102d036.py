"""Hands Passing a Heart.

Symbol plan: An upper hand grasps a heart by its right lobe above an open lower palm. Two matched circular lobes flow into a curved heart tip. Shared contact at (32,16) represents the actual grip; tiny cuffs and finger creases are omitted. Intentional asymmetry preserves the passing action.
Lucide: hand-heart; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e38bf7e-dc51-40c4-a6fe-0121c102d036'
SOURCE_PATH = 'pictographic-primitives/business/donation charity hand give heart_9e38bf7e-dc51-40c4-a6fe-0121c102d036.svg'
AUTHOR = 'gpt-6'

class HandsPassingAHeart(Solo48):
    icon_id = 'hands-passing-a-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('heart', 'hands', 'giving', 'care', 'love', 'donation', 'support', 'compassion')

    def build(self):
        self.path('heart',(22,16),(12,16,5,5,False),(22,26,12,20,18,24),(32,16,26,24,32,20),(22,16,5,5,False),closed=True)
        self.path('lower-hand',(6,34),(14,34),(22,34),(32,34),(40,42,8,8,True),(6,42),(6,34))
        self.path('upper-hand',(42,6),(42,10),(32,16,42,14,36,12),(38,24,34,22,36,24),(42,24))
        self.relate('connect','upper-hand','heart')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for index, step in enumerate(steps):
            member=f"{name}-{index+1}"
            if len(step)==2:
                self.add_line(member,point,step)
                point=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step
                self.add_arc(member,point,(x,y),radius_x=rx,radius_y=ry,sweep=sweep)
                point=(x,y)
            else:
                x,y,cx1,cy1,cx2,cy2=step
                self.add_bezier(member,point,((cx1,cy1),(cx2,cy2),(x,y)))
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),(x+r,y,r,r,True),(x,y+r,r,r,True),
                  (x-r,y,r,r,True),(x,y-r,r,r,True),closed=True)

    def rect(self,name,x,y,w,h,r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
