# additional_attrs = "pii, cid, FEATURE_SCORES"
additional_attrs = ""

attrs = list(map(str.strip, map(str.upper, additional_attrs.split(","))))

flags = {
    "PII": False,
    "FEATURE_SCORES": False,
    "CID": False,
}

for attr in attrs:
    if attr in flags:
        print(flags[attr])
    else:
        raise ValueError(f"Unknown attribute: {attr}")