# -*- mode: python ; coding: utf-8 -*-


import pygame
import os

# Находим путь к шрифтам pygame
pygame_fonts_path = os.path.join(os.path.dirname(pygame.__file__), 'freesansbold.ttf')

a = Analysis(
    ['src/game/__main__.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('src/game/config.json', 'game'),
        ('src/game/games', 'game/games'),
        ('src/game/ui', 'game/ui'),
        (pygame_fonts_path, 'pygame')
    ],
    hiddenimports=['pygame', 'appdirs', 'pygame.font'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GameCollection',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
