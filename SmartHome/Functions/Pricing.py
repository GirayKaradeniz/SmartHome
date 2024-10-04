def calculate_price(data, morning, peak, night):


    morningPrice = 0
    peakPrice = 0
    nightPrice = 0

    for mValue in data.iloc[-1, 2:13]:
        morningPrice += mValue * morning

    for pValue in data.iloc[-1, 13:17]:
        peakPrice += pValue * peak

    for nValue in data.iloc[-1, 18:26]:
        nightPrice += nValue * night

    energy_prices = morningPrice + peakPrice + nightPrice

    print(f"Morning Price: {morningPrice}")
    print(f"Peak Price: {peakPrice}")
    print(f"Night Price: {nightPrice}")
    print(f"Total Energy Price: {energy_prices}")

    return energy_prices
