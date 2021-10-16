def anagrame (sir1, sir2):
    if len(sir1)==len(sir2):
        return sorted(sir1)==sorted(sir2)
    else:
        return False
    print(anagrame("note","tone"))