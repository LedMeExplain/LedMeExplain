from manim import *

LME_color = "#27a0b3"

class Demostracion_1(Scene):
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
        title = Text( # Crea el título
            "¿De dónde sale la Fórmula General?",
            color = WHITE
        ).scale_to_fit_width(config["frame_width"]-4)

        # Crea el rectangulo que rodea al grupo
        frameTitle = SurroundingRectangle(title, LME_color, buff = 1)

        subtitle = Text( # Crea el subtítulo
            "Álgebra",
            color = LIGHT_GREY
        ).scale(0.6).next_to(frameTitle,DOWN, aligned_edge = RIGHT)


        # Aparece el titulo
        self.play(Write(title) , run_time = 0.8)
        # Crea el rectangulo
        self.play(Create(frameTitle))
        # Escribe el subtitulo
        self.play(Write(subtitle) , run_time = 0.7)
        self.wait(1.5) # Espera un momento
        # Desaparece el titulo, subtitulo y el rectangulo
        self.play(
            FadeOut(title, scale=0.7),
            FadeOut(subtitle, scale=0.7),
            FadeOut(frameTitle),
            run_time = 0.8
        )
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## Desarrollo del video
        ##------------------------------

        header = Title( # Crea el título
            'Esta es la Fórmula General',
            scale_factor = 1.5
        )

        eq_1 = MathTex( # Crea la ecuación general, ecuación 1
            r'x',r'=',r'{-',r'b',r'\pm',r'\sqrt{',r'b',r'^2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}',
            tex_template = TexFontTemplates.libertine # Tipo de letra
        ).scale(2)

        eq_1.set_color_by_tex('a',RED)
        eq_1.set_color_by_tex('b',GREEN)
        eq_1.set_color_by_tex('c',BLUE)

        eq_2 = MathTex( # Crea la ecuación de segundo grado arbitraria espaciada
            r'a',r'x',r'^2',r'\:\:',r'+',r'\:\:',r'b',r'x',r'\:\:',r'+',r'\:\:',r'c',r'\:\:',r'=',r'0',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_2.set_color_by_tex('a',RED)
        eq_2.set_color_by_tex('b',GREEN)
        eq_2.set_color_by_tex('c',BLUE)

        eq_3 = MathTex( # Crea la ecuación de segundo grado arbitraria sin espacios
            r'a',r'x',r'^2',r'+',r'b',r'x',r'+',r'c',r'=',r'0',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_3.set_color_by_tex('a',RED)
        eq_3.set_color_by_tex('b',GREEN)
        eq_3.set_color_by_tex('c',BLUE)

        eq_4 = MathTex(# Divide toda la ecuación sobre a
            r'{a',r'x',r'^2',r'+',r'b',r'x',r'+',r'c',r'=',r'0',r'\over',r'a}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_4.set_color_by_tex('a',RED)
        eq_4.set_color_by_tex('b',GREEN)
        eq_4.set_color_by_tex('c',BLUE)

        eq_5 = MathTex(
            r'{a',r'x',r'^2',r'+',r'b',r'x',r'+',r'c',r'\over',r'a}',r'=',r'0',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_5.set_color_by_tex('a',RED)
        eq_5.set_color_by_tex('b',GREEN)
        eq_5.set_color_by_tex('c',BLUE)

        eq_6 = MathTex(
            r'x',r'^2',r'+',r'{b',r'\over',r'a}',r'x',r'+',r'{c',r'\over',r'a}',r'=',r'0',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_6.set_color_by_tex('a',RED)
        eq_6.set_color_by_tex('b',GREEN)
        eq_6.set_color_by_tex('c',BLUE)

        eq_7 = MathTex(
            r'x',r'^2',r'+',r'{b',r'\over',r'a}',r'x',r'+',r'\left(',r'b',r'\over',r'2',r'a',r'\right)',r'^2',
            r'-',r'\left(',r'b',r'\over',r'2',r'a',r'\right)',r'^2',r'+',r'{c',r'\over',r'a}',r'=',r'0',
            tex_template = TexFontTemplates.libertine
        ).scale_to_fit_width(config["frame_width"]-2)

        eq_7.set_color_by_tex('a',RED)
        eq_7.set_color_by_tex('b',GREEN)
        eq_7.set_color_by_tex('c',BLUE)

        eq_8 = MathTex(
            r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)',r'^2',
            r'-',r'\left(',r'b',r'\over',r'2',r'a',r'\right)',r'^2',r'+',r'{c',r'\over',r'a}',r'=',r'0',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_8.set_color_by_tex('a',RED)
        eq_8.set_color_by_tex('b',GREEN)
        eq_8.set_color_by_tex('c',BLUE)

        eq_9 = MathTex(
            r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)',r'^2',r'=',
            r'\left(',r'b',r'\over',r'2',r'a',r'\right)',r'^2',r'-',r'{c',r'\over',r'a}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_9.set_color_by_tex('a',RED)
        eq_9.set_color_by_tex('b',GREEN)
        eq_9.set_color_by_tex('c',BLUE)

        eq_10 = MathTex(
            r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)',r'^2',r'=',
            r'{b',r'^2',r'\over',r'4',r'a',r'^2}',r'-',r'{c',r'\over',r'a}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_10.set_color_by_tex('a',RED)
        eq_10.set_color_by_tex('b',GREEN)
        eq_10.set_color_by_tex('c',BLUE)

        eq_11 = MathTex(
            r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)',r'^2',r'=',
            r'{b',r'^2',r'\over',r'4',r'a',r'^2}',r'-',r'{c',r'\over',r'a}',r'\left(',r'{4',r'a',r'\over',r'4',r'a}',r'\right)',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_11.set_color_by_tex('a',RED)
        eq_11.set_color_by_tex('b',GREEN)
        eq_11.set_color_by_tex('c',BLUE)

        eq_12 = MathTex(
            r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)',r'^2',r'=',
            r'{b',r'^2',r'\over',r'4',r'a',r'^2}',r'-',r'{4',r'a',r'c',r'\over',r'4',r'a',r'^2}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_12.set_color_by_tex('a',RED)
        eq_12.set_color_by_tex('b',GREEN)
        eq_12.set_color_by_tex('c',BLUE)


        eq_13 = MathTex(
            r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)',r'^2',r'=',r'{b',r'^2',r'-',r'4',r'a',r'c',r'\over',r'4',r'a',r'^2}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_13.set_color_by_tex('a',RED)
        eq_13.set_color_by_tex('b',GREEN)
        eq_13.set_color_by_tex('c',BLUE)


        eq_14 = MathTex(
            r'\sqrt{',r'\left(',r'x',r'+',r'{b',r'\over',r'2',r'a}',r'\right)',r'^2}',r'=',r'\pm',r'\sqrt',r'{b',r'^2',r'-',r'4',r'a',r'c',r'\over',r'4',r'a',r'^2}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_14.set_color_by_tex('a',RED)
        eq_14.set_color_by_tex('b',GREEN)
        eq_14.set_color_by_tex('c',BLUE)

        eq_15 = MathTex(
            r'x',r'+',r'{b',r'\over',r'2',r'a}',r'=',r'{\pm',r'\sqrt{',r'b',r'^2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_15.set_color_by_tex('a',RED)
        eq_15.set_color_by_tex('b',GREEN)
        eq_15.set_color_by_tex('c',BLUE)

        eq_16 = MathTex(
            r'x',r'=',r'-',r'{b',r'\over',r'2',r'a}',r'{\pm',r'\sqrt{',r'b',r'^2',r'-',r'4',r'a',r'c}',r'\over',r'2',r'a}',
            tex_template = TexFontTemplates.libertine
        ).scale(2)

        eq_16.set_color_by_tex('a',RED)
        eq_16.set_color_by_tex('b',GREEN)
        eq_16.set_color_by_tex('c',BLUE)


        text_2 = Text('Iniciamos con una ecuación de segundo grado arbitraria').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_3 = Text('Dividimos entre el coeficiente del término cuadrático').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_7 = Text('Completamos el Trinomio Cuadrado Perfecto').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_9 = Text('Finalmente, despejamos la ecuación para x').to_edge(UP*1.5).scale_to_fit_width(config["frame_width"]-2)
        text_16 = Tex('Q.E.D.').next_to(eq_1,DR)

        frame_a = SurroundingRectangle(eq_2[0:3],RED,buff=0.3)
        frame_b = SurroundingRectangle(eq_2[6:8],GREEN,buff=0.3)
        frame_c = SurroundingRectangle(eq_2[11],BLUE,buff=0.3)

        frame_bin_1 = SurroundingRectangle(eq_7[0:15],YELLOW_D,buff=0.3)
        frame_bin_2 = SurroundingRectangle(eq_8[0:9],YELLOW_D,buff=0.3)

        text_a = Text('Término cuadrático', color = RED).scale(0.6).next_to(frame_a,DOWN*2)
        text_b = Text('Término lineal', color = GREEN).scale(0.6).next_to(frame_b,UP*2)
        text_c = Text('Término independiente', color = BLUE).scale(0.6).next_to(frame_c,DOWN*2)



        self.play(FadeIn(header))
        self.play(Write(eq_1))
        self.wait()

        self.play(FadeOut(header),FadeOut(eq_1), run_time = 0.5)

        self.play(Write(text_2), run_time = 0.8)

        self.wait()

        self.play(FadeIn(eq_2))

        self.play(
            Create(frame_a),
            Create(frame_b),
            Create(frame_c),
            run_time = 0.5
        )

        self.play(Write(text_a),run_time = 0.7)
        self.play(Write(text_b),run_time = 0.7)
        self.play(Write(text_c),run_time = 0.7)

        self.wait(1.5)

        self.play(
            Uncreate(frame_a),
            Uncreate(frame_b),
            Uncreate(frame_c),
            FadeOut(text_a),
            FadeOut(text_b),
            FadeOut(text_c)
        )

        self.play(Unwrite(text_2), run_time = 0.7)

        self.play(TransformMatchingTex(eq_2,eq_3))

        self.play(Write(text_3), run_time = 0.8)

        self.wait()

        self.play(TransformMatchingShapes(eq_3[:10],eq_4[:10]))

        self.play(Write(eq_4[10:]))

        self.wait()

        ## ACLARACION ##
        ## Si se usa Transform es necesario hacer la transformación desde eq_3 hasta eq_5
        ## Si se usa TransformMatchingTex se utiliza la nueva ecuación como punto de partida, de eq_4 a eq_5

        #self.play(
        #    MoveTo(eq_4[10].copy(),eq_5[8]),
        #    MoveTo(eq_4[10],eq_5[12])
        #)

        self.play(TransformMatchingTex(eq_4,eq_5))

        self.wait(1.5)

        self.play(TransformMatchingTex(eq_5,eq_6))

        self.wait()

        self.play(Unwrite(text_3), run_time = 0.7)

        self.play(Write(text_7), run_time = 0.8)

        self.wait()

        self.play(
            TransformMatchingShapes(eq_6[:7],eq_7[:7]),
            TransformMatchingShapes(eq_6[7:],eq_7[23:]),
            )

        self.play(FadeIn(eq_7[7:23]))

        self.wait(1.5)

        self.play(Create(frame_bin_1))

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_7[0:1]+eq_7[2:15],eq_8[:9]),
            FadeOut(eq_7[1]),
            TransformMatchingShapes(eq_7[15:],eq_8[9:]),
            Transform(frame_bin_1,frame_bin_2)
        )

        self.wait(1.5)

        self.play(FadeOut(frame_bin_1))

        self.play(Unwrite(text_7),run_time = 0.7)

        self.play(Write(text_9), run_time = 0.8)

        self.wait()

        self.play(
            TransformMatchingShapes(eq_8[:9],eq_9[:9]),
            TransformMatchingShapes(eq_8[9:],eq_9[9:],path_arc=PI/2)
            )

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_9[:10],eq_10[:10]),
            TransformMatchingShapes(eq_9[17:],eq_10[16:]),
            FadeOut(eq_9[10:17]),
            FadeIn(eq_10[10:16])
        )


        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_10[:20],eq_11[:20]),
            FadeIn(eq_11[20:])
        )

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_11[:17],eq_12[:17]),
            FadeOut(eq_11[19]),
            TransformMatchingShapes(eq_11[17:19]+eq_11[20:],eq_12[17:])
        )

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_12[:10],eq_13[:10]),
            FadeOut(eq_12[13:16]),
            TransformMatchingShapes(eq_12[10:13]+eq_12[16:],eq_13[10:])
        )

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_13[:9],eq_14[1:10]),
            TransformMatchingShapes(eq_13[9],eq_14[10]),
            TransformMatchingShapes(eq_13[10:],eq_14[13:]),
        )

        self.play(
            Write(eq_14[0]),
            Write(eq_14[11:13]),
            )

        self.wait(1.5)

        self.play(
            FadeOut(eq_14[0:2]+eq_14[8:10]+eq_14[11:13]),
            TransformMatchingShapes(eq_14[2:8],eq_15[:6]),
            TransformMatchingShapes(eq_14[10],eq_15[6]),
            TransformMatchingShapes(eq_14[13:19],eq_15[9:15]),
            FadeIn(eq_15[7:9]),
            TransformMatchingShapes(eq_14[19:],eq_15[15:]),
            )

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_15[7:],eq_16[7:]),
            TransformMatchingShapes(eq_15[:7],eq_16[:7],path_arc=PI/2)
        )

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(eq_16[0:4],eq_1[0:4]),
            FadeOut(eq_16[4:7]),
            TransformMatchingShapes(eq_16[7:],eq_1[4:]),
        )

        self.wait(1.5)

        self.play(Unwrite(text_9), run_time = 0.7)
        self.wait()
        self.play(Write(text_16))
        self.wait(1.5)
        self.play(Indicate(eq_1))

        self.wait(2)

        self.play(
            FadeOut(text_16),
            FadeOut(eq_1)
        )

        self.wait()

        ##---------------------------------
        ##---------------------------------


class Soluciones_2(Scene):
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
            "¿Cómo son las soluciones de $ax^2+bx+c=0$?",
            color = WHITE
        ).scale_to_fit_width(config["frame_width"]-4)

        # Crea el rectangulo que rodea al grupo
        frameTitle = SurroundingRectangle(title, LME_color, buff = 1)

        subtitle = Text( # Crea el subtítulo
            "Álgebra",
            color = LIGHT_GREY
        ).scale(0.6).next_to(frameTitle,DOWN, aligned_edge = RIGHT)


        # Aparece el titulo
        self.play(Write(title) , run_time = 0.8)
        # Crea el rectangulo
        self.play(Create(frameTitle))
        # Escribe el subtitulo
        self.play(Write(subtitle) , run_time = 0.7)
        self.wait(1.5) # Espera un momento
        # Desaparece el titulo, subtitulo y el rectangulo
        self.play(
            FadeOut(title, scale=0.7),
            FadeOut(subtitle, scale=0.7),
            FadeOut(frameTitle),
            run_time = 0.8
        )
        ##---------------------------------
        ##---------------------------------

        ##------------------------------
        ## Desarrollo del video
        ##------------------------------



        ##---------------------------------
        ##---------------------------------
