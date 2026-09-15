"""A large circle holds a radiation trefoil: three wedge-shaped blades spaced evenly around a small central ring.

Symbol plan: Three radiation blades around a central radius3 ring; extremes (6,6)-(42,42).
Review notes: Lucide radiation informs three sectors and central hub. Drops the outer circle so the trefoil has room; broad blades share real hub endpoints. The two upper blades mirror about x24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fc04542-afd8-4d71-95a0-79c884808cbf'
SOURCE_PATH = 'pictographic-primitives/logos/nuke logo_3fc04542-afd8-4d71-95a0-79c884808cbf.svg'
AUTHOR = 'gpt-6'

class NukeLogo(Solo48):
    icon_id = 'nuke-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('nuke', 'foundry', 'compositing', 'radiation', 'logo', 'brand', 'vfx')

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
        points=[(19,24),(21,20),(27,20),(29,24),(27,28),(21,28)]
        for i,a in enumerate(points):self.add_arc(f'hub-{i}',a,points[(i+1)%6],radius_x=5)
        self.add_contour('hub',*[f'hub-{i}' for i in range(6)],closed=True)
        self.add_line('left-base',(19,24),(6,24));self.add_bezier('left-outer',(6,24),((6,16),(10,10),(15,6)));self.add_line('left-tip',(15,6),(21,20))
        self.add_contour('left','left-base','left-outer','left-tip')
        self.add_line('right-tip',(27,20),(33,6));self.add_bezier('right-outer',(33,6),((38,10),(42,16),(42,24)));self.add_line('right-base',(42,24),(29,24))
        self.add_contour('right','right-tip','right-outer','right-base')
        self.add_line('bottom-left',(21,28),(15,40));self.add_arc('bottom-outer',(15,40),(33,40),radius_x=9,radius_y=2,sweep=False);self.add_line('bottom-right',(33,40),(27,28))
        self.add_contour('bottom','bottom-left','bottom-outer','bottom-right')
        for a,indices in [('left-base',[0,5]),('left-tip',[0,1]),('right-tip',[1,2]),('right-base',[2,3]),('bottom-right',[3,4]),('bottom-left',[4,5])]:
         for i in indices:self.relate('connect',a,f'hub-{i}')
