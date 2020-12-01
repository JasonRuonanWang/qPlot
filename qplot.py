import matplotlib


def plot(d, t="default"):
    l = 0
    for p in d:
        l = len(p)
        break

    probabilities = []
    binaries = []
    decimals = []
    shots = 0

    for i in range(2**l):
        b = format(i,"0{0}b".format(l))
        v = d.get(b)
        if v == None:
            probabilities.append(0)
        else:
            probabilities.append(v)
            shots = shots + v
        binaries.append(b)
        decimals.append(i)

    title = "Probability distribution of {0} shots".format(shots)
    title = title + "\n" + t
    matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(decimals, probabilities)
    matplotlib.pyplot.xticks(decimals, binaries, rotation='vertical', fontsize=1.5)
    matplotlib.pyplot.title(title)
    matplotlib.pyplot.savefig("{0}.pdf".format(t))




