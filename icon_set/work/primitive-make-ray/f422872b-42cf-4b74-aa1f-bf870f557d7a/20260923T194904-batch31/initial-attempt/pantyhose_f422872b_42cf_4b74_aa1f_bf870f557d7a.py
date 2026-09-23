"""Crossed stockinged legs with one bent knee and a pointed standing foot.
Symbol plan: One bent leg passes in front of the standing leg; coherent curves retain the asymmetric pose. Ink extremes (8,2)-(40,46).
Construction: No useful exact Lucide match found; supplied leg pose owns the silhouette.
Human construction: human-reference.md and human_ref/full_body_ref.png inspected for coherent limb flow. This is a cropped garment/leg subject with no head, so detached-head spacing is inapplicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f422872b-42cf-4b74-aa1f-bf870f557d7a'
SOURCE_PATH = 'icon_set/work/todo-references/pantyhose_f422872b-42cf-4b74-aa1f-bf870f557d7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pantyhose'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pantyhose',)

    def build(self):
        self.add_line('waist-1',(14, 4),(24, 4))
        self.add_line('waist-2',(24, 4),(24, 12))
        self.add_bezier('bent-outer',(24,12),((30,16),(38,16),(38,22)),((38,25),(27,31),(18,36)))
        self.add_bezier('raised-foot',(18,36),((15,38),(13,40),(12,38)),((10,38),(10,36),(10,34)),((10,31),(13,30),(13,27)))
        self.add_bezier('bent-inner',(13,27),((16,29),(23,24),(29,21)),((23,19),(12,18),(12,13)),((12,9),(14,7),(14,4)))
        self.add_contour('bent-leg','waist-1','waist-2','bent-outer','raised-foot','bent-inner',closed=True)
        self.add_bezier('standing-leg',(20,35),((18,40),(21,41),(25,42)),((27,43),(29,43),(31,43)),((27,44),(22,44),(20,44)),((16,44),(15,44),(15,40)))
        self.add_line('back-upper-leg',(14,19),(14,27))

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self, name, x, y, right, bottom, r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b: continue
            n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def parking_letter(self,name,x,top,bottom,width=10,bowl_height=14):
        # Vertical stem split at the bowl attachment; one smooth half-ellipse owns its loop.
        mid=top+bowl_height; shoulder=x+3
        self.add_line(name+'-stem-upper',(x,mid),(x,top))
        self.add_line(name+'-top',(x,top),(shoulder,top))
        self.add_arc(name+'-bowl',(shoulder,top),(shoulder,mid),radius_x=width-3,radius_y=bowl_height//2)
        self.add_line(name+'-return',(shoulder,mid),(x,mid))
        self.add_contour(name+'-loop',name+'-stem-upper',name+'-top',name+'-bowl',name+'-return',closed=True)
        self.add_line(name+'-stem-lower',(x,mid),(x,bottom))
        self.relate('connect',name+'-loop',name+'-stem-lower')

    def plus(self,x,y,r=2):
        names=[]
        for i,p in enumerate(((x-r,y),(x+r,y),(x,y-4),(x,y+4))):
            n=f'plus-{i}';self.add_line(n,p,(x,y))
            for prev in names:self.relate('connect',n,prev)
            names.append(n)

