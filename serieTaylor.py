from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

## CAMBIAR BABEL A SPANISH

class serieTaylor(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo se ve la Serie de Taylor?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A,ORANGE,LME_B]).set_z_index(2)
        back_title = BackgroundRectangle(rect_title).scale(7.5).set_z_index(1)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Cálculo Diferencial').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        self.add(back_title,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        eq_1 = MathTex(r'f(x)',r'={\displaystyle \sum _{n=0}^{\infty }{\frac {f^{(n)}(a)}{n!}}(x-a)^{n}}').scale(0.8).next_to(subtitle,DOWN,aligned_edge=LEFT,buff=0.5).set_z_index(2)

        self.play(Write(eq_1))


        ax = Axes(x_range=[-2,6,1], y_range=[-3,3,1], x_length=6, y_length=4, tips = False).to_edge(LEFT).shift(DOWN*1.5)
        graph = ax.get_graph(lambda x: 2*np.cos(x), x_range = [-2,6], color = TEAL)
        graph_lbl = ax.get_graph_label(graph,r'2cos(x)', direction = UP*2.5, x_val = -1).scale(0.8)

        self.play(Create(ax), lag_ratio = 0.5, run_time = 2)
        self.play(Create(graph))
        self.play(
            FadeIn(graph_lbl),
            eq_1[0].animate.set_color(TEAL)
        )

        eq_2 = MathTex(r'a',r'=2').scale(0.7).next_to(ax,UP,buff=1).shift(LEFT).set_z_index(2)
        eq_2[0].set_color(RED)

        eq_3 = MathTex(r'n',r'=',r'0').scale(0.7).next_to(eq_2,RIGHT,aligned_edge=DOWN,buff=0.5).set_z_index(2)
        eq_3[0].set_color(ORANGE)

        a = 2
        a_line = ax.get_vertical_line(ax.i2gp(a,graph))
        a_line_lbl = MathTex(r'a').scale(0.7).next_to(ax.c2p(a,0),UP).set_color(RED)
        a_dot = Dot(radius = 0.05, color=RED).move_to(ax.i2gp(a,graph))
        a_group = VGroup(a_line,a_line_lbl,a_dot)

        self.play(Write(eq_2))
        self.play(Create(a_line))
        self.play(
            FadeIn(a_line_lbl),
            FadeIn(a_dot)
        )

        eq_4 = MathTex(r'f(x)',r'=',r'2\cos(2)',r'-2\sen(2)(x-2)',r'-\cos(2)(x-2)^2',r'+{1 \over 3}\sen(2)(x-2)^3',r'+{1 \over 12}\cos(2)(x-2)^4',r'-{1 \over 60}\sen(2)(x-2)^5',r'+...').scale(0.7).next_to(eq_1,DOWN,aligned_edge=LEFT,buff=0.5).set_z_index(2)
        eq_4[0].set_color(ORANGE)

        graphT = ax.get_graph(lambda x: 2*np.cos(2)).set_color(ORANGE)
        graphT1 = ax.get_graph(lambda x: 2*np.cos(2)-2*np.sin(2)*(x-2)).set_color(ORANGE)
        graphT2 = ax.get_graph(lambda x: 2*np.cos(2)-2*np.sin(2)*(x-2)-np.cos(2)*(x-2)**2).set_color(ORANGE)
        graphT3 = ax.get_graph(lambda x: 2*np.cos(2)-2*np.sin(2)*(x-2)-np.cos(2)*(x-2)**2+1/3*np.sin(2)*(x-2)**3).set_color(ORANGE)
        graphT4 = ax.get_graph(lambda x: 2*np.cos(2)-2*np.sin(2)*(x-2)-np.cos(2)*(x-2)**2+1/3*np.sin(2)*(x-2)**3+1/12*np.cos(2)*(x-2)**4).set_color(ORANGE)
        graphT5 = ax.get_graph(lambda x: 2*np.cos(2)-2*np.sin(2)*(x-2)-np.cos(2)*(x-2)**2+1/3*np.sin(2)*(x-2)**3+1/12*np.cos(2)*(x-2)**4-1/60*np.sin(2)*(x-2)**5).set_color(ORANGE)

        self.play(TransformMatchingShapes(eq_1[0].copy(),eq_4[0]))
        self.play(Write(eq_4[1:]))
        self.play(FadeIn(eq_3))
        self.play(Indicate(eq_4[2],color = ORANGE))
        self.play(Create(graphT))

        n1 = MathTex(r'1').scale(0.7).move_to(eq_3[2],aligned_edge=DOWN).set_z_index(2)
        n2 = MathTex(r'2').scale(0.7).move_to(eq_3[2],aligned_edge=DOWN).set_z_index(2)
        n3 = MathTex(r'3').scale(0.7).move_to(eq_3[2],aligned_edge=DOWN).set_z_index(2)
        n4 = MathTex(r'4').scale(0.7).move_to(eq_3[2],aligned_edge=DOWN).set_z_index(2)
        n5 = MathTex(r'5').scale(0.7).move_to(eq_3[2],aligned_edge=DOWN).set_z_index(2)

        self.play(eq_4.animate.shift(LEFT*eq_4[0:3].width))
        self.play(
            Indicate(eq_4[3],color = ORANGE),
            FadeOut(eq_3[2],shift=DOWN*.3),
            FadeIn(n1,shift=DOWN*.3)
        )
        self.play(graphT.animate.become(graphT1))

        self.play(eq_4.animate.shift(LEFT*eq_4[3].width))
        self.play(
            Indicate(eq_4[4],color = ORANGE),
            FadeOut(n1,shift=DOWN*.3),
            FadeIn(n2,shift=DOWN*.3)
        )
        self.play(graphT.animate.become(graphT2))

        self.play(eq_4.animate.shift(LEFT*eq_4[4].width))
        self.play(
            Indicate(eq_4[5],color = ORANGE),
            FadeOut(n2,shift=DOWN*.3),
            FadeIn(n3,shift=DOWN*.3)
        )
        self.play(graphT.animate.become(graphT3))

        self.play(eq_4.animate.shift(LEFT*eq_4[5].width))
        self.play(
            Indicate(eq_4[6],color = ORANGE),
            FadeOut(n3,shift=DOWN*.3),
            FadeIn(n4,shift=DOWN*.3)
        )
        self.play(graphT.animate.become(graphT4))

        self.play(eq_4.animate.shift(LEFT*eq_4[6].width))
        self.play(
            Indicate(eq_4[7],color = ORANGE),
            FadeOut(n4,shift=DOWN*.3),
            FadeIn(n5,shift=DOWN*.3)
        )
        self.play(graphT.animate.become(graphT5))

        self.wait()
