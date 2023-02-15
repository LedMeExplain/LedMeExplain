from manim import *
import numpy as np

quality_factor = 1
fps = 30


class SerieComplejaFourier:
    def __init__(self, f, k = 25):
        self.f = f
        self.t = np.linspace(0.0,1.0, num = len(f))
        self.k = k
        # Periodo
        self.T0 = 1
        # Velocidad angular
        self.w0 = 2*np.pi/self.T0

    def c(self, k):
        # Función a integrar
        fc = self.f*np.exp(-1j*k*self.w0*self.t)*(self.T0/self.f.size)
        # Integral
        int_fc = 1/self.T0*fc.sum()
        return int_fc

    def SerieFourierArray(self, x):
        serieFourier = np.array([SerieFourier(x,n) for n in range(-1*self.k,self.k+1)])
        return serieFourier

    def SerieFourier(self, x, n):
        assert (x >= self.t[0] and x <= self.t[-1]), "El valor para x está fuera de los límites ("+str(self.t[0])+","+str(self.t[-1])+")."
        return self.c(n)*np.exp(1j*n*self.w0*x)

    def SerieFourierSumN(self,x,terms):
        array_k = list(range(-1*self.k, self.k+1, 1))
        array_k.sort(key=abs)

        return np.array([self.SerieFourier(x,array_k[i]) for i in range(terms)]).sum()

    def SerieFourierSum(self, x):
        return self.SerieFourierArray(x).sum()

class serieFourierUpiitaFB(Scene):
    r_time = 10
    n_points = 1000
    k = 8
    t_tracker = ValueTracker(0)

    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR).set_z_index(2)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## 1. Título, enunciado y animación del problema
        ##------------------------------
        header = Title(r'Serie Compleja de Fourier', match_underline_width_to_text=False, scale_factor = 0.8).set_z_index(2)
        subtitle = Tex('Variable Compleja. Logotipo de la UPIITA-IPN').scale(0.4).set_opacity(0.7).next_to(header,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(header,subtitle)).set_opacity(0.6).set_z_index(1)

        self.add(back_rect)
        self.add(header,subtitle)
        ##
        eq_1 = MathTex(r"\displaystyle f(t)\sim \sum _{k=-\infty }^{\infty }c_{k}\,e^{i w_0 k t} \\ \displaystyle c_{k}={1 \over T_0}\int _{T_0}f(t)\,e^{-i w_0 k t}\,dt").set_z_index(2).scale(0.6).next_to(header,DOWN,aligned_edge=RIGHT,buff=.3)
        back_eq_1 = BackgroundRectangle(eq_1,buff=0.1).set_opacity(0.6).set_z_index(1)

        self.add(back_eq_1,eq_1)

        mob = self.get_svg('upiita.svg',width=8.5,stroke_width = 1).shift(LEFT*.5+DOWN*.5).set_stroke(opacity=0.3) #Star(outer_radius=4).round_corners(radius=0.25)
        points = [mob.point_from_proportion(t) for t in np.linspace(0,1,num=self.n_points+1)]#r_time*config['frame_rate'])]
        points = points[:-1]
        f = np.array([p[0]+1j*p[1] for p in points])

        self.plane = ComplexPlane().set_stroke(opacity = 0.3)

        self.add(self.plane,self.plane.get_coordinate_labels().set_opacity(0.6))
        self.add(mob)

        self.serie = SerieComplejaFourier(f,self.k)

        self.add(Circle(radius = np.linalg.norm(self.plane.n2p(0+1j*0)-self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),(1)))),stroke_width = 1,color=WHITE).move_to(self.plane.n2p(0+1j*0)).set_stroke(opacity=0.6))
        self.add(Arrow(self.plane.n2p(0+1j*0), self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),(1))),buff=0,stroke_width=1.7,tip_length=0.15,max_stroke_width_to_length_ratio=10).set_opacity(0.6))

        array_k = list(range(-1*self.k, self.k+1, 1))
        array_k.sort(key=abs)

        for n in range(self.k*2+1):
            if n == 0:
                continue
            if n == self.k*2:
                self.last_vector = self.get_arrow(n)
                self.add(self.get_circle(n))
                self.add(self.last_vector)
                self.path = TracedPath(self.last_vector.get_end,stroke_color=YELLOW,stroke_width=4)
                self.path.add_updater(self.trim_dots)
                self.add(self.path)
                continue
            self.add(self.get_circle(n))
            self.add(self.get_arrow(n))

        self.play(self.t_tracker.animate.set_value(1),run_time = self.r_time, rate_func = linear)

    def get_svg(self,file,width,stroke_width):
        svg = SVGMobject(file,width=width,stroke_width = stroke_width)[0]
        return svg

    def get_arrow(self, n):
        arrow = always_redraw(lambda:
            Arrow(
                self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),n)),
                self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),(n+1))),
                buff=0,stroke_width=1.7,tip_length=0.15,max_stroke_width_to_length_ratio=10
            ).set_opacity(0.6)
        )
        return arrow

    def get_circle(self, n):
        circle = always_redraw(lambda:
            Circle(
                radius = np.linalg.norm(self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),n))-self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),(n+1)))),
                stroke_width = 1,color=WHITE
            ).move_to(self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),n))).set_stroke(opacity=0.6)
        )
        return circle

    def trim_dots(self, mob, dt):
        if len(mob.points) > 600:
            mob.points = [h for sublist in mob.get_cubic_bezier_tuples()[1:] for h in sublist]
        return mob
        # for n in range(k*2+1):
        #     if n == 0:
        #         self.add(Arrow(plane.n2p(0+1j*0),plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),(n+1))),buff=0))
        #         self.add(Circle(radius = np.linalg.norm(plane.n2p(0+1j*0)-plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),(n+1)))),stroke_width=2,color=WHITE).move_to(plane.n2p(0+1j*0)))
        #     else:
        #         self.add(
        #             Arrow(
        #                 plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),n)),
        #                 plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),(n+1))),
        #                 buff=0
        #             ).add_updater(
        #                 lambda mob: mob.become(
        #                     Arrow(
        #                         plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),n)),
        #                         plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),(n+1))),
        #                         buff=0
        #                     )
        #                 )
        #             )
        #         )
        #         self.add(
        #             Circle(
        #                 radius = np.linalg.norm(plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),n))-plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),(n+1)))),
        #                 stroke_width=2,
        #                 color=WHITE
        #             ).move_to(plane.n2p(serie.SerieFourierSumN(t_tracker.get_value(),n)))
        #         )
        #self.wait()

        # self.add(TracedPath(vec.get_end,stroke_color=YELLOW,stroke_width=4))
        # self.play(t_tracker.animate.set_value(1),run_time = r_time, rate_func = linear)
