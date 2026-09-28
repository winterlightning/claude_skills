"""Fresh reconstruction of deepfake face from the supplied reference.
Construction references: Lucide brain-circuit; supplied wire-face reference. Symbol plan recorded in build().
Profile SOLO48, keyshape HRECT_L; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5e37ff04-4c02-4607-a4b2-b81aa6048524'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/deepfake face_5e37ff04-4c02-4607-a4b2-b81aa6048524.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'digital-face-with-input-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('deepfake', 'face')

    def circle(self, n, x, y, r):
        self.add_arc(n+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(n+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def box(self,n,l,t,r,b,k=4,top=(),bottom=()):
        p=[(l+k,t),*[(x,t) for x in sorted(top)],(r-k,t),(r,t+k),(r,b-k),(r-k,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,(a,z) in enumerate(zip(p,p[1:]+p[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if a[0]!=z[0] and a[1]!=z[1]:self.add_arc(name,a,z,radius_x=k)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # Restore the source's construction grid and curved smile; no invented eye dots.
        self.add_line('face-top-left',(24,8),(30,8))
        self.add_line('face-top-right',(30,8),(34,8))
        self.add_arc('face-tr',(34,8),(44,18),radius_x=10)
        self.add_line('face-right-lower',(44,18),(44,30))
        self.add_arc('face-br',(44,30),(34,40),radius_x=10)
        self.add_line('face-bottom-right',(34,40),(30,40))
        self.add_line('face-bottom-left',(30,40),(24,40))
        self.add_arc('face-bl',(24,40),(17,33),radius_x=7)
        self.add_line('face-left-lower',(17,33),(17,18))
        self.add_line('face-left-upper',(17,18),(17,15))
        self.add_arc('face-tl',(17,15),(24,8),radius_x=7)
        self.add_contour('face','face-top-left','face-top-right','face-tr','face-right-lower','face-br','face-bottom-right','face-bottom-left','face-bl','face-left-lower','face-left-upper','face-tl',closed=True)
        self.add_polyline('vertical-grid',(30,8),(30,18),(30,31),(30,40))
        self.add_polyline('horizontal-grid',(17,18),(30,18),(44,18))
        self.relate('connect','face','vertical-grid','horizontal-grid')
        self.add_arc('smile-left',(26,27),(30,31),radius_x=4,radius_y=4,sweep=False)
        self.add_arc('smile-right',(30,31),(34,27),radius_x=4,radius_y=4,sweep=False)
        self.add_contour('smile','smile-left','smile-right');self.relate('connect','smile','vertical-grid')
        for i,y in enumerate((10,24,38)):
            self.circle(f'node-{i}',6,y,2)
            end=[(24,8),(17,18),(24,40)][i]
            self.add_line(f'input-{i}',(8,y),end)
            self.relate('connect',f'input-{i}',f'node-{i}')
            self.relate('connect',f'input-{i}','face')
            if i==1:self.relate('connect',f'input-{i}','horizontal-grid')

    icon_id = 'digital-face-with-input-nodes'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('head', 'neural network', 'intelligence', 'connection', 'thinking', 'technology', 'brain', 'artificial intelligence')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
