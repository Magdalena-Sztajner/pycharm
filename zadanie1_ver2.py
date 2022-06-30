oprocentowanie = 3
rata = 200
pozyczka = 12000
mniej_0 = 0
splacone = 0

for i in range(12):
    miesiac = input()
    inflacja = float(input())

    do_splaty_lacznie = round((1 + ((inflacja + oprocentowanie) / 1200)) * pozyczka - rata)
    mniej_0 = round(pozyczka - do_splaty_lacznie)
    # pozyczka -= mniej_0
    pozyczka = do_splaty_lacznie