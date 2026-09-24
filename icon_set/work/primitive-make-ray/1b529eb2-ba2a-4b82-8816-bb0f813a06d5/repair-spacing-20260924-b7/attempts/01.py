"""microphone podcast international 1: fresh spacing repair.
Plan: Lucide mic: round capsule, concentric U support, shared stand endpoint. Globe above preserves international broadcast arrangement.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Globe reduced to upper hemisphere and one meridian; short microphone capsule.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1b529eb2-ba2a-4b82-8816-bb0f813a06d5'
SOURCE_PATH='pictographic-primitives/audio/microphone podcast international 1_1b529eb2-ba2a-4b82-8816-bb0f813a06d5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='microphone-podcast-international-1'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('microphone', 'podcast', 'international', '1')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def build(self):
        self.add_arc('globe-left',(8,20),(24,4),radius_x=16)
        self.add_arc('globe-right',(24,4),(40,20),radius_x=16)
        self.add_contour('globe','globe-left','globe-right')
        self.add_line('meridian',(24,4),(24,16));self.relate('connect','globe','meridian')
        self.add_polyline('equator',(8,20),(16,20))
        self.relate('connect','globe','equator')
        self.circle('microphone',24,28,4)
        self.add_arc('support-left',(12,28),(24,40),radius_x=12,sweep=False)
        self.add_arc('support-right',(24,40),(36,28),radius_x=12,sweep=False)
        self.add_contour('support','support-left','support-right')
        self.add_line('stand',(24,40),(24,44));self.relate('connect','support','stand')
        self.add_polyline('base',(16,44),(24,44),(32,44));self.relate('connect','stand','base')
