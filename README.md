<p align="center">
    <a href="https://www.youtube.com/channel/UCD_uHRFNcycLyFDtHSOgMOA"><img src="https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png"></a>
    <br />
    <br />
    <a href="https://twitter.com/ledmeexplain"><img src="https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40ledmeexplain" alt="Twitter"></a>
    <a href="https://www.youtube.com/channel/UCD_uHRFNcycLyFDtHSOgMOA"><img src ="https://img.shields.io/youtube/channel/subscribers/UCD_uHRFNcycLyFDtHSOgMOA?label=Suscriptores&style=social" alt="Youtube"></a>
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/LedMeExplain/LedMeExplain">
    <br />
    <br />
    <i>Explicaciones científicas y desarrollos matemáticos</i>
</p>
<hr />
<br/>
<h2 align="center">Próximamente, tutoriales de Manim</h2>



```python
LME_color = "#27a0b3"

class ExpZ_1(Scene):
    def construct(self):

        ##------------------------------
        ## Logo LME en la esquina
        ##------------------------------
        brand = Text(
            "LED Me Explain",
            fill_opacity = 0.5,
            color = WHITE,
            font = "Arial Rounded MT Bold",
            t2c = {"[:1]":LME_color,"[3:4]":LME_color,"[5:6]":LME_color} ## Los espacios no cuentan como caracteres
        ).scale(0.4).to_edge(DR)
        # Añade el logo
        self.add(brand)
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## Titulo y subtitulo del video
        ##------------------------------
        title = Tex( # Crea el título
            r"¿Cómo se ve la transformación ", r'$z$',r'$\,\rightarrow\,$',r'$e^z$',r' ?',
        ).scale_to_fit_width(config["frame_width"]-4)
        title_math = MathTex(r'z',r'\rightarrow',r'e^z', tex_template = TexFontTemplates.libertine).move_to(title[2], aligned_edge = DOWN).scale(1.2).shift(RIGHT*.1)
        title_math[0].set_color(TEAL_C)
        title_math[2].set_color(PURPLE_C)

        # Crea el rectangulo que rodea al grupo
        frameTitle = SurroundingRectangle(title, LME_color, buff = 1)

        subtitle = Text( # Crea el subtítulo
            "Variable Compleja",
            color = LIGHT_GREY
        ).scale(0.6).next_to(frameTitle,DOWN, aligned_edge = RIGHT)


        # Aparece el titulo
        self.play(
            FadeIn(title[0]),
            FadeIn(title[4]),
            FadeIn(title_math)
        )
        # Crea el rectangulo
        self.play(Create(frameTitle))
        # Escribe el subtitulo
        self.play(Write(subtitle) , run_time = 0.7)
        self.wait(1.5) # Espera un momento
        # Desaparece el titulo, subtitulo y el rectangulo
        self.play(
            FadeOut(title[0], scale=0.7),
            FadeOut(title[4], scale=0.7),
            FadeOut(title_math, scale = 0.7),
            FadeOut(subtitle, scale=0.7),
            FadeOut(frameTitle)
        )
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## 1. Título, enunciado y animación del problema
        ##------------------------------
        header = Title(r'Esta es la transformación ',r'$z$',r'$\,\rightarrow\,$',r'$e^z$', scale_factor = 1.5).set_z_index(1)
        header_math = MathTex(r'z',r'\rightarrow',r'e^z', tex_template = TexFontTemplates.libertine).move_to(header[2], aligned_edge = DOWN).scale(1.4).shift(UR*0.1).set_z_index(1)
        header_math[0].set_color(TEAL_C)
        header_math[2].set_color(PURPLE_C)

        self.play(
            FadeIn(header[0]),
            FadeIn(header[-1]),
            FadeIn(header_math)
        )
        self.wait()

        square_1 = Square(color = TEAL_C)
        rectPlane = NumberPlane(x_range=(-8, 8, 1)).set_opacity(0.3)

        lbl_x_axis = MathTex(r'Re', tex_template = TexFontTemplates.libertine).next_to(RIGHT*5,UP).set_opacity(0.3)
        lbl_y_axis = MathTex(r'Im', tex_template = TexFontTemplates.libertine).next_to(UP*2,RIGHT).set_opacity(0.3)
        lbl_x1 = Tex(r'$-1$', tex_template = TexFontTemplates.libertine).next_to(LEFT,DR*0.2,aligned_edge = LEFT).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_x2 = Tex(r'$1$', tex_template = TexFontTemplates.libertine).next_to(RIGHT,DR*0.2,aligned_edge = LEFT).shift(RIGHT*0.1).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_y1 = Tex(r'$-1$', tex_template = TexFontTemplates.libertine).next_to(DOWN,UR*0.2,aligned_edge = LEFT).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_y2 = Tex(r'$1$', tex_template = TexFontTemplates.libertine).next_to(UP,UR*0.2,aligned_edge = LEFT).shift(RIGHT*0.1).scale(0.7).set_opacity(0.7).set_z_index(1)

        self.play(Create(rectPlane, run_time=3, lag_ratio=0.1))
        self.play(
            FadeIn(lbl_x_axis),
            FadeIn(lbl_y_axis)
        )
        self.play(Create(square_1))
        self.play(
            FadeIn(lbl_x1),
            FadeIn(lbl_x2),
            FadeIn(lbl_y1),
            FadeIn(lbl_y2)
        )
        self.wait(2)

        self.play(
            FadeOut(rectPlane),
            FadeOut(lbl_x_axis),
            FadeOut(lbl_y_axis),
            FadeOut(lbl_x1),
            FadeOut(lbl_x2),
            FadeOut(lbl_y1),
            FadeOut(lbl_y2)
        )

        header_mini = Tex(r'$z$',r'$\,\rightarrow\,$',r'$e^z$', tex_template = TexFontTemplates.libertine).scale(1.5).to_edge(UL*1.5).set_z_index(1)
        header_mini[0].set_color(TEAL_C)
        header_mini[2].set_color(PURPLE_C)

        self.play(
            ApplyMethod(header_math.become,header_mini),
            FadeOut(header[0], target_position = header_mini, scale = 0.5),
            FadeOut(header[-1], target_position = header_mini, scale = 0.5)
        )

        polarPlane = PolarPlane(radius_max = 8).set_opacity(0.3).set_fill(opacity=0)
        line_a1 = Line(ORIGIN, polarPlane.polar_to_point(4,1),stroke_width=2).set_opacity(0.3).set_z_index(1)
        line_a2 = Line(ORIGIN, polarPlane.polar_to_point(4,TAU-1),stroke_width=2).set_opacity(0.3).set_z_index(1)
        lbl_a1 = Tex(r'$1$ rad', tex_template = TexFontTemplates.libertine).move_to(line_a1.get_end()+UP*0.2).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_a2 = Tex(r'$-1$ rad', tex_template = TexFontTemplates.libertine).move_to(line_a2.get_end()+DOWN*0.2).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_r1 = Tex(r'$e^{-1}$', tex_template = TexFontTemplates.libertine).move_to(polarPlane.polar_to_point(np.exp(-1),0)+DOWN*0.2+RIGHT*0.3).scale(0.7).set_opacity(0.7).set_z_index(1)
        lbl_r2 = Tex(r'$e^1$', tex_template = TexFontTemplates.libertine).move_to(polarPlane.polar_to_point(np.exp(1),0)+DOWN*0.2+RIGHT*0.1).scale(0.7).set_opacity(0.7).set_z_index(1)

        lbl_y_axis.next_to(UP*3,RIGHT)
        self.play(Create(polarPlane), run_time=3, lag_ratio=0.1)
        self.play(
            FadeIn(lbl_x_axis),
            FadeIn(lbl_y_axis)
        )

        def expZTransform(mobject):
            mobject.apply_complex_function(lambda z: np.exp(z)) #lambda z: np.exp(z)-np.exp((z-z.conjugate())/2) Convierte el primer cuadrante en un circulo
            mobject.set_color(PURPLE_C)
            return mobject

        self.play(ApplyFunction(expZTransform,square_1), run_time = 2)
        self.play(
            Create(line_a1),
            Create(line_a2),
            FadeIn(lbl_a1),
            FadeIn(lbl_a2),
            FadeIn(lbl_r1),
            FadeIn(lbl_r2)
        )
        self.wait(2)
        self.play(
            FadeOut(line_a1),
            FadeOut(line_a2),
            FadeOut(lbl_x_axis),
            FadeOut(lbl_y_axis),
            FadeOut(lbl_a1),
            FadeOut(lbl_a2),
            FadeOut(lbl_r1),
            FadeOut(lbl_r2),
            FadeOut(polarPlane),
            FadeOut(square_1),
            FadeOut(header_math)
        )

```
