"""
osrswiki_images
===============

Resolvers that map OSRS entities to their wiki pages and image URLs.

Public API
----------
- bucket_query(bucket_name, page_name): low-level bucket fetch
- item(name): item wiki URL and image; prefers default version
- spell(name): spell wiki URL and image
- construction(name): construction wiki URL and icon; default version
- quest(name): quest wiki URL; fixed quest icon
- skill(name): skill wiki URL and icon; validates known skills
- prayer(name): wiki URL and image from packaged CSV
- slayer_rewards(name): wiki URL and image from packaged CSV
- generalized_search(query): fallback OpenSearch resolver
- search_all(input): tries resolvers in order and returns the first match
"""

from .client import (
    bucket_query,
    construction,
    generalized_search,
    item,
    prayer,
    quest,
    search_all,
    skill,
    slayer_rewards,
    spell,
)

__all__ = [
    "bucket_query",
    "item",
    "spell",
    "construction",
    "quest",
    "skill",
    "prayer",
    "slayer_rewards",
    "generalized_search",
    "search_all",
]
