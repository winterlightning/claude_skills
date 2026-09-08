"""Normalized SVG path command, and conversion from the geometry AST.

This is the interchange type the vendored spacing engine consumes. Keeping it
here rather than importing the deprecated tree means the MIC engine has no
dependency outside this package.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..model.primitives import Arc, Line, Primitive


@dataclass
class Command:
    type: str
    points: list[tuple[float, float]]
    arc: tuple[float, float, float, int, int] | None = None


def commands_for_path(primitives: list[Primitive], closed: bool = False) -> list[Command]:
    """Turn one contiguous run of primitives into M/L/A(/Z) commands."""
    if not primitives:
        raise ValueError("a path needs at least one primitive")
    first = primitives[0]
    commands = [Command("M", [(float(first.start.x), float(first.start.y))])]
    for primitive in primitives:
        end = (float(primitive.end.x), float(primitive.end.y))
        if isinstance(primitive, Line):
            commands.append(Command("L", [end]))
        elif isinstance(primitive, Arc):
            commands.append(Command("A", [end], (
                float(primitive.radius_x), float(primitive.radius_y), 0.0,
                int(primitive.large_arc), int(primitive.sweep),
            )))
        else:  # pragma: no cover - guarded by the type union
            raise TypeError(f"unsupported primitive: {type(primitive).__name__}")
    if closed:
        commands.append(Command("Z", []))
    return commands
