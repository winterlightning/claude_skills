"""The cursive wordmark meetup in heavy connected script, the letters crowded into one wide band. The reference is dense and hard to read.

Symbol plan: Connected cursive meetup wordmark with repeated e loops and a descending p. Extremes (4,8)-(44,40).
Review notes: Retains the full six-letter script, repeated e loops, ascender and descender. This dense wordmark requires manual review if spacing cannot be met; no substitute abbreviation is invented. No useful Lucide wordmark match was found.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88b2352a-94a5-4240-946d-5f917d560ed5'
SOURCE_PATH = 'pictographic-primitives/logos/meetup logo_88b2352a-94a5-4240-946d-5f917d560ed5.svg'
AUTHOR = 'gpt-6'

class MeetupWordmark(Solo48):
    icon_id = 'meetup-wordmark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('meetup', 'events', 'wordmark', 'script', 'logo', 'brand', 'community')

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
        # Preserve all six letters in the candidate rather than substituting another brand mark.
        self.add_polyline('m-left',(4,30),(7,18))
        self.add_arc('m-a',(7,18),(13,18),radius_x=3)
        self.add_line('m-mid',(13,18),(10,30))
        self.add_arc('m-b',(13,18),(19,18),radius_x=3)
        self.add_polyline('m-right',(19,18),(16,30),(20,30))
        for a,b in [('m-left-1','m-a'),('m-a','m-mid'),('m-a','m-b'),('m-b','m-mid'),('m-b','m-right-1')]:self.relate('connect',a,b)
        for i,x in enumerate((22,29)):
            self.add_arc(f'e-loop-{i}',(x-2,26),(x+2,26),radius_x=2,radius_y=5)
            self.add_polyline(f'e-base-{i}',(x+2,26),(x-2,30),(x+3,30))
            self.relate('connect',f'e-loop-{i}',f'e-base-{i}-1')
        self.add_line('t-stem',(33,8),(30,30))
        self.add_line('t-bar',(28,16),(37,16))
        self.add_arc('u',(35,24),(41,24),radius_x=3,radius_y=6,sweep=False)
        self.add_line('p-stem',(44,20),(40,40))
        self.add_arc('p-loop',(44,20),(44,30),radius_x=4,radius_y=5,sweep=False)
        self.relate('connect','p-stem','p-loop')
