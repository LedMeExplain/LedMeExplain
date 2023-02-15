from manim import *

quality_factor = 2
fps = 15

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class productoMatrices(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = MathTex(r'\text{¿Cómo se multiplican las matrices?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([RED,PURPLE,PURPLE_D]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Álgebra Lineal').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))

        m0 = Matrix([
            [2, 4, 7],
            [-1, 6, 9]
        ]).scale(0.8)

        lbl_m0 = MathTex(r'A=')
        m0_g = VGroup(lbl_m0,m0).arrange()
        m0_size = MathTex('(','2','\,x\,','3',')', tex_template = TexFontTemplates.libertine).scale(0.8).next_to(m0,DOWN)
        m0_g.add(m0_size).scale(0.8).to_edge(LEFT*1.5).shift(UP*3.8)

        m1 = Matrix([
            [1, 8, 5, -2],
            [6, -5, 3, 9],
            [-2, 4, 1, -4],
        ]).scale(0.8).shift(UP*2+RIGHT)

        lbl_m1 = MathTex(r'B=')
        m1_g = VGroup(lbl_m1,m1).arrange().to_edge(LEFT*1.5)
        m1_size = MathTex('(','3','\,x\,','4',')', tex_template = TexFontTemplates.libertine).scale(0.8).next_to(m1,DOWN)
        m1_g.add(m1_size).scale(0.8).to_edge(LEFT*1.5).shift(UP*1.5)

        self.play(Write(m0_g))
        self.play(
            Indicate(m0_size[1],color=YELLOW),
            Indicate(m0.get_columns()[0],color=YELLOW)
        )
        self.play(
            Indicate(m0_size[3],color=ORANGE),
            Indicate(m0.get_rows()[0],color=ORANGE)
        )

        self.play(Write(m1_g))
        self.play(
            Indicate(m1_size[1],color=YELLOW),
            Indicate(m1.get_columns()[0],color=YELLOW)
        )
        self.play(
            Indicate(m1_size[3],color=ORANGE),
            Indicate(m1.get_rows()[0],color=ORANGE)
        )

        eq_1_aux = MathTex('(2x3)','\,','(3x4)','\,','(2x4)', tex_template = TexFontTemplates.libertine).scale(0.7)
        eq_1 = MathTex('A','*','B','=','C').add(*eq_1_aux).arrange_in_grid(rows = 2).shift(DOWN+LEFT)

        self.wait(0.5)

        self.play(FadeIn(eq_1))

        self.wait()
