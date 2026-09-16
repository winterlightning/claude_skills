"""Person Receiving Cheek Massage.

Symbol plan: A circular head receives a fingertip on the right cheek. One visible closed eye and a neutral mouth remain; the right eye is omitted beside the hand, along with swept hair and motion waves. The visible face uses circular arcs, and the hand retains the asymmetric massage gesture.
Lucide: hand; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c74b0042-fbea-4b7b-96ff-891487e1486b'
SOURCE_PATH = 'pictographic-primitives/beauty/facial cleansing massage_c74b0042-fbea-4b7b-96ff-891487e1486b.svg'
AUTHOR = 'gpt-6'

class PersonReceivingCheekMassage(Solo48):
    icon_id = 'person-receiving-cheek-massage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('massage', 'therapy', 'person', 'wellness', 'relaxation', 'treatment', 'body', 'spa')

    def build(self):
        self.path('face',(22,38),(6,22,16,16,True),(22,6,16,16,True),(38,22,16,16,True))
        self.path('finger',(38,22),(42,32,42,24,42,28),(42,42),(32,42),(32,34),(28,30),(28,26),(32,22,4,4,True),(38,22))
        self.relate('connect','face','finger')
        self.add_line('left-eye',(16,20),(20,20))
        self.add_line('mouth',(18,28),(20,28))

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
