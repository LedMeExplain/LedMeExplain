from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class perimetroCirculo1(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = MathTex(r'\text{¿Por qué el perímetro del círculo es}',r'\, 2 \pi r \,',r'\text{?}', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A,PINK]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Metodo 1. Geometría').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        circle_color = RED
        per_color = [RED,GREEN,MAROON]
        d_color = YELLOW_D

        circle = Circle(radius = 1.5, color = circle_color, fill_opacity = 1).set_sheen(-0.5, DR).shift(RIGHT*.3)

        self.play(DrawBorderThenFill(circle))
        self.wait()

        d = Line(circle.get_top(),circle.get_bottom(),color = d_color)
        d_lbl = Tex('D', tex_template = TexFontTemplates.libertine, color = d_color).next_to(d,RIGHT)

        self.play(Create(d))
        self.play(FadeIn(d_lbl))
        self.wait()

        per = Circle(radius = circle.radius).set_color_by_gradient(per_color).move_to(circle)
        per_1 = Line(ORIGIN,DOWN*TAU*circle.radius).set_color_by_gradient(per_color).move_to(circle.get_left())
        per_lbl = Tex('P', tex_template = TexFontTemplates.libertine, color = GREEN).next_to(per_1,LEFT,buff = 1)

        self.play(Create(per))
        self.wait(0.5)
        self.play(per.animate.become(per_1))
        self.play(FadeIn(per_lbl))
        self.wait()

        self.play(circle.animate.set_fill(opacity = 0))
        self.wait(0.5)

        tick = Line(per.get_top()+LEFT*.05,per.get_top()+RIGHT*.05, stroke_width = 2).move_to(per.get_top())
        dashed_tick = DashedLine(tick.get_center(),tick.get_center()+RIGHT*3).set_opacity(0.6)

        tick_group = VGroup(tick,dashed_tick)
        circle_group = VGroup(circle,d,d_lbl)
        lbl = Tex('1', tex_template = TexFontTemplates.libertine, color = d_color).next_to(tick.get_center()+DOWN*circle.radius,LEFT,buff = 0.3)

        self.play(Create(tick_group),run_time = 0.5)
        self.play(circle_group.animate.shift(UP*(PI*circle.radius-circle.radius)))
        self.play(FadeIn(lbl))
        self.wait(0.2)

        tick_group2 = tick_group.copy().shift(DOWN*circle.radius*2)
        circle_group2 = circle_group.copy().shift(DOWN*circle.radius*2)
        lbl_2 = Tex('2', tex_template = TexFontTemplates.libertine, color = d_color).next_to(circle_group2,LEFT,buff = 0.3)

        self.play(Create(tick_group2),run_time = 0.5)
        self.play(FadeIn(circle_group2, target_position = circle_group))
        self.play(FadeIn(lbl_2))
        self.wait(0.2)

        tick_group3 = tick_group2.copy().shift(DOWN*circle.radius*2)
        circle_group3 = circle_group2.copy().shift(DOWN*circle.radius*2)
        lbl_3 = Tex('3', tex_template = TexFontTemplates.libertine, color = d_color).next_to(circle_group3,LEFT,buff = 0.3)

        self.play(Create(tick_group3),run_time = 0.5)
        self.play(FadeIn(circle_group3, target_position = circle_group2))
        self.play(FadeIn(lbl_3))
        self.wait(0.2)

        tick_group4 = tick_group3.copy().shift(DOWN*circle.radius*2)
        circle_4 = Arc(radius=circle.radius,start_angle = PI/2-np.arccos(7-TAU),angle = 2*np.arccos(7-TAU)).set_color(RED).next_to(circle_group3,DOWN,buff=0)
        d_4 = Line(circle_4.get_top(),circle_4.get_bottom(),color = d_color)
        circle_group4 = VGroup(circle_4,d_4)
        lbl_4 = Tex('0.14159265...', tex_template = TexFontTemplates.libertine, color = d_color).scale(0.8).next_to(circle_group4,LEFT,buff = 0.6)

        self.play(Create(tick_group4),run_time = 0.5)
        self.play(FadeIn(circle_group4, target_position = circle_group3))
        self.play(FadeIn(lbl_4))
        self.wait(0.2)

        tick_group5 = tick_group4.copy().shift(DOWN*circle.radius*2*(PI-3))

        self.play(Create(tick_group5),run_time = 0.5)
        self.wait()

        eq_1 = MathTex(r'P',r'=',r'\pi',r'D', tex_template = TexFontTemplates.libertine).move_to(per_lbl).shift(LEFT*.3)
        eq_1[0].set_color(GREEN)
        eq_1[2].set_color(d_color)
        eq_1[3].set_color(d_color)

        self.play(TransformMatchingShapes(per_lbl[0],eq_1[0]))
        self.play(Write(eq_1[1]))
        self.play(
            FadeOut(lbl,target_position = eq_1[2]),
            FadeOut(lbl_2,target_position = eq_1[2]),
            FadeOut(lbl_3,target_position = eq_1[2]),
            FadeOut(lbl_4,target_position = eq_1[2]),
            FadeIn(eq_1[2])
        )
        self.play(
            FadeOut(circle_group[2].copy(),target_position = eq_1[3]),
            FadeOut(circle_group2[2].copy(),target_position = eq_1[2]),
            FadeOut(circle_group3[2].copy(),target_position = eq_1[2]),
            FadeIn(eq_1[3],target_position=d_lbl))
        self.wait()

        r_color = PINK
        r_line = Line(circle_group2[1].get_top(),circle_group2[1].get_center(),color=r_color)
        r_lbl = Tex('r', tex_template = TexFontTemplates.libertine, color = r_color).next_to(r_line,LEFT)

        eq_2 = MathTex(r'D',r'=',r'2',r'r', tex_template = TexFontTemplates.libertine).scale(0.8).next_to(eq_1,DOWN,buff=1)
        eq_2[0].set_color(d_color)
        eq_2[3].set_color(r_color)
        eq_3 = MathTex(r'P',r'=',r'\pi',r'2',r'r', tex_template = TexFontTemplates.libertine).move_to(eq_1,aligned_edge=LEFT)
        eq_3[0].set_color(GREEN)
        eq_3[2].set_color(d_color)
        eq_3[4].set_color(r_color)
        eq_4 = MathTex(r'P',r'=',r'2',r'\pi',r'r', tex_template = TexFontTemplates.libertine).move_to(eq_1,aligned_edge=LEFT)
        eq_4[0].set_color(GREEN)
        eq_4[3].set_color(d_color)
        eq_4[4].set_color(r_color)

        self.play(
            Create(r_line),
            FadeIn(r_lbl)
        )
        self.wait(0.5)
        self.play(Write(eq_2))
        self.wait(0.5)
        self.play(
            FadeOut(eq_1[3],shift=UP),
            FadeIn(eq_3[3:],target_position = eq_2[2:])
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(eq_1[2],eq_4[3]),
            TransformMatchingShapes(eq_3[3],eq_4[2]),
            TransformMatchingShapes(eq_3[4],eq_4[4])
        )
        self.play(Indicate(eq_4[2:],color=WHITE))
        self.wait(0.5)
