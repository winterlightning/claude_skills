"""Ear with Sound Waves.

Symbol plan: A coherent curved ear is paired with two separated sound waves. Both inner folds are omitted to preserve clear space at 48 pixels. The ear and waves deliberately have different curvature and size.
Lucide: ear; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7076c51a-8b84-5f46-8b1e-333c3a1adf18'
SOURCE_PATH = 'pictographic-primitives/audio/earpod listen_7076c51a-8b84-5f46-8b1e-333c3a1adf18.svg'
AUTHOR = 'gpt-6'

class EarWithTwoSoundWaves(Solo48):
    icon_id = 'ear-with-two-sound-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('ear', 'hearing', 'sound', 'listening', 'audio', 'wave', 'acoustic', 'anatomy')

    def build(self):
        self.path('ear',(6,22),(14,6,6,14,8,6),(24,18,14,6,24,6),(20,30,24,24,22,28),(18,36),(12,42,6,6,True),(6,36,6,6,True))
        self.add_arc('wave-inner',(32,22),(32,34),radius_x=1,radius_y=6,sweep=True)
        self.path('wave-outer',(38,12),(42,27,42,18,42,20),(38,42,42,34,42,36))

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
