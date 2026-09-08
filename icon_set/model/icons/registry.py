"""The single enumeration point for authored icons.

Builds, tests, and any future catalog read the corpus from here, so an icon
that is not discovered is not shipped and cannot silently skip validation.

Discovery is **by folder**. Each family named in the profile contract owns one
package -- ``sub/``, ``solo/``, ``container/`` -- and every public module in it
is imported. A module belongs to exactly one family, and every icon class it
defines must subclass *that* family's base: a ``Solo48`` dropped into ``sub/``
is refused with the two family names in the message, never quietly built on
the wrong canvas. That is the whole point of the folder split.
"""

from __future__ import annotations

import importlib
import inspect
from pathlib import Path
from typing import Callable, Iterator

from .. import contracts
from ..profiles import Profile
from .base import Icon
from .family import FamilyIcon

_HERE = Path(__file__).resolve().parent


def _family_base(family: str) -> type[FamilyIcon]:
    row = contracts.families()[family]
    package = row["package"].rsplit("/", 1)[-1]
    module = importlib.import_module(f".{package}._base", package=__package__)
    base = getattr(module, row["base_class"])
    if not (inspect.isclass(base) and issubclass(base, FamilyIcon)):
        raise TypeError(f"{row['base_class']} is not a FamilyIcon subclass")
    if base.family != family:
        raise ValueError(
            f"{base.__name__} declares family {base.family!r} but the contract "
            f"binds it to {family!r}"
        )
    if Profile.for_family(family) is not Profile[row["profile"]]:  # pragma: no cover
        raise ValueError(f"profile binding for {family!r} is inconsistent")
    return base


def families() -> dict[str, type[FamilyIcon]]:
    """Family name -> family base class, in contract order."""
    return {name: _family_base(name) for name in contracts.families()}


def _modules(family: str) -> list[str]:
    package = contracts.families()[family]["package"].rsplit("/", 1)[-1]
    folder = _HERE / package
    return sorted(
        f"{package}.{path.stem}"
        for path in folder.glob("*.py")
        if not path.name.startswith("_")
    )


def _collect(
    module: object,
    family: str,
    base: type[FamilyIcon],
    bases: dict[str, type[FamilyIcon]],
    factories: dict[str, Callable[[], Icon]],
) -> None:
    """Register every icon class ``module`` defines, refusing foreign families."""
    for _, member in inspect.getmembers(module, inspect.isclass):
        if member.__module__ != module.__name__:
            continue
        if not issubclass(member, FamilyIcon) or member is base:
            continue
        if not issubclass(member, base):
            owner = next(
                (name for name, other in bases.items() if issubclass(member, other)),
                member.family or "?",
            )
            raise TypeError(
                f"{module.__name__}.{member.__name__} is a {owner!r} icon "
                f"but lives in the {family!r} folder; each folder holds "
                "only its own family"
            )
        # Abstract bases carry no icon_id and are not shippable.
        if not member.icon_id:
            continue
        if member.icon_id in factories:
            raise ValueError(f"duplicate icon_id: {member.icon_id!r}")
        factories[member.icon_id] = member


def _discover() -> dict[str, Callable[[], Icon]]:
    factories: dict[str, Callable[[], Icon]] = {}
    bases = families()
    for family, base in bases.items():
        for dotted in _modules(family):
            module = importlib.import_module(f".{dotted}", package=__package__)
            _collect(module, family, base, bases, factories)
    return dict(sorted(factories.items()))


_FACTORIES: dict[str, Callable[[], Icon]] | None = None


def factories() -> dict[str, Callable[[], Icon]]:
    global _FACTORIES
    if _FACTORIES is None:
        _FACTORIES = _discover()
    return _FACTORIES


def icon_ids() -> tuple[str, ...]:
    return tuple(factories())


def create(icon_id: str) -> Icon:
    try:
        factory = factories()[icon_id]
    except KeyError as error:
        raise KeyError(f"unknown icon_id: {icon_id!r}") from error
    return factory()


def all_icons() -> Iterator[Icon]:
    """A fresh instance of every registered icon, in canonical id order."""
    for factory in factories().values():
        yield factory()


def icons_in(family: str) -> Iterator[Icon]:
    """Fresh instances of one family's icons, in canonical id order."""
    base = families()[family]
    for factory in factories().values():
        if issubclass(factory, base):  # type: ignore[arg-type]
            yield factory()
