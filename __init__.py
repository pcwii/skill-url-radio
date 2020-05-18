import sys
from os.path import dirname, abspath, join
import time
import subprocess
import json

from mycroft.filesystem import FileSystemAccess
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
from mycroft.util.parse import match_one

#import re
#from adapt.intent import IntentBuilder
#from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from mycroft.util.log import getLogger
from mycroft.util.log import LOG

sys.path.append(abspath(dirname(__file__)))

logger = getLogger(__name__)

__author__ = 'pcwii20200517'

class URLRadio(CommonPlaySkill):
    def __init__(self):
        super(URLRadio, self).__init__('URL Radio')
        file_name = 'url_list.json'
        skill_path = "/opt/mycroft/skills/skill-url-radio.pcwii"
        with open(join(skill_path, file_name)) as f:
            self.channel_list = json.load(f)
        lOG.info(str(self.channel_list))

    def initialize(self):
        LOG.info('initializing URLRadio')
        self.load_data_files(dirname(__file__))
        super(URLRadio, self).initialize()
#        for c in self.url.channels.keys():
#            self.register_vocabulary(c, 'ChannelKeyword')
#        intent = IntentBuilder('PlayChannelIntent' + self.name)\
#            .require('PlayKeyword')\
#            .require('ChannelKeyword')\
#            .build()
#        self.register_intent(intent, self.handle_play_channel)
#        intent = IntentBuilder('PlayFromIntent' + self.name)\
#            .require('PlayKeyword')\
#            .require('ChannelKeyword')\
#            .require('NameKeyword')\
#            .build()
#        self.register_intent(intent, self.handle_play_channel)


    def CPS_match_query_phrase(self, phrase):
        """
            The method is invoked by the PlayBackControlSkill.
        """
        LOG.info('URLRadio received the following phrase: ' + phrase)
        match, confidence = match_one(phrase, self.channel_list)
        # If the confidence is high enough return a match
        if confidence > 0.5:
            return match, CPSMatchLevel.TITLE, {"track": match}
        # Otherwise return None
        else:
            return None


    def CPS_start(self, phrase, data):
        """ Starts playback.
            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        LOG.info('URLRadio Skill received the following phrase and Data: ' + phrase + ' ' + data['track'])
#        self.speak_dialog('now.playing', data={"channel": play_request[0], "category": play_request[1]},
#                          expect_response=False)
        url = data['track']
#        self.audioservice.play(url)  #
        pass


def create_skill():
    return URLRadio()
