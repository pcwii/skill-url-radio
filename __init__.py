import sys
from os.path import dirname, abspath, join

import time
import subprocess
import json

from mycroft.filesystem import FileSystemAccess
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
from mycroft.audio import wait_while_speaking
from mycroft.skills.audioservice import AudioService

from mycroft.util.log import getLogger


class URLRadio(CommonPlaySkill):
    def __init__(self):
        super(URLRadio, self).__init__('URL Radio')
        file_name = 'url_list.json'
        skill_path = "/opt/mycroft/skills/skill-url-radio.pcwii"
        with open(join(skill_path, file_name)) as f:
            self.channel_list = json.load(f)
        self.log.info(str(self.channel_list))
        self.audio_service = ""

    def initialize(self):
        self.log.info('initializing URLRadio')
        self.load_data_files(dirname(__file__))
        self.audio_service = AudioService(self.bus)
        super(URLRadio, self).initialize()



    def CPS_match_query_phrase(self, phrase):
        """
            The method is invoked by the PlayBackControlSkill.
        """
        self.log.info('URLRadio received the following phrase: ' + phrase)
        for each_channel in self.channel_list["stations"]:  # loop through every interval
            if phrase in each_channel["name"]:
                print("Station Found, Exiting!")
                data = each_channel
                return phrase, CPSMatchLevel.TITLE, data
                break
            else:
                print("Station Not Found, Searching!")
        return None


    def CPS_start(self, phrase, data):
        """ Starts playback.
            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        self.log.info('URLRadio Skill received the following phrase and Data: ' + phrase + ' ' + str(data))
        self.speak_dialog('now.playing', data={"channel": data["name"]}, expect_response=False)
        url = str(data["url"])
        self.CPS_play(url, 'audio/mpeg')
        #self.audio_service.play(url)  #
        pass


def create_skill():
    return URLRadio()
