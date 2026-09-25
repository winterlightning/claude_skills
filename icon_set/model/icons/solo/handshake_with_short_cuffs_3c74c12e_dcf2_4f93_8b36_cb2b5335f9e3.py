"""Handshake with Shirt Cuffs.

Symbol plan: The second source has an independently named clasp with shorter cuffs and a raised upper hand. Broad tangent curves replace fine finger divisions; the original UUID stays separate.
Lucide: handshake; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c74c12e-dcf2-4f93-8b36-cb2b5335f9e3'
SOURCE_PATH = 'pictographic-primitives/business/deal handshake_3c74c12e-dcf2-4f93-8b36-cb2b5335f9e3.svg'
AUTHOR = 'gpt-6'


class HandshakeWithShortCuffs(Solo48):
    icon_id = 'handshake-with-short-cuffs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('handshake', 'agreement', 'partnership', 'business', 'cooperation', 'deal', 'greeting', 'hands')

    def build(self):
        self.path('left-cuff',(12,12),(4,12),(4,32),(8,32))
        self.path('right-cuff',(36,12),(44,12),(44,32),(40,32))
        self.add_line('left-upper-hand',(12,12),(24,12))
        self.path('thumb',(36,12),(28,8),(24,12),(16,20),(24,28,12,24,20,32),(32,20))
        self.path('palms',(8,32),(24,40,12,32,18,40),(40,32,30,40,36,32))
        self.relate('connect','left-upper-hand','left-cuff');self.relate('connect','left-upper-hand','thumb')
        self.relate('connect','thumb','right-cuff')
        for n in ('left','right'):self.relate('connect','palms',n+'-cuff')

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
