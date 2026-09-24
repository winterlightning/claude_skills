"""A square speech bubble containing a user bust.
Plan: Rounded bubble with lower-left tail encloses circular head and symmetric shoulder arch; detached head/shoulder ink gap exactly four.
Construction: human_ref/user.svg: circular head and broad shoulder arch; message-square: integrated speech tail
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '262dd529-82e6-4744-ac57-ec46c428f624'
SOURCE_PATH = 'icon_set/work/todo-references/square bubble user_262dd529-82e6-4744-ac57-ec46c428f624.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-bubble-user'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'bubble', 'user')

    def build(self):
        self.add_polyline('bubble',(8,4),(40,4),(40,38),(24,38),(16,44),(16,38),(8,38),closed=True)
        self.circle('head',24,16,3)
        self.add_arc('shoulders-left',(17,29),(24,27),radius_x=7,radius_y=2)
        self.add_arc('shoulders-right',(24,27),(31,29),radius_x=7,radius_y=2)
        self.add_contour('shoulders','shoulders-left','shoulders-right')
    def box(self,name,l=6,t=6,r=42,b=42,rad=4):
        mx,my=(l+r)//2,(t+b)//2
        pts=[(mx,t),(r-rad,t),(r,t+rad),(r,my),(r,b-rad),(r-rad,b),(mx,b),(l+rad,b),(l,b-rad),(l,my),(l,t+rad),(l+rad,t)]
        for i in range(12):
            a,z=pts[i],pts[(i+1)%12]
            if i in (1,4,7,10):self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(12)),closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def arrow(self,name,start,tip,a,b):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',a,tip,b)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')
