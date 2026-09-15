"""Three person figures of increasing size stand in a row from left to right, each a round head above a tall rounded body, the smallest head holding a dot.

Symbol plan: Three increasing-height busts spaced16 apart. Heads radius2; shoulders radius4. Extremes (4,8)-(44,40).
Review notes: Shared human_ref/user.svg informs circular heads and shoulder arches. Retains all three people and increasing heights while removing overlap and equalizing widths; tiny head rings read as dots. Each head-to-body centerline gap is8, hence ink gap4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c427fe3-fec6-4d96-8a60-ac9c6c0e8ddb'
SOURCE_PATH = 'pictographic-primitives/logos/my space logo_8c427fe3-fec6-4d96-8a60-ac9c6c0e8ddb.svg'
AUTHOR = 'gpt-6'

class MyspaceLogo(Solo48):
    icon_id = 'myspace-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('myspace', 'social', 'people', 'group', 'logo', 'brand', 'network')

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
        for i,x in enumerate((8,24,40)):
         cy=18-4*i;body_top=cy+2+8
         ring(f'head-{i}',x,cy,2)
         self.add_line(f'left-{i}',(x-4,40),(x-4,body_top+4))
         self.add_arc(f'shoulders-{i}',(x-4,body_top+4),(x+4,body_top+4),radius_x=4)
         self.add_line(f'right-{i}',(x+4,body_top+4),(x+4,40))
         self.add_contour(f'body-{i}',f'left-{i}',f'shoulders-{i}',f'right-{i}')
