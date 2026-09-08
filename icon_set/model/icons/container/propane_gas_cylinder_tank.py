"""A propane tank with a capped neck, rounded body and flared stabilizing foot.

Keyshape VRECT_L: (8, 0, 56, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide rectangle-horizontal informs tangent quarter-circle shoulders.
The foot distinguishes this tank from gas-cylinder-container; both neck rails and the broad base are retained.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class PropaneGasCylinderTank(Container64):
    icon_id = 'propane-gas-cylinder-tank'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('propane', 'gas', 'cylinder', 'tank')

    def build(self) -> None:
        self.add_line('tank0', (22, 18), (42, 18))
        self.add_arc('tank1', (42, 18), (50, 26), radius_x=8, radius_y=8, sweep=True)
        self.add_line('tank2', (50, 26), (50, 44))
        self.add_arc('tank3', (50, 44), (42, 52), radius_x=8, radius_y=8, sweep=True)
        self.add_line('tank4', (42, 52), (22, 52))
        self.add_arc('tank5', (22, 52), (14, 44), radius_x=8, radius_y=8, sweep=True)
        self.add_line('tank6', (14, 44), (14, 26))
        self.add_arc('tank7', (14, 26), (22, 18), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('tank', 'tank0', 'tank1', 'tank2', 'tank3', 'tank4', 'tank5', 'tank6', 'tank7', closed=True)
        self.add_line('cap', (18, 2), (46, 2))
        self.add_line('neck-left', (24, 2), (24, 18))
        self.add_line('neck-right', (40, 2), (40, 18))
        self.relate("connect", 'cap', 'neck-left')
        self.relate("connect", 'tank', 'neck-left')
        self.relate("connect", 'cap', 'neck-right')
        self.relate("connect", 'tank', 'neck-right')
        self.add_arc('foot-left', (22, 52), (10, 62), radius_x=12, radius_y=10, sweep=False)
        self.add_line('foot-bottom', (10, 62), (54, 62))
        self.add_arc('foot-right', (54, 62), (42, 52), radius_x=12, radius_y=10, sweep=False)
        self.add_contour('foot', 'foot-left', 'foot-bottom', 'foot-right', closed=False)
        self.relate("connect", 'tank', 'foot')
