CAT_AVATAR_LEVEL_HAPPINESS_GT_60 = '/img/cat1.jpeg'
CAT_AVATAR_LEVEL_HAPPINESS_GT_30_OR_LT_60 = '/img/cat2.jpeg'
CAT_AVATAR_LEVEL_HAPPINESS_LT_30 = '/img/cat3.jpeg'


class Cat:
    name = ''
    age = 1
    is_sleeping = False
    satiety = 40
    happiness = 40
    avatar = CAT_AVATAR_LEVEL_HAPPINESS_GT_30_OR_LT_60

    @classmethod
    def changing_avatar(cls):
        if cls.happiness >= 60:
            cls.avatar = CAT_AVATAR_LEVEL_HAPPINESS_GT_60
        elif 60 > cls.happiness >= 30:
            cls.avatar = CAT_AVATAR_LEVEL_HAPPINESS_GT_30_OR_LT_60
        else:
            cls.avatar = CAT_AVATAR_LEVEL_HAPPINESS_LT_30

    @classmethod
    def play(cls):
        cls.happiness += 15
        cls.satiety -= 10

        cls.changing_avatar()
