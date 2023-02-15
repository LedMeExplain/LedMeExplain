import numpy as np

# import scipy as sp
# from scipy.integrate import quad

class SerieComplejaFourier:
    def __init__(self, f, k = 25):
        self.f = f
        self.t = np.linspace(0.0,1.0, num = len(f))
        self.k = k
        # Periodo
        self.T0 = (self.t[-1]-self.t[0])
        # Velocidad angular
        self.w0 = 2*np.pi/self.T0

    def c(self, k):
        # Función a integrar
        fc = self.f*np.exp(-1j*k*self.w0*self.t)*(self.T0/self.f.size)
        # Integral
        int_fc = 1/self.T0*fc.sum()
        return int_fc

    def SerieFourierArray(self, x):
        assert (x >= self.t[0] and x <= self.t[-1]), "El valor para x está fuera de los límites ("+str(self.t[0])+","+str(self.t[-1])+")."
        serieFourier = np.array([self.c(k)*np.exp(1j*k*self.w0*x) for k in range(-1*self.k,self.k+1)])
        return serieFourier

    def SerieFourier(self, x):
        return self.SerieFourierArray(x).sum()




    # ####################################################################
    # ## Integración compleja usando la función quad de scipy.integrate ##
    # ## Creditos a dr jimbob https://stackoverflow.com/a/5966088       ##
    # ####################################################################
    # def complex_quad(self, f = self.f, a = self.periodo[0], b = self.periodo[1], **kwargs):
    #     def f_Re(t):
    #         return scipy.real(self.f(t))
    #     def f_Im(t):
    #         return scipy.imag(self.f(t))
    #     intregal_Re = quad(f_Re, a, b, **kwargs)
    #     intregal_Im = quad(f_Im, a, b, **kwargs)
    #     return (intregal_Re[0] + 1j*intregal_Im[0], integral_Re[1:], integral_Im[1:])
    #         # (resultado, error_real, error_imaginario)
    # #####################################################################

    # def c(k):
    #     T0 = self.periodo[1]-self.periodo[0]
    #     w0 = 2*sp.pi/T0
    #     def fck(t):
    #         return self.f(t)*sp.exp(-1j*k*w0*t)
    #     ck = 1/T0*
