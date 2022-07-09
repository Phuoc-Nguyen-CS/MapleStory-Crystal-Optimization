from collections import defaultdict


# A Class to store the boss data within Maple
# In :
#   bossName - The name of the boss
#   normalValue - the value of the boss in its normal mode
#   chaosValue - the value of the boss in its chaos mode
#   weekly - whether this boss is considered a weekly boss,
#            or a boss that can only be done once a week


class Boss:
    def __init__(self, bossName, normalValue, chaosValue):
        self.bossName = bossName
        self.normalValue = normalValue
        self.chaosValue = chaosValue

    def __str__(self):
        profits = "{:,}".format(self.get_weekly_profits())
        return self.get_name() + ' ' + profits

    def get_name(self):
        return self.bossName

    def get_normal_price(self):
        return self.normalValue

    def get_chaos_price(self):
        return self.chaosValue

    def get_weekly_profits(self):
        return 7 * self.get_normal_price() + self.get_chaos_price()


if __name__ == "__main__":

    bosses = {
        'Zakum': {'Normal': 612_500, 'Chaos': 16_200_000},
        'Horntail': {'Normal': 1_012_500, 'Chaos': 1_352_000},
        'Von Leon': {'Normal': 1_458_000, 'Chaos': 2_450_000},
        'Pink Bean': {'Normal': 1_404_500, 'Chaos': 12_800_000},
        'Magnus': {'Normal': 2_592_000, 'Chaos': 19_012_500},
        'Pierre': {'Normal': 968_000, 'Chaos': 16_200_000},
        'Von Bon': {'Normal': 968_000, 'Chaos': 16_200_000},
        'Crimson Queen': {'Normal': 968_000, 'Chaos': 16_200_000},
        'Vellum': {'Normal': 968_000, 'Chaos': 16_200_000},
        'Princess No': {'Normal': 0, 'Chaos': 16_200_000},
        'Lotus': {'Normal': 32_512_500, 'Chaos': 74_112_500},
        'Damien': {'Normal': 33_800_000, 'Chaos': 35_156_500},
        'Guardian Slime': {'Normal': 34_322_000, 'Chaos': 90_312_500},
        'Lucid': {'Normal': 40_612_500, 'Chaos': 80_000_000},
        'Will': {'Normal': 46_512_500, 'Chaos': 88_200_000},
        'Gloom': {'Normal': 49_612_500, 'Chaos': 92_450_000},
        'Versus Hilla': {'Normal': 89_520_000, 'Chaos': 110_450_000},
        'Darknell': {'Normal': 52_812_500, 'Chaos': 98_000_000},
        'Seren': {'Normal': 133_687_500, 'Chaos': 151_250_000},
    }

    holder = defaultdict(dict)

    reboot = True
    # k = key = Boss Name
    # v = values(Normal or Chaos)
    for k, v in bosses.items():
        if (reboot):
            holder[k] = Boss(k, v['Normal'] * 5, v['Chaos'] * 5)
        else:
            holder[k] = Boss(k, v['Normal'], v['Chaos'])

    print(holder['Lotus'])

#
# bosses = ['Zakum', 'Papulatus', 'Magnus', 'Hilla', 'Ranmaru', 'Pierre', 'Crimson Queen',
#           'Vellum', 'Horntail', 'Von Leon', 'Arkarium', 'Pink Bean', 'Cygnus', 'Princess No',
#           'Akechi', 'Lotus', 'Damien', 'Guardian Angel Slime', 'Lucid', 'Will', 'Gloom',
#           'Versus Hilla', 'Darknell']
#
# normalPrice = [612000, ]
