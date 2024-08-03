def lowercase_alphabet(startIdx, lngth):
    return [chr(i) for i in range(startIdx, startIdx + lngth )]

print(lowercase_alphabet(startIdx = 97, lngth = 26))
