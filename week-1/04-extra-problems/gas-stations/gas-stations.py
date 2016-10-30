# gas stations


def gas_stations(distance, tank_size, stations):
    stops = []
    last_st = 0
    for i in range(0, len(stations)):
        if stations[i] > distance:
            break
        if stations[i] - tank_size >= last_st:
            stops.append(stations[i - 1])
            last_st = stations[i - 1]
    stops.append(stations[len(stations) - 1])
    return stops


def main():
    print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
    print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


if __name__ == '__main__':
    main()
