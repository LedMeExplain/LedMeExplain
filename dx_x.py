from manim import *

LME_color = "#27a0b3"

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14
config.frame_width = 8

class dx_x(Scene):
    def construct(self):

        title = MathTex(r'\text{¿Cómo se deriva } \,y = x^x\, \text{?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5)

        rect_title = SurroundingRectangle(title,LME_color,buff = 0.4)

        brand = Text(
        "LED Me Explain",
        fill_opacity = 1,
        color = WHITE,
        font = "Arial Rounded MT Bold",
        t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT)

        self.add(title)
        self.play(Create(rect_title), FadeIn(brand))

        eq_l = [
            r'y',
            r'\ln(y)',
            r'{1 \over y} {dy \over dx}',
            r'{dy \over dx}',
            r'{dy \over dx}',
            r'{dy \over dx}'
        ]

        eq_r = [
            r'x^x',
            r'\ln(x^x)',
            r'\ln(x)+{x \over x}',
            r'y\,(\ln(x)+1)',
            r'x^x\,(\ln(x)+1)',
            r'x^x\ln(x)+x^x'
        ]

        eq_group = Group()

        for i in list(range(len(eq_l))):
            temp_l = MathTex(eq_l[i])
            temp_mid = MathTex(r'=')
            temp_r = MathTex(eq_r[i])
            eq_group.add(temp_l)
            eq_group.add(temp_mid)
            eq_group.add(temp_r)

        eq_group.arrange_in_grid(cols = 3, col_alignments = 'rcl', buff = (0.25,0.8)).shift(LEFT)

        self.play(FadeIn(eq_group[0:3]))

        text_aux_1 = Text('Logaritmo natural a ambos lados', color = RED).scale(0.35)
        text_aux_2 = Text('Derivación implícita', color = TEAL).scale(0.35)
        text_aux_3 = Text('Simplificación', color = YELLOW_D).scale(0.35)
        eq_aux_1 = MathTex(r'x\ln(x)')
        eq_aux_2 = MathTex(r'\ln(x)+1')

        eq_group_aux = Group(eq_aux_1,eq_aux_2,text_aux_1,text_aux_2,text_aux_3)

        for i in [0,3,6,9,12]:
            if i == 0:
                self.play(
                    Write(text_aux_1.next_to(eq_group[i+3],UP,aligned_edge = LEFT), run_time = 0.8)
                )
            if i == 3:
                self.play(
                    Write(text_aux_2.next_to(eq_group[i+3],UP,aligned_edge = LEFT), run_time = 0.8)
                )
            if i == 6:
                self.play(
                    Write(text_aux_3.next_to(eq_group[i+3],UP,aligned_edge = LEFT), run_time = 0.8)
                )

            self.play(
                TransformMatchingShapes(eq_group[i].copy(),eq_group[i+3]),
                TransformMatchingTex(eq_group[i+1].copy(),eq_group[i+4]),
                TransformMatchingTex(eq_group[i+2].copy(),eq_group[i+5])
            )

            if i == 0:
                self.wait()
                eq_aux_1.move_to(eq_group[i+5])
                self.play(eq_group[i+5].animate.become(eq_aux_1))

            if i == 3:
                self.wait()
                eq_aux_2.move_to(eq_group[i+5])
                self.play(eq_group[i+5].animate.become(eq_aux_2))

            self.wait()

        self.play(Indicate(eq_group[15:]))
        self.play(
            FadeOut(eq_group[:15]),
            FadeOut(eq_group_aux),
            eq_group[15:].animate.move_to(ORIGIN+UP*2).scale(1.5)
        )
        self.play(ApplyWave(eq_group[15:]))
        self.wait(0.5)
