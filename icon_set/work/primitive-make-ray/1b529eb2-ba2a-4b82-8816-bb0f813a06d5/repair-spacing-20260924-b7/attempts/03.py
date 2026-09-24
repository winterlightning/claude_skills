"""microphone podcast international 1: fresh spacing repair.
Plan: Mirrored globe sectors and microphone support. Lucide mic construction with true bottom stand attachment.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: One meridian, hemisphere globe, compact round microphone and no horizontal base.
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
        self.add_arc('globe-left',(8,16),(24,4),radius_x=16,radius_y=12)
        self.add_arc('globe-right',(24,4),(40,16),radius_x=16,radius_y=12)
        self.add_contour('globe','globe-left','globe-right')
        self.add_line('meridian',(24,4),(24,16));self.relate('connect','globe','meridian')
        self.add_polyline('equator',(8,16),(24,16),(40,16))
        self.relate('connect','globe','equator');self.relate('connect','meridian','equator')
        self.circle('microphone',24,28,3)
        self.add_arc('support-left',(8,25),(24,40),radius_x=16,radius_y=15,sweep=False)
        self.add_arc('support-right',(24,40),(40,25),radius_x=16,radius_y=15,sweep=False)
        self.add_contour('support','support-left','support-right')
        self.add_line('stand',(24,40),(24,44));self.relate('connect','support','stand')
