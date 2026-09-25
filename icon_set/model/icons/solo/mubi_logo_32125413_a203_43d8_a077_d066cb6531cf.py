"""Two identical person silhouettes stand side by side, each with a round head over rounded shoulders, the right figure overlapping the left.

Symbol plan: Two equal busts with head radius4 and shoulder radius8, centers12 and36; extremes (4,8)-(44,40).
Review notes: Shared human_ref/user.svg informs circular heads, broad shoulders and open bottoms. Removes overlap and bottom closures. Both heads end at16 and shoulders begin24, giving exactly4 visible units of detached head/body clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32125413-a203-43d8-a077-d066cb6531cf'
SOURCE_PATH = 'pictographic-primitives/logos/mubi logo_32125413-a203-43d8-a077-d066cb6531cf.svg'
AUTHOR = 'gpt-6'

class MubiLogo(Solo48):
    icon_id = 'mubi-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('mubi', 'film', 'people', 'users', 'logo', 'brand', 'streaming')

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
        for i,x in enumerate((12,36)):
         ring(f'head-{i}',x,12,4)
         self.add_line(f'left-{i}',(x-8,40),(x-8,32))
         self.add_arc(f'shoulders-{i}',(x-8,32),(x+8,32),radius_x=8)
         self.add_line(f'right-{i}',(x+8,32),(x+8,40))
         self.add_contour(f'body-{i}',f'left-{i}',f'shoulders-{i}',f'right-{i}')
