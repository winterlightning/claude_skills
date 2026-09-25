"""A side-view bicycle has two round wheels, a low sloping frame, and a short horizontal saddle. The front fork rises to a bent handlebar, leaving an open step-through space above the frame.

Equal wheels and shared frame dimensions; open step-through frame retained. Hubs and pedal detail omitted for clearance.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '69a8fe45-fd1b-5232-810c-0ec15457eede'
SOURCE_PATH = 'pictographic-primitives/sports/fitness bicycle_69a8fe45-fd1b-5232-810c-0ec15457eede.svg'
AUTHOR = "gpt-6"

class StepThroughBicycle(Solo48):
    icon_id = 'step-through-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('bicycle', 'bike', 'cycling', 'frame', 'transport', 'pedal')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self,branches):
        parts=[]
        for name,points in branches:
            members=[]
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}';members.append(key)
                self.add_line(key,a,b);parts.append((key,a,b))
            if len(members)>1:self.add_contour(name,*members)
        for index,(a,p,q) in enumerate(parts):
            for b,r,s in parts[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def rounded(self,name,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%8];key=f'{name}-{index}';members.append(key)
            if index%2:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def weight(self,name,x,y,w,h,r):
        # Expose bar attachment nodes at the midpoint of each vertical wall.
        middle=y+h//2
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,middle),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,middle),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%len(pts)];key=f'{name}-{index}';members.append(key)
            if index in [1,4,6,9]:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        for name,x in [('rear',9),('front',39)]:
         self.add_arc(name+'-right',(x,30),(x,40),radius_x=5)
         self.add_arc(name+'-left',(x,40),(x,30),radius_x=5)
         self.add_contour(name,name+'-right',name+'-left',closed=True)

        branches=[('rear-strut',[(16,20),(9,30)]),('seat-post',[(16,20),(16,11)]),('saddle',[(10,11),(16,11),(20,11)]),('fork',[(31,8),(35,20),(39,30)]),('handlebar',[(31,8),(37,8)]),('low-frame',[(16,20),(24,32),(35,20)])]

        self.skeleton(branches)
        for a in ['rear-right','rear-left']:self.relate('connect','rear-strut-0',a)
        for a in ['front-right','front-left']:self.relate('connect','fork-1',a)
