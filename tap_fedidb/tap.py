"""FediDB tap class."""

from __future__ import annotations

import typing as t

from singer_sdk import Stream, Tap

from tap_fedidb import streams


class TapFediDB(Tap):
    """Singer tap for FediDB."""

    name = "tap-fedidb"
    config_jsonschema: t.ClassVar[dict[str, t.Any]] = {
        "type": "object",
        "properties": {},
    }

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of FediDB streams.
        """
        return [
            streams.Servers(tap=self),
            streams.Software(tap=self),
            streams.PopularAccounts(tap=self),
        ]
