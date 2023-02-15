from manim import *
from manim_physics import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class campoMagnetico1(SpaceScene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo se ve un campo magnético?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A,YELLOW, ORANGE]).set_z_index(2)

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

        eq_1 = MathTex(r"\mathbf{B}(\mathbf{r})={\mu_0 \over 4\pi}\int{\mathbf{J} \times (\mathbf{r}-\mathbf{r'}) \over \norm{\mathbf{r}-\mathbf{r'}}^3} \, dV").set_z_index(2).scale(0.8).next_to(brand,DOWN,aligned_edge=RIGHT)
        back_eq_1 = BackgroundRectangle(eq_1,buff=0.1).set_opacity(0.6).set_z_index(1)

        self.play(
            FadeIn(back_eq_1),
            FadeIn(eq_1)
        )
        self.wait(0.5)

        current1 = Current(LEFT * 2.5 + UP)
        current2 = Current(RIGHT+UP*3, direction=IN)
        current3 = Current(DOWN*2, direction=IN)

        field1 = CurrentMagneticField(
            current1,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )

        field2 = CurrentMagneticField(
            current1,
            current2,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )

        field3 = CurrentMagneticField(
            current1,
            current2,
            current3,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )

        charge1 = Charge(-1, LEFT + DOWN*7)
        charge2 = Charge(-1, RIGHT*5)
        charge3 = Charge(-1, UP*7+LEFT*5)

        self.play(
            FadeIn(current1),
            FadeIn(field1)
        )
        self.wait(0.5)
        self.play(
            field1.animate.become(field2),
            FadeIn(current2)
        )
        self.wait(0.5)
        self.play(
            field1.animate.become(field3),
            FadeIn(current3)
        )

        field1.add_updater(
            lambda mob:
                mob.become(
                    CurrentMagneticField(
                        current1,
                        current2,
                        current3,
                        y_min=-7.5, y_max=7.5,
                        x_min=-4.5, x_max=4.5
                    )
                )
        )

        self.play(current1.animate.shift(RIGHT*2.5))
        self.wait(0.5)
        self.play(
            current1.animate(run_time = 2).move_to(3.5*UP+2*LEFT),
            current2.animate(run_time = 1).move_to(ORIGIN),
            current3.animate(run_time = 0.5).move_to(DOWN*2+LEFT)
        )
        self.wait()
        self.play(
            current1.animate.shift(DOWN*6+RIGHT*2),
            current2.animate.shift(UP*2),
            current3.animate.shift(UL*2)
        )

        self.wait()

        #
        # def field_move_UP(mob,dt):
        #     field3.nudge(mob,dt*5)
        #     mob.shift(dt*UP*1)
        #     return mob
        #
        # def field_move_LEFT(mob,dt):
        #     field3.nudge(mob,dt*5)
        #     mob.shift(dt*LEFT*2)
        #     return mob
        #
        # def field_move_DR(mob,dt):
        #     field3.nudge(mob,dt*5)
        #     mob.shift(dt*DR*2.5)
        #     return mob
        #
        # self.wait(0.5)
        #
        # self.add(charge1)
        # charge1.add_updater(field_move_UP)
        #
        # self.wait(9)
        #
        # charge1.remove_updater(field_move_UP)
        # self.remove(charge1)
        #
        # self.add(charge2)
        # charge2.add_updater(field_move_LEFT)
        #
        # self.wait(6)
        #
        # charge2.remove_updater(field_move_UP)
        # self.remove(charge2)
        #
        # self.add(charge3)
        # charge3.add_updater(field_move_DR)
        #
        # self.wait(6)
        #
        # charge3.remove_updater(field_move_DR)
        # self.remove(charge3)
