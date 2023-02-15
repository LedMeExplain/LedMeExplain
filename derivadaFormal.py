from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class derivada_1(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'Definición formal de la derivada', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5)
        rect_title = SurroundingRectangle(title,LME_B,buff = 0.4)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT)

        subtitle = Tex('Cálculo diferencial').scale(0.55).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT)

        self.add(title)
        self.play(Create(rect_title), FadeIn(brand), Write(subtitle))
        self.wait()

        eq_1 = MathTex(r'{dy \over dx}',r'=',r'\displaystyle\lim_{h \to 0}',r'{f(x+h)-f(x) \over h}', tex_template = TexFontTemplates.libertine).next_to(rect_title,DOWN,buff=1,aligned_edge = LEFT)

        self.play(Write(eq_1),run_time = 0.7)
        self.wait(0.5)
        self.play(eq_1.animate.set_opacity(0.6))

        ax = Axes(
            x_range=[0, 10], y_range=[0, 10], x_length = 5, y_length = 5, axis_config={"include_tip": False}
        ).shift(DL*.5)
        labels = ax.get_axis_labels(x_label="x", y_label="y").set_opacity(0.6)
        graph = ax.get_graph(lambda x: (x/3)**2, color=BLUE, x_range=[0, 10])
        graph_lbl = ax.get_graph_label(graph,'y = f(x)',direction = UR).set_color(BLUE)

        x_1 = 3

        fx_line = ax.get_horizontal_line(ax.i2gp(x_1,graph))
        fx_line_lbl = MathTex(r'f(x)', tex_template = TexFontTemplates.libertine).scale(0.6).next_to([ax.c2p(0,0)[0],ax.i2gp(x_1,graph)[1],0],LEFT)
        x_line = ax.get_vertical_line(ax.i2gp(x_1,graph))
        x_line_lbl = MathTex(r'x', tex_template = TexFontTemplates.libertine).scale(0.7).next_to(ax.c2p(x_1,0),DOWN)
        dot_x1 = Dot(ax.i2gp(x_1,graph), radius = 0.05)

        lines1_group = VGroup(x_line_lbl,x_line,fx_line_lbl,fx_line)

        x_2 =  ValueTracker(8)

        fxh_line = ax.get_horizontal_line(ax.i2gp(x_2.get_value(),graph))
        fxh_line_lbl = MathTex(r'f(x+h)', tex_template = TexFontTemplates.libertine).scale(0.5).next_to([ax.c2p(0,0)[0],ax.i2gp(x_2.get_value(),graph)[1],0],LEFT)
        xh_line = ax.get_vertical_line(ax.i2gp(x_2.get_value(),graph))
        xh_line_lbl = MathTex(r'x+h', tex_template = TexFontTemplates.libertine).scale(0.6).next_to(ax.c2p(x_2.get_value(),0),DOWN)
        dot_x2 = Dot(ax.i2gp(x_2.get_value(),graph), radius = 0.05)

        lines2_group = VGroup(xh_line_lbl,xh_line,fxh_line_lbl,fxh_line)

        secant = ax.get_secant_slope_group(x_1, graph, dx=x_2.get_value()-x_1, dx_line_color=GREEN_D, dy_line_color=RED, dx_label='h', dy_label='f(x+h)-f(x)', secant_line_color='YELLOW', secant_line_length=5)

        self.play(
            Create(ax),
            FadeIn(labels)
        )
        self.play(Create(graph))
        self.play(FadeIn(graph_lbl))
        self.play(
            FadeIn(dot_x1),
            Create(lines1_group),
            run_time = 2
        )

        h_line = Line(ax.c2p(x_1,0),ax.c2p(x_2.get_value(),0))
        h_lbl = MathTex(r'h', tex_template = TexFontTemplates.libertine).scale(0.6).next_to(h_line,UP)
        h_group = VGroup(h_line,h_lbl)

        self.play(Create(h_group))
        h_line.flip()
        self.wait()
        self.play(Uncreate(h_group))

        self.play(
            FadeIn(dot_x2),
            Create(lines2_group),
            run_time = 2
        )
        self.wait()
        self.play(Create(secant), run_time = 4, lag_ratio = 0.1)

        eq_2 = MathTex(r'm',r'=',r'{y',r'\over',r'x}', tex_template = TexFontTemplates.libertine).next_to(ax.i2gp(x_2.get_value(),graph),UL,aligned_edge = RIGHT)
        eq_2[0].set_color(YELLOW)
        eq_2[2].set_color(RED)
        eq_2[4].set_color(GREEN_D)

        eq_3 = MathTex(r'm',r'=',r'{f(x+h)-f(x)',r'\over',r'h}', tex_template = TexFontTemplates.libertine).scale(0.7).next_to(ax.i2gp(x_2.get_value(),graph),UL,aligned_edge = RIGHT)
        eq_3[0].set_color(YELLOW)
        eq_3[2].set_color(RED)
        eq_3[4].set_color(GREEN_D)

        dy_lbl = MathTex(r'dy', tex_template = TexFontTemplates.libertine).scale(0.6).next_to(ax.i2gp(x_1,graph),RIGHT,buff=0.5).set_color(RED)
        dx_lbl = MathTex(r'dx', tex_template = TexFontTemplates.libertine).scale(0.6).next_to(ax.i2gp(x_1,graph),DOWN,buff=0.15).set_color(GREEN_D)
        d_lbl = VGroup(dy_lbl,dx_lbl).set_opacity(0)
        self.add(d_lbl)

        self.play(Write(eq_2),run_time = 0.7)

        secant.add_updater(
            lambda mob: mob.become(
                ax.get_secant_slope_group(x_1, graph, dx=x_2.get_value()-x_1, dx_line_color=GREEN_D, dy_line_color=RED, dx_label='h', dy_label='f(x+h)-f(x)', secant_line_color='YELLOW', secant_line_length=5)
            )
        )

        dot_x2.add_updater(
            lambda mob: mob.become(
                Dot(ax.i2gp(x_2.get_value(),graph), radius = 0.05)
            )
        )

        self.wait()

        self.play(
            FadeOut(lines1_group),
            FadeOut(lines2_group)
        )
        self.play(TransformMatchingTex(eq_2,eq_3))
        self.wait()
        self.play(Indicate(eq_1[2], color = ORANGE), run_time = 1.5)
        self.play(
            x_2.animate.set_value(x_1+.1),
            eq_3.animate.set_opacity(0).move_to(eq_1),
            d_lbl.animate.set_opacity(1),
            eq_1.animate.set_opacity(1),
            eq_1[0].animate.set_color(YELLOW).set_opacity(1),
            run_time = 3

        )
        self.wait(1.5)
