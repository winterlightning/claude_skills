"""Automatic Bottle Filling Nozzle.

Symbol plan: A broad nozzle dispenses above two matching bottles. Reduce three bottles to two and the drop to one round mark; omit labels. One bottle definition preserves equal necks, shoulders and bases.
Lucide: bottle-wine; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bc8d9ffd-23d8-4477-a6d2-172cda5ebaf0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__automatic-bottle-filling-nozzle/20260926T073831Z-thuan-mac/reference/factory automated bottle fill_bc8d9ffd-23d8-4477-a6d2-172cda5ebaf0.svg'
AUTHOR = "claude-opus-5-5"

class AutomaticBottleFillingNozzle(Solo48):
    icon_id = 'automatic-bottle-filling-nozzle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        # Revision per review: three separate containers stand along the bottom - open-top jars
        # x 4..12, 20..28 and 36..44 (8 wide, 8 apart), walls from y 24 down to 36 and r4 round
        # bottoms on y 40. The filling nozzle above is a rounded hopper (8, 8)-(40, 8) with its
        # outlet (24, 14)-(24, 16) pointing into the middle jar, 8 above it. The reference's
        # falling drop is omitted: it cannot sit 8 from both the outlet and the jar.
        self.path('nozzle', (8, 8), (8, 10), (12, 14, 4, 4, False), (24, 14), (36, 14), (40, 10, 4, 4, False), (40, 8))
        self.add_line('outlet', (24, 14), (24, 16)); self.relate('connect', 'outlet', 'nozzle')
        for n, x in (('left', 4), ('middle', 20), ('right', 36)):
            self.path(n + '-container', (x, 24), (x, 36), (x + 8, 36, 4, 4, False), (x + 8, 24))

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
