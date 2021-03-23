#used to simmulate mixing Colors 
COLORKEY = {0: (192,192,192), 1: (255, 0, 0), 2: (0, 157, 255), 3: (144, 0, 255), 
            4: (255, 196, 0), 5: (255, 115, 0), 6: (0, 255, 17), 7: (255, 255, 255)}


def ColorMixer(RGB):
    key = 0
    if RGB[0]: key += 1
    if RGB[1]: key += 2
    if RGB[2]: key += 4
    return COLORKEY[key]

print (ColorMixer((True, False, False)))