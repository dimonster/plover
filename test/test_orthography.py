# Copyright (c) 2013 Hesky Fisher
# See LICENSE.txt for details.

from plover.orthography import add_suffix

from . import parametrize


ADD_SUFFIX_TESTS = (
    lambda: ('artistic', 'ly', 'artistically'),
    lambda: ('cosmetic', 'ly', 'cosmetically'),
    lambda: ('establish', 's', 'establishes'),
    lambda: ('speech', 's', 'speeches'),
    lambda: ('approach', 's', 'approaches'),
    lambda: ('beach', 's', 'beaches'),
    lambda: ('arch', 's', 'arches'),
    lambda: ('larch', 's', 'larches'),
    lambda: ('march', 's', 'marches'),
    lambda: ('search', 's', 'searches'),
    lambda: ('starch', 's', 'starches'),
    lambda: ('stomach', 's', 'stomachs'),
    lambda: ('monarch', 's', 'monarchs'),
    lambda: ('patriarch', 's', 'patriarchs'),
    lambda: ('oligarch', 's', 'oligarchs'),
    lambda: ('cherry', 's', 'cherries'),
    lambda: ('day', 's', 'days'),
    lambda: ('penny', 's', 'pennies'),
    lambda: ('pharmacy', 'ist', 'pharmacist'),
    lambda: ('melody', 'ist', 'melodist'),
    lambda: ('pacify', 'ist', 'pacifist'),
    lambda: ('geology', 'ist', 'geologist'),
    lambda: ('metallurgy', 'ist', 'metallurgist'),
    lambda: ('anarchy', 'ist', 'anarchist'),
    lambda: ('monopoly', 'ist', 'monopolist'),
    lambda: ('alchemy', 'ist', 'alchemist'),
    lambda: ('botany', 'ist', 'botanist'),
    lambda: ('therapy', 'ist', 'therapist'),
    lambda: ('theory', 'ist', 'theorist'),
    lambda: ('psychiatry', 'ist', 'psychiatrist'),
    lambda: ('lobby', 'ist', 'lobbyist'),
    lambda: ('hobby', 'ist', 'hobbyist'),
    lambda: ('copy', 'ist', 'copyist'),
    lambda: ('beauty', 'ful', 'beautiful'),
    lambda: ('weary', 'ness', 'weariness'),
    lambda: ('weary', 'some', 'wearisome'),
    lambda: ('lonely', 'ness', 'loneliness'),
    lambda: ('narrate', 'ing', 'narrating'),
    lambda: ('narrate', 'or', 'narrator'),
    lambda: ('generalize', 'ability', 'generalizability'),
    lambda: ('reproduce', 'able', 'reproducible'),
    lambda: ('grade', 'ations', 'gradations'),
    lambda: ('urine', 'ary', 'urinary'),
    lambda: ('achieve', 'able', 'achievable'),
    lambda: ('polarize', 'ation', 'polarization'),
    lambda: ('done', 'or', 'donor'),
    lambda: ('analyze', 'ed', 'analyzed'),
    lambda: ('narrate', 'ing', 'narrating'),
    lambda: ('believe', 'able', 'believable'),
    lambda: ('animate', 'ors', 'animators'),
    lambda: ('discontinue', 'ation', 'discontinuation'),
    lambda: ('innovate', 'ive', 'innovative'),
    lambda: ('future', 'ists', 'futurists'),
    lambda: ('illustrate', 'or', 'illustrator'),
    lambda: ('emerge', 'ent', 'emergent'),
    lambda: ('equip', 'ed', 'equipped'),
    lambda: ('defer', 'ed', 'deferred'),
    lambda: ('defer', 'er', 'deferrer'),
    lambda: ('defer', 'ing', 'deferring'),
    lambda: ('pigment', 'ed', 'pigmented'),
    lambda: ('refer', 'ed', 'referred'),
    lambda: ('fix', 'ed', 'fixed'),
    lambda: ('alter', 'ed', 'altered'),
    lambda: ('interpret', 'ing', 'interpreting'),
    lambda: ('wonder', 'ing', 'wondering'),
    lambda: ('target', 'ing', 'targeting'),
    lambda: ('limit', 'er', 'limiter'),
    lambda: ('maneuver', 'ing', 'maneuvering'),
    lambda: ('monitor', 'ing', 'monitoring'),
    lambda: ('color', 'ing', 'coloring'),
    lambda: ('inhibit', 'ing', 'inhibiting'),
    lambda: ('master', 'ed', 'mastered'),
    lambda: ('target', 'ing', 'targeting'),
    lambda: ('fix', 'ed', 'fixed'),
    lambda: ('scrap', 'y', 'scrappy'),
    lambda: ('trip', 's', 'trips'),
    lambda: ('equip', 's', 'equips'),
    lambda: ('bat', 'en', 'batten'),
    lambda: ('smite', 'en', 'smitten'),
    lambda: ('got', 'en', 'gotten'),
    lambda: ('bite', 'en', 'bitten'),
    lambda: ('write', 'en', 'written'),
    lambda: ('flax', 'en', 'flaxen'),
    lambda: ('wax', 'en', 'waxen'),
    lambda: ('fast', 'est', 'fastest'),
    lambda: ('white', 'er', 'whiter'),
    lambda: ('crap', 'y', 'crappy'),
    lambda: ('lad', 'er', 'ladder'),
    lambda: ('translucent', 'cy', 'translucency'),
    lambda: ('bankrupt', 'cy', 'bankruptcy'),
    lambda: ('inadequate', 'cy', 'inadequacy'),
    lambda: ('secret', 'cy', 'secrecy'),
    lambda: ('impolite', 'cy', 'impolicy'),
    lambda: ('idiot', 'cy', 'idiocy'),
    lambda: ('free', 'ed', 'freed'),
    lambda: ('free', 'er', 'freer'),
    lambda: ('regulate', 'ry', 'regulatory'),
)

@parametrize(ADD_SUFFIX_TESTS)
def test_add_suffix(word, suffix, expected):
    assert add_suffix(word, suffix) == expected
