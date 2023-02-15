from manim import *
import numpy as np

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps


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

class serieTest_fourier(Scene):
    def construct(self):
        r_time =  10
        n_points = 1000 # !! NO USAR MENOS DE 1000 PUNTOS
        k = 100
        #Prueba con 10, 100, 100 y square.scale(2)

        mob = Square().scale(2)#Star(outer_radius=4).round_corners(radius=0.25)
        points = [mob.point_from_proportion(t) for t in np.linspace(0,1,num=n_points+1)]#r_time*config['frame_rate'])]
        points = points[:-2]
        f = np.array([p[0]+1j*p[1] for p in points])

        plane = ComplexPlane(x_range=(- 4.1, 4.1, 1), y_range=(- 7.1, 7.1, 1)).add_coordinates().set_stroke(opacity = 0.4)

        self.add(plane)

        self.add(*[Dot(plane.n2p(p),0.04,color=RED) for p in f])

        self.wait()

        serie = SerieComplejaFourier(f,k)

        t_tracker = ValueTracker(0)
        vec = always_redraw(lambda: Arrow(plane.n2p(0+1j*0),plane.n2p(serie.SerieFourierSum(t_tracker.get_value())),buff = 0))

        self.add(vec)
        self.add(TracedPath(vec.get_end))
        self.play(t_tracker.animate.set_value(1),run_time = r_time, rate_func = linear)

class serieTest_dots(Scene):
    def construct(self):
        square = Square(color=WHITE)
        dots_1 = VGroup(*[Dot(square.point_from_proportion(x),0.04, color = RED) for x in np.linspace(0,1,num=41)])
        self.add(square,dots_1)

        circle = Circle(color=WHITE).shift(UP*4)
        dots_2 = VGroup(*[Dot(circle.point_from_proportion(x),0.04, color = GREEN) for x in np.linspace(0,1,num=41)])
        self.add(circle,dots_2)

        triangle = Triangle(color = WHITE).shift(LEFT*3)
        dots_3 = VGroup(*[Dot(x,0.04,color = YELLOW) for x in triangle.get_points_defining_boundary()])
        self.add(triangle,dots_3)
        self.wait()

class serieTest_1(Scene):
    r_time = 10
    n_points = 1000
    k = 8
    t_tracker = ValueTracker(0)

    def construct(self):

        ## Titulo y subtitulo
        title = Tex(r'Transformada Compleja de Fourier', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([WHITE,LME_A]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Variable Compleja').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait(0.5)
        ##

        eq_1 = MathTex(r"\displaystyle f(t)\sim \sum _{k=-\infty }^{\infty }c_{k}\,e^{i w_0 k t} \\ \displaystyle c_{k}={1 \over T_0}\int _{T_0}f(t)\,e^{-i w_0 k t}\,dt").set_z_index(2).scale(0.7).next_to(brand,DOWN,aligned_edge=RIGHT)
        back_eq_1 = BackgroundRectangle(eq_1,buff=0.1).set_opacity(0.6).set_z_index(1)

        self.play(
            FadeIn(back_eq_1),
            Write(eq_1)
        )

        mob = self.get_svg('upiita.svg',width=6,stroke_width = 1).shift(LEFT*.5).set_stroke(opacity=0.3) #Star(outer_radius=4).round_corners(radius=0.25)
        points = [mob.point_from_proportion(t) for t in np.linspace(0,1,num=self.n_points+1)]#r_time*config['frame_rate'])]
        points = points[:-1]
        f = np.array([p[0]+1j*p[1] for p in points])

        self.plane = ComplexPlane(x_range=(- 4.1, 4.1, 1), y_range=(- 7.1, 7.1, 1)).set_stroke(opacity = 0.2)
        self.play(
            Create(self.plane),
            FadeIn(self.plane.get_coordinate_labels().set_opacity(0.6)),
            lag_ratio = 0.3,
            run_time = 2
        )

        self.play(FadeIn(mob))

        self.serie = SerieComplejaFourier(f,self.k)

        self.play(FadeIn(Circle(radius = np.linalg.norm(self.plane.n2p(0+1j*0)-self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),(1)))),stroke_width = 1,color=WHITE).move_to(self.plane.n2p(0+1j*0)).set_stroke(opacity=0.6)))
        self.play(Create(Arrow(self.plane.n2p(0+1j*0), self.plane.n2p(self.serie.SerieFourierSumN(self.t_tracker.get_value(),(1))),buff=0,stroke_width=1.7,tip_length=0.15,max_stroke_width_to_length_ratio=10).set_opacity(0.6)))

        array_k = list(range(-1*self.k, self.k+1, 1))
        array_k.sort(key=abs)

        for n in range(self.k*2+1):
            if n == 0:
                continue
            if n == self.k*2:
                self.last_vector = self.get_arrow(n)
                self.play(FadeIn(self.get_circle(n)),run_time = 0.1)
                self.play(FadeIn(self.last_vector),run_time = 0.1)
                self.path = TracedPath(self.last_vector.get_end,stroke_color=YELLOW,stroke_width=4)
                self.add(self.path)
                continue
            self.play(FadeIn(self.get_circle(n)),run_time = 0.1)
            self.play(FadeIn(self.get_arrow(n)),run_time = 0.1)

        self.play(self.t_tracker.animate.set_value(1),run_time = self.r_time, rate_func = linear)
        self.t_tracker.set_value(0)
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
