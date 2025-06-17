def ida_to_pymeow(ida_pattern : str):
    byte_pattern = []
    mask = []
    
    for part in ida_pattern.split():
        if part == "??":
            byte_pattern.append(0)
            mask.append("?")
        else:
            byte_pattern.append(int(part, 16))
            mask.append("x")
    
    return bytes(byte_pattern), "".join(mask)


if __name__ == "__main__":
    # Example usage
    ida_pattern = "48 8B 05 ?? ?? ?? ?? F3 0F 10 88 34 01 00 00"
    byte_pattern, mask = ida_to_pymeow(ida_pattern)
    print(byte_pattern)
    print(mask)