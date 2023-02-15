from manim import *
import random
from manim_physics import *

quality_factor = 1
fps = 250

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class pendulo4(SpaceScene):
    i_color = 0
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¡Especial 4000 seguidores!', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([YELLOW, GOLD]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Péndulo Cuádruple').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        def color_updater(mob,dt):
            times_per_second = 15

            if self.i_color == int(config['frame_rate']/times_per_second):
                mob.set_color_by_gradient([utils.color.random_color(),utils.color.random_color()])
                self.i_color = 0
            else :
                self.i_color = self.i_color + 1

            return mob

        rect_title.add_updater(color_updater)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        p = MultiPendulum(
            UP*4+RIGHT*0.1,
            UP*6+RIGHT*0.3,
            UP*7.5+RIGHT*0.7, # positions of the bobs.
            UP*10+RIGHT, # positions of the bobs.
            pivot_point = UP*3+LEFT*.5
        )

        colors_b = [TEAL,RED,PURPLE,GREEN]

        p.bobs[0].set_color(colors_b[0])
        p.bobs[1].set_color(colors_b[1])
        p.bobs[2].set_color(colors_b[2])
        p.bobs[3].set_color(colors_b[3])

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

        self.add(TracedPath(p.bobs[0].get_center, stroke_color=colors_b[0]))
        self.add(TracedPath(p.bobs[1].get_center, stroke_color=colors_b[1]))
        self.add(TracedPath(p.bobs[2].get_center, stroke_color=colors_b[2]))
        self.add(TracedPath(p.bobs[3].get_center, stroke_color=colors_b[3]))
        self.wait(30)

##############################################
## CODIGO PARA ALTERAR VELOCIDAD DE UPDATER ##
##############################################
# class prueba(Scene):
#     i = 0
#
#     def construct(self):
#         circle = Circle().set_color_by_gradient([YELLOW, GOLD])
#
#         def color_updater(mob,dt):
#             if prueba.i == int(config['frame_rate']/4):
#                 mob.set_color_by_gradient([utils.color.random_color(),utils.color.random_color()])
#                 prueba.i = 0
#             else :
#                 prueba.i = prueba.i + 1
#             return mob
#
#         circle.add_updater(color_updater)
#         self.add(circle)
#         self.wait(5)
