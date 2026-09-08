"""Structured validation results.

Every failure names the check that produced it and, wherever geometry is
involved, the element id and the actual coordinates — a report should be
enough to repair the icon without re-deriving the measurement.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Status = Literal["valid", "invalid", "review", "not_implemented"]

#: The fixed order from ICON_SYSTEM_PLAN.md section 5.
CHECK_ORDER = (
    "schema/profile",
    "style/grid",
    "canvas/keyshape bounds",
    "mic",
    "keyshape",
    "composition",
    "svg round-trip",
    "reproducibility",
)


@dataclass(frozen=True)
class Finding:
    check: str
    message: str
    element_id: str | None = None
    detail: dict = field(default_factory=dict)

    def __str__(self) -> str:
        where = f" [{self.element_id}]" if self.element_id else ""
        return f"{self.check}{where}: {self.message}"


@dataclass(frozen=True)
class ValidationReport:
    status: Status
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    findings: tuple[Finding, ...] = ()
    checks_run: tuple[str, ...] = ()

    @property
    def ok(self) -> bool:
        return self.status == "valid"

    @classmethod
    def build(
        cls,
        errors: list[Finding],
        warnings: list[Finding],
        checks_run: list[str],
        *,
        review: bool = False,
    ) -> "ValidationReport":
        if errors:
            status: Status = "invalid"
        elif review:
            status = "review"
        else:
            status = "valid"
        return cls(
            status=status,
            errors=tuple(str(finding) for finding in errors),
            warnings=tuple(str(finding) for finding in warnings),
            findings=tuple(errors) + tuple(warnings),
            checks_run=tuple(checks_run),
        )

    def describe(self) -> str:
        lines = [f"status: {self.status}"]
        for error in self.errors:
            lines.append(f"  ERROR  {error}")
        for warning in self.warnings:
            lines.append(f"  WARN   {warning}")
        return "\n".join(lines)
