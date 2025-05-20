class Counter :
    count = 0

    @classmethod
    def diplay_obj(cls,value):
        cls.count +=value
        print(f"total no. of objects created {cls.count}")
counter = Counter()

counter.diplay_obj(1)
counter1 = Counter()
counter1.diplay_obj(1)
