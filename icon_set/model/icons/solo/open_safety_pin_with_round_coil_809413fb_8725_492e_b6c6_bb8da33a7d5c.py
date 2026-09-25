"""Open Safety Pin with Round Coil.

Symbol plan: One spring loop, upright arm and open needle. The hook is a tangent semicircle; asymmetry preserves the open pin.
Lucide construction: pin; original and atomic-debug inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '809413fb-8725-492e-b6c6-bb8da33a7d5c'
SOURCE_PATH = 'pictographic-primitives/clothes/clothes design pin_809413fb-8725-492e-b6c6-bb8da33a7d5c.svg'
AUTHOR = 'gpt-6'


class OpenSafetyPinWithRoundCoil(Solo48):
    icon_id = 'open-safety-pin-with-round-coil'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('open', 'safety', 'pin', 'with', 'round', 'coil')

    def build(self):
        self.path('coil',(28,38),(40,38,6,6,True),(28,38,6,6,True),closed=True)
        self.path('clasp',(40,38),(40,16),(16,16,12,12,False),(16,20),(24,20))
        self.add_line('needle',(28,38),(8,18))
        self.relate('connect','coil','clasp')
        self.relate('connect','coil','needle')

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
