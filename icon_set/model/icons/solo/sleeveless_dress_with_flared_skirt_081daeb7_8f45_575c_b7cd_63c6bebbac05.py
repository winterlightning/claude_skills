"""Sleeveless Dress with Flared Skirt.

Symbol plan: A fitted bodice opens into a flared skirt. Mirrored armholes and waist curves meet a shallow rounded hem. Straps merge into the bodice edges; garment seams are omitted.
Lucide: shirt; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '081daeb7-8f45-575c-b7cd-63c6bebbac05'
SOURCE_PATH = 'pictographic-primitives/clothes/dress_081daeb7-8f45-575c-b7cd-63c6bebbac05.svg'
AUTHOR = 'gpt-6'

class SleevelessDressWithFlaredSkirt(Solo48):
    icon_id = 'sleeveless-dress-with-flared-skirt'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('dress', 'skirt', 'clothing', 'garment', 'fashion', 'apparel', 'hem', 'waist')

    def build(self):
        self.path('dress',(14,4),(24,12,18,10,21,12),(34,4,27,12,30,10),(34,14),(30,22,34,18,30,18),(40,40),(24,44,36,44,30,44),(8,40,18,44,12,44),(18,22),(14,14,18,18,14,18),(14,4),closed=True)

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
