"""A circular progress enclosure with a continuous arc and three separated dashes.

CIRCLE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide loader-circle: long circular arc with open end; source retains dashed remainder. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class IncompleteCircularProgressIndicator(Container64):
    icon_id = 'incomplete-circular-progress-indicator'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('incomplete', 'circular', 'progress', 'indicator')

    def build(self) -> None:
        self.add_arc('solid-right', (32,2), (32,62), radius_x=30)
        self.add_arc('solid-bottom-left',(32,62),(2,32),radius_x=30)
        self.add_contour('solid','solid-right','solid-bottom-left')
        self.add_arc('dash-upper-left',(8,14),(14,8),radius_x=30)
        self.add_arc('dash-top',(22,4),(25,3),radius_x=30)
        self.add_arc('dash-left',(3,25),(4,22),radius_x=30)
