from manim import *
from manim_physics import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class CampoElectrico1(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'¿Cómo se ve un campo eléctrico?', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A,GREEN,LME_B]).set_z_index(2)
        back_title = BackgroundRectangle(rect_title).set_z_index(1)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Electromagnetismo').scale(0.55).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        self.add(back_title,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))
        self.wait()

        ## Desarrollo del video
        eq_1 = MathTex(r"\mathbf{E}(\mathbf{r})={1 \over 4\pi\epsilon_0}\sum_{i=1}^{n}{q_i \over \norm{\mathbf{r}-\mathbf{r_i'}}^3} \left( \mathbf{r} - \mathbf{r_i'} \right)").set_z_index(2).scale(0.8).next_to(brand,DOWN,aligned_edge=RIGHT)
        back_eq_1 = BackgroundRectangle(eq_1,buff=0.1).set_opacity(0.6).set_z_index(1)

        self.play(
            FadeIn(back_eq_1),
            FadeIn(eq_1)
        )
        self.wait(0.5)

        charge1 = Charge(-1, 1.5*LEFT + 2*DOWN)
        charge2 = Charge(2, 0.5*RIGHT)
        charge3 = Charge(-1, 1.5*LEFT + 2*UP)
        field1 = ElectricField(charge1,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )
        field2 = ElectricField(charge1, charge2,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )
        field3 = ElectricField(charge1, charge2, charge3,
            y_min=-7.5, y_max=7.5,
            x_min=-4.5, x_max=4.5
        )
        self.play(
            FadeIn(charge1),
            FadeIn(field1)
        )
        self.wait()
        self.play(
            FadeIn(charge2),
            field1.animate.become(field2)
        )
        self.wait()
        self.play(
            FadeIn(charge3),
            field1.animate.become(field3)
        )
        self.wait()

        field1.add_updater(lambda mob:
            mob.become(ElectricField(charge1, charge2, charge3,
                    y_min=-7.5, y_max=7.5,
                    x_min=-4.5, x_max=4.5
                )
            )
        )

        self.play(charge2.animate.shift(LEFT*2))
        self.wait(0.5)
        self.play(
            charge1.animate(run_time = 2).move_to(3*UP+2.5*LEFT),
            charge2.animate(run_time = 1).move_to(1.5*UP),
            charge3.animate(run_time = 3).move_to(2.5*DOWN)
        )
        self.wait(0.5)
        self.play(
            charge1.animate.shift(DOWN*2),
            charge3.animate.shift(LEFT*1.5)
        )

        self.wait()
