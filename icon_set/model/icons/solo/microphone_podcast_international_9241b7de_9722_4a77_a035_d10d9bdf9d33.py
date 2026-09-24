"""microphone podcast international: fresh spacing repair.
Plan: Lucide mic concentric support and central stand; symmetric hemisphere with one longitude.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Two meridians reduced to one; latitude simplified to hemisphere baseline; microphone rounded; base omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9241b7de-9722-4a77-a035-d10d9bdf9d33'
SOURCE_PATH='pictographic-primitives/audio/microphone podcast international_9241b7de-9722-4a77-a035-d10d9bdf9d33.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='microphone-podcast-international'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('microphone', 'podcast', 'international')

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
        self.add_arc('globe-left',(8,14),(24,4),radius_x=16,radius_y=10)
        self.add_arc('globe-right',(24,4),(40,14),radius_x=16,radius_y=10)
        self.add_contour('globe','globe-left','globe-right')
        self.add_line('meridian',(24,4),(24,14));self.relate('connect','globe','meridian')
        self.add_polyline('equator',(8,14),(24,14),(40,14))
        self.relate('connect','globe','equator');self.relate('connect','meridian','equator')
        self.path('microphone',(20,27),[('A',(28,27),4),('L',(28,29)),('A',(20,29),4),('L',(20,27))],True)
        self.add_arc('support-left',(8,23),(24,42),radius_x=16,radius_y=19,sweep=False)
        self.add_arc('support-right',(24,42),(40,23),radius_x=16,radius_y=19,sweep=False)
        self.add_contour('support','support-left','support-right')
        self.add_line('stand',(24,42),(24,44));self.relate('connect','support','stand')
