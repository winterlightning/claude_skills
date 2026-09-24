"""specialty hearing: fresh spacing repair.
Plan: Lucide ear supplies continuous outer helix and lobe with smaller hooked interior. Intentional anatomy and left waveform asymmetry.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Inner ear simplified to one compact hooked fold; waveform shortened.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4c966f3f-127d-48b1-9cb4-530f9109feb3'
SOURCE_PATH='pictographic-primitives/health/specialty hearing_4c966f3f-127d-48b1-9cb4-530f9109feb3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='specialty-hearing'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('specialty', 'hearing')

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
        self.add_arc('outer-top',(18,16),(42,16),radius_x=12,radius_y=10)
        self.add_bezier('outer-side',(42,16),((42,29),(34,27),(34,34)))
        self.add_arc('lobe',(34,34),(18,34),radius_x=8)
        self.add_contour('outer','outer-top','outer-side','lobe')
        self.path('fold',(33,18),[('A',(27,18),3,False),('L',(27,20)),('A',(27,26),3)])
        self.add_polyline('sound',(6,24),(8,24),(10,28),(13,22),(16,26))
