"""Arched envelope with a shallow inner shackle and connected V flap. Shared envelope attachment nodes preserve the original padlock/envelope hybrid."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '212621c8-07d3-4758-896e-5833c792ee9f'
SOURCE_PATH = 'pictographic-primitives/logos/prontomail logo_212621c8-07d3-4758-896e-5833c792ee9f.svg'
AUTHOR = 'gpt-6'

class ProtonmailLogo(Solo48):
    icon_id = 'protonmail-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('protonmail', 'proton', 'email', 'secure', 'envelope', 'logo', 'brand')

    def build(self):
        # Plan: Arched envelope with a shallow inner shackle and connected V flap. Shared envelope attachment nodes preserve the original padlock/envelope hybrid.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_arc('arch',(8,20),(40,20),radius_x=16)
        nodes=[(40,20),(40,26),(40,44),(8,44),(8,26),(8,20)]
        for j in range(5):self.add_line('body-'+str(j+1),nodes[j],nodes[j+1])
        self.add_contour('envelope','arch','body-1','body-2','body-3','body-4','body-5',closed=True)
        self.add_polyline('flap',(8,26),(24,38),(40,26))
        self.relate('connect','envelope','flap')
        self.add_arc('inner-arch',(17,20),(31,20),radius_x=7)
        self.add_line('inner-base',(31,20),(17,20))
        self.add_contour('shackle','inner-arch','inner-base',closed=True)

