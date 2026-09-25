"""Finger Tapping Wireless Earbud.

Symbol plan: A bent index finger approaches the earbud from above-right. One rounded earpiece and long stem retain its identity. The small vent, tap accent and minor finger folds are omitted; the hand remains deliberately asymmetric.
Lucide: pointer; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3dd80037-97ba-4429-978b-686a886746d0'
SOURCE_PATH = 'pictographic-primitives/audio/earpods double tap_3dd80037-97ba-4429-978b-686a886746d0.svg'
AUTHOR = 'gpt-6'

class FingerTappingWirelessEarbud(Solo48):
    icon_id = 'finger-tapping-wireless-earbud'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('earbud', 'wireless', 'audio', 'listening', 'headphone', 'music', 'device', 'sound')

    def build(self):
        self.path('earbud',(12,18),(20,26,8,8,True),(20,36),(16,40,4,4,True),(12,36,4,4,True),(12,30),(4,26,8,4,True),(4,22),(12,18,8,4,True),closed=True)
        self.path('finger',(44,20),(34,10),(28,8,32,8,30,8),(24,12,4,4,False),(34,26),(30,30),(40,36))

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
