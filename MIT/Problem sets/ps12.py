# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab
import copy

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).
        """
        # TODO
        if not 0<=maxBirthProb<=1:
            raise ValueError
        if not 0<=clearProb<=1:
            raise ValueError
        else:
            self.maxBirthProb=maxBirthProb
            self.clearProb=clearProb

    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step.

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        # TODO
        potential=random.random()
        if potential<=self.clearProb:
            return True
        return False


    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        # TODO
        self.popDensity=popDensity
        PowerOfReproduction=random.random()
        if PowerOfReproduction<=(self.maxBirthProb*(1-popDensity)):
            offspring=SimpleVirus(self.maxBirthProb, self.clearProb)
#            print("offspring is", offspring)
            return offspring
        else:
            raise NoChildException()
            pass


class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses=viruses
        self.maxPop=maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population.

        returns: The total virus population (an integer)
        """
        # TODO
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        VirusesAfterUpdate=self.viruses
#        print("Viruses before", self.viruses)
        for virus in self.viruses:
            if virus.doesClear():
#                print("Virus cleared")
                VirusesAfterUpdate.remove(virus)

            else:
                try:
                    VirusesAfterUpdate.append(virus.reproduce(self.getTotalPop()/self.maxPop))
                    virus.popDensity=self.getTotalPop()/self.maxPop
#                    print("The virus mutated", self.viruses)
                except NoChildException:
#                    print("The virus did not mutate")
                    pass



        self.viruses=VirusesAfterUpdate
#        print("These two should be identical")
#        print(self.viruses, "AND", VirusesAfterUpdate)
#        print("Viruses after", self.viruses)
        return self.getTotalPop()

Flu=SimpleVirus(0.5, 0.5)
print(Flu.doesClear())
#Flu.reproduce(0.1)
#JohnDoe=SimplePatient([Flu, Flu], 10)
#JohnDoe.update()
#
# PROBLEM 2
#
def createViruses(numViruses, maxBirthProb, clearProb, virusType, resistances):
    VIRUSES=[]
    for i in range(numViruses):
        if virusType==SimpleVirus:
            VIRUSES.append(SimpleVirus(maxBirthProb, clearProb))
        if virusType==ResistantVirus:
            VIRUSES.append(ResistantVirus(maxBirthProb, clearProb, resistances, 0.005))
#    print(VIRUSES)
#    print(len(VIRUSES))
    return VIRUSES



def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.
    """
    # TODO
    runtime=0
    SimTime=300
    VirusesAtTime=[]
    runtimelist=[]
    sickness=createViruses(100, 0.1, 0.05, SimpleVirus)
    JaneDoe=SimplePatient(sickness, 1000)
    while runtime<=SimTime:
        runtimelist.append(runtime)
        JaneDoe.update()
        print("viruses at time: ", runtime, JaneDoe.getTotalPop())
        runtime+=1
        VirusesAtTime.append(JaneDoe.getTotalPop())

    pylab.ylabel("Viruses in Jane Doe")
    pylab.xlabel("Time")
    pylab.plot(runtimelist, VirusesAtTime)
    pylab.show()

#problem2()


#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        # TODO
        self.maxBirthProb=maxBirthProb
        self.clearProb=clearProb
        self.resistances=resistances
        self.mutProb=mutProb


    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # TODO
#        print("drug", drug, "self.resistances[drug]", self.resistances[drug])
#        print("self.resistances", self.resistances)
        return self.resistances.get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        # TODO
        self.popDensity=popDensity
        self.activeDrugs=activeDrugs
        undefeatedDrugs=0
        newResistances=copy.deepcopy(self.resistances)
        fightingresistances=copy.deepcopy(self.resistances)
        for i in self.activeDrugs:
#            print("i", i)
#            print("self.resistances(grimpex)", self.getResistance("grimpex"))
#            print("Self.resistances[i]", self.getResistance(str(i)))
            if i not in self.resistances:
                undefeatedDrugs+=1
#                print("Marker 1")
            else:
                if self.getResistance(i)==False:
#                    print("Marker 2")
                    fightingresistances.pop(i)
                    undefeatedDrugs+=1
                    self.activeDrugs={}
                    if self.activeDrugs=={}:
                        raise NoChildException


        PowerOfReproduction=random.random()
#        print("PowerOfReproduction", PowerOfReproduction, "(self.maxBirthProb*(1-popDensity))", self.maxBirthProb*(1-popDensity))
        if PowerOfReproduction<=(self.maxBirthProb*(1-popDensity)):
            for resistance in self.resistances:
                if random.random()<=(1-self.mutProb):
                    newResistances[resistance]=self.resistances[resistance]
                else:
                    newResistances[resistance]= not self.resistances[resistance]
            offspring=ResistantVirus(self.maxBirthProb, self.clearProb, newResistances, self.mutProb)
#            print("offspring is", offspring)
            return offspring
        else:
            raise NoChildException()
            pass

Tuberculosis=ResistantVirus(0.1, 0.005, {"guttagonol":False, "grimpex":True}, 0.5)
#Tuberculosis.getResistance("guttagonol")
#Tuberculosis.reproduce(0.1, ["grimpex", "guttagonol"])

class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses=viruses
        self.maxPop=maxPop
        currentPrescription=[]
        self.currentPrescription=currentPrescription

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        self.currentPrescription.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO
        return self.currentPrescription

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        strongviruses=0
        for virus in self.viruses:
            Drugsresisted=0
            for drug in drugResist:
                if virus.getResistance(drug):
                    Drugsresisted+=1
            if Drugsresisted==len(drugResist):
    #            print("Drugsresisted", Drugsresisted, "len(drugResist)", len(drugResist))
                strongviruses+=1
#                print("Drugsresisted==len(drugResist)", Drugsresisted, len(drugResist), Drugsresisted==len(drugResist))
#        print("strongviruses", strongviruses)

        return strongviruses




    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        VirusesAfterUpdate=self.viruses
#        print("Viruses before", self.viruses)
        prescriptions=self.getPrescriptions()
        for virus in self.viruses:
            if virus.doesClear():
#                print("Virus cleared")
                VirusesAfterUpdate.remove(virus)

            else:
                try:
                    VirusesAfterUpdate.append(virus.reproduce((self.getTotalPop()/self.maxPop), prescriptions))
                    virus.popDensity=self.getTotalPop()/self.maxPop
#                    print("The virus mutated")
                except NoChildException:
#                    print("The virus did not mutate")
                    pass



        self.viruses=VirusesAfterUpdate
#        print("These two should be identical")
#        print(self.viruses, "AND", VirusesAfterUpdate)
#        print("Viruses after", self.viruses)
#        print("Total viruses", self.getTotalPop())
        return self.getTotalPop()


Charlie=Patient(createViruses(100, 0.1, 0.05, ResistantVirus, {"guttagonol" : False}), 1000)
#Charlie.addPrescription("guttagonol")
#Charlie.addPrescription("grimpex")
#print(Charlie.getPrescriptions())
#Charlie.update()

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    runtime=0
    midpoint=150
    endpoint=300
    VirusesAtTime=[]
    runtimelist=[]
    guttag=[]
    sickness=createViruses(100, 0.1, 0.05, ResistantVirus, {"guttagonol" : False})
    Charlie=Patient(sickness, 1000)
    while runtime<=midpoint:
        runtimelist.append(runtime)
        guttag.append(Charlie.getResistPop(["guttagonol"]))
        Charlie.update()
        print("viruses at time: ", runtime, Charlie.getTotalPop())
        runtime+=1
        VirusesAtTime.append(Charlie.getTotalPop())

    Charlie.addPrescription("guttagonol")

    while runtime<=endpoint:
        runtimelist.append(runtime)
        guttag.append(Charlie.getResistPop(["guttagonol"]))
        Charlie.update()
        print("viruses at time: ", runtime, Charlie.getTotalPop())
        runtime+=1
        VirusesAtTime.append(Charlie.getTotalPop())

    print("guttag", Charlie.getResistPop(["guttagonol"]))


    pylab.ylabel("Viruses in Charlie")
    pylab.xlabel("Time")
    pylab.plot(VirusesAtTime, label="Total")
    pylab.plot(guttag, label="guttagonol-resistant viruses")
    pylab.legend(loc=2)
    pylab.show()

#problem4()

#
# PROBLEM 5
#

def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
    """
    # TODO
    midpoints=[300, 150, 75, 0]
    endpoint=0
    VirusesAtTime=[]
    runtimelist=[]
    guttag=[]
    sickness=createViruses(100, 0.1, 0.05, ResistantVirus, {"guttagonol" : False})
    TestPatient=Patient(sickness, 1000)
    numCharlies=200

    for i in midpoints:
        print("i", i)
        VirusesAtTime=[]
        CuredCharlies=0
        for Charlies in range(numCharlies):
            Charlie=copy.deepcopy(TestPatient)
            print("Charlies", (Charlies+1))
#            print("FIRST Charlie.getTotalPop", Charlie.getTotalPop())
            runtime=0
            while runtime<=i:
                runtimelist.append(runtime)
                guttag.append(Charlie.getResistPop(["guttagonol"]))
                Charlie.update()
#                print("viruses at time: ", runtime, Charlie.getTotalPop())
                runtime+=1
#                print("i", i, "Charlies", Charlies, "runtime", runtime)
#                VirusesAtTime.append(Charlie.getTotalPop())

            Charlie.addPrescription("guttagonol")
            endpoint=i+150
            while runtime<=endpoint:
                runtimelist.append(runtime)
                guttag.append(Charlie.getResistPop(["guttagonol"]))
                Charlie.update()
#                print("viruses at time: ", runtime, Charlie.getTotalPop())
                runtime+=1
            VirusesAtTime.append(Charlie.getTotalPop())
#                print(VirusesAtTime)
#                print("Charlie.getTotalPop()", Charlie.getTotalPop())
            if Charlie.getTotalPop()<=50:
                CuredCharlies+=1
#            print(VirusesAtTime)

#           print("guttag", Charlie.getResistPop(["guttagonol"]))
        pylab.figure()
        print("CuredCharlies", CuredCharlies)
        pylab.title("Histogram when guttagonol is administered at time: " + str(i))
        pylab.ylabel("No. of Charlies")
        pylab.xlabel("Viruses in Charlie" + str(100 * ( float( CuredCharlies ) / float( numCharlies ))) + "% cured.")
        pylab.hist(VirusesAtTime, label="Total")
#        pylab.hist(guttag, label="guttagonol-resistant viruses")
        pylab.legend(loc=2)
        print("Time done", i, "!")

    pylab.show()

#problem5()
#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO
    sickness=createViruses(100, 0.1, 0.05, ResistantVirus, {"guttagonol" : False, "grimpex" : False})
    PatientPaul=Patient(sickness, 1000)
    firstSprint=150
    midpoints=[300+firstSprint, 150+firstSprint, 75+firstSprint, 0+firstSprint]
    endpoint=0
    VirusesAtTime=[]
    runtimelist=[]
    numPauls=30

    for i in midpoints:
        print("i", i)
        VirusesAtTime=[]
        CuredPauls=0
        guttag=[]
        grimpex=[]
        gutgrim=[]
        for Pauls in range(numPauls):
            Paul=copy.deepcopy(PatientPaul)
            print("Pauls", (Pauls+1))
            runtime=0
            while runtime<=firstSprint:
                if i==0:
                    break
                runtimelist.append(runtime)
                Paul.update()
                runtime+=1
            Paul.addPrescription("guttagonol")
            while runtime<=i:
                if i==0:
                    break
                runtimelist.append(runtime)
                Paul.update()
                runtime+=1
            Paul.addPrescription("grimpex")
            endpoint=i+150
            while runtime<=endpoint:
                runtimelist.append(runtime)
                runtime+=1
                Paul.update()
                guttag.append(Paul.getResistPop(["guttagonol"]))
                grimpex.append(Paul.getResistPop(["grimpex"]))
                gutgrim.append(Paul.getResistPop(["guttagonol", "grimpex"]))
#            print("guttag", guttag[-1])
#            print("grimpex", grimpex[-1])
#            print("gutgrim", gutgrim[-1])

#            print("Paul no. ", (Pauls+1), "have viruses with the following resistances")
#            print("Resistant to guttagonol", guttag[Pauls], Paul.getResistPop(["guttagonol"]))
#            print("Resistant to grimpex", grimpex[Pauls], Paul.getResistPop(["grimpex"]))
#            print("Resistant to both", gutgrim[Pauls], Paul.getResistPop(["guttagonol", "grimpex"]))
            VirusesAtTime.append(Paul.getTotalPop())
            print("TotalViruses", VirusesAtTime)
            if Paul.getTotalPop()<=50:
                CuredPauls+=1

        pylab.figure()
        print("CuredPauls", CuredPauls)
        pylab.title("Histogram when guttagonol is administered at time: " + str(firstSprint) + "and grimpex at time: " + str(i))
        pylab.ylabel("No. of Pauls")
        pylab.xlabel("Viruses in Paul " + str(100 * ( float( CuredPauls ) / float( numPauls ))) + "% cured.")
        pylab.hist(VirusesAtTime, label="Total")
#        pylab.hist(guttag, label="guttagonol-resistant viruses")
        pylab.legend(loc=2)
        print("Time done", i, "!")
    pylab.show()



#problem6()

#
# PROBLEM 7
#

def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.
    """
    # TODO
    sickness=createViruses(100, 0.1, 0.05, ResistantVirus, {"guttagonol" : False, "grimpex" : False})
    RyanPatient=Patient(sickness, 1000)
    Simulations=[1,2]
    numRyans=1
    for simulation in Simulations:
        VirusesAtTime=[]
        CuredRyans=0
        guttag=[]
        grimpex=[]
        gutgrim=[]
        runtimelist=[]
        runtime=0
        if simulation==1:
            for Ryans in range(numRyans):
                Ryan=copy.deepcopy(RyanPatient)
                while runtime<=150:
                    runtimelist.append(runtime)
                    Ryan.update()
                    runtime+=1
                    guttag.append(Ryan.getResistPop(["guttagonol"]))
                    grimpex.append(Ryan.getResistPop(["grimpex"]))
                    gutgrim.append(Ryan.getResistPop(["guttagonol", "grimpex"]))
                    VirusesAtTime.append(Ryan.getTotalPop())
                Ryan.addPrescription("guttagonol")
                while runtime<=450:
                    runtimelist.append(runtime)
                    Ryan.update()
                    runtime+=1
                    guttag.append(Ryan.getResistPop(["guttagonol"]))
                    grimpex.append(Ryan.getResistPop(["grimpex"]))
                    gutgrim.append(Ryan.getResistPop(["guttagonol", "grimpex"]))
                    VirusesAtTime.append(Ryan.getTotalPop())
                Ryan.addPrescription("grimpex")
                while runtime<=600:
                    runtimelist.append(runtime)
                    Ryan.update()
                    runtime+=1
                    guttag.append(Ryan.getResistPop(["guttagonol"]))
                    grimpex.append(Ryan.getResistPop(["grimpex"]))
                    gutgrim.append(Ryan.getResistPop(["guttagonol", "grimpex"]))
                    VirusesAtTime.append(Ryan.getTotalPop())
#            print("guttag", guttag)
#            print("grimpex", grimpex)
#            print("gutgrim", gutgrim)
#            print("VirusesAtTime", VirusesAtTime)
            pylab.figure()
            pylab.title("Histogram when guttagonol is administered at time: 150 and grimpex at time: 450")
            pylab.ylabel("Viruses in Ryan")
            pylab.xlabel("Time")
            pylab.plot(runtimelist, VirusesAtTime, label="Total")
            pylab.plot(guttag, label="guttagonol-resistant viruses")
            pylab.plot(grimpex, label="grimpex-resistant viruses")
            pylab.plot(gutgrim, label="gutgrim-resistant viruses")
            pylab.legend(loc=2)
        if simulation==2:
            for Ryans in range(numRyans):
                Ryan=copy.deepcopy(RyanPatient)
                while runtime<=150:
                    runtimelist.append(runtime)
                    Ryan.update()
                    runtime+=1
                    guttag.append(Ryan.getResistPop(["guttagonol"]))
                    grimpex.append(Ryan.getResistPop(["grimpex"]))
                    gutgrim.append(Ryan.getResistPop(["guttagonol", "grimpex"]))
                    VirusesAtTime.append(Ryan.getTotalPop())
                Ryan.addPrescription("guttagonol")
                Ryan.addPrescription("grimpex")
                while runtime<=300:
                    runtimelist.append(runtime)
                    Ryan.update()
                    runtime+=1
                    guttag.append(Ryan.getResistPop(["guttagonol"]))
                    grimpex.append(Ryan.getResistPop(["grimpex"]))
                    gutgrim.append(Ryan.getResistPop(["guttagonol", "grimpex"]))
                    VirusesAtTime.append(Ryan.getTotalPop())
#            print("guttag", guttag)
#            print("grimpex", grimpex)
#            print("gutgrim", gutgrim)
#            print("VirusesAtTime", VirusesAtTime)
            pylab.figure()
            pylab.title("Histogram when guttagonol and grimpex are administered at time: 150")
            pylab.ylabel("Viruses in Ryan")
            pylab.xlabel("Time")
            pylab.plot(runtimelist, VirusesAtTime, label="Total")
            pylab.plot(guttag, label="guttagonol-resistant viruses")
            pylab.plot(grimpex, label="grimpex-resistant viruses")
            pylab.plot(gutgrim, label="gutgrim-resistant viruses")
            pylab.legend(loc=2)
    pylab.show()

problem7()
