"""Hand Inserting Coin Into Slot.
Symbol plan: Hand pinches a round coin beside a vertical machine slot. HRECT_L (4,8)-(44,40) gives the gesture horizontal room. human_ref/full_body_ref.png informs simple rounded human action strokes. No useful exact Lucide match. Circular coin has real shared endpoints at top and bottom where finger and thumb touch; keep machine edge and slot, omit cuff and secondary finger creases. Rightward hand and wrist retain intentional asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '599426d3-551d-5760-9320-e6e51fd9160d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/casino pull machine slot_599426d3-551d-5760-9320-e6e51fd9160d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-pinching-coin-beside-vertical-machine-slot'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('hand', 'inserting', 'coin', 'into', 'slot')

    def build(self):
        self.add_polyline('machine',(4,8),(4,26),(4,38),(4,40))
        self.add_polyline('slot',(4,26),(12,26),(12,38),(4,38));self.relate('connect','slot','machine')
        self.add_arc('coin-left',(26,14),(26,26),radius_x=6,sweep=False)
        self.add_arc('coin-right',(26,26),(26,14),radius_x=6,sweep=False)
        self.add_contour('coin','coin-left','coin-right',closed=True)
        self.add_bezier('finger',(26,14),((26,8),(36,8),(40,14)),((42,17),(44,20),(44,24)))
        self.relate('connect','finger','coin')
        self.add_line('thumb-tip',(26,26),(26,30))
        self.add_arc('thumb-bend',(26,30),(30,34),radius_x=4,sweep=False)
        self.add_bezier('thumb',(30,34),((36,34),(38,35),(44,40)))
        self.add_contour('hand-lower','thumb-tip','thumb-bend','thumb');self.relate('connect','hand-lower','coin')

    def rounded(self, name, l, t, r, b, radius, nodes=()):
        # One radius owns all tangent corners; split straight walls at real joins.
        pts=[(l+radius,t),(r-radius,t),(r,t+radius),(r,b-radius),
             (r-radius,b),(l+radius,b),(l,b-radius),(l,t+radius)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; part=f"{name}-{i}"
            if i%2:
                self.add_arc(part,a,z,radius_x=radius)
                members.append(part)
            else:
                on=[p for p in nodes if p!=a and p!=z and
                    (z[0]-a[0])*(p[1]-a[1])==(z[1]-a[1])*(p[0]-a[0]) and
                    min(a[0],z[0])<=p[0]<=max(a[0],z[0]) and min(a[1],z[1])<=p[1]<=max(a[1],z[1])]
                on.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                path=[a,*on,z]
                for j,(v,w) in enumerate(zip(path,path[1:])):
                    if v==w: continue
                    member=f"{part}-{j}";self.add_line(member,v,w);members.append(member)
        self.add_contour(name,*members,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
