from wxpy import *
import json
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

config = json.load(open('config','r'))
# load config as a json object which has api_key, friends, groups, reportTo keys.

bot, tuling = Bot(cache_path=True), Tuling(api_key=config['api_key'])

friends, groups, reportTo = config['friends'], config['groups'], config['reportTo']

scheduler = BackgroundScheduler()


def searchFriends(friend_names, type_name):
    friends = []
    for name in friend_names:
        if hasattr(bot, type_name):
            ret = getattr(bot, type_name)().search(name)
            if len(ret): friends.append(ret[0])
    return friends


def report():
    r = open('report.txt', 'r')
    contents = ''.join(r.readlines())
    print(contents)
    for recipient in searchFriends(reportTo,"groups"):
        recipient.send(contents)


@bot.register(searchFriends(friends, "friends") + searchFriends(groups, "groups"), TEXT)
def auto_reply(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        msg.reply(tuling.reply_text(msg))


scheduler.add_job(report, 'cron', hour=21, minute=10, id="dailyReport")
scheduler.start()

embed()




