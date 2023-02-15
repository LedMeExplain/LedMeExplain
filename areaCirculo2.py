from manim import *
from manim_physics import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class areaCirculo2(SpaceScene):
    def construct(self):
        ## Titulo y subtitulo
        title = MathTex(r'\text{¿Por qué el área del círculo es}',r'\,\pi r^2\,',r'\text{?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([PURPLE,LME_A,GREEN]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Método 2. Geometría').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        circle_radius = 1.5
        dr = 0.02
        circle = Circle(radius = circle_radius,color = WHITE, fill_opacity=1).set_stroke(width = 0).shift(LEFT*.7)
        circle_center = circle.get_center()

        c_color = WHITE
        l_color = [GREEN,TEAL,PURPLE]
        r_color = PURE_RED
        c0_color = YELLOW
        c = VGroup()
        l = VGroup()
        for i in range(int(circle_radius/dr)) :
            c.add(Circle(radius = circle_radius - dr*i, stroke_width = dr*200, color = c_color).move_to(circle))
            l.add(Line(start = ORIGIN, end = UP*TAU*(circle_radius - dr*i), stroke_width = dr*100).flip(LEFT).move_to(c[i].get_left()))

        l.set_color_by_gradient(l_color)
        l[0].set_color(c0_color).set_z_index(1)
        c[0].set_z_index(1)

        r = Line(circle_center,circle_center+circle_radius*LEFT,color = r_color).set_z_index(1)
        r_lbl = MathTex(r'r', color = r_color, tex_template = TexFontTemplates.libertine).scale(0.9).next_to(r,UP).set_z_index(1)
        c0_lbl = MathTex(r'2 \pi r', color = c0_color, tex_template = TexFontTemplates.libertine).scale(0.9).next_to(c[0],LEFT).set_z_index(1)

        self.play(FadeIn(c))

        self.play(c[0].animate.set_color(c0_color),run_time = 1)
        self.play(FadeIn(c0_lbl))
        self.play(Create(r))
        self.play(FadeIn(r_lbl))

        # for i in range(int(circle_radius/dr)-1) :
        #     self.play(c[i+1].animate.set_color(l_color),run_time = 0.3)
        #     self.play(c[i+1].animate.become(l[i]),run_time = 0.3)

        self.play(c.animate.become(l),lag_ratio = 1.1 ,run_time = 15, rate_func = rate_functions.ease_in_quad)

        eq_0 = MathTex(r'A =', tex_template = TexFontTemplates.libertine).next_to(brand,DOWN,buff=1,aligned_edge=RIGHT).shift(LEFT*3)
        eq_1 = MathTex(r'{\,\,\,b\,\,\,',r'\,\,h\,\,',r'\over',r'2', tex_template = TexFontTemplates.libertine).next_to(eq_0,RIGHT,buff=0.2)
        eq_2 = MathTex(r'{2',r'\pi r\,\,',r'\,r',r'\over',r'2', tex_template = TexFontTemplates.libertine).move_to(eq_1)
        eq_2[0].set_color(c0_color)
        eq_2[1].set_color(c0_color)
        eq_2[2].set_color(r_color)
        eq_3 = MathTex(r'\pi',r'r^2', tex_template = TexFontTemplates.libertine).next_to(eq_0,RIGHT,buff=0.2,aligned_edge=DOWN)

        self.play(
            Write(eq_0),
            Write(eq_1)
        )
        self.wait(0.5)
        self.play(
            FadeOut(eq_1[0],shift = UP),
            FadeIn(eq_2[0:2],target_position = c0_lbl)
        )
        self.wait(0.5)
        self.play(
            FadeOut(eq_1[1],shift = UP),
            FadeIn(eq_2[2],target_position = r_lbl)
        )
        self.wait(0.5)
        self.play(
            FadeOut(eq_1[2:]),
            FadeOut(eq_2[0])
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(eq_2[1:3],eq_3[:])
        )

        self.wait()

        self.play(Indicate(VGroup(eq_3,eq_0),color=GREEN), run_time = 2)

        self.wait()
