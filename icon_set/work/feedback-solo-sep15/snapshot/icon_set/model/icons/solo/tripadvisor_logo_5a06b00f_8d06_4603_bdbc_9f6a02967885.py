"""Paired circular owl eyes with dot pupils, a central beak and angular brow tufts. Share equal eye radii and explicit rim attachment points; remove doubled pupil rings and reduce the beak to a descending stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a06b00f-8d06-4603-bdbc-9f6a02967885'
SOURCE_PATH = 'pictographic-primitives/logos/tripadvisor logo_5a06b00f-8d06-4603-bdbc-9f6a02967885.svg'
AUTHOR = 'gpt-6'

class TripadvisorLogo(Solo48):
    icon_id = 'tripadvisor-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('tripadvisor', 'owl', 'travel', 'reviews', 'logo', 'brand', 'eyes')

    def build(self):
        # Plan: Paired circular owl eyes with dot pupils, a central beak and angular brow tufts. Share equal eye radii and explicit rim attachment points; remove doubled pupil rings and reduce the beak to a descending stroke.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        for j,x in enumerate((14,34)):
            nodes=[(x,16),(x+10,26),(x+6,34),(x,36),(x-6,34),(x-10,26)]
            for k,a in enumerate(nodes):self.add_arc(f'eye-{j}-{k}',a,nodes[(k+1)%6],radius_x=10)
            self.add_contour('eye-'+str(j),*[f'eye-{j}-{k}' for k in range(6)],closed=True)
            self.add_dot('pupil-'+str(j),(x,26))
        self.relate('connect','eye-0','eye-1')
        self.add_polyline('brow',(4,8),(14,16),(24,8),(34,16),(44,8))
        self.add_line('beak',(24,26),(24,40))
        for n in ('brow','beak'):
            for j in range(2):self.relate('connect',n,'eye-'+str(j))

