from manim import *

## Recordatorio ##
# Usar [spanish]babel en manim/utils/tex_templates.py

quality_factor = 1
fps = 60
config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class senx_2(Scene):
    def construct(self):

        title = MathTex(r'\text{¿Por qué}',r'\,\sen^{2}(x) = {1-\cos(2x) \over 2}\,',r'\text{?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5)
        title[1].set_color(LME_C)
        rect_title = SurroundingRectangle(title,LME_A,buff = 0.4)

        brand = Text(
        "LED Me Explain",
        fill_opacity = 1,
        color = WHITE,
        font = "Arial Rounded MT Bold",
        t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT)

        subtitle = Tex('Trigonometría').scale(0.55).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT)

        self.add(title)
        self.play(Create(rect_title), FadeIn(brand), Write(subtitle))
        self.wait(0.5)

        senx_2 = r'\sen^{2}(x)'
        plus = r'+'
        minus = r'-'
        cosx_2 = r'\cos^{2}(x)'
        cos2x = r'\cos(2x)'
        equal = r'='

        eq_group = Group()

        eq_1 = MathTex(senx_2,plus,cosx_2,equal,'1', tex_template = TexFontTemplates.libertine)
        text_1 = Tex('Identidad Pitagórica').scale(0.6).next_to(eq_1, UP, aligned_edge = LEFT).shift(DOWN*0.1).set_color(RED)
        eq_1_group = Group(text_1,eq_1)
        eq_group.add(eq_1_group)

        eq_2 = MathTex(cos2x,equal,cosx_2,minus,senx_2, tex_template = TexFontTemplates.libertine)
        text_2 = Tex('Coseno del ángulo doble').scale(0.6).next_to(eq_2, UP, aligned_edge = LEFT).shift(DOWN*0.1).set_color(BLUE)
        eq_2_group = Group(text_2,eq_2)
        eq_group.add(eq_2_group)

        eq_3 = MathTex(cos2x,plus,senx_2,equal,cosx_2, tex_template = TexFontTemplates.libertine)
        eq_group.add(eq_3)

        eq_4 = MathTex(senx_2,plus,cos2x,plus,senx_2,equal,'1', tex_template = TexFontTemplates.libertine)
        text_4 = Tex('Despejamos $\sen^{2}(x)$').scale(0.6).next_to(eq_4, UP, aligned_edge = LEFT).shift(DOWN*0.1).set_color(GREEN)
        eq_4_group = Group(text_4,eq_4)
        eq_group.add(eq_4_group)

        eq_5 = MathTex('2',senx_2,plus,cos2x,equal,'1', tex_template = TexFontTemplates.libertine)
        eq_group.add(eq_5)

        eq_6 = MathTex('2',senx_2,equal,'1',minus,cos2x, tex_template = TexFontTemplates.libertine)
        eq_group.add(eq_6)

        eq_7 = MathTex(senx_2,equal,r'{1',minus,cos2x,r'\over','2}', tex_template = TexFontTemplates.libertine)
        eq_group.add(eq_7)

        eq_group.arrange_in_grid(cols = 1, buff = 0.6, cell_alignment = LEFT).shift(DOWN*.7+LEFT*.5)

        eq_2_aux = eq_2.copy().move_to(eq_3)

        eq_5_aux = eq_5.copy().move_to(eq_6)

        self.play(Write(text_1, run_time = 0.8))
        self.play(Write(eq_1,run_time = 0.8))
        self.wait(0.5)
        self.play(Write(text_2, run_time = 0.8))
        self.play(Write(eq_2,run_time = 0.8))
        self.wait(0.5)
        self.play(FadeIn(eq_2_aux, target_position = eq_2))
        self.play(TransformMatchingShapes(eq_2_aux,eq_3,path_arc=PI/2))
        self.wait(0.5)
        self.play(
            Indicate(eq_1[2]),
            Indicate(eq_3[4]), run_time = 2
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(eq_1[0:2].copy(),eq_4[0:2]),
            TransformMatchingShapes(eq_1[3:].copy(),eq_4[5:]),
        )
        self.play(
            TransformMatchingShapes(eq_3[0:3].copy(),eq_4[2:5])
        )
        self.wait(0.5)
        self.play(Write(text_4), run_time = 0.8)
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(eq_4[0].copy(),eq_5[1]),
            TransformMatchingShapes(eq_4[1].copy(),eq_5[2]),
            FadeIn(eq_5[0]),
            FadeOut(eq_4[4].copy(), target_position = eq_5[1]),
            TransformMatchingShapes(eq_4[2].copy(),eq_5[3]),
            TransformMatchingShapes(eq_4[5:].copy(),eq_5[4:]),
        )
        self.wait(0.5)
        self.play(FadeIn(eq_5_aux, target_position = eq_5))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq_5_aux,eq_6,path_arc=PI/2))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(eq_6[0].copy(),eq_7[-1]),
            Create(eq_7[-2]),
            TransformMatchingShapes(eq_6[1:].copy(),eq_7[0:5])
        )
        self.wait()
        self.play(Indicate(eq_7,color = GREEN), run_time = 2)
        self.play(
            FadeOut(eq_group[:-1]),
            eq_7.animate.move_to(ORIGIN+UP*2).scale(1.2)
        )
        self.play(Wiggle(eq_7))
