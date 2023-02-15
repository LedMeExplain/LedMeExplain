from manim import *

quality_factor = 1
fps = 30

config['pixel_height'] = int(1920/quality_factor)
config['pixel_width'] = int(1080/quality_factor)
config['frame_height'] = 14
config['frame_width'] = 8
config['frame_rate'] = fps

class HolaMundo(Scene):
    def construct(self):
        ## Titulo y subtitulo
        title = Tex(r'Hola Mundo en Manim CE', tex_template = TexFontTemplates.libertine).to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-1.5).set_z_index(2)
        rect_title = SurroundingRectangle(title,buff = 0.4).set_color_by_gradient([LME_A,LIGHT_PINK,LME_B]).set_z_index(2)

        brand = Text(
            "LED Me Explain",
            fill_opacity = 1,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_A,"[3:4]":LME_A,"[5:6]":LME_A} ## Los espacios no cuentan como caracteres
        ).scale(0.4).next_to(rect_title,DOWN,aligned_edge = RIGHT).set_z_index(2)

        subtitle = Tex('Python. Manim CE v0.8.0').scale(0.6).set_opacity(0.6).next_to(rect_title,DOWN,aligned_edge = LEFT).set_z_index(2)

        back_rect = BackgroundRectangle(VGroup(rect_title,brand,subtitle)).set_z_index(1)

        self.add(back_rect,title)
        self.play(Create(rect_title),FadeIn(brand), Write(subtitle))

        code = '''from manim import *

class HolaMundo(Scene):
    def construct(self):
        texto = Text('Hola Mundo!')
        self.play(FadeIn(texto))
        self.play(ApplyWave(texto))
        self.wait()
'''
        rendered_code = Code(code=code, tab_width=4, scale_factor= 0.4, background="window",
                            language="Python", font="Monospace", style='default').next_to(back_rect,DOWN,buff=0.5)
        self.play(Write(rendered_code), run_time = 4)

        carg_circulo = Circle(radius = 0.3, color = LME_A, stroke_width = 8)
        carg_circulo = Circle(radius = 0.3, color = LME_A, stroke_width = 8)
        carg_texto = Text('Cargando ...').scale(0.4).next_to(carg_circulo,DOWN)
        carg = VGroup(carg_circulo,carg_texto).shift(DL)

        self.play(Create(carg_circulo),FadeIn(carg_texto))
        carg_circulo.flip(LEFT)
        self.play(Uncreate(carg_circulo),FadeOut(carg_texto))
        carg_circulo.become(Circle(radius = 0.3, color = RED, stroke_width = 8).move_to(carg_circulo).shift(LEFT*carg_circulo.radius))
        self.play(Create(carg_circulo),FadeIn(carg_texto))
        carg_circulo.flip(LEFT)
        self.play(Uncreate(carg_circulo),FadeOut(carg_texto))
        carg_circulo.become(Circle(radius = 0.3, color = GREEN, stroke_width = 8).move_to(carg_circulo).shift(LEFT*carg_circulo.radius))
        self.play(Create(carg_circulo),FadeIn(carg_texto))
        carg_circulo.flip(LEFT)
        self.play(Uncreate(carg_circulo),FadeOut(carg_texto))

        texto = Text('Hola Mundo!').scale(0.8).move_to(carg)
        rect = RoundedRectangle(corner_radius=0.1,height=3,width=3*16/9,stroke_width=1).move_to(texto)
        self.play(FadeIn(rect))
        self.wait(0.5)
        self.play(FadeIn(texto))
        self.play(ApplyWave(texto))
        self.wait()
