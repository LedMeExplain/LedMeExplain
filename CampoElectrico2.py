from manim import *
from manim_physics import *

quality_factor = 2
fps = 10

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class campoMagnetico1(SpaceScene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo se ve un electrón en un campo eléctrico?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A,YELLOW]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Electromagnetismo').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        charge1 = Charge(-1,LEFT * 2.5 + UP)
        charge2 = Charge(2,RIGHT+UP*3)
        charge3 = Charge(1,DOWN*2)

        field1 = ElectricField(
            charge1,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )

        field2 = ElectricField(
            charge1,
            charge2,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )

        field3 = ElectricField(
            charge1,
            charge2,
            charge3,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )

        charge4 = Charge(-1, LEFT + DOWN*7)
        charge5 = Charge(-1, RIGHT*5)
        charge6 = Charge(-1, UP*7+LEFT*5)

        self.play(
            FadeIn(charge1),
            FadeIn(field1)
        )
        self.wait(0.5)
        self.play(
            field1.animate.become(field2),
            FadeIn(charge2)
        )
        self.wait(0.5)
        self.play(
            field1.animate.become(field3),
            FadeIn(charge3)
        )

        def field_move_UP(mob,dt):
            field3.nudge(mob,dt*5)
            mob.shift(dt*UP*1)
            return mob

        def field_move_LEFT(mob,dt):
            field3.nudge(mob,dt*5)
            mob.shift(dt*LEFT*2)
            return mob

        def field_move_DR(mob,dt):
            field3.nudge(mob,dt*5)
            mob.shift(dt*DR*2.5)
            return mob

        self.wait(0.5)

        self.add(charge4)
        charge4.add_updater(field_move_UP)

        self.wait(9)

        charge4.remove_updater(field_move_UP)
        self.remove(charge4)

        self.add(charge5)
        charge5.add_updater(field_move_LEFT)

        self.wait(6)

        charge5.remove_updater(field_move_UP)
        self.remove(charge5)

        self.add(charge6)
        charge6.add_updater(field_move_DR)

        self.wait(6)

        charge6.remove_updater(field_move_DR)
        self.remove(charge6)
