from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class dx_2(Scene):
    def construct(self):

        ## Titulo y subtitulo
        title = MathTex(r'\text{¿Cuál es la derivada de } \,y = x^2\, \text{?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5)
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

        scale = 0.8

        eq_1 = MathTex(r'y',r'=',r'f(x)',r'=',r'x^2').scale(scale)
        eq_2 = MathTex(r'{dy',r'\over',r'dx}',r'=',r'\displaystyle\lim_{h \to 0}',r'{f(x+h)',r'-',r'f(x)',r'\over',r'h}').scale(scale)
        eq_3 = MathTex(r'{d(x^2)',r'\over',r'dx}',r'=',r'\displaystyle\lim_{h \to 0}',r'{(x+h)^2',r'-',r'x^2',r'\over',r'h}').scale(scale)
        eq_4 = MathTex(r'{d(x^2)',r'\over',r'dx}',r'=',r'\displaystyle\lim_{h \to 0}',r'{x^2+2xh+h^2',r'-',r'x^2',r'\over',r'h}').scale(scale)
        eq_5 = MathTex(r'{d(x^2)',r'\over',r'dx}',r'=',r'\displaystyle\lim_{h \to 0}',r'{x^2+',r'2xh+h^2',r'-x^2',r'\over',r'h}').scale(scale)
        eq_5_aux = MathTex(r'{d(x^2)',r'\over',r'dx}',r'=',r'\displaystyle\lim_{h \to 0}',r'{2xh+h^2',r'\over',r'h}').scale(scale)
        eq_5_aux2 = MathTex(r'{d(x^2)',r'\over',r'dx}',r'=',r'\displaystyle\lim_{h \to 0}',r'2x+h').scale(scale)
        eq_6 = MathTex(r'{d(x^2)',r'\over',r'dx}',r'=',r'2x').scale(scale)


        eq_group = Group(eq_1,eq_2,eq_3,eq_4,eq_5_aux2,eq_6).arrange_in_grid(cols = 1,buff=0.7,cell_alignment = LEFT).to_edge(LEFT*.8)
        eq_5.move_to(eq_5_aux2,aligned_edge = LEFT)
        eq_5_aux.move_to(eq_5_aux2,aligned_edge = LEFT)

        text_aux_2 = Text('Definición formal de la derivada', color = RED).scale(0.4).next_to(eq_2,UP,buff=0.2,aligned_edge=LEFT)
        text_aux_3 = Text('Sustitución', color = TEAL).scale(0.35).next_to(eq_3,UP,buff=0.2,aligned_edge=LEFT)
        text_aux_4 = Text('Simplificación', color = YELLOW_D).scale(0.35).next_to(eq_4,UP,buff=0.2,aligned_edge=LEFT)

        txt_group = Group(text_aux_2,text_aux_3,text_aux_4)

        # Eq_1
        self.play(FadeIn(eq_1))
        self.wait(0.5)

        # Eq_2
        self.play(Write(text_aux_2))
        self.wait(0.5)
        self.play(Write(eq_2), run_time = 2)
        self.wait(0.5)

        # Eq_3
        self.play(Write(text_aux_3))
        self.wait(0.5)
        self.play(
            FadeOut(eq_1[4].copy(),target_position = eq_3[0]),
            TransformMatchingShapes(eq_2[0].copy(),eq_3[0]),
            TransformMatchingShapes(eq_2[1:4].copy(),eq_3[1:4])
        )
        self.play(
            Write(eq_3[4])
        )
        self.play(
            FadeOut(eq_1[4].copy(),target_position = eq_3[5]),
            FadeOut(eq_2[5].copy(),target_position = eq_3[5]),
            FadeIn(eq_3[5])
        )
        self.play(
            Write(eq_3[6])
        )
        self.play(
            FadeOut(eq_1[4].copy(),target_position = eq_3[7]),
            FadeOut(eq_2[7].copy(),target_position = eq_3[7]),
            FadeIn(eq_3[7])
        )
        self.play(
            Write(eq_3[8:])
        )

        self.wait(0.5)

        # Eq_4
        self.play(Write(text_aux_4))
        self.play(
            TransformMatchingShapes(eq_3[0].copy(),eq_4[0]),
            TransformMatchingShapes(eq_3[1:4].copy(),eq_4[1:4])
        )
        self.play(
            Write(eq_4[4])
        )
        self.play(
            TransformMatchingShapes(eq_3[5].copy(),eq_4[5])
        )
        self.play(
            Write(eq_4[6])
        )
        self.play(
            TransformMatchingShapes(eq_3[7].copy(),eq_4[7])
        )
        self.play(
            TransformMatchingShapes(eq_3[8:].copy(),eq_4[8:])
        )

        self.wait(0.5)

        # Eq_5
        self.play(
            FadeIn(eq_5[5:],target_position = eq_4[5:]),
            FadeIn(eq_5_aux2[:5],target_position = eq_4[:5])
        )
        self.play(
            FadeOut(eq_5[5]),
            FadeOut(eq_5[7])
        )

        self.play(
            TransformMatchingShapes(eq_5[6],eq_5_aux[5]),
            TransformMatchingShapes(eq_5[8],eq_5_aux[6]),
            TransformMatchingShapes(eq_5[9],eq_5_aux[7]),
        )
        self.wait()

        self.play(
            FadeOut(eq_5_aux[6]),
            FadeOut(eq_5_aux[7]),
            TransformMatchingShapes(eq_5_aux[5],eq_5_aux2[5]),
        )

        self.wait()

        self.play(
            Indicate(eq_5_aux2[4]),
        )
        self.wait(0.5)

        # Eq_6
        self.play(
            TransformMatchingShapes(eq_5_aux2[:4].copy(),eq_6[:4]),
            FadeIn(eq_6[4],target_position=eq_5_aux2[5])
        )

        self.wait()
        eq_group.remove(eq_6)

        self.play(
            FadeOut(eq_group),
            FadeOut(txt_group),
            eq_6.animate.scale(1.5).move_to(ORIGIN+LEFT*.5)
        )

        self.play(ApplyWave(eq_6,color=PURE_GREEN))

        self.wait(0.5)
