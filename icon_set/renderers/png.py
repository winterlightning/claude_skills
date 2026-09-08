"""Rasterize the same resolved scene the SVG renderer emits.

PNG dimensions are exactly the profile canvas: 32, 48, or 64 pixels. Larger
previews are derived QA assets produced by ``scripts/contact_sheet.py``, never
a canonical ``export_icon_to()`` result.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .svg import render_svg

if TYPE_CHECKING:  # pragma: no cover - typing only
    from ..model.icons.base import Icon

DEFAULT_INK = "#111111"


def render_png(icon: "Icon", *, ink: str = DEFAULT_INK, scale: int = 1) -> bytes:
    """Render to PNG at the native canvas size (or an integer QA multiple)."""
    try:
        import cairosvg
    except ImportError as error:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "PNG export needs cairosvg; install it or export SVG instead"
        ) from error
    if scale < 1 or int(scale) != scale:
        raise ValueError("scale must be a positive integer")
    canvas = icon.profile.spec.canvas_size
    # currentColor has no cascade in a standalone document; bind it explicitly.
    document = render_svg(icon).replace(
        'fill="none"', f'color="{ink}" fill="none"', 1
    )
    return cairosvg.svg2png(
        bytestring=document.encode("utf-8"),
        output_width=canvas * scale,
        output_height=canvas * scale,
    )
