import numpy


class Data:
    x = []
    
    def __init__(this, x):
        this.x = x[::]
        
    def count(this):
        return len(this.x)

    def sum(this):
        return sum(this.x)
    
    def moment(this, k):
        s = 0
        for i in this.x:
            s += i ** k
        s /= this.count()
        return s
    
    def mean(this):
        return this.moment(1)
    
    def var(this):
        s = 0
        mx = this.mean()
        for i in this.x:
            s += (i - mx) ** 2
        s /= this.count()
        return s
        
    def std(this):
        return this.var() ** 0.5
    
    def percentile(this, p):
        p = p * 100
        return numpy.percentile(this.x, p)
    
    def median(this):
        return this.percentile(1/2)
    
    def __str__(this):
        s = ""
        s += "Count: {}\n".format(this.count())
        s += "Mean: {}\n".format(this.mean())
        s += "Variance: {}\n".format(this.var())
        s += "Standard deviation: {}\n".format(this.std())
        s += "2nd moment: {}\n".format(this.moment(2))
        s += "3rd moment: {}\n".format(this.moment(3))
        s += "4th moment: {}\n".format(this.moment(4))
        s += "Median: {}\n".format(this.median())
        s += "25% quantile: {}\n".format(this.percentile(0.25))
        s += "75% quantile: {}\n".format(this.percentile(0.75))
        return s


if __name__ == "__main__":
    print("Sample Data object:")
    x = Data([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    print(x)