"""A running athlete holds a flaming torch upright in the forward hand on the right. The other arm swings back while the legs separate into a long stride beneath the torso.

Upright torch, pointed flame silhouette and running stride retained. Flame interior and doubled body outlines omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf69141f-78b0-4910-b341-912076827fbd'
SOURCE_PATH = 'pictographic-primitives/sports/olympics torch_bf69141f-78b0-4910-b341-912076827fbd.svg'
AUTHOR = 'gpt-6'

class TorchRelayRunner(Solo48):
    icon_id = 'torch-relay-runner'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('torch', 'relay', 'runner', 'flame', 'athletics', 'sport')

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
        self.circle('head',18,9,3)
        self.add_arc('flame-right',(36,6),(42,14),radius_x=6,radius_y=8)
        self.add_arc('flame-br',(42,14),(36,20),radius_x=6)
        self.add_arc('flame-bl',(36,20),(30,14),radius_x=6)
        self.add_arc('flame-left',(30,14),(36,6),radius_x=6,radius_y=8)
        self.add_contour('flame','flame-right','flame-br','flame-bl','flame-left',closed=True)
        self.skeleton([('torso',[(20,22),(18,32)]),('left-arm',[(20,22),(12,22),(6,28)]),('right-arm',[(20,22),(28,30),(36,30)]),('torch',[(36,20),(36,30),(36,34)]),('rear-leg',[(18,32),(10,40),(6,40)]),('front-leg',[(18,32),(24,42)])])
        for a in ['flame-br','flame-bl']:self.relate('connect','torch-0',a)
