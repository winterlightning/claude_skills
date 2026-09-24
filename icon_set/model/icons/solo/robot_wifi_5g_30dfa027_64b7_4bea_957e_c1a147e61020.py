"""An articulated robot arm receiving a wireless signal.

Plan: Two circular pivots joined by parallel arm edges; base and gripper retain direction; two nested wireless arcs.
Construction: bot: circular joints and minimal machine detail
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30dfa027-64b7-4bea-957e-c1a147e61020'
SOURCE_PATH = 'icon_set/work/todo-references/robot wifi 5g_30dfa027-64b7-4bea-957e-c1a147e61020.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'robot-wifi-5g'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('robot', 'wifi', '5g')

    def build(self):
        self.add_arc('wifi-outer',(6,10),(22,10),radius_x=8,radius_y=4)
        self.add_arc('wifi-inner',(10,18),(18,18),radius_x=4,radius_y=3)
        self.circle('base-joint',14,32,6)
        # Four quarters expose real attachment nodes on the upper pivot.
        pts=[(29,18),(34,13),(39,18),(34,23)]
        for i in range(4):self.add_arc(f'upper-{i}',pts[i],pts[(i+1)%4],radius_x=5)
        self.add_contour('upper-joint',*(f'upper-{i}' for i in range(4)),closed=True)
        self.add_line('arm-top',(14,26),(29,18))
        self.add_line('arm-bottom',(20,32),(34,23))
        self.add_line('base-left',(8,32),(12,42))
        self.add_line('base-right',(20,32),(24,42))
        self.add_polyline('gripper',(39,18),(42,24),(42,30))
        for a,bs in [('arm-top',['base-joint-top','upper-0','upper-3']),('arm-bottom',['base-joint-top','base-joint-bottom','upper-2','upper-3']),('base-left',['base-joint-top','base-joint-bottom']),('base-right',['base-joint-top','base-joint-bottom']),('gripper-1',['upper-1','upper-2'])]:
            for b in bs:self.relate('connect',a,b)
        self.relate('connect','base-right','arm-bottom')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, l, t, r, b, rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i in range(8):
            a,z=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def arrow(self, name, start, tip, wing1, wing2):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',wing1,tip,wing2)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')

    def heart(self, name, x, top, half, bottom):
        # Mirrored lobes share dimensions and meet the pointed lower silhouette.
        self.add_bezier(name+'-left',(x,top+2),((x-half,top-5),(x-half-3,top+4),(x-half,top+7)),((x-half+2,top+10),(x, bottom),(x,bottom)))
        self.add_bezier(name+'-right',(x,bottom),((x,bottom),(x+half-2,top+10),(x+half,top+7)),((x+half+3,top+4),(x+half,top-5),(x,top+2)))
        self.add_contour(name,name+'-left',name+'-right',closed=True)
