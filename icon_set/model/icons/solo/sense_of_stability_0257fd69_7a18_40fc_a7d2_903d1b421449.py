from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0257fd69-7a18-40fc-a7d2-903d1b421449'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/sense of stability_0257fd69-7a18-40fc-a7d2-903d1b421449.svg'
AUTHOR='gpt-6'
PLAN='Cylinder with outstretched human. VRECT_L extremes8,4–40,44 add feet clearance; inner wall strips and bands omitted. Shared human full_body_ref: radius3 head bottom19 to torso27 gives exact8 centerline/4 ink gap, longer torso and balanced limbs.'
class Drawing(Solo48):
    icon_id='sense-of-stability'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        self.add_arc('rim',(8,10),(40,10),radius_x=16,radius_y=6)
        self.add_line('right',(40,10),(40,38))
        self.add_arc('bottom',(40,38),(8,38),radius_x=16,radius_y=6)
        self.add_line('left',(8,38),(8,10))
        self.add_contour('enclosure','rim','right','bottom','left',closed=True)
        self.circle('head',24,16,3)
        self.add_line('torso',(24,27),(24,31))
        self.add_polyline('arms',(17,27),(24,27),(31,27));self.relate('connect','torso','arms')
        self.add_polyline('legs',(20,35),(24,31),(28,35));self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
