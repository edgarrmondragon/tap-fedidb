"""Stream type classes for tap-fedidb."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th

from tap_fedidb.client import FediDBStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context


class Servers(FediDBStream):
    """Servers stream."""

    name = "servers"
    path = "/v1/servers"
    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.meta.next_cursor"  # noqa: S105

    _page_size = 40

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("domain", th.StringType),
        th.Property("open_registration", th.BooleanType),
        th.Property("description", th.StringType),
        th.Property("banner_url", th.StringType),
        th.Property(
            "location",
            th.ObjectType(
                th.Property("city", th.StringType),
                th.Property("country", th.StringType),
            ),
        ),
        th.Property(
            "software",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("url", th.StringType),
                th.Property("version", th.StringType),
            ),
        ),
        th.Property(
            "stats",
            th.ObjectType(
                th.Property("status_count", th.IntegerType),
                th.Property("user_count", th.IntegerType),
                th.Property("monthly_active_users", th.IntegerType),
            ),
        ),
        th.Property("first_seen_at", th.DateTimeType),
        th.Property("last_seen_at", th.DateTimeType),
    ).to_dict()

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: str | None,
    ) -> dict[str, t.Any] | str:
        """Return a dictionary of params or a string for the request URL."""
        params = super().get_url_params(context, next_page_token)

        params["limit"] = self._page_size  # type: ignore[index]

        if next_page_token:
            params["cursor"] = next_page_token  # type: ignore[index]

        return params


class Software(FediDBStream):
    """Software stream."""

    name = "software"
    path = "/v1/software"
    records_jsonpath = "$[*]"

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("url", th.StringType),
        th.Property("name", th.StringType),
        th.Property("license", th.StringType),
        th.Property("website", th.StringType),
        th.Property("user_count", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("details_url", th.StringType),
        th.Property("source_repo", th.StringType),
        th.Property("status_count", th.IntegerType),
        th.Property("instance_count", th.IntegerType),
        th.Property(
            "latest_version",
            th.ObjectType(
                th.Property("version", th.StringType),
                th.Property("published_at", th.DateTimeType),
            ),
        ),
        th.Property("monthly_active_users", th.IntegerType),
    ).to_dict()


class PopularAccounts(FediDBStream):
    """Popular accounts stream."""

    name = "popular_accounts"
    path = "/v1/popular-accounts"
    records_jsonpath = "$.data[*]"

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("rank", th.IntegerType),
        th.Property("username", th.StringType),
        th.Property("name", th.StringType),
        th.Property("domain", th.StringType),
        th.Property("account_url", th.StringType),
        th.Property("avatar_url", th.StringType),
        th.Property("following_count", th.IntegerType),
        th.Property("followers_count", th.IntegerType),
        th.Property("status_count", th.IntegerType),
        th.Property("webfinger", th.StringType),
        th.Property("bio", th.StringType),
        th.Property("account_created_at", th.DateTimeType),
        th.Property("last_fetched_at", th.DateTimeType),
    ).to_dict()
