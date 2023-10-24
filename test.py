import string
s = 'CRL Blumcraft® manufactures a complete line of. Electrified \Mortise .\!?,/() "Lock with Deadbolt, Fail Secure, Both Levers EU, Double Cylinder Override, Standard Cylinder, 12/24VDC, Bright Stainless SteelThe Schlage L909x Series is the next generation of electrified mortise lock. The series utilizes the latest technology to offer tremendous utility and flexibility. The universal input voltage will accept 12 or 24VDC and fail safe/fail secure functions are user selectable in the field by flipping a switch in the lock case. The all new RX switch monitors the inside lever with enhanced detection level that balances security with lever sensitivity, and can be added in the field without opening the lock case.'

# print(s.translate(str.maketrans('', '', string.punctuation)))


def normalization_text(txt):
    return txt.translate(str.maketrans('', '', string.punctuation)).lower()

print(normalization_text(s))