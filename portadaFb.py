
from manim import *
import random

LME_color = "#27a0b3"
#config["background_color"] = '#4C5454'#'#C7E4F0'

class portadaFb(Scene):
    def construct(self):

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(1.5)

        eq_array = [
            r'x = \frac {-b \pm \sqrt {b^2 - 4ac}}{2a}',
            r'a x^3 + b x^2 + c x + d = 0',
            r'\lim_{x \to \infty} \left( \frac{1}{x} \right)',
            r'\hat H \left| \psi \right> = - \hbar \frac{\mathrm{d}}{\mathrm{d}t} \left| \psi \right>',
            r'\vec{p}=m\vec{v}',
            r'\mathrm{e}^x = \sum_{n=0}^\infty \frac{x^n}{n!}',
            r'\sin(\omega t + \phi_0)',
            r'R_{\mu\nu} - \frac12 g_{\mu\nu} R = \kappa T_{\mu\nu}',
            r'\vec{L}=\vec {r}\times\vec{p}'
        ]

        random.shuffle(eq_array)
        eq_array[4] = ''

        eq_group = Group()

        for eq in eq_array:
            eq_temp = MathTex(eq)
            eq_temp.scale(np.random.rand()*0.5+.4)
            eq_temp.rotate((np.random.randint(50)-25)*DEGREES)
            eq_temp.set_opacity(np.random.rand()*.4+.2)
            eq_group.add(eq_temp)

        eq_group.arrange_in_grid(rows=3,buff = (2.5,.6))

        for eq in eq_group:
            eq.shift([np.random.rand()*1.5-0.75,np.random.rand()*.5-0.25,0])

        self.add(eq_group)
        self.add(brand)
