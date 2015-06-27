#!/usr/bin/env fontforge
#
# Copyright (c) 2014-2015, Sungsit Sawaiwan (https://sungsit.com | gibbozer [at] gmail [dot] com).
#
# This Font Software is licensed under the SIL Open Font License, Version 1.1 (OFL).
# You should have received a copy of the OFL License along with this file.
# If not, see http://scripts.sil.org/OFL
#

# This script will only work with FontForge's Python extension.
import fontforge
import os

# Predifined vars
family = 'F0ntUni'
version = '1.0-beta2'
source = 'F0ntUni.ufo'
copyright =  'Copyright (c) 2014-2015, Sungsit Sawaiwan (https://sungsit.com | gibbozer [at] gmail [dot] com). This Font Software is licensed under the SIL Open Font License, Version 1.1 (http://scripts.sil.org/OFL).'
features = ['Bare', 'Basic', 'Extended']
feature_dir = 'features/'
build_dir = family + '/'

def setFontInfo(source,family,feature):
  font = fontforge.open(source)
  font.familyname = family
  font.fontname = family + '-' + feature
  font.fullname = family + ' ' + feature
  font.version = version
  font.copyright = copyright

def printFontInfo(fontfile):
  font = fontforge.open(fontfile)
  print('\nFamily Name: ' + font.familyname)
  print('Font Name: ' + font.fontname)
  print('Full Name: ' + font.fullname)
  print('Font Version: ' + font.version)
  print('Font Copyright: ' + font.copyright)
  font.close()

def clearThaiPUA(source):
  font = fontforge.open(source)
  font.encoding = 'UnicodeFull'
  font.selection.select(('ranges','unicode'),'uniF884','uniF899')
  font.clear()
  font.selection.select(('ranges','unicode'),'uniF89B','uniF89D')
  font.clear()
  font.selection.select(('ranges','unicode'),'uniF8A0','uniF8A4')
  font.clear()
  
def buildFont(source,family,feature):
  font = fontforge.open(source)
  setFontInfo(source,family,feature)

  fea = feature_dir + 'Thai-' + feature + '.fea'
  otf = build_dir + font.fontname + '.otf'
  genflags  = ('opentype', 'PfEd-lookups', 'no-hints')

  if (feature == 'Basic'):
    clearThaiPUA(source)

  font.mergeFeature(fea)  
  font.generate(otf, flags=genflags)
  printFontInfo(otf)
  font.close()


if not os.path.exists(build_dir):
  os.makedirs(build_dir)

for feature in features:
  buildFont(source,family,feature)
