"""Side + container icon combination — main icon plus a sub ("state") icon on
one 1024x1024 canvas, with the main icon's strokes erased wherever the sub
icon's buffered hull covers them.

Ported from pg_app_processing/combination_jobs/side-combination/ — see
PROVENANCE.md for what differs and how to re-sync.

    from icon_combination import CombineConfig, combine_svgs
    combine_svgs("main.svg", "sub.svg", "out.svg", position="bottom-right")

`combine_svgs` is a thin keyword wrapper; the engine entry point
`process_svg_icons_4_steps_with_dynamic_alignment` is re-exported unchanged for
callers that want its full signature.

Agg is selected BEFORE the submodules load: every one of them imports
matplotlib.pyplot at module scope, and a server process must never end up on an
interactive backend. Same guard svg_extraction/execution.py and
png_to_svg_new/qa_overlays.py already apply.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

from .combine import (  # noqa: E402  — must follow the backend selection
    CombineConfig,
    process_svg_icons_4_steps_with_dynamic_alignment,
)
from .constants import get_aspect_ratio  # noqa: E402
from .fit_canvas import fit_svg_to_canvas, geometry_bbox  # noqa: E402

__all__ = [
    "CANVAS",
    "POSITIONS",
    "CombineConfig",
    "combine_svgs",
    "fit_svg_to_canvas",
    "geometry_bbox",
    "get_aspect_ratio",
    "process_svg_icons_4_steps_with_dynamic_alignment",
]

#: The engine's fixed working canvas. Sizes expressed as a percentage by
#: callers (the API, the CLI) are resolved against this.
CANVAS = 1024

#: Every alignment the engine accepts for the SUB icon. The main icon goes to
#: the opposite anchor (alignment_decision.calculate_main_icon_position);
#: 'center' is the container case — main icon at 100% scale, sub icon centred
#: inside it.
POSITIONS = (
    "top-left", "top", "top-right",
    "left", "center", "right",
    "bottom-left", "bottom", "bottom-right",
)


def combine_svgs(
    main_svg_path,
    sub_svg_path,
    output_svg_path,
    *,
    position: str = "bottom-right",
    sub_size: float = 512,
    buffer_radius: float = 64,
    stroke_width: float = 30,
    main_stroke_width: float = 25,
    sub_stroke_width: float = 25,
    main_color: str = "#000000",
    sub_color: str = "#000000",
    center_point: tuple[float, float] | None = None,
    center_is_offset: bool = False,
    is_text: bool = False,
    fit_canvas: bool = True,
    config: CombineConfig | None = None,
):
    """Combine two SVGs and write the result. Returns the engine's result dict
    (falsy / None on failure), with a `fit` key added — see ``fit_canvas``.

    ``position`` is the SUB icon's anchor; ``'center'`` is the container mode.
    ``sub_size`` is the sub icon's box in canvas px (square).
    ``buffer_radius`` is the erasure margin around the sub icon, in canvas px.

    ``center_point`` overrides the anchor with an explicit (x, y) in canvas px.
    Its meaning follows ``center_is_offset``:

    * ``False`` (default) — (x, y) IS the sub icon's centre.
    * ``True`` — (x, y) is added to the anchor's base position, matching what
      pg_app_processing's ``POST /side-combination`` sends (``is_shifted``).

    ``fit_canvas`` (default on) rewrites the written SVG so the icon's STROKED
    extent fits inside the canvas. The engine places icons on their centerlines
    and allows nothing for stroke width, so at 51.2 an anchored combination is
    cut off at the canvas edge — and the clipped ink then makes the key-shape
    snap land off-grid. See fit_canvas.py. It is a no-op for combinations that
    already fit, so turning it off only matters when you want the engine's
    output untouched.
    """
    if position not in POSITIONS:
        raise ValueError(
            f"position must be one of {POSITIONS}, got {position!r}")

    result = process_svg_icons_4_steps_with_dynamic_alignment(
        main_svg_path=str(main_svg_path),
        state_svg_path=str(sub_svg_path),
        output_svg_path=str(output_svg_path),
        state_width=sub_size,
        state_height=sub_size,
        position=position,
        stroke_width=stroke_width,
        buffer_radius=buffer_radius,
        main_color=main_color,
        state_color=sub_color,
        main_stroke_width=main_stroke_width,
        state_stroke_width=sub_stroke_width,
        is_custom_center_point=center_point is not None,
        center_point_x=center_point[0] if center_point else None,
        center_point_y=center_point[1] if center_point else None,
        is_shifted=bool(center_point) and center_is_offset,
        is_text=is_text,
        config=config,
        show_matplotlib=False,
    )

    fit = None
    if fit_canvas and result and result.get("step4_saved"):
        out = Path(output_svg_path)
        text, fit = fit_svg_to_canvas(
            out.read_text(encoding="utf-8"),
            stroke=max(main_stroke_width, sub_stroke_width),
            canvas=CANVAS,
        )
        if fit:
            out.write_text(text, encoding="utf-8")
    if isinstance(result, dict):
        result["fit"] = fit
    return result
