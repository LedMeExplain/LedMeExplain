from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class formulaGen1(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = MathTex(r'\text{¿Cómo demostrar la Fórmula General?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([GREEN,TEAL, GREEN_A]).set_z_index(2)

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

        def color_eq(mob):
            mob.set_color_by_tex('a',RED)
            mob.set_color_by_tex('b',BLUE)
            mob.set_color_by_tex('c',GREEN)
            return mob

        eq_1 = MathTex(r'{a',r'x^',r'2',r'+',r'b',r'x',r'+',r'c',r'=',r'0',r'\over',r'a}').scale(1.5).to_edge(LEFT*1.5)
        eq_1[-1].set_color(RED)

        self.play(Write(eq_1[:10]), run_time = 0.7)
        self.play(
            eq_1[0].animate.set_color(RED),
            eq_1[4].animate.set_color(BLUE),
            eq_1[7].animate.set_color(GREEN)
        )

        self.wait(0.5)

        self.play(Write(eq_1[10:]))

        self.wait(0.5)

        eq_2 = MathTex(r'{a',r'x^',r'2',r'+',r'b',r'x',r'+',r'c',r'\over',r'a}',r'=',r'{0',r'\over',r'a}').scale(1.5).to_edge(LEFT*1.5)
        color_eq(eq_2)

        bar1 = eq_1[10].copy()

        self.play(
            TransformMatchingShapes(eq_1[:8],eq_2[:8]),
            TransformMatchingShapes(eq_1[8],eq_2[10]),
            TransformMatchingShapes(eq_1[9],eq_2[11]),
            Transform(bar1,eq_2[8]),
            Transform(eq_1[10],eq_2[12]),
            TransformMatchingShapes(eq_1[11].copy(),eq_2[9]),
            TransformMatchingShapes(eq_1[11],eq_2[13]),
        )

        self.wait(0.5)

        eq_3 = MathTex(r'{a',r'x^',r'2',r'+',r'b',r'x',r'+',r'c',r'\over',r'a}',r'=',r'0').scale(1.5).to_edge(LEFT*1.5)
        color_eq(eq_3)

        self.play(
            TransformMatchingShapes(eq_2[:11],eq_3[:11]),
            TransformMatchingShapes(eq_2[11],eq_3[11]),
            FadeOut(bar1),
            FadeOut(eq_1[10]),
            FadeOut(eq_2[13])
        )

        self.wait(0.5)

        eq_4 = MathTex(r'{a',r'\over',r'a}',r'x^',r'2',r'+',r'{b',r'\over',r'a}',r'x',r'+',r'{c',r'\over',r'a}',r'=',r'0').scale(1.5).to_edge(LEFT*1.5)
        color_eq(eq_4)

        bar2 = eq_3[8].copy()
        a2 = eq_3[9].copy()
        bar3 = eq_3[8].copy()
        a3 = eq_3[9].copy()

        self.play(
            TransformMatchingShapes(eq_3[0],eq_4[0]),
            TransformMatchingShapes(eq_3[1:5],eq_4[3:7]),
            TransformMatchingShapes(eq_3[5:8],eq_4[9:12]),
            TransformMatchingShapes(eq_3[10:12],eq_4[14:16]),
            TransformMatchingShapes(eq_3[9],eq_4[2]),
            TransformMatchingShapes(a2,eq_4[8]),
            TransformMatchingShapes(a3,eq_4[13]),
            Transform(eq_3[8],eq_4[1]),
            Transform(bar2,eq_4[7]),
            Transform(bar3,eq_4[12]),
        )

        self.wait(0.5)

        self.play(
            FadeOut(eq_4[:3]),
            FadeOut(eq_3[8])
        )

        self.wait(0.5)

        self.play(
            eq_4[3:10].animate.shift(UP*3),
            FadeOut(bar2,shift=UP*3),
            eq_4[10:].animate.shift(DOWN+LEFT*.8),
            FadeOut(bar3,shift=DOWN+LEFT*.8)
        )

        self.wait(0.5)

        eq_5 = MathTex(r'+',r'\left(',r'b',r'\over',r'2',r'a',r'\right)^',r'2').scale(1.5).next_to(eq_4[3:10],RIGHT,aligned_edge = DOWN)
        color_eq(eq_5)
        eq_6 = MathTex(r'-',r'\left(',r'b',r'\over',r'2',r'a',r'\right)^',r'2').scale(1.5).next_to(eq_4[10:],LEFT,aligned_edge = DOWN)
        color_eq(eq_6)

        self.play(Write(eq_5,run_time = 0.7))
        self.play(Write(eq_6,run_time = 0.7))

        self.wait(0.5)

        tcp = Tex('Trinomio Cuadrado Perfecto').scale(0.7).set_color(GOLD).shift(UP*1.5)

        self.play(FadeIn(tcp))
        eq_g1 = VGroup(eq_4[3:10],eq_5)
        self.play(
            Indicate(eq_g1,color=GOLD),
            Indicate(tcp,color=GOLD),
        )

        self.wait(0.5)

        eq_7 = MathTex(r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)^',r'2').scale(1.5).move_to(eq_g1)
        color_eq(eq_7)

        self.play(
            TransformMatchingShapes(eq_5[1],eq_7[0]),
            TransformMatchingShapes(eq_4[3],eq_7[1]),
            TransformMatchingShapes(eq_5[0],eq_7[2]),
            TransformMatchingShapes(eq_5[2:6],eq_7[3:7]),
            TransformMatchingShapes(eq_5[6:8],eq_7[7:9]),
            FadeOut(eq_4[4:10], shift = UP*.5)
        )

        self.play(FadeOut(tcp))

        self.wait(0.5)

        eq_8 = MathTex(r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)^',r'2',r'-',r'\left(',r'b',r'\over',r'2',r'a',r'\right)^',r'2',r'+',r'{c',r'\over',r'a}',r'=',r'0').scale(1.1).shift(UP*3)
        color_eq(eq_8)

        self.play(
            TransformMatchingShapes(eq_7[:],eq_8[:9]),
            TransformMatchingShapes(eq_6[:],eq_8[9:17]),
            TransformMatchingShapes(eq_4[10:],eq_8[17:]),
        )

        self.wait(0.5)

        eq_9 = MathTex(r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)^',r'2',r'=',r'\left(',r'b',r'\over',r'2',r'a',r'\right)^',r'2',r'-',r'{c',r'\over',r'a}').scale(1.1).shift(UP*3)
        color_eq(eq_9)

        self.play(
            TransformMatchingShapes(eq_8,eq_9,path_arc = PI/2)
        )

        self.wait(0.5)

        eq_10 = MathTex(r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)^',r'2',r'=',r'{b^',r'2',r'\over',r'4',r'a^',r'2}',r'-',r'{c',r'\over',r'a}').scale(1.1).shift(UP*3)
        color_eq(eq_10)

        self.play(
            TransformMatchingShapes(eq_9[0:10],eq_10[0:10]),
            FadeOut(eq_9[11:15],shift=UP*.5),
            FadeIn(eq_10[10:16],shift=UP*.5),
            FadeOut(eq_9[10:11]),
            FadeOut(eq_9[15:17]),
            TransformMatchingShapes(eq_9[17:],eq_10[16:]),
        )

        self.wait(0.5)

        eq_11 = MathTex(r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)^',r'2',r'=',r'{b^',r'2',r'\over',r'4',r'a^',r'2}',r'-',r'{4',r'a',r'c',r'\over',r'4',r'a^',r'2}').scale(1.1).shift(UP*3)
        color_eq(eq_11)

        self.play(
            TransformMatchingShapes(eq_10[:17],eq_11[:17]),
            TransformMatchingShapes(eq_10[17:19],eq_11[19:21]),
            TransformMatchingShapes(eq_10[19],eq_11[22]),
            FadeIn(eq_11[17:19]),
            FadeIn(eq_11[21]),
            FadeIn(eq_11[23]),
        )

        self.wait(0.5)

        self.play(
            Indicate(eq_11[13:16]),
            Indicate(eq_11[21:24]),
        )

        self.wait(0.5)

        eq_12 = MathTex(r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)^',r'2',r'=',r'{b^',r'2',r'-',r'4',r'a',r'c',r'\over',r'4',r'a^',r'2}').scale(1.1).shift(UP*3)
        color_eq(eq_12)

        self.play(
            TransformMatchingShapes(eq_11[:12],eq_12[:12]),
            TransformMatchingShapes(eq_11[12],eq_12[16]),
            TransformMatchingShapes(eq_11[16],eq_12[12]),
            TransformMatchingShapes(eq_11[17:20],eq_12[13:16]),
            FadeOut(eq_11[20]),
            FadeOut(eq_11[13:16], target_position = eq_12[17:20]),
            FadeOut(eq_11[21:24], target_position = eq_12[17:20]),
            FadeIn(eq_12[17:20])
        )

        self.wait(0.5)

        eq_13 = MathTex(r'x',r'+',r'{b',r'\over',r'2',r'a}',r'=',r'\pm',r'\sqrt{',r'b^',r'2',r'-',r'4',r'a',r'c',r'\over',r'4',r'a^',r'2}').scale(1.1).shift(UP*3)
        color_eq(eq_13)

        self.play(

            FadeOut(eq_12[0],target_position=eq_13[8]),
            FadeOut(eq_12[7:9],target_position=eq_13[8]),
            FadeIn(eq_13[7:9]),
            TransformMatchingShapes(eq_12[1:7],eq_13[:6]),
            TransformMatchingShapes(eq_12[9],eq_13[6]),
            TransformMatchingShapes(eq_12[10:],eq_13[9:]),
        )

        self.wait(0.5)

        eq_14 = MathTex(r'x',r'+',r'{b',r'\over',r'2',r'a}',r'=',r'{\pm',r'\sqrt{',r'b^',r'2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}').scale(1.1).shift(UP*3)
        color_eq(eq_14)

        self.play(
            TransformMatchingShapes(eq_13[:15],eq_14[:15]),
            TransformMatchingShapes(eq_13[15],eq_14[15]),
            TransformMatchingShapes(eq_13[16:],eq_14[16:])
        )

        self.wait(0.5)

        eq_15 = MathTex(r'x',r'=',r'-',r'{b',r'\over',r'2',r'a}',r'{\pm',r'\sqrt{',r'b^',r'2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}').scale(1.1).shift(UP*3)
        color_eq(eq_15)

        self.play(
            TransformMatchingShapes(eq_14[0],eq_15[0]),
            TransformMatchingShapes(eq_14[1],eq_15[2]),
            TransformMatchingShapes(eq_14[2:6],eq_15[3:7]),
            TransformMatchingShapes(eq_14[6],eq_15[1]),
            TransformMatchingShapes(eq_14[7:],eq_15[7:]),
        )

        self.wait(0.5)

        self.play(
            Indicate(eq_15[5:7]),
            Indicate(eq_15[16:18]),
        )

        self.wait(0.5)

        eq_16 = MathTex(r'x',r'=',r'{-',r'b',r'\pm',r'\sqrt{',r'b^',r'2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}').scale(1.1).shift(UP*3)
        color_eq(eq_16)

        self.play(
            TransformMatchingShapes(eq_15[:4],eq_16[:4]),
            FadeOut(eq_15[4:7]),
            TransformMatchingShapes(eq_15[7:],eq_16[4:]),
        )

        self.wait(0.5)

        self.play(
            eq_16.animate.scale(0.7).next_to(brand,DOWN,aligned_edge=RIGHT)
        )

        self.wait(0.5)

        eq_17 = MathTex(r'a',r'x^',r'2',r'+',r'b',r'x',r'+',r'c',r'=',r'0').scale(0.9)
        eq_18 = MathTex(r'x_1',r'=',r'{-',r'b',r'+',r'\sqrt{',r'b^',r'2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}').scale(0.9)
        eq_19 = MathTex(r'x_2',r'=',r'{-',r'b',r'-',r'\sqrt{',r'b^',r'2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}').scale(0.9)
        color_eq(eq_17)
        color_eq(eq_18)
        color_eq(eq_19)

        VGroup(eq_17,eq_18,eq_19).arrange(DOWN,buff=1.5).to_edge(LEFT*1.5)

        self.play(
            Write(eq_17)
        )

        self.play(
            FadeIn(eq_18,target_position = eq_17),
        )

        self.play(
            FadeIn(eq_19,target_position = eq_17),
        )


        self.wait()
