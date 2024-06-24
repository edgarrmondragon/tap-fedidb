"""REST client handling, including FediDBStream base class."""

from __future__ import annotations

import typing as t

from singer_sdk import RESTStream


class FediDBStream(RESTStream[t.Any]):
    """FediDB stream class."""

    url_base = "https://api.fedidb.org"

    @property
    def http_headers(self) -> dict[str, str]:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        return {"User-Agent": f"{self.tap_name}/{self._tap.plugin_version}"}
