"""A rounded square with a capital Y overlaps the left side of three fanned blades radiating to the right.

Symbol plan: Y beside three attached fan blades; extremes (4,8)-(44,40).
Review notes: Drops the Y tile border, keeping the three-part fan with shared upper/lower divisions. The rightward fan remains intentionally asymmetric; no useful Lucide brand match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46a7486a-bde8-4433-b06e-c89b5d9c526b'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft yammers logo_46a7486a-bde8-4433-b06e-c89b5d9c526b.svg'
AUTHOR = 'gpt-6'

class MicrosoftYammerLogo(Solo48):
    icon_id = 'microsoft-yammer-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('yammer', 'microsoft', 'social', 'office', 'logo', 'brand', 'letter-y')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        self.add_polyline('y-arms',(4,16),(12,26),(20,16))
        self.add_line('y-stem',(12,26),(12,40))
        for m in ['y-arms-1','y-arms-2']:self.relate('connect','y-stem',m)
        points=[(28,8),(36,8),(40,16),(44,24),(40,32),(36,40),(28,40),(28,30),(28,18)]
        self.add_polyline('fan',*points,closed=True)
        for name,a,b,edges in [('upper',(28,18),(40,16),['fan-8','fan-9','fan-2','fan-3']),('lower',(28,30),(40,32),['fan-7','fan-8','fan-4','fan-5'])]:
         self.add_line(name,a,b)
         for e in edges:self.relate('connect',name,e)
