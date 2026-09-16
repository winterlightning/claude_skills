"""Three Vertical Audio Sliders.

Symbol plan: Three equal circular controls occupy different heights on matching vertical tracks. One repeated knob definition owns radius and axis spacing; ellipses simplify to circles.
Lucide: sliders-vertical; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1711a2d8-c668-583b-b4f8-3a05405df9f1'
SOURCE_PATH = 'pictographic-primitives/audio/equalizer stereo_1711a2d8-c668-583b-b4f8-3a05405df9f1.svg'
AUTHOR = 'gpt-6'

class ThreeVerticalAudioSliders(Solo48):
    icon_id = 'three-vertical-audio-sliders'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('equalizer', 'slider', 'audio', 'mixer', 'control', 'settings', 'level', 'sound')

    def build(self):
        for j,(x,y) in enumerate(((8,24),(24,32),(40,16))):
            n=f'slider-{j}';self.circle(n,x,y,4)
            self.add_line(n+'-upper',(x,8),(x,y-4));self.add_line(n+'-lower',(x,y+4),(x,40))
            self.relate('connect',n,n+'-upper');self.relate('connect',n,n+'-lower')

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
