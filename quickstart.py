""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random
users_to_follow = ['ramoswasoffside', 'passporttoearth', 'fav_skies', 'super_photosunsets', 'njsunrise_sunset', 'adventures_shutter', 'myskynow', 'newjerseyisbeautiful', 'igersmood', 'amazingly_sunsets', 'hey_ihadtosnapthat', 'passion_4_living_photos', 'goventureorange', 'onlythebestcapture', 'goandcapturethelight', 'bestpicturesgallery', 'rthouse']
random.shuffle(users_to_follow)
# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="mufnature",
                  password="2611fine",
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.follow_likers(users_to_follow, photos_grab_amount=1, follow_likers_per_photo=30, randomize=False, sleep_delay=60, interact=False)
    session.unfollow_users(amount=226, allFollowing=True, style="LIFO", unfollow_after=48 * 60 * 60, sleep_delay=10)
    # activity
    #session.like_by_tags(["natgeo"], amount=10)
