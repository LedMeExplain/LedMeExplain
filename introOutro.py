from manim import *

LME_color = "#27a0b3"

class Intro(Scene):
    def construct(self):

        ##------------------------------
        ## Animación de LED Me Explain
        ##------------------------------
        brandInit = Text(
            "LME",
            fill_opacity = 1,
            color = LME_color,
            font = "Arial Rounded MT Bold"
        )

        brandEnd = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        )

        # Añade las siglas LME
        self.add(brandInit)
        self.wait() #Espera un momento
        # Mueve las siglas al inicio de cada palabra
        self.play(
            ApplyMethod(brandInit[0].move_to, brandEnd[0]),
            ApplyMethod(brandInit[1].move_to, brandEnd[3]),
            ApplyMethod(brandInit[2].move_to, brandEnd[5]),
            run_time = 0.7
        )
        # Aparece el nombre completo
        self.play(FadeIn(brandEnd))
        # Remuever las siglas
        self.remove(brandInit)
        self.wait(0.5) #Espera un momento
        # Mueve el nombre hacia la esquina inf-der y hacerlo pequeño
        def brandToMiniature(mobject):
            mobject.scale(0.4)
            mobject.to_edge(DR)
            mobject.set_opacity(0.5)
            return mobject
        self.play(ApplyFunction(brandToMiniature,brandEnd))

        ##---------------------------------
        ##---------------------------------

        self.wait()

class Outro(Scene):
    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## Animación Final
        ##------------------------------

        def brandToCenter(mobject):
            mobject.scale(2.5)
            mobject.move_to(ORIGIN)
            mobject.set_opacity(1)
            return mobject

        createdWith = Text('Creado con:').shift(UP*1).scale(0.7)
        manimBrand = ManimBanner().scale(0.3).next_to(createdWith,DOWN*2)

        self.play(ApplyFunction(brandToCenter,brand))
        self.wait(1.5)
        self.play(
            FadeOut(brand, shift = UP*2),
            FadeIn(createdWith, shift = UP*2)
        )
        self.wait()
        self.play(manimBrand.create())
        self.play(manimBrand.expand())

        ##---------------------------------
        ##---------------------------------

        self.wait()
