from apscheduler.schedulers.blocking import BlockingScheduler
""" Quickstart script for InstaPy usage """

# imports
import os
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random
from instapy import get_workspace

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=os.environ['hour'],minute=os.environ['minute'])
def scheduled_job():
    users_to_follow = ['ramoswasoffside', 'passporttoearth', 'fav_skies', 'super_photosunsets', 'njsunrise_sunset', 'adventures_shutter', 'myskynow', 'newjerseyisbeautiful', 'igersmood', 'amazingly_sunsets', 'hey_ihadtosnapthat', 'passion_4_living_photos', 'goventureorange', 'onlythebestcapture', 'goandcapturethelight', 'bestpicturesgallery', 'rthouse']
    random.shuffle(users_to_follow)
    # set workspace folder at desired location (default is at your home folder)
    set_workspace(path="./")
    workspace_in_use = get_workspace()
    print(workspace_in_use["path"])

    # get an InstaPy session!
    session = InstaPy(username=os.environ['username'],
                      password=os.environ['password'],
                      headless_browser=True)

    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_dont_include(["friend1", "friend2", "friend3"])
        #session.follow_likers(users_to_follow, photos_grab_amount=1, follow_likers_per_photo=14, randomize=False, sleep_delay=60, interact=False)
        session.unfollow_users(amount=250, allFollowing=True, style="LIFO", unfollow_after=48 * 60 * 60, sleep_delay=random.randint(1, 10)*60)
        # activity
        #session.like_by_tags(["natgeo"], amount=10)

sched.start()
