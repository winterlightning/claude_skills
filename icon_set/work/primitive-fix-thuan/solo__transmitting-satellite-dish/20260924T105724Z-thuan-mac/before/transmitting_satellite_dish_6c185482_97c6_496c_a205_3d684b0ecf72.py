"""Transmitting Satellite Dish — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c185482-97c6-496c-a205-3d684b0ecf72'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/internet/antenna_6c185482-97c6-496c-a205-3d684b0ecf72.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'transmitting-satellite-dish'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'internet'
    aliases = ()
    keywords = ('transmitting', 'satellite', 'dish')

    def build(self):
        # Plan: tilted circular dish, tapered stand, feed receiver and one broad signal arc.
        # HRECT_L extremes4,8,44,40. Lucide satellite-dish supplies bowl and wave construction.
        # One of the two signal arcs is dropped to keep the receiver and stand clear.
        pts=[(8,12),(4,20),(8,28),(14,30),(20,28)]
        for i in range(4):self.add_arc(f'bowl-{i}',pts[i],pts[i+1],radius_x=10,sweep=False)
        self.add_line('rim-a',(20,28),(14,20));self.add_line('rim-b',(14,20),(8,12))
        self.add_contour('dish',*[f'bowl-{i}' for i in range(4)],'rim-a','rim-b',closed=True)
        self.add_polyline('stand',(8,28),(6,40),(22,40),(20,28))
        self.add_line('feed',(14,20),(26,20));self.circle('receiver',28,20,2)
        self.add_arc('signal',(26,8),(44,26),radius_x=18)
        self.join_shared()


    def circle(self,n,x,y,r,attachments=()):
        from math import atan2
        pts=list(dict.fromkeys([(x+r,y),(x,y+r),(x-r,y),(x,y-r)]+list(attachments)))
        pts.sort(key=lambda p:atan2(p[1]-y,p[0]-x))
        for j in range(len(pts)):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%len(pts)],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(len(pts))],closed=True)

    def box(self,n,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h//2),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+h//2),(x,y+r)]
        ids=[]
        for i,(a,z) in enumerate(zip(pts,pts[1:]+pts[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if i in (2,5,8,11):self.add_arc(name,a,z,radius_x=r)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def join_shared(self):
        from icon_set.renderers.svg import build_paths
        paths=build_paths(self.draw())
        for i,a in enumerate(paths):
            ap={(p.start.x,p.start.y) for p in a['primitives']}|{(p.end.x,p.end.y) for p in a['primitives']}
            for z in paths[i+1:]:
                zp={(p.start.x,p.start.y) for p in z['primitives']}|{(p.end.x,p.end.y) for p in z['primitives']}
                if ap & zp:self.relate('connect',a['id'],z['id'])

