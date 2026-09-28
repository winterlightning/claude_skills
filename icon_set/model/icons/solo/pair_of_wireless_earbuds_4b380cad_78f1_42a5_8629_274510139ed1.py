"""Pair of Wireless Earbuds.

Symbol plan: Two mirrored earbuds share one rounded earpiece and stem definition. Omit small vents; keep the outward-facing bowl and inward stem notch.
Lucide: headphones; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b380cad-78f1-42a5-8629-274510139ed1'
SOURCE_PATH = 'pictographic-primitives/audio/earpods_4b380cad-78f1-42a5-8629-274510139ed1.svg'
AUTHOR = 'gpt-6'

class PairOfWirelessEarbuds(Solo48):
    icon_id = 'pair-of-wireless-earbuds'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('earbud', 'wireless', 'audio', 'listening', 'headphone', 'music', 'device', 'sound')

    def build(self):
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (48-x if mirror else x,y)
            self.path(n+'-bud',p(12,8),(*p(20,16),8,8,not mirror),p(20,36),(*p(16,40),4,4,not mirror),(*p(12,36),4,4,not mirror),p(12,24),(*p(4,20),*p(8,24),*p(4,24)),p(4,16),(*p(12,8),8,8,not mirror),closed=True)

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
