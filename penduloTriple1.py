from manim import *
from manim_physics import *

quality_factor = 1
fps = 200

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class penduloTriple1(SpaceScene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo se ve el péndulo triple?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A,RED,LME_B,GREEN]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Mecánica clásica').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        p = MultiPendulum(
            UP*3+RIGHT*0.1,
            UP*4.5+RIGHT*0.3,
            UP*6.5+RIGHT*0.7, # positions of the bobs.
            pivot_point = UP*2+LEFT*.5
        )
        p.bobs[0].set_color(RED)
        p.bobs[1].set_color(GREEN)
        p.bobs[2].set_color(TEAL)

        dot0 = Dot(radius=0.1).move_to(p.pivot_point)

        self.play(GrowFromCenter(dot0))
        self.play(Create(p,lag_ratio=0.5), run_time = 2)
        # self.play(Create(p.rods[0]))
        # self.play(GrowFromCenter(p.bobs[0]))
        # self.play(Create(p.rods[1][0]))
        # self.play(GrowFromCenter(p.bobs[1]))
        # self.play(Create(p.rods[1][1]))
        # self.play(GrowFromCenter(p.bobs[2]))
        self.wait()

        self.make_rigid_body(p.bobs) # make the bobs fall free.
        p.start_swinging() # attach them to their pivots.

        self.add(TracedPath(p.bobs[0].get_center,stroke_color=RED))
        self.add(TracedPath(p.bobs[1].get_center, stroke_color=GREEN))
        self.add(TracedPath(p.bobs[2].get_center, stroke_color=TEAL))
        self.wait(30)
