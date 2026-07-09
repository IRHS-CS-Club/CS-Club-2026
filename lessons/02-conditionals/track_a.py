"""
SYNTAX CHEAT SHEET:
if condition:
    # runs if true
elif another_condition:
    # runs if true
else:
    # fallback
Symbols: >, <, == (equals)
"""
print("=== Security Gate Check ===")

try:
    clearance_level = 2

    # 📝 TODO: Build logic branches. Level >= 3 is Admin. Level 1 or 2 is Standard. Else Denied.
    if clearance_level >= 3:
        print("Status: Admin Access")
    else:
        pass

except Exception:
    print("\n[💡 HINT]: Check your indentation and verify each condition ends with a colon (:)")