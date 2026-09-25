"""A stylised person: a large ring for the head above two arms that curve inward like a chevron, crossing into two legs that splay out below.

Symbol plan: Ring head over crossed arms and legs, symmetric about x24; extremes (8,4)-(40,44).
Review notes: Shared full_body_ref.png informs the round head and simple round-ended limbs. Replaces outlined limbs with coherent strokes. Head radius9 ends at22; mirrored shoulder curves meet at (24,30), giving exactly8 centerline and4 visible units to the detached head. The curve pair remains outside that exact clearance circle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e22a6735-222b-47fb-a75d-a28dab99036a'
SOURCE_PATH = 'pictographic-primitives/logos/odnoklassniki logo_e22a6735-222b-47fb-a75d-a28dab99036a.svg'
AUTHOR = 'gpt-6'

class OdnoklassnikiLogo(Solo48):
    icon_id = 'odnoklassniki-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('odnoklassniki', 'ok', 'social', 'person', 'logo', 'brand', 'russian')

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
        ring('head',24,13,9)
        self.add_bezier('arm-left',(8,26),((12,28),(16,30),(20,30)))
        self.add_line('middle-left',(20,30),(24,30));self.add_line('middle-right',(24,30),(28,30))
        self.add_bezier('arm-right',(28,30),((32,30),(36,28),(40,26)))
        self.add_contour('arm-middle','middle-left','middle-right')
        self.relate('connect','arm-left','middle-left');self.relate('connect','middle-right','arm-right')
        self.add_line('leg-left',(24,30),(16,44));self.add_line('leg-right',(24,30),(32,44))
        for a,bs in [('leg-left',['middle-left','middle-right','leg-right']),('leg-right',['middle-left','middle-right'])]:
         for b in bs:self.relate('connect',a,b)
