from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class integral_1(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo se ve una integral definida?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([RED,LME_B])

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":BLUE,"[3:4]":BLUE,"[5:6]":BLUE} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT)

        subtitle = Tex('Cálculo integral').scale(0.55).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT)

        self.add(title)
        self.play(Create(rect_title), FadeIn(brand), Write(subtitle))
        self.wait()

        ax = Axes(
            x_range=[0, 10], y_range=[0, 10], x_length = 5, y_length = 5, axis_config={"include_tip": False}
        ).shift(DL*.5)
        labels = ax.get_axis_labels(x_label="x", y_label="y").set_opacity(0.6)
        graph = ax.get_graph(lambda x: ((x-4.5)/2)**3 - x + 11, x_range=[0, 8.5]).set_color(ORANGE)
        graph_lbl = ax.get_graph_label(graph,'y = f(x)',direction = UR, x_val = 8.5).set_color(ORANGE)

        x_1 = 2
        x_2 =  8

        riemann = ax.get_riemann_rectangles(graph, x_range=[x_1,x_2], dx=1, stroke_width=1)
        brace = VGroup(Line(ax.c2p(x_1,0),ax.c2p(x_1+1,0)).set_color(LIGHT_PINK),MathTex(r'\Delta x', tex_template = TexFontTemplates.libertine).set_color(LIGHT_PINK).scale(0.8).move_to(ax.c2p(x_1+1,-1)))

        a_line = ax.get_vertical_line(ax.i2gp(x_1,graph))
        a_line_lbl = MathTex(r'a', tex_template = TexFontTemplates.libertine).scale(0.7).next_to(ax.c2p(x_1,0),DOWN)
        a_graph_lbl = ax.get_graph_label(graph,'f(a)',direction = UP*1.3, x_val = x_1).set_color(ORANGE).scale(0.9)

        lines1_group = VGroup(a_line_lbl,a_line)

        b_line = ax.get_vertical_line(ax.i2gp(x_2,graph))
        b_line_lbl = MathTex(r'b', tex_template = TexFontTemplates.libertine).scale(0.6).next_to(ax.c2p(x_2,0),DOWN)
        b_graph_lbl = ax.get_graph_label(graph,'f(b)',direction = RIGHT, x_val = x_2).set_color(ORANGE).scale(0.9)

        lines2_group = VGroup(b_line_lbl,b_line)

        self.play(
            Create(ax),
            FadeIn(labels)
        )
        self.play(Create(graph))
        self.play(FadeIn(graph_lbl))
        self.play(
            Create(lines1_group)
        )
        self.play(
            Create(lines2_group)
        )

        self.play(FadeIn(riemann[0]))
        self.wait(0.5)
        self.play(FadeIn(a_graph_lbl))
        self.play(FadeIn(brace))
        self.wait(0.5)

        eq_0 = MathTex(r'A_a',r'=',r'f(a)\,',r'\Delta x', tex_template = TexFontTemplates.libertine).next_to(rect_title,DOWN,buff=1,aligned_edge = LEFT)
        eq_0[0].set_color(riemann[0].get_fill_color())
        eq_0[2].set_color(ORANGE)
        eq_0[3].set_color(LIGHT_PINK)

        self.play(FadeIn(eq_0,target_position=riemann))
        self.wait()
        self.play(FadeOut(a_graph_lbl))
        self.play(FadeIn(riemann[1:]),lag_ratio=1,run_time = 2.5)

        eq_1 = MathTex(r'A_{ab}',r'=',r'\sum_{i=a}^{b}',r'f(i)\,',r'\Delta x', tex_template = TexFontTemplates.libertine).next_to(rect_title,DOWN,buff=1,aligned_edge = LEFT)
        eq_1[0].set_color_by_gradient([riemann[0].get_fill_color(),riemann[-1].get_fill_color()])
        eq_1[3].set_color(ORANGE)
        eq_1[4].set_color(LIGHT_PINK)

        self.play(
            FadeOut(eq_0,shift=UP),
            FadeIn(eq_1,shift=UP),
        )
        self.wait()

        for i in [.5,.2,.1,.05]:
            if i == 0.05:
                self.play(
                    riemann.animate.become(ax.get_area(graph, x_range=[x_1,x_2], opacity=1)),
                    brace[1].animate.become(MathTex(r'dx', tex_template = TexFontTemplates.libertine).set_color(LIGHT_PINK).scale(0.8).move_to(ax.c2p(x_1+1,-1))),
                    brace[0].animate.become(Dot(color=LIGHT_PINK).move_to(ax.c2p(x_1,0)))
                )
            else:
                self.play(
                    riemann.animate.become(ax.get_riemann_rectangles(graph, x_range=[x_1,x_2], dx=i, stroke_width=i)),
                    brace[0].animate.become(Line(ax.c2p(x_1,0),ax.c2p(x_1+i,0)).set_color(LIGHT_PINK))
                )
            self.wait(0.5)

        eq_2 = MathTex(r'A_{ab}',r'=',r'\displaystyle \int_{a}^{b}',r'f(x)\,',r'dx', tex_template = TexFontTemplates.libertine).next_to(rect_title,DOWN,buff=1,aligned_edge = LEFT)
        eq_2[0].set_color_by_gradient([riemann[0].get_fill_color(),riemann[-1].get_fill_color()])
        eq_2[3].set_color(ORANGE)
        eq_2[4].set_color(LIGHT_PINK)

        self.play(
            FadeOut(eq_1,shift=UP),
            FadeIn(eq_2,shift=UP),
        )

        self.wait()

        self.play(eq_2.animate.set_color(WHITE))
        self.play(Indicate(eq_2,color=PURE_GREEN))

        self.wait()
