from random import choice


class Human(object):
    def __init__(self, name, birthyear, birthplace, mother, father):
        self.name = name
        self.birthyear = birthyear
        self.birthplace = birthplace
        self.mother = mother
        self.father = father

    def age(self, currentyear):
        return currentyear - self.birthyear

    def get_name(self):
        return self.name


class Woman(Human):
    def __init__(self, name="Eva", birthyear=0, birthplace="God's Garden of Eden", mother="Not Found", father="God",
                 hairlenght=0, breastsize=0):
        super(Woman, self).__init__( name, birthyear, birthplace, mother, father)
        self.hairlenght = hairlenght
        self.breastsize = breastsize

    def age(self, currentyear):
        age = super(Woman, self).age(currentyear)
        if age > 18:
            raise Exception("That's really bad question.. ")
        return age


class Man(Human):
    def __init__(self, name="Adam", birthyear=0, birthplace="God's Garden of Eden", mother="Not Found", father="God",
                 recordinrun=0, recordonbench=0):
        super(Man, self).__init__(name, birthyear, birthplace, mother, father)
        self.recordinrun = recordinrun
        self.recordonbench = recordonbench

    def bench(self):
        if self.recordonbench < 10:
            return 120
        return self.recordonbench


def createfirsth():
    return Man(), Woman()


def names(humans):
    names = []
    for human in humans:
        names.append(human.get_name())
    return tuple(names)


def birthofchild(parents, nameforfemale, nameformale, birthyear, birthplace):
    if len(parents) != 2:
        raise Exception("Wowow, wait! Only 2 parents are allowed")

    if isinstance(parents[0], Man) and isinstance(parents[1], Woman):
        father, mother = parents[0], parents[1]

    elif isinstance(parents[1], Man) and isinstance(parents[0], Woman):
        father, mother = parents[0], parents[1]

    else:
        raise Exception("Bad combination of parents")

    gender = choice(("male", "female"))
    if gender == "male":
        return Man(name=nameformale, birthyear=birthyear, birthplace=birthplace, mother=mother.get_name(), father=father.get_name())
    return Woman(name=nameforfemale, birthyear=birthyear, birthplace=birthplace, mother=mother.get_name(), father=father.get_name())


def main():
    print("Start 5. task")
    humans = createfirsth()
    print("Names of the first humans are.. {0} ".format(", ".join(names(humans))))
    child = birthofchild(humans, "Alex", 256, "Olomouc")
    print(child.get_name())


if __name__ == "__main__":
    main()
