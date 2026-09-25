"""A penguin standing front-on with two oval eyes, a beak, a rounded white belly outline and two flat feet splayed at the bottom.

Symbol plan: Front-facing penguin with mirrored shoulders, eyes and feet. Extremes (8,4)-(40,44).
Review notes: Eyes reduce to paired dots; belly reduces to an open oval arc and feet merge into the outer silhouette. Rounded head and mirrored anatomy retain Tux. No useful local Lucide penguin match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5024e7e4-a399-417b-921e-035df1588c8d'
SOURCE_PATH = 'pictographic-primitives/logos/linux logo_5024e7e4-a399-417b-921e-035df1588c8d.svg'
AUTHOR = 'gpt-6'

class LinuxTuxLogo(Solo48):
    icon_id = 'linux-tux-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('linux', 'tux', 'penguin', 'operating-system', 'logo', 'brand', 'open-source')

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
        self.add_arc('head',(10,17),(38,17),radius_x=14,radius_y=13)
        chain('right-side',(38,17),(36,24),(40,34),(40,40),(30,44),(28,42),(24,42))
        chain('left-side',(24,42),(20,42),(18,44),(8,40),(8,34),(12,24),(10,17))
        self.add_contour('body','head',*[f'right-side-{i}' for i in range(1,7)],*[f'left-side-{i}' for i in range(1,7)],closed=True)
        axis=24
        for side,x in [('left',axis-4),('right',axis+4)]:self.add_dot(side+'-eye',(x,14))
        self.add_polyline('beak',(22,23),(24,24),(26,23))
        self.add_arc('belly',(19,31),(29,31),radius_x=5,radius_y=2,sweep=False)
