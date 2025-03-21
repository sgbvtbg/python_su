# coding: utf-8
import matplotlib.pyplot as plt
from astropy import unites as u
from astropy import units as u
plt.ion()
b=[23,45,88]*u.second
c=[3,7,10]*u.second
plt.plot(b,c,'og'.ls='')
plt.plot(b,c,'og', ls='')
plt.figure()
plt.plot(b,c,'og', ls='')
plt.xlabels('seconds')
plt.xlabel('seconds')
plt.ylabel('distance')
plt.savefig('test.png')
print "done"
print ("done")
