# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Memory.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
for i in range(1,10):
    a.datas += [(f'cat{i}.PNG',f'/home/sinisa/Desktop/source/python/Memory/cat{i}.PNG', 'Data')]
    a.datas += [(f'dog{i}.PNG',f'/home/sinisa/Desktop/source/python/Memory/dog{i}.PNG', 'Data')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Memory',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
