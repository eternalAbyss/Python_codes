def replace_quotes(self, query: str):
    """
    Convert only the outer single quotes around JSON-like keys and values
    to double quotes, preserving inner apostrophes and leaving already
    double-quoted strings untouched.

    Handles:
      - Keys:    {'key': ...}   -> {"key": ...}
      - Values:  : 'value'      -> : "value"
      - Arrays:  ['a', 'b']     -> ["a", "b"]
      - Inner apostrophes (it's, O'Reilly) remain as-is.
    """
    # logger().log({"msg": "[Start] PayloadModifier - replace_quotes function"}, "DEBUG")

    s = query
    n = len(s)
    i = 0
    out = []

    def prev_sig_idx(k: int) -> int:
        """index of previous non-space char before k, or -1 if none."""
        k -= 1
        while k >= 0 and s[k].isspace():
            k -= 1
        return k

    def next_sig_idx(k: int) -> int:
        """index of next non-space char at/after k, or n if none."""
        while k < n and s[k].isspace():
            k += 1
        return k

    in_dq = False     # inside a double-quoted string
    esc = False       # last char was backslash (for escapes within double quotes)

    while i < n:
        ch = s[i]

        # Respect existing JSON double-quoted strings: do not touch contents.
        if in_dq:
            out.append(ch)
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == '"':
                in_dq = False
            i += 1
            continue

        # Not inside a double-quoted string
        if ch == '"':
            in_dq = True
            esc = False
            out.append(ch)
            i += 1
            continue

        # Potential single-quoted key/value/array element
        if ch == "'":
            start = i
            j = i + 1
            # Find the matching closing single quote (no special escapes in JSON for single quotes;
            # treat backslash as ordinary char here to avoid overfitting to non-standard escaping).
            while j < n and s[j] != "'":
                j += 1
            if j >= n:
                # No closing quote: emit as-is and move on
                out.append(ch)
                i += 1
                continue

            # Determine context to ensure this is a JSON token we should convert
            # Look at the char before the opening quote and after the closing quote.
            prev_i = prev_sig_idx(start)
            next_j = next_sig_idx(j + 1)
            prev_ch = s[prev_i] if prev_i >= 0 else None
            next_ch = s[next_j] if next_j < n else None

            is_key   = (next_ch == ':') and (prev_ch in (None, '{', ',',))  # '{' or ',' or start
            is_value = (prev_ch in (':', '[', ',', None)) and (next_ch in (',', '}', ']', None))

            if is_key or is_value:
                # Replace only the outer quotes; keep inner apostrophes intact
                out.append('"')
                out.append(s[start + 1:j])
                out.append('"')
                i = j + 1
                continue
            else:
                # Looks like a bare apostrophe usage not forming key/value; leave it
                out.append(ch)
                i += 1
                continue

        # Default: copy through
        out.append(ch)
        i += 1

    result = ''.join(out)
    # logger().log({"msg": "[End] PayloadModifier - replace_quotes function"}, "DEBUG")
    return result



class Dummy:
    def replace_quotes(self, q):  # just to call the method as written
        return replace_quotes(self, q)