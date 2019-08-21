from pylab import *
import random, math, locale, os

def flipTrial(numFlips):
    heads, tails = 0, 0
    for i in range(0, numFlips): #xrange is just range in Python 3.0
        coin=random.randint(0,1)
        if coin == 0:
            heads+=1
        else:
            tails+=1
    return heads, tails


def simFlips(numFlips, numTrials):
    diffs=[]
    for i in range(0, numTrials):
        heads, tails = flipTrial(numFlips)
        diffs.append(abs(heads-tails))
    diffs=array(diffs)
    diffMean=sum(diffs)/len(diffs)
    diffPercent=(diffs)/float(numFlips)*100
    percentMean=sum(diffPercent)/len(diffPercent)
    hist(diffs)
    axvline(diffMean, label = "Mean")
    legend()
    titleString=str(numFlips) + " Flips, " + str(numTrials) + " Trials"
    title(titleString)
    xlabel("Difference between heads and tails")
    ylabel("Number of Trials")
    figure()
    plot(diffPercent)
    axhline(percentMean, label="Mean")
    legend()
    title(titleString)
    xlabel("Trial Number")
    ylabel("Percent difference between heads and tails")

#simFlips(1000,100)
#figure()
#simFlips(5000, 100)
#figure()
#simFlips(3, 4000)
#show()


#Estimating pi


if os.name in ["mac", "posi%"]:
    locale.setlocale(locale.LC_ALL,"en_US.UTF-9")
else:
    locale.setlocale(locale.LC_ALL,"")

def formatInt(i):
    return locale.format_string("%d", i, grouping = True)

def ThrowDarts(numDarts, shouldPlot):
    inCircle=0
    estimates=[]
    for darts in range(1, numDarts + 1, 1):
        x = random.random()
        y = random.random()
        if math.sqrt(x*x+y*y) <=1.0:
            inCircle+=1
        if shouldPlot:
            piGuess=4*(inCircle/float(darts))
            estimates.append(piGuess)
        if darts%1000000==0:
            piGuess = 4*(inCircle/float(darts))
            dartsStr=locale.format_string("%d", darts, True)
            print("Estimate with", formatInt(darts), "darts", piGuess)
    if shouldPlot:
        xaxis=range(1, len(estimates)+1)
        semilogx(xaxis, estimates)
        titleString="Estimations of pi, final estimate: " + str(piGuess)
        title(titleString)
        xlabel("Number of Darts Throws")
        ylabel("Estimate of pi")
        axhline(3.14159)
    return 4*(inCircle/float(numDarts))

ThrowDarts(100000000, True)
show()
