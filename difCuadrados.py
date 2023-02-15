from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

config["tex_template"] = TexFontTemplates.libertine

class difCuadrados(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = MathTex(r'\text{¿Cómo se ve una Diferencia de Cuadrados?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([BLUE_A,BLUE,BLUE_E]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Álgebra').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))

        eq_1 = MathTex(r'(a+b)',r'(a-b)',r'=',r'a^2',r'-',r'b^2').next_to(rect_title,DOWN,buff=1)

        self.play(Write(eq_1[0:2]),run_time = 0.7)

        base = DashedVMobject(Polygon(ORIGIN,RIGHT*4,RIGHT*4+UP*3,UP*3),num_dashes=45)
        base.add(DashedLine(RIGHT,RIGHT+UP*3))
        base.add(DashedLine(UP*2,RIGHT*4+UP*2))
        base.set_stroke(opacity = 0.4,width = 2)

        a = Polygon(RIGHT,RIGHT*4,RIGHT*4+UP*2,RIGHT+UP*2, color = BLUE, fill_opacity = 0.7)

        b = Polygon(ORIGIN,RIGHT,RIGHT+UP*2,UP*2, color = GREEN, fill_opacity = 0.7)

        a_cuad = Polygon(RIGHT,RIGHT*4,RIGHT*4+UP*3,RIGHT+UP*3, color = RED, fill_opacity = 0.4)
        b_cuad = Polygon(RIGHT+UP*2,UR*2,UR*2+UP,RIGHT+UP*3, color = ORANGE, fill_opacity = 0.4)
        ab_cuad = Polygon(RIGHT,RIGHT*4,UR*3+RIGHT,UR*2+UP,UR*2,RIGHT+UP*2, color = YELLOW, fill_opacity = 0.4)

        group = VGroup(base,a,b,a_cuad,b_cuad,ab_cuad).scale(1.2).to_edge(LEFT*1.5).shift(DOWN)

        a_1 = BraceLabel(a,'a',DOWN)
        b_1 = BraceLabel(b,'b',DOWN)

        def rotate_label(mob):
            mob[1].rotate(-PI/2).next_to(mob[0],RIGHT)

        a_2 = BraceLabel(base,'a',RIGHT)
        rotate_label(a_2)
        b_2 = BraceLabel(Line(a.get_corner(UR),base.get_corner(UR)),'b',RIGHT)
        rotate_label(b_2)
        a_b = BraceLabel(a,'a-b',RIGHT)
        rotate_label(a_b)

        self.play(Create(base))

        self.play(DrawBorderThenFill(a))

        self.play(FadeIn(a_1))

        self.play(DrawBorderThenFill(b))

        self.play(FadeIn(b_1))

        self.play(
            Indicate(eq_1[0]),
            Indicate(VGroup(a_1,b_1)),
        )

        self.play(FadeIn(a_2))
        self.play(
            a_2.animate.become(a_b),
            FadeIn(b_2)
        )

        self.play(
            Indicate(eq_1[1]),
            Indicate(a_2),
        )

        self.wait(0.5)

        self.play(
            Indicate(eq_1[0:2]),
            Indicate(VGroup(a,b)),
            run_time = 1.5
        )

        self.play(Write(eq_1[2]))

        self.play(b.animate.rotate(-PI/2).next_to(a,UP,buff=0,aligned_edge= RIGHT))

        self.play(
            Write(eq_1[3]),
            DrawBorderThenFill(a_cuad)
        )

        self.play(
            Indicate(eq_1[3],color=RED),
            Indicate(a_cuad,color=RED)
        )

        self.wait(0.5)

        self.play(
            Write(eq_1[4:]),
            DrawBorderThenFill(b_cuad)
        )

        self.play(
            Indicate(eq_1[5],color=ORANGE),
            Indicate(b_cuad,color=ORANGE)
        )

        self.wait(0.5)

        self.play(
            FadeOut(a_cuad),
            FadeOut(b_cuad),
            FadeIn(ab_cuad)
        )

        self.play(
            Indicate(eq_1[3:]),
            Indicate(ab_cuad)
        )

        self.play(FadeOut(ab_cuad),run_time = 0.5)

        self.wait()
