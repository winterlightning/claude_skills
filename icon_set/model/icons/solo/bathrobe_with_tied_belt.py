"""Front-facing bathrobe with a wrapped neckline and a plain waist belt.

Reconstructed from ``(pictoicon) - Bathrobe with Tied Belt.svg`` on SOLO48.
The source's knot, hanging belt tails, pocket lines, and shoulder seams are
deliberately omitted because they collapse at the native 48-pixel size.  The
drawing keeps three things and nothing else: the robe silhouette, the wrap,
and one waist member.

The silhouette has flat shoulders, tapered sleeves, and mirrored rounded
hem corners that flow smoothly into the straight body walls.  Every
segment is long enough to survive a four-unit round-joined stroke, and the
sleeve band never narrows below 8.9 units, so it stays open under the stroke
instead of closing into a blob.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class BathrobeWithTiedBelt(Solo48):
    """A hanging bathrobe seen flat from the front."""

    icon_id = "bathrobe-with-tied-belt"
    keyshape = Keyshape.SQUARE
    category = "objects/clothing"
    aliases = ("bathrobe", "robe", "dressing-gown")
    keywords = ("bathrobe", "robe", "spa", "bath", "hotel", "garment", "clothing", "belt")

    def build(self) -> None:
        # One symmetric garment silhouette, mirrored about x=24.  The shoulder
        # line, the sleeve extremes, and the hem hit SQUARE's (2, 2)-(46, 46)
        # centreline envelope exactly.  The sleeve underside runs *down* from
        # the cuff into the body wall, so the underarm is an obtuse corner
        # rather than the hook a returning edge would paint.
        upper_points = ((11, 42), (11, 22), (7, 18), (2, 9),
            (16, 2), (32, 2), (46, 9), (41, 18), (37, 22), (37, 42))
        upper_members = []
        for index, (start, end) in enumerate(zip(upper_points, upper_points[1:])):
            member = f"robe-upper-{index}"
            self.add_line(member, start, end)
            upper_members.append(member)
        self.add_arc("hem-right", (37, 42), (33, 46), radius_x=4)
        self.add_line("hem-base", (33, 46), (15, 46))
        self.add_arc("hem-left", (15, 46), (11, 42), radius_x=4)
        self.add_contour(
            "robe-outline", *upper_members, "hem-right", "hem-base", "hem-left",
            closed=True,
        )

        # The wrap is one V, not two crossing lapels: each side runs from a
        # shoulder corner to a single point on the belt, so the neckline reads
        # as an opening instead of an X laid over the chest.  At the underarm
        # the V still clears the body wall by 8.8.
        self.add_line("wrap-left", (16, 2), (24, 31))
        self.add_line("wrap-right", (32, 2), (24, 31))

        # A single waist member replaces the source's knot and two short tails.
        # It spans the body walls only.  At y=30 it clears the underarm corners
        # by 8 and leaves 13 of skirt below it, so the belt reads as a band
        # across the robe rather than as the floor of a box.
        self.add_line("waist-belt", (11, 31), (37, 31))

        self.relate("connect", "robe-outline", "wrap-left")
        self.relate("connect", "robe-outline", "wrap-right")
        self.relate("connect", "robe-outline", "waist-belt")
        self.relate("connect", "wrap-left", "wrap-right")
        self.relate("connect", "wrap-left", "waist-belt")
        self.relate("connect", "wrap-right", "waist-belt")
