# tests/test_query_wiki_api.py
import pytest

pytestmark = pytest.mark.integration

from osrswiki_images import (
    construction,
    item,
    prayer,
    quest,
    search_all,
    skill,
    slayer_rewards,
    spell,
)

# (name, wiki_url, image_url)
testdata_item = [
    (
        "abyssal whip",
        "https://oldschool.runescape.wiki/w/Abyssal_whip",
        "https://oldschool.runescape.wiki/images/Abyssal_whip.png",
    ),
    (
        "trident of the swamp",
        "https://oldschool.runescape.wiki/w/Trident_of_the_swamp",
        "https://oldschool.runescape.wiki/images/Trident_of_the_swamp.png",
    ),
    (
        "amulet of glory",
        "https://oldschool.runescape.wiki/w/Amulet_of_glory",
        "https://oldschool.runescape.wiki/images/Amulet_of_glory(4).png",
    ),
    (
        "ring of dueling",
        "https://oldschool.runescape.wiki/w/Ring_of_dueling",
        "https://oldschool.runescape.wiki/images/Ring_of_dueling(8).png",
    ),
    (
        "games necklace",
        "https://oldschool.runescape.wiki/w/Games_necklace",
        "https://oldschool.runescape.wiki/images/Games_necklace(8).png",
    ),
    (
        "combat bracelet",
        "https://oldschool.runescape.wiki/w/Combat_bracelet",
        "https://oldschool.runescape.wiki/images/Combat_bracelet.png",
    ),
    (
        "tumeken's shadow",
        "https://oldschool.runescape.wiki/w/Tumeken's_shadow",
        "https://oldschool.runescape.wiki/images/Tumeken's_shadow.png",
    ),
    (
        "black mask (i)",  # no default version → fallback path
        "https://oldschool.runescape.wiki/w/Black_mask_(i)",
        "https://oldschool.runescape.wiki/images/Black_mask_(i).png",
    ),
]

testdata_construction = [
    (
        "occult altar",
        "https://oldschool.runescape.wiki/w/Occult_altar",
        "https://oldschool.runescape.wiki/images/Occult_altar_icon.png",
    ),
    (
        "dark altar (construction)",
        "https://oldschool.runescape.wiki/w/Dark_altar_(Construction)",
        "https://oldschool.runescape.wiki/images/Dark_altar_(Construction)_icon.png",
    ),
    (
        "dark altar",  # suffix retry path
        "https://oldschool.runescape.wiki/w/Dark_altar_(Construction)",
        "https://oldschool.runescape.wiki/images/Dark_altar_(Construction)_icon.png",
    ),
    (
        "rejuvenation pool",  # multiple versions; one default
        "https://oldschool.runescape.wiki/w/Rejuvenation_pool",
        "https://oldschool.runescape.wiki/images/Rejuvenation_pool_icon.png",
    ),
]

testdata_spell = [
    (
        "ice barrage",
        "https://oldschool.runescape.wiki/w/Ice_Barrage",
        "https://oldschool.runescape.wiki/images/Ice_Barrage.png",
    ),
    (
        "vengeance",
        "https://oldschool.runescape.wiki/w/Vengeance",
        "https://oldschool.runescape.wiki/images/Vengeance.png",
    ),
    (
        "resurrect greater ghost",
        "https://oldschool.runescape.wiki/w/Resurrect_Greater_Ghost",
        "https://oldschool.runescape.wiki/images/Resurrect_Greater_Ghost.png",
    ),
]

testdata_skill = [
    (
        "agility",
        "https://oldschool.runescape.wiki/w/Agility",
        "https://oldschool.runescape.wiki/images/Agility_icon.png",
    ),
    (
        "runecrafting",  # normalization to Runecraft
        "https://oldschool.runescape.wiki/w/Runecraft",
        "https://oldschool.runescape.wiki/images/Runecraft_icon.png",
    ),
]

testdata_quest = [
    (
        "icthlarin's little helper",
        "https://oldschool.runescape.wiki/w/Icthlarin's_Little_Helper",
        "https://oldschool.runescape.wiki/images/Quest_point_icon.png",
    ),
    (
        "lost city",
        "https://oldschool.runescape.wiki/w/Lost_City",
        "https://oldschool.runescape.wiki/images/Quest_point_icon.png",
    ),
]

testdata_slayer_rewards = [
    (
        "bigger and badder",
        "https://oldschool.runescape.wiki/w/Slayer_Rewards",
        "https://oldschool.runescape.wiki/images/Bigger_and_Badder.png",
    ),
    (
        "reptile got ripped",
        "https://oldschool.runescape.wiki/w/Slayer_Rewards",
        "https://oldschool.runescape.wiki/images/Lizardmen_icon.png",
    ),
]

testdata_prayer = [
    (
        "rigour",
        "https://oldschool.runescape.wiki/w/Rigour",
        "https://oldschool.runescape.wiki/images/Rigour.png",
    ),
    (
        "protect from melee",
        "https://oldschool.runescape.wiki/w/Protect_from_Melee",
        "https://oldschool.runescape.wiki/images/Protect_from_Melee.png",
    ),
]

testdata_all = (
    testdata_item
    + testdata_construction
    + testdata_spell
    + testdata_skill
    + testdata_quest
    + testdata_slayer_rewards
    + testdata_prayer
)


def _ids(data):
    return [t[0] for t in data]


def _check(result, wiki_url_truth, image_url_truth):
    assert result is not None, "resolver returned None"
    assert result["wikiUrl"] == wiki_url_truth
    assert result["imgUrl"] == image_url_truth


@pytest.mark.parametrize("name,wiki,img", testdata_item, ids=_ids(testdata_item))
def test_item(name, wiki, img):
    _check(item(name), wiki, img)


@pytest.mark.parametrize(
    "name,wiki,img", testdata_construction, ids=_ids(testdata_construction)
)
def test_construction(name, wiki, img):
    _check(construction(name), wiki, img)


@pytest.mark.parametrize("name,wiki,img", testdata_spell, ids=_ids(testdata_spell))
def test_spell(name, wiki, img):
    _check(spell(name), wiki, img)


@pytest.mark.parametrize("name,wiki,img", testdata_skill, ids=_ids(testdata_skill))
def test_skill(name, wiki, img):
    _check(skill(name), wiki, img)


@pytest.mark.parametrize("name,wiki,img", testdata_quest, ids=_ids(testdata_quest))
def test_quest(name, wiki, img):
    _check(quest(name), wiki, img)


@pytest.mark.parametrize(
    "name,wiki,img", testdata_slayer_rewards, ids=_ids(testdata_slayer_rewards)
)
def test_slayer_rewards(name, wiki, img):
    _check(slayer_rewards(name), wiki, img)


@pytest.mark.parametrize("name,wiki,img", testdata_prayer, ids=_ids(testdata_prayer))
def test_prayer(name, wiki, img):
    _check(prayer(name), wiki, img)


@pytest.mark.parametrize("name,wiki,img", testdata_all, ids=_ids(testdata_all))
def test_search_all(name, wiki, img):
    _check(search_all(name), wiki, img)


# Negative-path coverage
def test_skill_invalid_returns_none():
    assert skill("NotASkill") is None


def test_item_unknown_returns_none():
    assert item("this definitely does not exist 12345") is None
