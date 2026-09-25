"""nightclub: standalone SOLO48 repair.
Plan: Two music-note pairs above a club entrance.
Keyshape: HRECT_L; shared dimensions and nodes own repeated elements.
Reduction: Kept all four notes; reduced cornice to one rail and changed the crowded arched door to a shallow rectangular opening.
Lucide originals and atomic-debug construction reference: music, house.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4f2adf74-2b0c-4983-8567-ce3c6c50bff8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/nightclub_4f2adf74-2b0c-4983-8567-ce3c6c50bff8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='nightclub'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('nightclub',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # Four noteheads on a common baseline; shared pair spacing is 12.
        self.add_line('cornice',(4,28),(44,28))
        self.add_polyline('building',(8,28),(8,40),(16,40),(16,36),(32,36),(32,40),(40,40),(40,28))
        self.relate('connect','building','cornice')
        for j,x in enumerate((6,30)):
            self.circle(f'note-{j}-left',x,18,2)
            self.circle(f'note-{j}-right',x+12,18,2)
            self.add_polyline(f'beam-{j}',(x+2,18),(x+2,8),(x+14,8),(x+14,18))
            self.relate('connect',f'beam-{j}',f'note-{j}-left')
            self.relate('connect',f'beam-{j}',f'note-{j}-right')
