import random

class Component():
    def __init__(this, ID, size, randomPreferences):
        this.preferences = []
        this.id = ID
        this.matched = False
        this.matchedWith = -1
        if randomPreferences:
            this.setRandomPreferences(size)
    def setRandomPreferences(this, size):
        this.preferences = list(range(size))
        random.shuffle(this.preferences)
    def __repr__(this):
        return str(this.id)
    def display(this):
        return str(this.id) + " - " + "-".join(list(map(str, this.preferences)))

class Doctor(Component):
    def __init__(this, ID, size, randomPreferences):
        super().__init__(ID, size, randomPreferences)
    def __repr__(this):
        return "d_" + super().__repr__()
    def display(this):
        return "d_" + super().display()

class Hospital(Component):
    def __init__(this, ID, size, randomPreferences):
        super().__init__(ID, size, randomPreferences)
    def __repr__(this):
        return "h_" + super().__repr__()
    def display(this):
        return "h_" + super().display()

class StableMatching:
    def __init__(this, size):
        this.doctors = []
        this.hospitals = []
        this.size = size
        for i in range(size):
            d_i = Doctor(i, size, True)
            this.doctors.append(d_i)
            h_i = Hospital(i, size, True)
            this.hospitals.append(h_i)

    def __repr__(this):
        x = "Doctors:\n"
        for doctor in this.doctors:
            x += "  " + doctor.display() + "\n"
        x += "Hospitals:\n"
        for hospital in this.hospitals:
            x += "  " + hospital.display() + "\n"
        if this.Matching:
            print(this.Matching)
        return x


    def GaleShapley(this):
        M = []
        P = []
        HospitalOfferCount = [0] * this.size
        times = 0
        while not all(list(map(lambda i : i.matched, x.hospitals))):
            hIndex = list(map(lambda i : i.matched, x.hospitals)).index(False)
            offersMade = HospitalOfferCount[hIndex]
            if (offersMade == this.size):
                print("Hospital left alone")
                break
            h = this.hospitals[hIndex]
            dIndex = h.preferences[offersMade]
            d = this.doctors[dIndex]
            HospitalOfferCount[hIndex] += 1
            P.append("h_" + str(hIndex) + " offers to d_" + str(dIndex))
            if not d.matched:
                P.append("Matching h_" + str(hIndex) + " and d_" + str(dIndex))
                M.append([d, h])
                d.matched = True
                d.matchedWith = hIndex
                h.matched = True
                h.matchedWith = dIndex
            else:
                if d.preferences.index(hIndex) < d.preferences.index(d.matchedWith):
                    P.append("Removing h_" + str(d.matchedWith) + " from d_" + str(dIndex))
                    M.remove([d, this.hospitals[d.matchedWith]])
                    this.hospitals[d.matchedWith].matched = False
                    this.hospitals[d.matchedWith].matchedWith = -1
                    P.append("Matching h_" + str(hIndex) + " to d_" + str(dIndex))
                    M.append([d, h])
                    d.matchedWith = hIndex
                    h.matched = True
                    h.matchedWith = dIndex

        this.Matching = M
        this.Progression = P


x = StableMatching(3)
print(x)
x.GaleShapley()



                
