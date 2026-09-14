"""Hand Holding a Remote with Signal — authored for the current SOLO48 contract."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59459f00-ae4b-4c9c-bc12-4f62f145e1be'
SOURCE_PATH = 'pictographic-primitives/tv/modern tv remote hand_59459f00-ae4b-4c9c-bc12-4f62f145e1be.svg'
AUTHOR = 'gpt-6'

class HandHoldingRemoteWithSignal(Solo48):
    icon_id = 'hand-holding-remote-with-signal'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('remote', 'hand', 'tv', 'control', 'signal', 'wireless', 'channel', 'holding')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, x, y, right, bottom, r=3, attachments=()):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; k=f'{name}-{i}'; members.append(k)
            if i%2: self.add_arc(k,a,b,radius_x=r)
            else:
                nodes=[p for p in attachments if (a[0]==b[0]==p[0] and min(a[1],b[1])<p[1]<max(a[1],b[1])) or (a[1]==b[1]==p[1] and min(a[0],b[0])<p[0]<max(a[0],b[0]))]
                if nodes:
                    members.pop()
                    nodes.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                    chain=[a]+nodes+[b]
                    for j,(u,v) in enumerate(zip(chain,chain[1:])):
                        part=f'{k}-{j}'; members.append(part); self.add_line(part,u,v)
                else: self.add_line(k,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):

        # Upright remote; the right hand remains deliberately asymmetric.
        # Centerline extremes (8,6)-(40,42).
        self.add_arc('signal',(8,8),(28,8),radius_x=10,radius_y=4)
        self.add_line('remote-top',(11,17),(25,17))
        self.add_arc('remote-ne',(25,17),(28,20),radius_x=3)
        self.add_line('remote-right-a',(28,20),(28,23))
        self.add_line('remote-right',(28,23),(28,30))
        self.add_line('remote-bottom',(18,38),(11,38))
        self.add_arc('remote-sw',(11,38),(8,35),radius_x=3)
        self.add_line('remote-left',(8,35),(8,20))
        self.add_arc('remote-nw',(8,20),(11,17),radius_x=3)
        self.add_contour('remote-outline','remote-bottom','remote-sw','remote-left','remote-nw','remote-top','remote-ne','remote-right-a','remote-right')
        self.add_line('thumb-tip-a',(32,34),(28,30))
        self.add_line('thumb-tip',(28,30),(26,28))
        self.add_arc('thumb-round',(26,28),(20,34),radius_x=5,sweep=False)
        self.add_line('thumb-palm-1',(20,34),(24,39))
        self.add_line('thumb-palm-2',(24,39),(26,42))
        self.add_contour('grip','thumb-tip-a','thumb-tip','thumb-round','thumb-palm-1','thumb-palm-2')
        self.add_polyline('outer-hand',(28,23),(36,31),(36,38),(40,42))
        self.relate('connect','remote-outline','outer-hand')
        self.relate('connect','remote-outline','grip')
