"""Four parallel diagonal streaks fall from upper left to lower right, the longest through the centre and shorter streaks on each side, like a meteor trail.

Symbol plan: Five parallel diagonal streaks derived from common twelve-unit offsets. Extremes (6,6)-(42,42).
Review notes: The actual source render contains five streaks although the brief says four. All five are retained, with centerline separation 12/sqrt(2), above eight. No useful local Lucide brand match; the directional asymmetry is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f97436a9-8b66-4162-a32b-1ab652b6297e'
SOURCE_PATH = 'pictographic-primitives/logos/meteor logo_f97436a9-8b66-4162-a32b-1ab652b6297e.svg'
AUTHOR = 'gpt-6'

class MeteorLogo(Solo48):
    icon_id = 'meteor-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('meteor', 'javascript', 'framework', 'streaks', 'logo', 'brand', 'developer')

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
        self.add_line('central',(6,6),(42,42))
        for i,offset in enumerate((12,24)):
            self.add_line(f'upper-{i}',(6+offset,6),(42,42-offset))
            self.add_line(f'lower-{i}',(6,6+offset),(42-offset,42))
