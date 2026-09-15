"""A shield-like pentagon with a V-notched top holds a smaller matching V-notched shape inside.

Symbol plan: Outer V-notched shield and one matching interior chevron. Extremes (8,4)-(40,44).
Review notes: Retains the distinct double V at the shield top. The inner shield sides/base are removed as redundant detail so the nested mark remains open. Deliberate corners follow the brand; no useful Lucide shield match was needed beyond geometric enclosure practice.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd728de55-3b5f-477a-98eb-a64c2a66e247'
SOURCE_PATH = 'pictographic-primitives/logos/mcafee logo_d728de55-3b5f-477a-98eb-a64c2a66e247.svg'
AUTHOR = 'gpt-6'

class McafeeLogo(Solo48):
    icon_id = 'mcafee-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('mcafee', 'antivirus', 'security', 'shield', 'logo', 'brand', 'protection')

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
        axis=24
        self.add_polyline('shield',(8,4),(axis,14),(40,4),(40,34),(axis,44),(8,34),closed=True)
        self.add_polyline('inner-v',(16,20),(axis,25),(32,20))
