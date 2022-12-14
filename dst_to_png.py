import pyembroidery
pattern = pyembroidery.read_dst("testpattern06_d4.0_R3.0_corr.dst")
pyembroidery.write_png(pattern, 'testpattern06_d4.0_R3.0_corr.png')
