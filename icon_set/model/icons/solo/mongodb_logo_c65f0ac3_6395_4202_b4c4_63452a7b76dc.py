"""A rounded shield outline holds a slender leaf with a vertical stem line running through it and past its base.

Symbol plan: Symmetric pointed leaf with central vein and extended stem; extremes (8,4)-(40,44).
Review notes: Removes the surrounding shield to preserve the identifying leaf and vein. Lucide leaf informs coherent curved lobes and stem; this leaf is deliberately upright and mirrored.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c65f0ac3-6395-4202-b4c4-63452a7b76dc'
SOURCE_PATH = 'pictographic-primitives/logos/mongodb logo_c65f0ac3-6395-4202-b4c4-63452a7b76dc.svg'
AUTHOR = 'gpt-6'

class MongodbLogo(Solo48):
    icon_id = 'mongodb-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('mongodb', 'database', 'leaf', 'shield', 'logo', 'brand', 'developer')

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
        self.add_bezier('left-upper',(24,4),((16,12),(8,18),(8,24)))
        self.add_bezier('left-lower',(8,24),((8,30),(16,36),(24,40)))
        self.add_bezier('right-lower',(24,40),((32,36),(40,30),(40,24)))
        self.add_bezier('right-upper',(40,24),((40,18),(32,12),(24,4)))
        self.add_contour('leaf','left-upper','left-lower','right-lower','right-upper',closed=True)
        self.add_line('vein',(24,16),(24,40));self.add_line('stem',(24,40),(24,44))
        self.add_contour('midrib','vein','stem')
        for a in ['vein','stem']:
         for b in ['left-lower','right-lower']:self.relate('connect',a,b)
