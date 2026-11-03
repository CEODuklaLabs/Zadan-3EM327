def soucet_do_n(n):
    """
    DONE Vrať součet všech celých čísel od 1 do n (včetně n) pomocí cyklu for a range().
    DONE Pokud je n menší než 1, vrať 0.
    DONE Pokud n není celé číslo (int), vyhoď TypeError s výstižnou zprávou.

    Příklad:
        soucet_do_n(5) -> 15  (1+2+3+4+5)
        soucet_do_n(1) -> 1
        soucet_do_n(0) -> 0
    """

    # TODO: doplň řešení
    if not isinstance(n, int):
        raise TypeError("Vystižná zpráva, kterou pochopí pouze AI")
    
    if n < 1:
        return 0
    
    res=0
    for i in range(1,n+1):
        res += i

    return res
    
