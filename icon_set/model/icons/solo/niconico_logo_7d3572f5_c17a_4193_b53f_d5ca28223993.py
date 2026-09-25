"""A retro television with a V-shaped antenna on top, a rounded screen inside its frame and two short legs below.

Symbol plan: Retro TV with V antenna and two feet; extremes (6,6)-(42,42).
Review notes: Lucide tv supplies rounded body and shared V antenna construction. Drops the inner screen border to preserve room for the short feet and antenna; all structural identifying features remain.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d3572f5-c17a-4193-b53f-d5ca28223993'
SOURCE_PATH = 'pictographic-primitives/logos/niconico logo_7d3572f5-c17a-4193-b53f-d5ca28223993.svg'
AUTHOR = 'gpt-6'

class NiconicoLogo(Solo48):
    icon_id = 'niconico-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('niconico', 'video', 'television', 'tv', 'logo', 'brand', 'streaming')

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
        self.add_polyline('antenna',(14,6),(24,16),(34,6))
        self.add_line('top-left',(12,16),(24,16));self.add_line('top-right',(24,16),(36,16))
        self.add_arc('tr',(36,16),(42,22),radius_x=6)
        self.add_line('right',(42,22),(42,32));self.add_arc('br',(42,32),(36,38),radius_x=6)
        chain('bottom',(36,38),(32,38),(16,38),(12,38))
        self.add_arc('bl',(12,38),(6,32),radius_x=6);self.add_line('left',(6,32),(6,22));self.add_arc('tl',(6,22),(12,16),radius_x=6)
        self.add_contour('case','top-left','top-right','tr','right','br','bottom-1','bottom-2','bottom-3','bl','left','tl',closed=True)
        for a in ['antenna-1','antenna-2']:
         for b in ['top-left','top-right']:self.relate('connect',a,b)
        for side,x,end,edges in [('l',16,14,['bottom-2','bottom-3']),('r',32,34,['bottom-1','bottom-2'])]:
         self.add_line(side+'-foot',(x,38),(end,42))
         for e in edges:self.relate('connect',side+'-foot',e)
