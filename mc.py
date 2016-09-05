#!/usr/bin/env python

import potentials
import random, math
import copy

class System(object):
    """An object for calculating 1D Monte Carlo trajectories."""

    def __init__(self, nparticles=2, spread=1.0, kT=0.5959):
        """Initialize the class.
        PARAMETERS
        nparticles  - the number of particles
        spread      - the width of Gaussian spread for initial particle positions (Angstroms).
        kT          - thermal energy (k_B times the temperature of the system), in kcal/mol."""

        self.nparticles = nparticles
        self.spread     = spread
        self.kT         = kT          # in kcal/mol

        self.positions  = []  # a list of 1D particle positions


        # set initial positions randomly
        for i in range(self.nparticles):
            self.positions.append( random.normalvariate(0.0, spread) )

        # make a list of (pointers to) energy functions that must be calculated
        self.energyFunctions = []
        self.energyFunctions.append( potentials.LJ )
        # self.energyFunctions.append( potentials.harmonic )

        self.energy = self.computeEnergy(self.positions) 

        # mc statistics
        self.attempted = 0.  # keep these floats, so we can divide to get acc. ratio 
        self.accepted  = 0.


    def computeEnergy(self, positions):
        """Returns the energy of the system."""

        energy = 0.0
        for fn in self.energyFunctions:
            for i in range(self.nparticles):
               for j in range(i+1, self.nparticles):  # this avoids double-counting
                   r = abs(positions[i] - positions[j])
                   energy += fn(r)
        return energy  

    def simulate(self, nsteps, dsigma=0.1, verbose=True):
        """Simulate nsteps of Monte Carlo dynamics, with a move set
        of random Gaussian perturbations of width dsigma.  Returns (energy, positions)."""

        for step in range(nsteps):

            accept = False 
            new_positions = copy.copy(self.positions)
  
            # perturb all particles' positions
            for i in range(self.nparticles):
                new_positions[i] = self.positions[i] + dsigma*random.normalvariate(0.0, dsigma) 
            new_energy = self.computeEnergy(new_positions)

            # accept according to the Metropolis Criterion 
            if new_energy < self.energy:
                accept = True
            elif random.random() < math.exp( -(new_energy - self.energy)/self.kT ):
                accept = True

            # process accepted moves
            if accept:
                self.energy = new_energy
                self.positions = new_positions
                self.accepted  += 1.0 
            self.attempted += 1.0

            # print status 
            if verbose:
                print "Accept: %d of %d"%(self.accepted, self.attempted), self
       
        return (self.energy, self.positions) 


    def __repr__(self):
        """Returns a string representation of the class."""

        outstring = "Energy: %3.6f "%self.energy 
        outstring += "Positions:"
        for i in range(self.nparticles):
            outstring += " %3.6f"%self.positions[i]
        return outstring 
          

### Main ###

if __name__ == "__main__":

    import sys

    usage = """Usage: python run_mc.py NPARTICLES NITERATIONS 
        Performs NITERATIONS of Monte Carlo for a 1D system with NPARTICLES."""

    if len(sys.argv) < 3:
        print usage
        sys.exit(1)

    N = int(sys.argv[1])      # the number of particles
    niters = int(sys.argv[2]) # the number of iterations

    UseMatplotlib = True
    try:
        import matplotlib
        import pylab
    except:
        UseMatplotlib = False

    # import mc


    # s = mc.System(nparticles=N)
    s = System(nparticles=N)

    steps_per_iter = 1
    energies =  []
    trajectories = [ [] for p in range(N)]
    for t in range(niters):
        e, c = s.simulate(steps_per_iter, verbose=False)
        energies.append(e)
        for i in range(N):
            trajectories[i].append(c[i])

    # print the trajectories
    print '#iteration\tE\tpositions'
    for t in range(niters):
        print t, energies[t],
        for i in range(N):
           print trajectories[i][t], 
        print 

    if UseMatplotlib:
        # plot the trajectories
        pylab.figure()
        for i in range(N):
            pylab.plot(range(niters), trajectories[i])
            pylab.hold(True)
        pylab.show()
        
