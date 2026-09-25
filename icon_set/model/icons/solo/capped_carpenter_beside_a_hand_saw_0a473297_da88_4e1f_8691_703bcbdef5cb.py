"""A capped carpenter beside a hand saw.
Plan: HRECT_L fits the saw alongside the circular head.
Reduction: Saw has fewer broad teeth; fine handle division and doubled cap band omitted.
Construction: Shared human user.svg for circular head; no useful exact Lucide match for the combined occupational portrait.
Layout: Saw is intentionally placed to the left of the head; no torso or detached head-body gap applies."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a473297-da88-4e1f-8691-703bcbdef5cb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/avatar carpenter_0a473297-da88-4e1f-8691-703bcbdef5cb.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'capped-carpenter-beside-a-hand-saw'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('capped', 'carpenter', 'beside', 'a', 'hand', 'saw')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        path('head',(24,18),[(24,24),((44,24),10,10,False),(44,18)])
        path('cap',(24,18),[((44,18),10,10,True),(24,18)],True)
        self.relate('connect','cap','head')
        self.add_polyline('saw',(4,40),(4,8),(14,8),(12,16),(14,24),(12,32),(14,40),(4,40),closed=True)
